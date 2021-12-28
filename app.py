import tkinter as tk
from moviepy.editor import VideoFileClip
from PIL import Image, ImageTk # to display logo
from tkinter.filedialog import *
from tkinter import messagebox

root = tk.Tk() # window object. 

# Set size of Canvas
canvas = tk.Canvas(root, width=600, height=600)

# Logo
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(columnspan=2, row=0)

# Function to convert jpg to gif
def mp4_to_gif():
    
    # Get the input value for fps
    fps = fps_var.get()

    if fps > 0:
        # Import the mp4 from  folder
        import_filename = askopenfilename()
        if import_filename.endswith(".mp4"):
            clip = VideoFileClip(import_filename)
            clip.write_gif("app_low.gif", fps=fps)
            messagebox.showinfo("success ", "Your video has been converted into a GIF")
    else:
        messagebox.showerror(title="invalid entry", message="You must choose a number which is greater than 0")

# FPS entry
fps_var = tk.IntVar()
fps_label = tk.Label(root, text = "Choose FPS", font="Raleway")
fps_label.grid(column=0, row=2)
fps_entry = tk.Entry(root, textvariable=fps_var, font="Raleway")
fps_entry.grid(column=1, row=2)

# Instructions
instructions = tk.Label(root, text="Select a MP4 file on your computer", font="Raleway")
instructions.grid(column=0, row=3)

# Browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: mp4_to_gif(), font="Raleway", bg="#8c86fc", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=3)

root.mainloop()