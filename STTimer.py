from tkinter import *
import time
import random

let = ["R", "R'", "L", "L'", "U", "U'", "D", "D'", "F", "F'", "B", "B'", "R2", "L2", "U2", "F2", "D2", "B2"]
r, l, f, b, u, d = [["R", "R'", "R2"], ["L", "L'", "L2"], ["F", "F'", "F2"], ["B", "B'", "B2"], ["U", "U'", "U2"],
                    ["D", "D'", "D2"]]


def generate_scramble():
    global r, l, f, b, u, d, let
    scramble = ""
    prev = str(random.choice(let))
    prevlist = []
    for i in range(1, 22):
        k = 0
        while k == 0:
            if prev in r:
                prevlist = r.copy()
            elif prev in l:
                prevlist = l.copy()
            elif prev in f:
                prevlist = f.copy()
            elif prev in b:
                prevlist = b.copy()
            elif prev in u:
                prevlist = u.copy()
            elif prev in d:
                prevlist = d.copy()

            curr = str(random.choice(let))
            if curr in prevlist:
                continue
            else:
                scramble = scramble + " " + curr
                prev = curr
                k = 1
    return scramble


scrambles = str(generate_scramble())


def Main():
    global root

    root = Tk()
    root.title("ST Cubing")
    width = 600
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Top = Frame(root, width=600)
    Top.pack(side=TOP)
    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)
    Bottom = Frame(root, width=600)
    Bottom.pack(side=BOTTOM)
    Reset = Button(Bottom, text='Reset', font=("Avenir Next", 40), command=stopWatch.Reset, width=10, height=2)
    Reset.pack(side=LEFT)
    Exit = Button(Bottom, text='Close', font=("Avenir Next", 40), command=stopWatch.Exit, width=10, height=2)
    Exit.pack(side=RIGHT)
    Start = Button(Bottom, text='Start', font=("Avenir Next", 40), command=stopWatch.Start, width=10, height=2)
    Start.pack(side=LEFT)
    Stop = Button(Bottom, text='Stop', font=("Avenir Next", 40), command=stopWatch.Stop, width=10, height=2)
    Stop.pack(side=RIGHT)
    Scramble = Label(Top, text=scrambles, font=("Avenir Next", 15), width=150, height=2, fg="yellow", bg="gray10")
    Scramble.pack(side=TOP)
    Title = Label(Top, text="ST Cubing Timer", font=("Avenir Next", 150), fg="aqua", bg="gray10")
    Title.pack(fill=X)
    root.config(bg="gray10")
    root.mainloop()


class StopWatch(Frame):

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()

    def MakeWidget(self):
        timeText = Label(self, textvariable=self.timestr, font=("Avenir Next", 135), fg="yellow", bg="gray10")
        self.SetTime(self.nextTime)
        timeText.pack(fill=X, expand=YES)

    def Updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)

    def SetTime(self, nextElap):
        minutes = int(nextElap / 60)
        seconds = int(nextElap - minutes * 60.0)
        miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d.%02d' % (minutes, seconds, miliSeconds))

    def Start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1

    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0

    def Exit(self):
        root.destroy()
        exit()

    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)
        Main()


if __name__ == '__main__':
    Main()
