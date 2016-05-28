import Tkinter as tk
import tkMessageBox
#http://ygchan.blogspot.hk/2012/05/python-stop-watch-timer-source-code.html

def update_timeText():
    if (state):
        global timer
        timer[2] += 1

        if (timer[2] >= 100):
            timer[2] = 0
            timer[1] += 1

        if (timer[1] == 60):
            timer[1] = 0
            timer[0] += 1
        timelabel = pattern.format(timer[0], timer[1], timer[2])
        timeText.configure(text=timelabel)
    root.after(10, update_timeText)

def start_time():
    global state
    state = True

def pause():
    global state
    state = False

def reset():
    global timer
    timer = [0, 0, 0]
    timeText.configure(text='00:00:00')

def exist():
    root.destroy()

state = False

root = tk.Tk()
root.wm_title('Balance board stopwatch')
# Our time structure [min, sec, centsec]
timer = [0, 0, 0]
# The format is padding all the
pattern = '{0:02d}:{1:02d}:{2:02d}'

timeText = tk.Label(root, text="00:00:00", font=("Times", 150))
timeText.pack()

startButton = tk.Button(root, text='Start', command=start_time)
startButton.pack()

pauseButton = tk.Button(root, text='Pause', command=pause)
pauseButton.pack()

resetButton = tk.Button(root, text='Reset', command=reset)
resetButton.pack()

quitButton = tk.Button(root, text='Quit', command=exist)
quitButton.pack()

update_timeText()
root.mainloop()
