from tkinter import *
from wit import Wit
win = Tk()
access_token="QWMZWOWJFZHRGOE64VXIDHZ7GJNAII5K"
cli = Wit(access_token=access_token)

def response(text):
    res = cli.message(text)
    entity = None
    value = None
    try:
        entity = list(res['entities'])[0]
        value = res['entities'][entity][0]['value']
    except:
        pass
    return entity, value

def reply(strs):
    entity, value = response(strs)
    if entity == 'formula':
        if value == 'addition':
            lst.insert(END, "Here is the formula for " + value + " a + b")
        elif value == 'subtraction':
            lst.insert(END, "Here is the formula for " + value + " a - b")
        elif value == 'multiplication':
            lst.insert(END, "Here is the formula for " + value + " a * b")
        elif value == 'division':
            lst.insert(END, "Here is the formula for " + value + " a / b")
        elif value == 'modulo':
            lst.insert(END, "Here is the formula for " + value + " a % b")
        elif value =="square":
            lst.insert(END, "Here is the formula for " + value + " a * a")
        elif value == "rectangle":
            lst.insert(END, "Here is the formula for " + value + " length * breadth")

        else:
            lst.insert(END, "I can't find this")
    elif entity == 'thanking':
        lst.insert(END, "you are welcome")
    elif entity == 'question':
        if value == "who are you":
            lst.insert(END, "I am a Math Bot to tell formulas")
        elif value == "how are you":
            lst.insert(END, "I am Fine!!! And you")
    elif entity== "reply":
        lst.insert(END, "That's cool!!!")
    elif entity == 'greeting':
        if value == 'bye':
            lst.insert(END, "bye! Have a nice day")
        else:
            lst.insert(END, "hi! How can i help you...")
    else:
        lst.insert(END, "I can't find this")


def getMessage():
    strs = string.get()
    lst.insert(END, strs)
    reply(strs)




lst = Listbox(win,height=10,width=100)
lst.grid(row=0,column=0,columnspan=3)
scroll = Scrollbar(win)
scroll.grid(row=0, column=2, rowspan=6)
lst.configure(yscrollcommand=scroll.set)
scroll.configure(command=lst.yview)
string = StringVar()
lb = Label(win,text="Messaage")
lb.grid(row=1,column=0)
entry = Entry(win, textvariable=string,width=50)
entry.grid(row=1, column=1)
btn = Button(win,text="send",command=getMessage,width=20)
btn.grid(row=1,column=2)
win.mainloop()


