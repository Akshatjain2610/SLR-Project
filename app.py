import tkinter as tk
import os

root = tk.Tk()

def runApps():
    os.startfile("test.py")

lable = tk.Label(root,text="Welcome to Sign Language Recognizer (SLR)",font=('Times', 26))
lable.pack()
canvas = tk.Canvas(root, height=500, width=760, bg="#263D42")
canvas.pack()


frame = tk.Frame(root)
l7 = tk.Label(frame,text=" INSTRUCTIONS", fg='red',font=('Times', 30),pady=20)
l7.grid()
l1 = tk.Label(frame,text="1. This convertor convert American signs into text.", fg='blue',font=('Times', 20),pady=10)
l1.grid()
l2 = tk.Label(frame,text="2. This convertor also speaks the predicted output.", fg='blue',font=('Times', 20),pady=10)
l2.grid()
l3 = tk.Label(frame,text="3. This convertor currently working for only one hand.", fg='blue',font=('Times', 20),pady=10)
l3.grid()
l4 = tk.Label(frame,text="4. Make sure your Camera works properly.", fg='blue',font=('Times', 20),pady=10)
l4.grid()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


Start = tk.Button(root, text="Start",font=('Times', 20),padx=30, fg='white', bg="#263D42", command=runApps)
Start.pack()

root.mainloop()
