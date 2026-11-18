package ai.openjarvis.mobile

import android.app.Application
import android.util.Log
import java.io.File

class JarvisApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        val previous = Thread.getDefaultUncaughtExceptionHandler()
        Thread.setDefaultUncaughtExceptionHandler { thread, error ->
            try {
                File(filesDir, "jarvis_last_crash.txt").writeText(
                    "Thread: ${thread.name}\n\n" + Log.getStackTraceString(error)
                )
            } catch (_: Exception) {
                // Preserve the original crash even if writing the report fails.
            }
            previous?.uncaughtException(thread, error)
        }
    }
}
