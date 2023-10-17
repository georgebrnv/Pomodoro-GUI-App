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
REPS = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global REPS

    window.after_cancel(timer)
    timer_label.config(text="TIMER")
    canvas.itemconfig(countdown_text, text="00:00")
    check_mark.config(text="")
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global REPS
    REPS += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Timer function call
    if REPS % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(countdown_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        checkmarks = ""
        for _ in range(math.floor(REPS / 2)):
            checkmarks += "✓"
        check_mark.config(text=checkmarks)

        # Bring the window in front
        window.lift()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
countdown_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# "TIMER" label
timer_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

# Start button
start_button = Button(text="Start", highlightbackground=YELLOW, command=timer_start)
start_button.grid(column=0, row=2)

# Reset button
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

# Break check marks
check_mark = Label(text="", fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)


window.mainloop()
