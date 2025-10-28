import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self) -> None:
        self.root = tk.Tk()  # creates top level widget aka main window of the app
        self.root.geometry("600x500")  # larger initial window size
        self.root.minsize(500, 400)  # minimum window size
        self.root.title("Modern Text App")  # updated title
        self.root.configure(bg="#f0f0f0")  # light gray background
        
        # Main container with padding
        self.mainframe = tk.Frame(self.root, bg="#ffffff", relief=tk.FLAT, bd=0)
        self.mainframe.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Configure grid weights for responsive layout
        self.mainframe.columnconfigure(0, weight=3)
        self.mainframe.columnconfigure(1, weight=1)
        self.mainframe.rowconfigure(0, weight=2)
        self.mainframe.rowconfigure(1, weight=0)
        self.mainframe.rowconfigure(2, weight=0)
        self.mainframe.rowconfigure(3, weight=0)
        self.mainframe.rowconfigure(4, weight=0)

        # Display area frame with border
        display_frame = tk.Frame(self.mainframe, bg="#ffffff", relief=tk.SOLID, bd=2, highlightbackground="#e0e0e0", highlightthickness=1)
        display_frame.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="NSEW", padx=10)
        display_frame.grid_propagate(False)
        
        # Main text label with modern styling
        self.text = tk.Label(
            display_frame,
            text="Sample Text",
            bg="#ffffff",
            fg="#2c3e50",
            font=("Helvetica", 36, "bold"),
            wraplength=550,
            justify="center"
        )
        self.text.place(relx=0.5, rely=0.5, anchor="center")

        # Section label for input
        input_label = tk.Label(
            self.mainframe,
            text="Text Input",
            bg="#ffffff",
            fg="#34495e",
            font=("Helvetica", 11, "bold")
        )
        input_label.grid(row=1, column=0, sticky="W", padx=10, pady=(0, 5))

        # Modern styled entry field
        self.set_text_field = ttk.Entry(self.mainframe, font=("Helvetica", 12))
        self.set_text_field.grid(row=2, column=0, pady=(0, 15), sticky="EW", padx=10)

        # Set text button with modern styling
        self.set_text_button = tk.Button(
            self.mainframe, 
            text="Set Text", 
            command=self.set_text,
            bg="#3498db",
            fg="white",
            font=("Helvetica", 11, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            padx=20,
            pady=10,
            activebackground="#2980b9",
            activeforeground="white"
        )
        self.set_text_button.grid(row=2, column=1, pady=(0, 15), padx=10, sticky="EW")
        self.set_text_button.bind("<Enter>", lambda e: self.set_text_button.config(bg="#2980b9"))
        self.set_text_button.bind("<Leave>", lambda e: self.set_text_button.config(bg="#3498db"))

        # Section label for color
        color_label = tk.Label(
            self.mainframe,
            text="Text Color",
            bg="#ffffff",
            fg="#34495e",
            font=("Helvetica", 11, "bold")
        )
        color_label.grid(row=3, column=0, sticky="W", padx=10, pady=(0, 5))

        # Expanded color options with more modern colors
        color_options = [
            "Red", "Blue", "Green", "Black", "White",
            "Purple", "Orange", "Pink", "Teal", "Navy",
            "Coral", "Indigo", "Crimson", "Gold", "Silver"
        ]
        
        # Style for combobox
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Modern.TCombobox', fieldbackground='white', background='white', foreground='#2c3e50')
        
        self.set_color_field = ttk.Combobox(
            self.mainframe, 
            values=color_options, 
            font=("Helvetica", 12),
            state="readonly",
            style='Modern.TCombobox'
        )
        self.set_color_field.grid(row=4, column=0, sticky="EW", pady=(0, 15), padx=10)
        self.set_color_field.set("Select a color")

        # Set color button
        self.set_color_button = tk.Button(
            self.mainframe, 
            text="Set Color", 
            command=self.set_color,
            bg="#9b59b6",
            fg="white",
            font=("Helvetica", 11, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            padx=20,
            pady=10,
            activebackground="#8e44ad",
            activeforeground="white"
        )
        self.set_color_button.grid(row=4, column=1, pady=(0, 15), padx=10, sticky="EW")
        self.set_color_button.bind("<Enter>", lambda e: self.set_color_button.config(bg="#8e44ad"))
        self.set_color_button.bind("<Leave>", lambda e: self.set_color_button.config(bg="#9b59b6"))

        # Reverse text button - full width
        self.reverse_button = tk.Button(
            self.mainframe, 
            text="🔄 Reverse Text", 
            command=self.reverse,
            bg="#e74c3c",
            fg="white",
            font=("Helvetica", 11, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            padx=20,
            pady=12,
            activebackground="#c0392b",
            activeforeground="white"
        )
        self.reverse_button.grid(row=5, column=0, columnspan=2, sticky="EW", pady=(5, 0), padx=10)
        self.reverse_button.bind("<Enter>", lambda e: self.reverse_button.config(bg="#c0392b"))
        self.reverse_button.bind("<Leave>", lambda e: self.reverse_button.config(bg="#e74c3c"))
        
        self.root.mainloop()
        return

    # functions to perform the button actions: set text, set color, reverse text
    def set_text(self):
        new_text = self.set_text_field.get()
        self.text.config(text=new_text)

    def set_color(self):
        new_color = self.set_color_field.get()
        self.text.config(foreground=new_color)

    def reverse(self):
        new_text = self.text.cget("text")
        reverse_text = new_text[::-1]
        self.text.config(text=reverse_text)


if __name__ != "__main__":
    pass
else:
    App()
