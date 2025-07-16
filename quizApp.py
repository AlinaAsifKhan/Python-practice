import tkinter as tk
from tkinter import messagebox

# Quiz Data
quiz_data = [
    {"question": "What is the capital of France?", "options": ["Paris", "Rome", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "Which language is used for web development?", "options": ["Python", "HTML", "C++", "Java"], "answer": "HTML"},
    {"question": "What is 5 + 3?", "options": ["5", "8", "9", "7"], "answer": "8"},
]

# Global variables
score = 0
question_index = 0

# Functions
def load_question():
    global question_index
    if question_index < len(quiz_data):
        q = quiz_data[question_index]
        question_label.config(text=q["question"])
        
        # Update radio buttons with colors
        for i in range(4):
            option_buttons[i].config(text=q["options"][i], value=q["options"][i], bg="#ffffff", activebackground="#d1e7dd")
        
        selected_option.set(None)
    else:
        show_result()

def next_question():
    global question_index, score
    selected = selected_option.get()
    
    if not selected:
        messagebox.showwarning("Warning", "Please select an option!")
        return
    
    if selected == quiz_data[question_index]["answer"]:
        score += 1
    
    question_index += 1
    load_question()

def show_result():
    messagebox.showinfo("Quiz Completed", f"Your Score: {score}/{len(quiz_data)}")
    window.destroy()

# GUI Setup
window = tk.Tk()
window.title("Quiz App")
window.geometry("550x450")
window.config(bg="#f9f9f9")

# Title
title_label = tk.Label(window, text="QUIZ APP", font=("Arial", 20, "bold"), fg="#333", bg="#f9f9f9")
title_label.pack(pady=10)

# Question Label
question_label = tk.Label(window, text="", font=("Arial", 14), wraplength=400, bg="#f9f9f9", fg="#222")
question_label.pack(pady=15)

# Radio Buttons for Options
selected_option = tk.StringVar()
option_buttons = []

for _ in range(4):
    btn = tk.Radiobutton(window, text="", variable=selected_option, font=("Arial", 12), bg="#ffffff",
                         fg="#333", activeforeground="#000", selectcolor="#d1e7dd", padx=15, pady=5)
    btn.pack(anchor="w", padx=50, pady=5)
    option_buttons.append(btn)

# Next Button with hover effect
def on_hover(e):
    next_btn.config(bg="#45a049")

def on_leave(e):
    next_btn.config(bg="#4CAF50")

next_btn = tk.Button(window, text="Next", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white",
                     activebackground="#45a049", width=12, command=next_question)
next_btn.pack(pady=20)

# Bind hover
next_btn.bind("<Enter>", on_hover)
next_btn.bind("<Leave>", on_leave)

# Load first question
load_question()
window.mainloop()
