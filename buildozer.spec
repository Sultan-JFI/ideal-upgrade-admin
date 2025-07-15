[app]

title = NewsApp
package.name = newsapp
package.domain = org.example

source.dir = .
source.include_exts = py,json
version = 0.1
requirements = python3,kivy==2.2.1,requests
orientation = portrait
fullscreen = 0

android.api = 31
android.ndk = 25b
android.archs = arm64-v8a
android.minapi = 21
android.permissions = INTERNET

# آیکون دلخواه:
# icon.filename = %(source.dir)s/icon.png

# اگر فایل kv هم داری، اینجا لیست کن
# presplash.filename = %(source.dir)s/data/presplash.png

# (اختیاری) فونت پیش‌فرض فارسی:
# android.additional_fonts = B_Nazanin.ttf

[buildozer]

log_level = 2
warn_on_root = 1

[globals]

# بقیه گزینه‌ها به تنظیمات پیش‌فرض برگردن
