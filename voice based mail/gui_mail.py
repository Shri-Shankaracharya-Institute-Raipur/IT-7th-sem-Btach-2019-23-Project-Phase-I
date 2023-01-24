from tkinter import *
from tkinter.messagebox import showinfo
import speech_recognition as sr
import os
from PIL import ImageTk, Image
import smtplib, ssl

mainwindow = Tk()
mainwindow.title(' Voice based Mail')
mainwindow.geometry('1024x720')
mainwindow.resizable(0, 0)
frame = Frame(mainwindow, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
global text,text1,text2
# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("10131.jpg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()
class Mail:

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = ""
        self.password = ""

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender_mail, self.password)

        for email in emails:
            result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()
def send():
    global text, text1, text2
    mails = text.get()
    subject = text1.get()
    content = text2.get()
    mail = Mail()
    mail.send(mails, subject, content)


def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="en-IN")
                file1 = open("myfile.txt", "a", encoding="utf-8")
                file1.writelines("SPEECH TO TEXT")
                file1.write('\n')
                file1.write(text)
                file1.write('\n')
                file1.close()
            except:
                pass
            return text


def SpeechToText():
    global text, text1, text2
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title(' Voice based Mail')
    speechtotextwindow.geometry('1024x720')
    speechtotextwindow.resizable(0, 0)
    Label(speechtotextwindow, text='Voice based Mail', font=("Comic Sans MS", 15),
          bg='IndianRed').place(x=10)
    Label(speechtotextwindow, text='EMAIL', font=("Comic Sans MS", 15)).place(x=10,y=100)
    Label(speechtotextwindow, text='SUBJECT', font=("Comic Sans MS", 15)).place(x=10,y=200)
    Label(speechtotextwindow, text='MESSAGE', font=("Comic Sans MS", 15)).place(x=10,y=300)

    text = Text(speechtotextwindow, font=12, height=3, width=30)
    text.place(x=200, y=100)
    text1 = Text(speechtotextwindow, font=12, height=3, width=30)
    text1.place(x=200, y=200)
    text2 = Text(speechtotextwindow, font=12, height=10, width=30)
    text2.place(x=200, y=300)
    recordbutton = Button(speechtotextwindow, text='Record', bg='Sienna',font=("Comic Sans MS", 15),
                          command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=550, y=100)
    recordbutton1 = Button(speechtotextwindow, text='Record', bg='Sienna',font=("Comic Sans MS", 15),
                          command=lambda: text1.insert(END, recordvoice()))
    recordbutton1.place(x=550, y=200)
    recordbutton2 = Button(speechtotextwindow, text='Record', bg='Sienna',font=("Comic Sans MS", 15),
                          command=lambda: text2.insert(END, recordvoice()))
    recordbutton2.place(x=550, y=300)
    recordbutton3 = Button(speechtotextwindow, text='Record', bg='Sienna', font=("Comic Sans MS", 15),
                           command=send)
    recordbutton3.place(x=400, y=500)

Label(mainwindow, text='VOICE BASED MAIL',
      font=('Times New Roman', 16)).place(x=400, y=100)

speechtotextbutton = Button(mainwindow, text='click For Record ', font=('Times New Roman', 16), bg='lightgreen',
                            command=SpeechToText)
speechtotextbutton.place(x=430, y=540)

Label(mainwindow, text='DESIGNED',
      font=('Times New Roman', 16), bg='red', wrap=True, wraplength=450).place(x=450, y=630)
mainwindow.update()
mainwindow.mainloop()
