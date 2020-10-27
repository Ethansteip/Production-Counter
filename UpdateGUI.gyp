from tkinter import *

root = Tk()
root.geometry("800x480")

number = 0

def plusOne():
    global number
    number += 1
    count.config(text=number)

def minusOne():
    global number
    number -= 1
    count.config(text=number)

btn_plus = Button(root, text="+", font=("Helvetica", 35, 'bold'), command=plusOne)
btn_plus.grid(column=1, row=2, ipadx=45, ipady=25, padx=125 )

btn_minus = Button(root, text="-", font=("Helvetica", 35, 'bold'), command=minusOne)
btn_minus.grid(column=3, row=2, ipadx=45, ipady=25, padx=125 )

count = Label(root, text=number, bg="white", font=("Helvetica", 75, 'bold'), height=2, width=3)
count.grid(column=2, row=1, pady=25)




root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(2, weight=1)



root.mainloop()



