import datetime
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()
recognizer = sr.Recognizer()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=8, phrase_time_limit=8)
    try:
        query = recognizer.recognize_google(audio, language="en-US")
        print("You:", query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand.")
    except sr.RequestError:
        speak("Internet connection problem.")
    return ""


def run():
    speak("Hello, I am your voice assistant. How can I help you?")
    while True:
        try:
            query = listen()
        except sr.WaitTimeoutError:
            continue

        if not query:
            continue

        if "wikipedia" in query:
            topic = query.replace("wikipedia", "").replace("search", "").strip()
            try:
                speak(wikipedia.summary(topic, sentences=2))
            except Exception:
                speak("Could not find that topic.")
        elif "time" in query:
            speak("The time is " + datetime.datetime.now().strftime("%I:%M %p"))
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
        elif "open google" in query:
            webbrowser.open("https://www.google.com")
        elif "exit" in query or "stop" in query or "bye" in query:
            speak("Goodbye!")
            break
        else:
            speak("I heard: " + query)


if __name__ == "__main__":
    run()
