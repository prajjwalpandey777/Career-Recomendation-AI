import tkinter as tk
from tkinter import ttk

# ----------- LOGIC -----------

def recommend_career(interest, math, communication, creativity):
    results = []

    # TECH
    if interest == "Coding" and math == "High":
        results.append(("Software Engineer", ["Python", "DSA", "Algorithms"]))

    if interest == "Coding" and communication in ["Medium", "High"]:
        results.append(("Data Scientist", ["Python", "ML", "Statistics"]))

    if interest == "Gaming":
        results.append(("Game Developer", ["Unity", "C#", "Game Design"]))

    # DESIGN
    if interest == "Design" and creativity == "High":
        results.append(("UI/UX Designer", ["Figma", "UX Design"]))

    # BUSINESS
    if interest == "Management":
        results.append(("Business Manager", ["Leadership", "Business Strategy"]))

    if interest == "Marketing":
        results.append(("Digital Marketer", ["SEO", "Social Media"]))

    if interest == "Entrepreneurship":
        results.append(("Entrepreneur", ["Startup Basics", "Finance"]))

    # FINANCE
    if interest == "Finance":
        results.append(("Financial Analyst", ["Excel", "Accounting"]))

    # MEDICAL
    if interest == "Biology":
        results.append(("Doctor", ["Biology", "Medical Studies"]))

    # EDUCATION
    if interest == "Teaching":
        results.append(("Teacher", ["Pedagogy", "Subject Knowledge"]))

    # CREATIVE
    if interest == "Writing":
        results.append(("Content Writer", ["Creative Writing", "SEO Writing"]))

    if interest == "Music":
        results.append(("Musician", ["Music Theory", "Instruments"]))

    # SOCIAL
    if interest == "Psychology":
        results.append(("Psychologist", ["Counseling", "Psychology"]))

    if interest == "Law":
        results.append(("Lawyer", ["Law Studies", "Legal Practice"]))

    # SPORTS
    if interest == "Sports":
        results.append(("Athlete", ["Physical Training", "Sports Science"]))

    # 🌱 AGRICULTURE (NEW)
    if interest == "Agriculture":
        if creativity == "high":
            results.append(("Agri-Entrepreneur", ["Organic Farming", "Agri-Business"]))
        else:
            results.append(("Agricultural Officer", ["Crop Science", "Soil Management"]))

    # Default fallback
    if not results:
        results.append(("General Suggestion", ["Explore skills", "Try internships"]))

    return results


# ----------- BUTTON FUNCTION -----------

def get_recommendation():
    interest = interest_var.get()
    math = math_var.get()
    communication = comm_var.get()
    creativity = creativity_var.get()

    results = recommend_career(interest, math, communication, creativity)

    output_box.config(state="normal")
    output_box.delete(1.0, tk.END)

    for career, courses in results:
        output_box.insert(tk.END, f"🎯 {career}\n", "title")
        for c in courses:
            output_box.insert(tk.END, f"   • {c}\n")
        output_box.insert(tk.END, "\n")

    output_box.config(state="disabled")


# ----------- MAIN WINDOW -----------

root = tk.Tk()
root.title("Career AI")
root.geometry("600x600")
root.configure(bg="#0f172a")  # deep navy

# ----------- TITLE -----------

title = tk.Label(root, text="🚀 Career Recommendation AI",
                 font=("Segoe UI", 18, "bold"),
                 bg="#0f172a", fg="#38bdf8")
title.pack(pady=15)

# ----------- CARD FRAME -----------

card = tk.Frame(root, bg="#1e293b", bd=0)
card.pack(pady=10, padx=20, fill="both")

# ----------- INPUTS -----------

def styled_label(text, row):
    tk.Label(card, text=text,
             bg="#1e293b", fg="white",
             font=("Segoe UI", 10)).grid(row=row, column=0, pady=8, padx=10, sticky="w")

def styled_combo(var, values, row):
    box = ttk.Combobox(card, textvariable=var, values=values, state="readonly")
    box.grid(row=row, column=1, pady=8, padx=10)
    box.set(values[0])


interest_var = tk.StringVar()
math_var = tk.StringVar()
comm_var = tk.StringVar()
creativity_var = tk.StringVar()

styled_label("Interest", 0)
styled_combo(interest_var, [
    "Coding", "Design", "Management", "Marketing",
    "Biology", "Finance", "Gaming", "Writing",
    "Psychology", "Agriculture", "Sports", "Music",
    "Law", "Entrepreneurship", "Teaching"
], 0)

styled_label("Math Skill", 1)
styled_combo(math_var, ["Low", "Medium", "High"], 1)

styled_label("Communication", 2)
styled_combo(comm_var, ["Low", "Medium", "High"], 2)

styled_label("Creativity", 3)
styled_combo(creativity_var, ["Low", "Medium", "High"], 3)

# ----------- BUTTON -----------

btn = tk.Button(root,
                text="✨ Get Recommendation",
                command=get_recommendation,
                bg="#38bdf8",
                fg="black",
                font=("Segoe UI", 11, "bold"),
                relief="flat",
                padx=10,
                pady=5)

btn.pack(pady=15)

# ----------- OUTPUT CARD -----------

output_frame = tk.Frame(root, bg="#1e293b")
output_frame.pack(padx=20, pady=10, fill="both", expand=True)

output_box = tk.Text(output_frame,
                     bg="#020617",
                     fg="white",
                     font=("Consolas", 10),
                     bd=0,
                     padx=10,
                     pady=10)

output_box.pack(fill="both", expand=True)
output_box.tag_config("title", foreground="#38bdf8", font=("Segoe UI", 11, "bold"))
output_box.config(state="disabled")

root.mainloop()