import json
import os
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import mainthread
from kivy.utils import platform
from kivy.core.window import Window

# رنگ زمینه برنامه
Window.clearcolor = (0.95, 0.95, 0.95, 1)

# تنظیمات گیت‌هاب
GITHUB_USERNAME = "Sultan-JFI"
GITHUB_REPO_NAME = "news_site_date-"
GITHUB_BRANCH = "main"
NEWS_FILE_PATH = "data/news_articles.json"
NEWS_API_URL = f"https://raw.githubusercontent.com/{GITHUB_USERNAME}/{GITHUB_REPO_NAME}/{GITHUB_BRANCH}/{NEWS_FILE_PATH}"
CACHE_FILE_NAME = "news_cache.json"

class NewsApp(App):

    def build(self):
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # سربرگ برنامه
        header = Label(
            text='[b][size=24sp]📰 خبرخوان جادویی[/size][/b]',
            markup=True,
            size_hint_y=None,
            height=50,
            color=(0.2, 0.2, 0.2, 1)
        )
        root.add_widget(header)

        # ساخت ScrollView برای لیبل خبرها
        self.news_layout = GridLayout(cols=1, size_hint_y=None, padding=10, spacing=10)
        self.news_layout.bind(minimum_height=self.news_layout.setter('height'))

        self.news_label = Label(
            text='در حال بارگذاری...',
            markup=True,
            size_hint_y=None,
            halign='right',
            valign='top',
            text_size=(Window.width - 40, None),
            color=(0.1, 0.1, 0.1, 1)
        )
        self.news_label.bind(texture_size=self.news_label.setter('size'))
        self.news_layout.add_widget(self.news_label)

        scroll = ScrollView(size_hint=(1, 0.85))
        scroll.add_widget(self.news_layout)
        root.add_widget(scroll)

        # دکمه به‌روزرسانی اخبار
        self.refresh_button = Button(
            text='🔄 به‌روزرسانی اخبار',
            size_hint=(1, 0.1),
            background_color=(0.2, 0.6, 0.86, 1),
            color=(1, 1, 1, 1),
            font_size='16sp'
        )
        self.refresh_button.bind(on_press=self.fetch_news)
        root.add_widget(self.refresh_button)

        self.load_cached_news()
        self.fetch_news()
        return root

    def get_cache_path(self):
        return os.path.join(self.user_data_dir if platform == 'android' else os.path.dirname(__file__), CACHE_FILE_NAME)

    def load_cached_news(self):
        cache_path = self.get_cache_path()
        if os.path.exists(cache_path):
            try:
                with open(cache_path, 'r', encoding='utf-8') as f:
                    news_data = json.load(f)
                self.display_news(news_data, cached=True)
            except Exception as e:
                self.news_label.text = f"[color=FF0000]خطا در بارگذاری کش: {e}[/color]"
        else:
            self.news_label.text = "[color=777777]اخبار کش‌شده یافت نشد.[/color]"

    def save_news_to_cache(self, news_data):
        try:
            with open(self.get_cache_path(), 'w', encoding='utf-8') as f:
                json.dump(news_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"خطا در ذخیره کش: {e}")

    def fetch_news(self, instance=None):
        self.news_label.text = "[color=444444]در حال دریافت اخبار جدید...[/color]"
        from threading import Thread
        Thread(target=self._fetch_news_thread).start()

    def _fetch_news_thread(self):
        try:
            response = requests.get(NEWS_API_URL, timeout=10)
            response.raise_for_status()
            news_data = response.json()
            self.save_news_to_cache(news_data)
            self.display_news_on_main_thread(news_data)
        except Exception as e:
            self.display_error_on_main_thread(f"[color=FF0000]خطا در دریافت اخبار: {e}[/color]")
            self.load_cached_news()

    @mainthread
    def display_news_on_main_thread(self, news_data):
        self.display_news(news_data)

    @mainthread
    def display_error_on_main_thread(self, message):
        self.news_label.text = message

    def display_news(self, news_data, cached=False):
        if not news_data:
            self.news_label.text = "[color=FF0000]هیچ خبری یافت نشد.[/color]"
            return

        display_text = "[b][size=20sp]📌 تازه‌ترین اخبار[/size][/b]\n\n"
        for i, item in enumerate(news_data):
            title = item.get("title", "بدون عنوان")
            content = item.get("content", "بدون محتوا")
            display_text += f"[b]{i+1}. {title}[/b]\n{content}\n\n"

        if cached:
            display_text += "\n[color=008000](بارگذاری از حافظه کش)[/color]"
        else:
            display_text += "\n[color=0000FF](بارگذاری از اینترنت)[/color]"

        self.news_label.text = display_text


if __name__ == '__main__':
    NewsApp().run()
