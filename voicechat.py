
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import requests
import json
from dotenv import load_dotenv

load_dotenv()

def speak(text):
    print(f"Assistant: {text}")
    try:
        engine=pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        print("Speech output not supported in colab")

def wish_user():
    hour=int(datetime.datetime.now().hour)
    if hour <12:
        st='Good morning !'
    elif hour<18:
        st="good afternoon!"
    else:
        st="Good evening!"
    speak(st+"boss")
    speak("I am JARVIS . what could i search for you boss?")

def take_command():
    
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Microphone as source
    with sr.Microphone() as source:
        print("Talk")
        # Optional but highly recommended: helps it ignore background static
        r.adjust_for_ambient_noise(source) 
        audio_text = r.listen(source)
        print("Thanks for your input.")
        
        try:
            # Save the recognized text to a variable and make it lowercase
            command_text = r.recognize_google(audio_text).lower()
            print("Text: " + command_text)
            return command_text # Return the STRING, not the raw audio
            
        except Exception as e:
            print("Sorry, I did not get that")
            return "" # Return an empty string if it didn't catch anything

def run_assistant():
    wish_user()
    while True:
        query=take_command()
        if query == "":
            continue

        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia",'')
            try:
                result=wikipedia.summary(query, sentences=2)
                speak("According to wikipedia:")
                speak(result)
            except:
                speak("sorry! i couldn't find anything.")
        
        elif 'search youtube for' in query:
            # 1. Remove the command words to isolate the search term (e.g., "301 dairies")
            search_term = query.replace("search youtube for", "").strip()
            speak(f"Searching YouTube for {search_term}...")
            
            # 2. Format it into a YouTube search link (spaces become '+')
            formatted_search = search_term.replace(" ", "+")
            search_url = f"https://www.youtube.com/results?search_query={formatted_search}"
            
            # 3. Open the specific search results page
            webbrowser.open(search_url)
        
        elif 'search google for' in query:
            search_term = query.replace("search google for", "").strip()
            speak(f"Searching google for {search_term}...")
            
            # 2. Format it into a google search link (spaces become '+')
            formatted_search = search_term.replace(" ", "+")
            search_url = f"https://www.google.com/search?q={formatted_search}"
            
            # 3. Open the specific search results page
            webbrowser.open(search_url)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"the current time is {strTime}")

        elif 'joke' in query:
            joke=pyjokes.get_joke()
            speak(joke)

        elif 'exit' in query or 'bye' in query:
            speak("Goodbye! Have a nice day boss!")
            break

        else:
            OPENROUTER_API_KEY=os.getenv("api_key")

            if not OPENROUTER_API_KEY:
                speak("THERE is some issue with the api key boss.")
                continue

           
            speak("thinking about your query boss...")
            try:
                response = requests.post(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                        "Content-Type": "application/json",
                        },
                    data=json.dumps({
                        "model": "nvidia/nemotron-3-ultra-550b-a55b:free",
                        "messages": [
    {"role": "system", "content": "Respond in plain conversational text with no markdown formatting, since your reply will be read aloud."},
    {"role": "user", "content": query}
]
                    }),
                    timeout=15,
                )
                results=response.json()
                answer=results["choices"][0]['message']['content']
                speak(answer)
            except Exception as e:
                speak("Sorry boss not able to get the information..")
                print(f"Error:{e}")

run_assistant()


