"""Weekly Status Report Agent: the starter for Zero to Live AI Agent on Cloud.

It works the moment you deploy it. With no AI key it runs in DEMO MODE and
writes a simple report using plain rules, so you can see your live link on
Day 1. Add your own AI key (see README) and it switches to a real model.

You will change two things over the next two days:
  prompts.py  -> the agent's job description (Day 2)
  app.py      -> the screen (Day 2)
"""
import os

import streamlit as st

from demo import demo_report
from prompts import SYSTEM_PROMPT

st.set_page_config(page_title="Weekly Status Report Agent", page_icon="📝")


def setting(name: str, default: str = "") -> str:
    """Read a setting from Streamlit secrets first, then from the environment."""
    try:
        value = st.secrets.get(name, "")
    except Exception:  # no secrets file: perfectly normal in demo mode
        value = ""
    return str(value or os.getenv(name, default)).strip()


API_KEY = setting("AI_API_KEY")
BASE_URL = setting("AI_BASE_URL", "https://api.openai.com/v1")
MODEL = setting("AI_MODEL", "gpt-4o-mini")


def write_report(updates: str) -> str:
    """Ask the model for the report. Returns plain markdown."""
    from openai import OpenAI  # imported here so demo mode needs no key and no network

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    reply = client.chat.completions.create(
        model=MODEL,
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": updates},
        ],
    )
    return reply.choices[0].message.content or "The model sent back an empty answer. Please try again."


st.title("📝 Weekly Status Report Agent")
st.write("Paste a week of rough updates. Get a clean report in five sections.")

if API_KEY:
    st.success(f"Using a real AI model ({MODEL}).")
else:
    st.info("Demo mode: no AI key added yet, so this uses simple rules. Add your key to use a real model (see the README).")

with open("sample_updates.txt", encoding="utf-8") as f:
    SAMPLE = f.read()

if "updates" not in st.session_state:
    st.session_state.updates = ""

if st.button("Load a sample week"):
    st.session_state.updates = SAMPLE

updates = st.text_area("Your updates", key="updates", height=240, placeholder="Paste your rough notes here, one per line...")

if st.button("Write my report", type="primary"):
    if not updates.strip():
        st.warning("Paste some updates first, or press 'Load a sample week'.")
    else:
        with st.spinner("Writing your report..."):
            try:
                report = write_report(updates) if API_KEY else demo_report(updates)
            except Exception as err:  # a wrong key, no credit, no network: say it in plain words
                st.error(f"The AI model could not answer. Check your key and model name in Settings, then try again. Details: {err}")
            else:
                st.markdown(report)
