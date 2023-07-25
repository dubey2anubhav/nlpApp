from tkinter import *
from mydp import database
from tkinter import messagebox
from myapi import API
class NLPApp:

    def __init__(self):

        self.dbo = database() # to import data base info
        self.apio = API() # to import API key from website

        # login ka gui load krna hain
        self.root = Tk()
        self.root.title('NLPApp')  #name change of gui
        # self.root.iconbitmap(enter path here)  for icon change
        self.root.geometry('360x600')
        self.root.configure(bg = '#34495E')

        self.login_gui()

        self.root.mainloop()  # hold the gui so that able to stay on screen

    # login function

    def login_gui(self):
        #login page code
        self.clear()  # to get clear screen

        # NLPApp as heading ka code
        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        # email enter code

        label1 = Label(self.root,text='Enter email')
        label1.pack(pady=(30,30))

        # email entry bar code
        # The Entry widget is used to accept single-line text strings from a user
        self.email_input = Entry(self.root, width=50)
        self.email_input .pack(pady=(5,10),ipady=4)  #ipady is for height adjusting

        #password code
        label2 = Label(self.root, text='Enter password')
        label2.pack(pady=(30, 30))

        # password entry bar code
        self.password_input = Entry(self.root, width=50,show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)


        # login button code
        login_btn = Button(self.root,text='LOGIN',width=30,height=2,command=self.perform_login)
        login_btn.pack(pady=(20,20))

        #label for not member
        #If you want to display one or more lines of text that cannot be modified by the user, then you should use the Label widget.
        label3 = Label(self.root, text='NOT A MEMBER?')
        label3.pack(pady=(20, 20))

        #redirect button for register
        redirect_btn = Button(self.root, text='REGISTER NOW', command=self.register_gui)
        redirect_btn.pack(pady=(20, 20))

    # register function

    def register_gui(self):
        # register ka code
        self.clear()

        # NLPApp as heading ka code
        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(20, 20))
        heading.configure(font=('verdana', 24, 'bold'))

        # label to enter name
        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(20, 20))

        # entry for single line text
        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=4)  # ipady is for height adjusting


        label1 = Label(self.root, text='Enter email')
        label1.pack(pady=(20, 20))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=4)  # ipady is for height adjusting


        label2 = Label(self.root, text='Enter password')
        label2.pack(pady=(20, 20))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=4)

        register_btn = Button(self.root, text='REGISTER', width=30, height=2,command= self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='ALREADY A  MEMBER?')
        label3.pack(pady=(10, 10))

        redirect_btn = Button(self.root, text='LOGIN NOW', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))


    # clear function to clear the screen when new page is to be loaded
    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy() # destroy is  used to clear the gui


    def perform_registration(self):
        # registration page gui


       name = self.name_input.get()
       email = self.email_input.get()
       password = self.password_input.get()

       response = self.dbo.add_data(name,email,password)

       if response:
          messagebox.showinfo('success','Registration.you can login')
          #message box to diplay message on screen rather than console
       else:
          messagebox.showerror('email exist')

    def perform_login(self):
        # login page

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email, password)
        if response:
            messagebox.showinfo('seccess','login succeeded')
            self.home_gui()
        else:
            messagebox.showerror('error','incorrect email/password')

    def home_gui(self):
        # analysis page gui

       self.clear()

       heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
       heading.pack(pady=(30, 30))
       heading.configure(font=('verdana', 24, 'bold'))

       sentiment_btn = Button(self.root, text='Sentiment Analysis', width=30, height=4, command=self.sentiment_gui)
       sentiment_btn.pack(pady=(10, 10))

       ner_btn = Button(self.root, text='name entitiy recognition', width=30, height=4, command=self.perform_registration)
       ner_btn.pack(pady=(10, 10))

       emotion_btn = Button(self.root, text='emotion prediction', width=30, height=4, command=self.perform_registration)
       emotion_btn.pack(pady=(10, 10))

       logout_btn = Button(self.root, text='logout', width=30, height=4, command=self.login_gui)
       logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):

        # sentiment analysis code
        self.clear()

        heading = Label(self.root, text='NLPApp', bg='#34495E', fg='white')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg='#34495E', fg='white')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 24,))

        label1 = Label(self.root, text='Enter text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=4)  # ipady is for height adjusting

        sentiment_btn = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='   ',bg='#34495E',fg ='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        # code to import api from myapi.py folder

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ''
        for i in result['sentiment']:
            txt = txt + i + '->' +str(result['sentiment'][i]) + '\n'
            print(i,result['sentiment'][i])

        print(txt)
        self.sentiment_result['text'] = txt



nlp = NLPApp()


