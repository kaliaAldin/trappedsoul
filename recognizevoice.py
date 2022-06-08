import speech_recognition as sr
import pyttsx3
import  time
import RPi.GPIO as GPIO
from motorModule import Motor

myMotor = Motor ("kalia" , (29,31) , (32,33))

#initialize speech recognition
command_list = ["come" , "come here" , "come to me"]
command_goback = [" go back ", "return", "go away"]
turnleft = ["turn left ", "go left ", " move left",]
turnRight = ["turn rightt ", "go right ", " move right",]
r = sr.Recognizer()

#Function to convert the text to speech
def speak_text(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
while True:
    with sr.Microphone() as source2 :

        #wait until it clean the noise and It will hear you

        r.adjust_for_ambient_noise(source2 )
        print("would you like to tell me something ")

        #Listen to the sound input
        audio2 = r.listen(source2)
        #Using google recognition to convert the sound to text
        my_text = r.recognize_google(audio2)
        my_text = my_text.lower()


    #Basic question
    #come
    for item in command_list:
        if item in my_text:
            speak_text("I heared Come")
    #goback
    for item in command_goback:
        if item in my_text:
           speak_text("I heared go")
    #turnleft
    for item in turnleft :
        if item in my_text :
           speak_text("I heared Turn left")

    for item in turnRight :
        if item in my_text :
            speak_text("I heared Turn right")
