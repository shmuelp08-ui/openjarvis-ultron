# Jarvis Android APK

Standalone Android client embedding the OpenJarvis Python source tree from `../src`.
The Android app invokes OpenJarvis' own `CloudEngine` and `Message` types; it does not
reuse the legacy ULTRON Android app. The first build supports OpenAI API credentials
and a selectable model. The API key is stored only in this app's private preferences.

Build output name: `Jarvis-APK.apk`.
