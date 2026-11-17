plugins {
    id("com.android.application")
    id("com.chaquo.python")
}
android {
    namespace = "ai.openjarvis.mobile"
    compileSdk = 35
    defaultConfig {
        applicationId = "ai.openjarvis.mobile"
        minSdk = 26
        targetSdk = 35
        versionCode = 1
        versionName = "1.0"
        ndk { abiFilters += listOf("arm64-v8a") }
    }
}
chaquopy {
    defaultConfig {
        version = "3.11"
        pip {
            install("openai>=1.30")
            install("httpx>=0.27")
            install("tomlkit>=0.12")
            install("filelock>=3.12")
            install("click>=8")
            install("rich>=13")
            install("requests>=2.31")
            install("websockets>=12")
        }
    }
    sourceSets {
        getByName("main").srcDir("../../src")
    }
}
