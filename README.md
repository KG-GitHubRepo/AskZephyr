# 🤖 Q&A Demo (Streamlit + Hugging Face)

A minimal **Q&A web app** built with **Streamlit** that calls the **Hugging Face Inference API** to generate answers from open-source LLMs.  
It first tries a **chat** model and automatically falls back to a **text-generation** model if needed.

---

## ✨ Features

- 🖥 **Streamlit UI** – Clean and interactive interface
- 🔑 **Secure API Authentication** – Uses Hugging Face Access Tokens via environment variables
- 🧠 **Two-stage model flow**:
  1. `HuggingFaceH4/zephyr-7b-beta` via `chat_completion`
  2. Fallback: `tiiuae/falcon-7b-instruct` via `text_generation`
- 🚦 **Error Handling** – Displays clear error messages and status info
- 🌐 **Deployable** to **Hugging Face Spaces** with minimal setup

---

## 📂 Project Structure

```
.
├── app.py               # Main Streamlit application code
├── requirements.txt     # Python dependencies needed to run the app
├── README.md            # Project documentation
```

---

<!--
## ⚙️ Local Installation

```
1️⃣ Clone this repo
------------------
git clone https://github.com/<your-username>/qa-demo-genai.git
cd qa-demo-genai

2️⃣ Create virtual environment (optional but recommended)
---------------------------------------------------------
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate

3️⃣ Install dependencies
------------------------
pip install -r requirements.txt

4️⃣ Get Hugging Face API Token
------------------------------
- Sign in or create a Hugging Face account: https://huggingface.co/
- Go to Access Tokens: https://huggingface.co/settings/tokens
- Create a new token with **Read** access

5️⃣ Set environment variable for your token
-------------------------------------------
# macOS/Linux
export HUGGINGFACEHUB_API_TOKEN="hf_your_token_here"

# Windows PowerShell
setx HUGGINGFACEHUB_API_TOKEN "hf_your_token_here"
*(Restart terminal after running this on Windows)*

6️⃣ Run the app
---------------
streamlit run app.py
Open http://localhost:8501 in your browser.
```

--- 
-->

## 🚀 Deploy to Hugging Face Spaces

```
1. Create a Space: https://huggingface.co/spaces
   - SDK: Streamlit
   - Runtime: Python 3.10+

2. Push code to Space repository
   git remote add space https://huggingface.co/spaces/<username>/<space-name>
   git push space main

3. Add your API token as a secret
   - Go to Space → Settings → Repository secrets
   - Add HUGGINGFACEHUB_API_TOKEN with your Hugging Face token value

4. Space will build and deploy automatically.
```

---

## 🧠 How It Works

```
1. User enters a question in the input box.
2. App verifies Hugging Face token via HfApi().whoami().
3. Attempts to answer with chat_completion using Zephyr-7B.
4. If chat model fails, falls back to text_generation using Falcon-7B.
5. Displays the answer in the UI.
```

---

## 🛠 Configuration

```
Environment Variable:
- HUGGINGFACEHUB_API_TOKEN (required, must start with hf_)

Models:
- Primary: HuggingFaceH4/zephyr-7b-beta
- Fallback: tiiuae/falcon-7b-instruct

Parameters:
- max_tokens / max_new_tokens: control output length
- temperature, top_p: adjust randomness
```

---

## 🩹 Troubleshooting

```
Token Error:
- Ensure your token is valid and starts with hf_
- Check that it's exported in the same shell session

Model Error:
- Switch to another available model on Hugging Face
- Check model’s Inference API page to confirm it supports chat or text generation
```

---


## 🤝 Contributing

```
1. Fork the repository
2. Create your feature branch (git checkout -b feature/YourFeature)
3. Commit your changes (git commit -m "Add some feature")
4. Push to the branch (git push origin feature/YourFeature)
5. Open a Pull Request
```

---


