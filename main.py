from tkinter import *
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
    window.after_cancel(timer)
    #timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #title_label_ "Timer"
    label_timer.config(text="Timer")
    #reset check_marks
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 2 != 0:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)
    if reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Short Break", fg=PINK)
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Long Break", fg=RED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1 )
    else:
        start_timer()
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            new_text = symbol + "✔"
            check_mark.config(text=new_text)





# ---------------------------- UI SETUP ------------------------------- #

#Window
window = Tk()
window.title("Pomodoro")
window.config(padx=100 , pady=50, bg=YELLOW)

#Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

#Time
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#Timer as a label
label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold" ))
label_timer.grid(column=1, row=0 )

#Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)

start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

#Check mark as a label
symbol = "✔"
check_mark = Label(text="", fg=GREEN,bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()
