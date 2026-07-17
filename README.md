# VoiceAssisstanceWithLLM

## JARVIS - Python Voice Assistant

JARVIS is a Python-based desktop voice assistant that listens to your voice commands and responds using text-to-speech. It can search the web, summarize Wikipedia articles, tell jokes, and hold intelligent conversations using the OpenRouter AI API.

### Features
* **Voice Recognition & Speech:** Listens to microphone input and responds with synthesized voice output.
* **AI Conversations:** Integrates with OpenRouter (using the `nvidia/nemotron-3-ultra-550b-a55b:free` model) for conversational responses.
* **Web Searching:** Automatically opens your browser to search Google or YouTube based on your voice commands.
* **Wikipedia Summaries:** Fetches and reads short summaries of requested topics from Wikipedia.
* **Time & Utilities:** Tells the current time and fetches random programming jokes.

### Prerequisites
You will need Python 3.x installed on your system. 

To run this project, install the required Python libraries. Note that `SpeechRecognition` requires `PyAudio` to interface with your system's microphone.

```bash
pip install SpeechRecognition pyttsx3 wikipedia pyjokes requests python-dotenv PyAudio
