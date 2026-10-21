# Marson's Voice Assistant

A personal voice assistant built as a custom **Google Gemini Gem**. It answers out loud in Estonian or English, keeps replies short for voice, and helps with Sisulaine Media work, EBS University studies, daily planning and quick drafts.

**Project page:** https://sneax74.github.io/voice-agent/

**Try it in Gemini:** https://gemini.google.com/gem/1l1yxxJtod04J4jTfLrYYssm9ZnaH5Awn?usp=sharing (sign in with a Google account)

## How it is built

| Part | What it does |
| --- | --- |
| Platform | Google Gemini, custom Gem (free plan) |
| Instructions | [`system-prompt.md`](system-prompt.md): role, language, voice style, actions that need a "yes", honesty rules |
| Knowledge | Marson's CV (PDF), used for interview practice, self-introductions and job applications |
| Voice | Gemini app on the phone: open the Gem and tap the microphone |

## How to use it

1. Open the shared Gem: https://gemini.google.com/gem/1l1yxxJtod04J4jTfLrYYssm9ZnaH5Awn?usp=sharing
2. Sign in with a Google account if asked.
3. Tap the microphone and talk, for example:
   - "Tere! Mida ma täna kõige esimesena tegema peaksin?"
   - "Give me three video ideas for a gym client."
   - "Ask me interview questions for a marketing job."

## Make your own copy

1. Go to gemini.google.com, open **Gems**, then **New Gem**.
2. Paste the contents of [`system-prompt.md`](system-prompt.md) into **Instructions** and change the personal details to your own.
3. Save, then open the Gem in the Gemini app and talk to it.

## Talking on the website

The page at https://sneax74.github.io/voice-agent/ has its own voice assistant:

- **Listening:** the browser's speech recognition (Chrome, Edge and Safari), in English, Estonian or Russian.
- **Thinking:** Google Gemini (`gemini-3.5-flash-lite` for fast answers, `gemini-3.5-flash` as backup) through a small Cloudflare Worker in [`worker/worker.js`](worker/worker.js). The Worker keeps the Gemini API key secret, only accepts requests from this website and limits message length.
- **Speaking:** Gemini text-to-speech (`gemini-3.8-flash-lite-tts`), or the browser voice as a fallback.

If the Worker isn't reachable, the page falls back to prepared answers.
