import tkinter as tk
from tkinter import messagebox
import random

# Quiz Data
quiz_data = [
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Venus", "Jupiter"], "answer": "Mars"},
    {"question": "What is the largest ocean on Earth?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "Mark Twain", "Charles Dickens", "Jane Austen"], "answer": "William Shakespeare"},
    {"question": "What is the chemical symbol for Gold?", "options": ["Ag", "Au", "Gd", "Pt"], "answer": "Au"},
    {"question": "How many bones are in the adult human body?", "options": ["206", "201", "210", "190"], "answer": "206"},
    {"question": "What gas do plants absorb from the atmosphere?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "answer": "Carbon Dioxide"},
]

random.shuffle(quiz_data)
for q in quiz_data:
    random.shuffle(q["options"])

score = 0
question_index = 0
time_left = 10
timer_id = None  # to store after() callback ID

def load_question():
    global question_index, time_left, timer_id
    if question_index < len(quiz_data):
        q = quiz_data[question_index]
        question_label.config(text=q["question"])
        
        for i in range(4):
            option_buttons[i].config(text=q["options"][i], value=q["options"][i])
        
        selected_option.set(None)
        score_label.config(text=f"Score: {score}")
        
        # Reset timer
        if timer_id:
            window.after_cancel(timer_id)
        time_left = 10
        update_timer()
    else:
        show_result()

def update_timer():
    global time_left, timer_id
    timer_label.config(text=f"Time Left: {time_left}s")
    if time_left > 0:
        time_left -= 1
        timer_id = window.after(1000, update_timer)
    else:
        next_question()

def next_question():
    global question_index, score, timer_id
    if timer_id:
        window.after_cancel(timer_id)
    selected = selected_option.get()
    if selected == quiz_data[question_index]["answer"]:
        score += 1
    question_index += 1
    load_question()

def show_result():
    if timer_id:
        window.after_cancel(timer_id)
    messagebox.showinfo("Quiz Completed", f"Your Score: {score}/{len(quiz_data)}")
    window.destroy()

# GUI
window = tk.Tk()
window.title("Quiz App")
window.geometry("550x450")
window.config(bg="#f9f9f9")

title_label = tk.Label(window, text="QUIZ APP", font=("Arial", 20, "bold"), fg="#333", bg="#f9f9f9")
title_label.pack(pady=10)

score_label = tk.Label(window, text="Score: 0", font=("Arial", 12), bg="#f9f9f9", fg="#333")
score_label.pack()

timer_label = tk.Label(window, text="Time Left: 10s", font=("Arial", 12), bg="#f9f9f9", fg="red")
timer_label.pack(pady=5)

question_label = tk.Label(window, text="", font=("Arial", 14), wraplength=400, bg="#f9f9f9", fg="#222")
question_label.pack(pady=15)

selected_option = tk.StringVar()
option_buttons = []
for _ in range(4):
    btn = tk.Radiobutton(window, text="", variable=selected_option, font=("Arial", 12), bg="#ffffff",
                         fg="#333", selectcolor="#d1e7dd", padx=15, pady=5)
    btn.pack(anchor="w", padx=50, pady=5)
    option_buttons.append(btn)

next_btn = tk.Button(window, text="Next", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=12, command=next_question)
next_btn.pack(pady=20)

load_question()
window.mainloop()
