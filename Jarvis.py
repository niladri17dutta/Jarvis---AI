# Import necessary libraries
import datetime
import os
import webbrowser
import smtplib
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()


# Function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to greet the user
def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        print("Good Morning!")
        speak("Good Morning!")

    elif 12 <= hour < 18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")
    print("I am your personal voice assistant. Please tell me how may I help you ?")
    speak("I am your personal voice assistant. Please tell me how may I help you")


# Function to take user input through voice
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not get that. Please repeat.")
        speak("Sorry, I did not get that. Please repeat.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

# Function to perform actions based on user input
def execute_command(command):
    # Logic for executing tasks based on query
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.org/"],
             ["google", "https://www.google.com"], ["stack overflow", "https://www.stackoverflow.com/"],
             ["academia", "https://academia.srmist.edu.in/"], ["coursera", "https://www.coursera.org/"],
             ["spotify", "https://open.spotify.com/"], ["linkedin", "https://www.linkedin.com/"],
             ["whatsapp", "https://web.whatsapp.com/"], ["udemy", "https://www.udemy.com/"]]
    for site in sites:
        if f"Open {site[0]}".lower() in command:
            print(f"Opening {site[0]} ...")
            speak(f"Opening {site[0]}")
            webbrowser.open(site[1])

    if 'in wikipedia' in command:
        speak('Searching Wikipedia...')
        query = command.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print("According to Wikipedia")
        print(results)
        speak(results)

    elif 'in google' in command:
        print("I found these results in google. Please have a look...")
        speak("I found these results in google. Please have a look")
        webbrowser.open_new_tab('https://www.google.co.in/search?q=' + command)

    elif 'in youtube' in command:
        print("I found these results in youtube. Please have a look...")
        speak("I found these results in youtube. Please have a look")
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + command)

    elif "the time" in command:
        hour = datetime.datetime.now().strftime("%H")
        minis = datetime.datetime.now().strftime("%M")
        print(f"The time is {hour} hour and {minis} minutes.")
        speak(f"The time is {hour} hour and {minis} minutes.")

    elif 'open code' in command:
        print("Opening V S Code...")
        speak("Opening V S Code")
        codepage = "D:\\Microsoft VS Code\\Code.exe"
        os.startfile(codepage)

    elif 'open word' in command:
        print("Opening Microsoft Word...")
        speak("Opening Microsoft Word")
        codepage = "C:\\Program Files\\Microsoft Office\\root\Office16\\WINWORD.exe"
        os.startfile(codepage)

    elif 'email to prabir' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "prabir1234@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email to Prabir")
    
    elif 'play music' in query:
              music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
              songs = os.listdir(music_dir)
              print(songs)    
              os.startfile(os.path.join(music_dir, songs[0]))

    else:
        speak("I'm sorry, I don't understand that command.")
        print("I'm sorry, I don't understand that command.")


# Main function
def main():
    greet()

    while True:
        command = listen()
        if command:
            if "exit" in command:
                speak("Good Bye! See you soon...")
                print("Good Bye! See you soon...")
                break
            else:
                execute_command(command)


if __name__ == "__main__":
    main()
