# -*- coding: utf8 -*-

import sys
import tkinter as tk
import tkinter.messagebox as tkm

# define the button
def button_click(text):
	# tkm.showinfo('会計期間更新しました:', text, 'hi')
	tkm.showinfo('会計期間更新しました:', text)


# def showMessage(text):
#     tkm.showinfo('info', text)

# create a window
root = tk.Tk()

# set a title
root.title("会計期間")

# set size of the window
root.geometry('400x300')

# create a label
Static1 = tk.Label(text='会計期間をご入力ください')
Static1.pack()
# set the place
# Static1.place(x=150, y=50)

# create a entry
Entry1 = tk.Entry()
Entry1.pack()

# get the value in the Entry1
# global Entry1_value
Entry1_value = Entry1.get()
# print(Entry1.get())


# set the button
# Button = tk.Button(text='実行ボタン', command=lambda: button_click(Entry1_value))
# Button = tk.Button(text=u'何も起こらないボタン', width=50, command=lambda: showMessage(Entry1.get()))
# Button = tk.Button(text=u'何も起こらないボタン', width=50, command=lambda: showMessage(Entry1_value))
Button = tk.Button(text='実行ボタン', command=lambda: button_click(Entry1.get()))
Button.pack()

# active the window
root.mainloop()
# print(Entry1_value)
