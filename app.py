import os
import streamlit as st
from huggingface_hub import HfApi, InferenceClient, __version__ as hf_ver

st.set_page_config(page_title="Q&A Demo", page_icon="🤖")
st.header("Q&A Demo")

HF_TOKEN = (os.getenv("HUGGINGFACEHUB_API_TOKEN") or "").strip().strip('"').strip("'")
st.caption(f"huggingface_hub={hf_ver} | token_present={bool(HF_TOKEN)} len={len(HF_TOKEN) if HF_TOKEN else 0}")

if not HF_TOKEN or not HF_TOKEN.startswith("hf_"):
    st.error("Fix HUGGINGFACEHUB_API_TOKEN in Settings → Repository secrets, then Restart.")
    st.stop()

# prove auth
try:
    HfApi(token=HF_TOKEN).whoami()
except Exception as e:
    st.error(f"whoami failed: {e}")
    st.stop()

client = InferenceClient(token=HF_TOKEN)

def generate_answer(q: str) -> str:
    # 1) Try chat (models that expose 'conversational' on serverless)
    try:
        resp = client.chat_completion(
            model="HuggingFaceH4/zephyr-7b-beta",
            messages=[{"role": "user", "content": q}],
            max_tokens=128,
        )
        return resp.choices[0].message.content
    except Exception as e1:
        # 2) Fallback to plain text-generation
        try:
            return client.text_generation(
                model="tiiuae/falcon-7b-instruct",
                prompt=q,
                max_new_tokens=128,
                return_full_text=False,
            )
        except Exception as e2:
            raise RuntimeError(f"chat_completion error: {repr(e1)} | text_generation error: {repr(e2)}")

q = st.text_input("Ask me anything:")
if st.button("Generate") and q.strip():
    with st.spinner("Thinking..."):
        try:
            st.subheader("Answer")
            st.write(generate_answer(q))
        except Exception as e:
            st.error(f"Generation failed → {e}")import os
import streamlit as st
from huggingface_hub import HfApi, InferenceClient, __version__ as hf_ver

st.set_page_config(page_title="Q&A Demo", page_icon="🤖")
st.header("Q&A Demo")

HF_TOKEN = (os.getenv("HUGGINGFACEHUB_API_TOKEN") or "").strip().strip('"').strip("'")
st.caption(f"huggingface_hub={hf_ver} | token_present={bool(HF_TOKEN)} len={len(HF_TOKEN) if HF_TOKEN else 0}")

if not HF_TOKEN or not HF_TOKEN.startswith("hf_"):
    st.error("Fix HUGGINGFACEHUB_API_TOKEN in Settings → Repository secrets, then Restart.")
    st.stop()

# prove auth
try:
    HfApi(token=HF_TOKEN).whoami()
except Exception as e:
    st.error(f"whoami failed: {e}")
    st.stop()

client = InferenceClient(token=HF_TOKEN)

def generate_answer(q: str) -> str:
    # 1) Try chat (models that expose 'conversational' on serverless)
    try:
        resp = client.chat_completion(
            model="HuggingFaceH4/zephyr-7b-beta",
            messages=[{"role": "user", "content": q}],
            max_tokens=128,
        )
        return resp.choices[0].message.content
    except Exception as e1:
        # 2) Fallback to plain text-generation
        try:
            return client.text_generation(
                model="tiiuae/falcon-7b-instruct",
                prompt=q,
                max_new_tokens=128,
                return_full_text=False,
            )
        except Exception as e2:
            raise RuntimeError(f"chat_completion error: {repr(e1)} | text_generation error: {repr(e2)}")

q = st.text_input("Ask me anything:")
if st.button("Generate") and q.strip():
    with st.spinner("Thinking..."):
        try:
            st.subheader("Answer")
            st.write(generate_answer(q))
        except Exception as e:
            st.error(f"Generation failed → {e}")
