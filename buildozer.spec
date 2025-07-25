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
android.build_tools_version = 33.0.2
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
