import tkinter as tk

#initialise
root = tk.Tk()

#window+answer
w = root.title("Calculator")
root.resizable(True,True)
root.config(background = 'black')
a = tk.Entry(root)
a.grid(row = 0,columnspan = 10)
answer = tk.Entry(root)
answer.grid(row=1,columnspan = 10)


#row spacing
#root.rowconfigure(0, pad=3)
#root.rowconfigure(1, pad=3)
#root.rowconfigure(2, pad=3)
#root.rowconfigure(3, pad=3)
#root.rowconfigure(4, pad=3)

#button commands
def oneb():
    a.insert(len(a.get())  + 1,'1')

def twob():
    a.insert(len(a.get()) + 1,'2')

def threeb():
    a.insert(len(a.get()) + 1, '3')

def fourb():
    a.insert(len(a.get()) + 1, '4')

def fiveb():
    a.insert(len(a.get()) + 1, '5')

def sixb():
    a.insert(len(a.get()) + 1, '6')

def sevenb():
    a.insert(len(a.get()) + 1, '7')

def eightb():
    a.insert(len(a.get()) + 1, '8')

def nineb():
    a.insert(len(a.get()) + 1, '9')

def zerob():
    a.insert(len(a.get()) + 1, '0')

def plusb():
    a.insert(len(a.get()) + 1, '+')

def subb():

    a.insert(len(a.get()) + 1, '-')

def mulb():
    a.insert(len(a.get()) + 1, '*')

def divb():
    a.insert(len(a.get()) + 1, '/')

def dotb():
    a.insert(len(a.get()) + 1, '.')

def equalto():
    try:
        eval(a.get())
    except ZeroDivisionError:
        answer.insert(0, 'Syntax Error')
    ans = eval(a.get())
    string_answer = str(ans)
    answer.delete(0,'end')
    answer.insert(0,string_answer)


def clearb():
    string = ''
    a.delete(0,'end')
    answer.delete(0,'end')

#buttons
one = tk.Button(root, text = '1',command = oneb)
one.grid(row=2,column = 0)

two = tk.Button(root, text = '2',command = twob)
two.grid(row=2,column = 1)


three = tk.Button(root, text = '3',command = threeb)
three.grid(row=2,column = 2)

four = tk.Button(root, text = '4',command = fourb)
four.grid(row=3,column = 0)

five = tk.Button(root, text = '5',command = fiveb)
five.grid(row=3,column = 1)

six = tk.Button(root, text = '6',command = sixb)
six.grid(row=3,column = 2)

seven = tk.Button(root, text = '7',command = sevenb)
seven.grid(row=4,column = 0)

eight = tk.Button(root, text = '8',command = eightb)
eight.grid(row=4,column = 1)

nine = tk.Button(root, text = '9',command = nineb)
nine.grid(row=4,column = 2)

zero = tk.Button(root, text = '0',command = zerob)
zero.grid(row=5,column = 0)

dot = tk.Button(root, text = '.',command = dotb)
dot.grid(row=5,column = 1)


plus = tk.Button(root, text = '+',command = plusb)
plus.grid(row = 2,column = 3)

sub = tk.Button(root, text = '-',command = subb)
sub.grid(row = 3,column = 3)

mul = tk.Button(root, text = '*',command = mulb)
mul.grid(row = 4,column = 3)

div = tk.Button(root, text = '/',command = divb)
div.grid(row = 5,column = 3)

equal = tk.Button(root, text = '=',command = equalto)
equal.grid(row = 5,column = 2)

clear = tk.Button(root, text = 'CLC',command = clearb)
clear.grid(row = 6,columnspan = 4)


root.mainloop()