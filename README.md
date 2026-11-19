# Agent Template Pack: Weekly Status Report Agent

The starter for **Zero to Live AI Agent on Cloud** (Future Proof India).

It turns a week of rough work notes into a clean five-section report. It works as soon as you put it online. You do not need to install anything on your computer.

## Get your live link in about ten minutes

1. **Copy this project.** Click the green **Use this template** button at the top right of this page, then **Create a new repository**. Give it any name, keep it **Public**, and click **Create repository**.
2. **Put it online.** Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub. Click **Create app**, choose **Deploy a public app from GitHub**, pick the repository you just made, leave the main file as `app.py`, and click **Deploy**.
3. **Open your link.** After a minute or two you get a web address ending in `streamlit.app`. Open it, press **Load a sample week**, then **Write my report**. That is your agent, live.

It starts in **demo mode**: it sorts your notes with simple rules, no AI key needed. That is deliberate, so you see something live on Day 1.

## Use a real AI model (Day 1 evening or Day 2)

1. Get a key from an AI provider (Google Gemini has a free tier).
2. In Streamlit, open your app, then **Settings → Secrets**, and paste the three lines from `.streamlit/secrets.toml.example` with your own key and the provider you chose. Click **Save**.
3. Refresh your app. The green box now says it is using a real model.

Never paste a key into a file on GitHub, into a chat or into a screenshot.

## Change it yourself (Day 2)

Open a file on GitHub, click the pencil icon, change it, and press **Commit changes**. Your live app updates by itself within a minute.

| File | What it is | When you change it |
|---|---|---|
| `prompts.py` | the agent's job description | Day 2 |
| `app.py` | the screen people see | Day 2 |
| `sample_updates.txt` | a sample week of notes | Day 2 |
| `demo.py` | the simple rules used in demo mode | you can ignore this |

Ask your AI assistant to write the new text, then paste it into the file on GitHub.

## If something fails

Open your app, click **Manage app** at the bottom right, and read the last lines of the log. Paste them into your AI assistant and ask: "What is wrong, in plain words, and what exact change should I make?"
