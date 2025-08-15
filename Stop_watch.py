import tkinter as Tkinter
from datetime import datetime

counter = 0
running = False

def counter_label(label):
    def count():
        
        if running:
            global counter

            if counter == 0:
                display = "ready"

            else:
                time = datetime.utcfromtimestamp(counter)
                string = time.strftime("%H:%M:%S")
                display = string
            label['text'] = display

            label.after(1000,count)

            counter = counter +1

    count()


def start(label):
    global running
    running = True
    counter_label(label)
    Start['state'] = 'disabled'
    Stop['state'] = 'normal'
    Reset['state'] = 'normal'


def stop():
    global running
    Start['state'] = 'normal'
    Stop['state'] = 'disabled'
    Reset['state'] = 'normal'
    running = False


def reset(label):
    global counter
    counter = 0

    if not running:
        Reset['state'] ='disabled'
        label['text'] = '00:00:00'

    else:
        label['text'] = '00:00:00'



root = Tkinter.Tk()

root.title("Stopwatch")

root.minsize(width = 250, height = 70)
label = Tkinter.Label(root, text='ready', fg='black', font='Verdana 30 bold')
label.pack()

SW = Tkinter.Frame(root)

Start =Tkinter.Button(SW,text = 'START', width =6, command = lambda: start(label))
Stop =Tkinter.Button(SW, text = 'STOP', width =6, state = 'disabled', command = stop)
Reset=Tkinter.Button(SW, text = 'RESET', width = 6, state = 'disabled', command = lambda: reset(label))


SW.pack(anchor='center', pady=5)
Start.pack(side = 'left')
Stop.pack(side = 'left')
Reset.pack(side = 'left')

root.mainloop()

        
