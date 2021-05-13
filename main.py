import pyttsx3
import smtplib
import os
import speech_recognition as sr

try:
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.starttls()                                                                                        
    server.login("uniqueQueue87898@gmail.com","pas")


    pyttsx3.speak("To whom you want to send email")
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)
        command = listener.recognize_google(audio)
        EmailTo = str(command).lower().replace(" at ", "@").replace(" ", "").replace("at", "@")
        print(EmailTo)

    pyttsx3.speak("Tell me the text in your email")
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source, None, 10)
        command = listener.recognize_google(audio)
        Content = str(command)
        print(Content)

    server.sendmail("uniqueQueue87898@gmail.com", "EmailTo", "Content")
    pyttsx3.speak("Email sent Successfully!")
    print("Email sent Successfully!" + To ,+ EmailTo )

except Exception as e:
    print(e)
    pyttsx3.speak("SomeThing Went Wrong, Please Try Again!"   )
