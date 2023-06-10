from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#Functionality Part

def forget_pass():
    def change_password():
        if user_entry.get()==''or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error','All Fields Are Required!',parent=window)
        elif newpass_entry.get() !=confirmpass_entry.get():
            messagebox.showerror('Error','Passwords are not matching!',parent=window)
        else:
            con = pymysql.connect(host='localhost',user='root',password='mercur1453H*',database='userdata')
            mycursor = con.cursor()
            query = 'select * from data where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username!',parent=window)
            else:
                query='update data set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, please login with new password!',parent=window)
                window.destroy()



    window = Toplevel()
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bglabel = Label(window, image=bgPic)
    bglabel.grid()

    heading_label = Label(window, text='RESET_PASSWORD', font=('arial',22,'bold'),
                          bg='white', fg='magenta2')
    heading_label.place(x=500,y=60)

    userLabel = Label(window, text='Username', font=('arial', 12, 'bold'),
                          bg='white', fg='orchid1')
    userLabel.place(x=470, y=130)

    user_entry = Entry(window, width=35, fg='magenta2', font=('arial', 11, 'bold'), bd=0)
    user_entry.place(x=470, y=160)

    Frame(window, width=253, height=2, bg='orchid1').place(x=470,y=180)

    passwordLabel = Label(window, text='New Password', font=('arial',12,'bold'),bg='white',fg='orchid1')
    passwordLabel.place(x=470,y=210)

    newpass_entry = Entry(window, width=35,fg='magenta2', font=('arial', 11, 'bold'), bd=0)
    newpass_entry.place(x=470, y=240)

    Frame(window, width=253, height=2, bg='orchid1').place(x=470,y=260)

    confirmpassLabel = Label(window, text='Confirm Password', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
    confirmpassLabel.place(x=470, y=290)

    confirmpass_entry = Entry(window, width=35, fg='magenta2', font=('arial', 11, 'bold'), bd=0)
    confirmpass_entry.place(x=470, y=320)

    Frame(window, width=253, height=2, bg='orchid1').place(x=470, y=340)

    submitButton = Button(window, text='Submit',bd=0,bg='magenta2',fg='magenta2',font=('Open Sans',25,'bold'),
                          width=13,cursor='hand2',activebackground='magenta2',activeforeground='magenta2',command=change_password)
    submitButton.place(x=470, y=390)

    window.mainloop()

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All Fields Are Required!')

    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='mercur1453H*')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established, try again!')
            return
        query='use userdata'
        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is successful!')



def signup_page():
    login_window.destroy()
    import signup

def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

#GUI
login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login Page')
bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0, y=0)

heading=Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold')
              ,bg='white', fg='firebrick1')
heading.place(x=630, y=120)

usernameEntry=Entry(login_window,width=30,font=('Microsoft Yahei UI Light', 12,)
                    ,bd=0,fg='firebrick1')
usernameEntry.place(x=575, y=190)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)

Frame(login_window,width=247,height=2,bg='firebrick1').place(x=575,y=212)

passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei UI Light', 12,)
                    ,bd=0,fg='firebrick1')
passwordEntry.place(x=575, y=250)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)

frame2=Frame(login_window,width=208,height=2,bg='firebrick1')
frame2.place(x=575,y=272)
openeye=PhotoImage(file='openeye.png')
eyeButton=Button(login_window,image=openeye,bd=0,bg='white',activebackground='white'
                 ,cursor='hand2',command=hide)
eyeButton.place(x=798, y=247)

forgetButton=Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white'
                 ,cursor='hand2',font=('Microsoft Yahei UI Light', 9, 'bold')
                    ,fg='firebrick1', activeforeground='firebrick1',command=forget_pass)
forgetButton.place(x=709, y=290)

loginButton=Button(login_window, text='Login', font=('Open Sans',15,'bold'),
                   fg='firebrick1',bg='white',activeforeground='firebrick1'
                   ,activebackground='firebrick1',cursor='hand2',bd=0,width=20,height=2,command=login_user)
loginButton.place(x=578,y=330)

orLabel=Label(login_window,text='--------------- OR ---------------', font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=578,y=380)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=630,y=420)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=690,y=420)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=750,y=420)

signupLabel=Label(login_window,text='Dont have an account?',font=('Open Sans',13,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=630,y=465)

newaccountButton=Button(login_window, text='Create new one', font=('Open Sans',13,'bold underline'),
                   fg='blue',bg='white',activeforeground='blue'
                   ,activebackground='white',cursor='hand2',bd=0,command=signup_page)
newaccountButton.place(x=638,y=500)



login_window.mainloop()