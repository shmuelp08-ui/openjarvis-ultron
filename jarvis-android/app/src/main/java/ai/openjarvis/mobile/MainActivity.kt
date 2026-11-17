package ai.openjarvis.mobile

import android.app.Activity
import android.os.Bundle
import android.graphics.Color
import android.view.Gravity
import android.view.ViewGroup
import android.widget.*
import com.chaquo.python.Python
import com.chaquo.python.android.AndroidPlatform
import java.util.concurrent.Executors

class MainActivity : Activity() {
    private val executor = Executors.newSingleThreadExecutor()
    private lateinit var output: TextView
    private lateinit var prompt: EditText
    private lateinit var key: EditText
    private lateinit var model: EditText
    private lateinit var send: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val prefs = getSharedPreferences("jarvis", MODE_PRIVATE)
        val root = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(24, 28, 24, 20)
            setBackgroundColor(Color.rgb(10, 12, 18))
        }
        fun field(hint: String, value: String = "") = EditText(this).apply {
            this.hint = hint; setText(value); setTextColor(Color.WHITE); setHintTextColor(Color.GRAY)
            setSingleLine(true); setPadding(14, 8, 14, 8)
            backgroundTintList = android.content.res.ColorStateList.valueOf(Color.rgb(40, 190, 220))
        }
        root.addView(TextView(this).apply {
            text = "JARVIS"; textSize = 28f; setTextColor(Color.rgb(40, 210, 235))
            gravity = Gravity.CENTER; setPadding(0, 8, 0, 18)
        })
        key = field("OpenAI API key", prefs.getString("api_key", "") ?: "")
        root.addView(key, LinearLayout.LayoutParams(-1, 54))
        model = field("Model", prefs.getString("model", "gpt-4o-mini") ?: "gpt-4o-mini")
        root.addView(model, LinearLayout.LayoutParams(-1, 54))
        output = TextView(this).apply {
            text = "Jarvis is ready. Add your API key to start."
            textSize = 15f; setTextColor(Color.LTGRAY); setPadding(4, 16, 4, 16)
        }
        val scroll = ScrollView(this); scroll.addView(output)
        root.addView(scroll, LinearLayout.LayoutParams(-1, 0, 1f))
        prompt = field("Message Jarvis…")
        root.addView(prompt, LinearLayout.LayoutParams(-1, 58))
        send = Button(this).apply {
            text = "SEND"; setTextColor(Color.WHITE); setBackgroundColor(Color.rgb(0, 125, 155))
        }
        root.addView(send, LinearLayout.LayoutParams(-1, 52))
        send.setOnClickListener { ask(prefs) }
        setContentView(root)
    }

    private fun ask(prefs: android.content.SharedPreferences) {
        val question = prompt.text.toString().trim()
        val apiKey = key.text.toString().trim()
        val modelName = model.text.toString().trim().ifBlank { "gpt-4o-mini" }
        if (apiKey.isBlank() || question.isBlank()) {
            output.text = "Enter your API key and a message first."; return
        }
        prefs.edit().putString("api_key", apiKey).putString("model", modelName).apply()
        send.isEnabled = false
        output.append("\n\nYou: $question\nJarvis: thinking…")
        prompt.setText("")
        executor.execute {
            try {
                if (!Python.isStarted()) Python.start(AndroidPlatform(this@MainActivity))
                val py = Python.getInstance()
                val result = py.getModule("jarvis_mobile").callAttr("ask", apiKey, modelName, question).toString()
                runOnUiThread { output.append("\n$result"); send.isEnabled = true }
            } catch (e: Exception) {
                runOnUiThread { output.append("\n[Jarvis error] ${e.message}"); send.isEnabled = true }
            }
        }
    }
}
