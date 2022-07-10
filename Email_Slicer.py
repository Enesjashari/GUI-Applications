from cProfile import label
import tkinter as tk

window = tk.Tk()
window.geometry("480x440")
window.config(bg="#add8e6")
window.resizable(width=False,height=False)
window.title('Simple Email Slicer')

def email_brain():
    email = entry.get()
    u_email = email.strip()
    username = u_email[0:u_email.index('@')]
    domain = u_email[u_email.index('@') + 1:]
    text_box.delete('1.0', tk.END)
    msg = 'email given was {0}\nemail is {1}\ndomain is {2}'.format(u_email,username,domain)
    text_box.insert(tk.END,msg)

def reset_all():
    text_box.delete('1.0', tk.END)
    entry.delete(0, 'end')

#labels
label1 = tk.Label(text='welcome')
label2 = tk.Label(text='this app is used to slice a email into email & domain')
label3 = tk.Label(text='enter you email here ')



#entry
# entry = Entry()
e1=tk.StringVar()
entry = tk.Entry(font=(11),width=50,justify='center',textvariable=e1)


#Button
button = tk.Button(text='submit',command=email_brain)
reset = tk.Button(text='Reset',command=reset_all)



text_box = tk.Text(height=5,width=50)
#Packing Everything Together
label1.pack()
label2.pack()
label3.pack()
entry.pack()
button.pack()
reset.pack()
text_box.pack()


window.mainloop()














