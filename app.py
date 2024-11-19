import tkinter as tk
from tkinter import messagebox
from jokes import search
from categories import CATEGORIES

# Function to get and display a joke
def get_joke():
    category = category_var.get().lower()  # Get selected category from dropdown
    if category not in CATEGORIES:
        messagebox.showerror("Error", "Invalid category selected!")
        return

    # Fetch joke and display it
    joke = search(category)
    joke_label.config(text=joke)

# Function to create a gradient background
def create_gradient(canvas, width, height, color1, color2):
    for i in range(height):
        r1, g1, b1 = app.winfo_rgb(color1)  # RGB values of color1
        r2, g2, b2 = app.winfo_rgb(color2)  # RGB values of color2
        r = int(r1 + (r2 - r1) * (i / height))
        g = int(g1 + (g2 - g1) * (i / height))
        b = int(b1 + (b2 - b1) * (i / height))
        hex_color = f"#{r >> 8:02x}{g >> 8:02x}{b >> 8:02x}"
        canvas.create_line(0, i, width, i, fill=hex_color)

# Create the main application window
app = tk.Tk()
app.title("Random Joke Generator")
app.geometry("600x500")
app.resizable(False, False)

# Create Canvas for Gradient Background
canvas = tk.Canvas(app, width=600, height=500)
canvas.pack(fill="both", expand=True)

# Create Gradient: Blue to White
create_gradient(canvas, 600, 500, "#87CEEB", "#FFFFFF")  # Sky Blue to White Gradient

# Title Label
title_label = tk.Label(
    app,
    text="Random Joke Generator",
    font=("Helvetica", 20, "bold"),
    bg="#87CEEB",  # Light sky blue
    fg="#333333",
)
title_label_window = canvas.create_window(300, 30, window=title_label)

# Category Selection
category_label = tk.Label(
    app,
    text="Select a Category:",
    font=("Times New Roman", 14, "italic"),
    bg="#87CEEB",
    fg="#333333",
)
category_label_window = canvas.create_window(300, 80, window=category_label)

# Dropdown Menu for Categories
category_var = tk.StringVar(value="misc")
category_dropdown = tk.OptionMenu(app, category_var, *CATEGORIES)
category_dropdown.configure(font=("Courier", 12), bg="#d3d3d3", fg="#333333")
category_dropdown_window = canvas.create_window(300, 120, window=category_dropdown)

# Button to Fetch Joke
fetch_button = tk.Button(
    app,
    text="Get Joke",
    font=("Verdana", 14, "bold"),
    bg="#add8e6",
    fg="#000000",
    command=get_joke,
)
fetch_button_window = canvas.create_window(300, 170, window=fetch_button)

# Label to Display Joke
joke_label = tk.Label(
    app,
    text="",
    wraplength=400,
    font=("Comic Sans MS", 16),
    justify="center",
    bg="#87CEEB",
    fg="#333333",
)
joke_label_window = canvas.create_window(300, 250, window=joke_label)

# Run the app
app.mainloop()
