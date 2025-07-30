from  tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    start.config(state=NORMAL)
    reset.config(state=DISABLED)
    if timer is not None:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start.config(state=DISABLED)
    reset.config(state=NORMAL)
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 1:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        check_marks.config(text="✓")
    else:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    minutes_left = math.floor(count/60)
    seconds_left = count % 60
    if seconds_left < 10:
        seconds_left = f"0{seconds_left}"
    canvas.itemconfig(timer_text, text=f"{minutes_left}:{seconds_left}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✓"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Pomodoro Timer/tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
check_marks.grid(column=1, row=3)


start = Button(text="Start", highlightthickness=0,highlightbackground=YELLOW,command=start_timer)
start.grid(column=0,row=2)

reset = Button(text="Reset",highlightthickness=0,highlightbackground=YELLOW,command=reset_timer)
reset.grid(column=2,row=2)
window.mainloop()

