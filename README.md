
# Smart Email Assistant

![Python](https://img.shields.io/badge/python-3.10-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-%E2%9C%93-orange) ![License](https://img.shields.io/badge/license-MIT-green)

> **Project by [@GenAILearniverse](https://huggingface.co/spaces/GenAILearniverse)**

The **Smart Email Assistant** is a Streamlit application powered by OpenAI GPT models (e.g., `gpt-3.5-turbo`). It helps users generate professional email responses in different tones, suggests concise subject lines, and summarizes email threads instantly.

---

## 🚀 Features

- ✉️ **Auto-generate Email Replies** based on the conversation thread.
- 🎯 **Tone Selection:** Professional, Casual, Friendly, Formal.
- 📧 **Subject Line Suggestion** for the generated reply.
- 📝 **Thread Summarization** for a quick overview.
- 🔒 **API Key Management** via sidebar input or `secrets.toml`.

---

## 🛠️ Tech Stack

- **Python** 3.10+
- **Streamlit** for the web UI
- **OpenAI GPT** (`gpt-3.5-turbo` by default)

---

## 📦 Installation

1. **Clone your forked repo**
   ```bash
   git clone https://github.com/YOUR-USERNAME/SmartEmailAssistant.git
   cd SmartEmailAssistant
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate       # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your OpenAI API key**

   - **Option A:** Enter your key in the Streamlit sidebar at runtime.
   - **Option B:** Create a file at `./.streamlit/secrets.toml`:
     ```toml
     OPENAI_API_KEY = "your_openai_api_key_here"
     ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 📁 Project Structure

```plaintext
SmartEmailAssistant/
├── app.py                 # Streamlit application code
├── requirements.txt       # Python dependencies
├── README.md              # This documentation
└── .streamlit/
    └── secrets.toml       # (Optional) API key settings
```

---

## 🚀 Usage

1. **Open** the app in your browser (usually at `http://localhost:8501`).
2. **Enter** your email thread in the left pane.
3. **Select** the desired tone (Professional, Casual, Friendly, Formal).
4. **Provide** any additional context (optional).
5. **Click** **Generate Response**.
6. **View** the suggested subject line, email reply, and summary on the right.

### Example

**Input Thread:**
```plaintext
Hi team,

Can we schedule a meeting to discuss the quarterly report? I've noticed some interesting trends that I'd like to explore further.

Best regards,
John
```

**Output:**
- **Subject:** `Meeting Request: Q3 Report Discussion`
- **Reply:**
  ```plaintext
  Hi John,

  Thank you for highlighting the upcoming trends. I'd be happy to organize a meeting to review the quarterly report. Please let me know your availability, and I'll coordinate with the team.

  Best regards,
  [Your Name]
  ```
- **Summary:**
  ```plaintext
  John wants to schedule a team meeting to discuss trends in the Q3 report.
  ```

---

## 🔗 Useful Links

- **OpenAI API Docs:** https://platform.openai.com/docs
- **Streamlit Docs:** https://docs.streamlit.io
- **Hugging Face Space:** https://huggingface.co/spaces/GenAILearniverse/SmartEmailAssistant

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 🙌 Acknowledgments

- [OpenAI](https://openai.com) for GPT models
- [Streamlit](https://streamlit.io) for the UI framework
