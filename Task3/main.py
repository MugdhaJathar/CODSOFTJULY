from tkinter import *
import random
import pyperclip
import string

def generator():
    small_letters = string.ascii_lowercase
    capital_letters = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all = small_letters + capital_letters + numbers + special_characters
    password_length = int(length_Box.get())

    if choice.get()== 1:
        passwordField.insert(0,random.sample(small_letters,password_length))

    if choice.get()== 2:
        passwordField.insert(0,random.sample(small_letters + capital_letters,password_length))

    if choice.get()== 3:
        passwordField.insert(0,random.sample(all,password_length))

def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)

root=Tk()
root.config(bg ='#6C3428')
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text = 'PASSWORD GENERATOR',font = ('georgia',20,'bold'),bg='#6C3428',fg='#FAF0D7')
passwordLabel.grid(pady=15,padx=10)

weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font = ('georgia',15),fg="#FAF0D7",bg='#6C3428')
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font = ('georgia',15),fg="#FAF0D7",bg='#6C3428')
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font = ('georgia',15),fg="#FAF0D7",bg='#6C3428')
strongradioButton.grid(pady=10)

lengthLabel=Label(root,text='Select Password Length:',font = ('georgia',15),bg='#6C3428',fg='#FAF0D7')
lengthLabel.grid(pady=15)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font = ('georgia',15),bg='#FAF0D7',fg='#6C3428')
length_Box.grid(pady=10)

generateButton=Button(root,text='Generate password',font = ('georgia',15),bg='#FAF0D7',fg='#6C3428',command=generator)
generateButton.grid(pady=15)

passwordField=Entry(root,width=25,bd=2,font = ('georgia',15),bg='#FAF0D7',fg='#6C3428')
passwordField.grid()

copyButton=Button(root,text='Copy password',font = ('georgia',15),bg='#FAF0D7',fg='#6C3428',command=copy)
copyButton.grid(pady=25)

root.mainloop()
