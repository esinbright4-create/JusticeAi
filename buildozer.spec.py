[app]
title = JusticeApp
package.name = justiceapp
package.domain = org.yourname
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
android.api = 33
android.sdk = 24
android.ndk = 25b
android.arch = arm64-v8a
android.minapi = 21
android.private_storage = True
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1