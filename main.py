import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('Sender_Email', 'Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'jungkok': 'jungkook@btsArmy.org',
    'jennie': 'jennie19@blackpink.com',
    'lisa': 'lisa73@blackpink.com',
    'irene': 'irene@redvelvet.com'
    'kusi': 'kusimusi9@gmail.com',
}


def get_email_info():
    talk('To Whom you want to send the email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me your thought, that is going to be in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey lazy. Your email is sent successfully')
    talk('Do you want to send another email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
