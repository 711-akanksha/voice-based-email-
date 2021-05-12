import pyttsx3
import smtplib
import os
import speech_recognition as sr

try:
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.starttls()
    server.login("akanksha1116gupta@gmail.com","xyz")

    pyttsx3.speak("To whom you want to send email")
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source, None, 10)
        command = listener.recognize_google(audio)
        EmailTo = str(command).lower().replace(" at ", "@").replace(" ", "").replace("at", "@")
        print(EmailTo)

    pyttsx3.speak("Tell me the text in your email")
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)
        command = listener.recognize_google(audio)
        Content = str(command)
        print(" hel me out")

    server.sendmail("akanksha1116gupta@gmail.com", "bakuaku738@gmail.com", "made new project")
    pyttsx3.speak("Email sent Successfully!")
    print("Email sent Successfully!" + akanksha1116gupta@gmail.com ,+bakuaku738@gmail.com)

except Exception as e:
    print(e)
    pyttsx3.speak("SomeThing Went Wrong, Please Try Again!")