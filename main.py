import tkinter as tk
from tkinter import ttk


class App:
    def __init__(self):
        self.root = tk.Tk()  # creates top level widget aka main window of the app
        self.root.geometry("400x400")  # window size
        self.root.title("Text App")  # title
        self.mainframe = tk.Frame(self.root, highlightbackground="white")
        self.mainframe.pack(fill="both", expand=True)

        self.text = ttk.Label(
            self.mainframe,
            text="Sample Text Gui",
            background="white",  # this seems to be dependent on the macOS them(light or dark)
            font=("Brass Mono", 30),
        )
        self.text.grid(row=0, column=0)  # positioning of Heading Area

        # creating and positioning the set text field
        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10, sticky="NWES")

        # create set text button
        set_text_button = ttk.Button(
            self.mainframe, text="Set Text", command=self.set_text
        )
        # set text button position
        set_text_button.grid(row=1, column=1, pady=10)

        # create and position set color button and dropdown options
        color_options = ["Red", "Blue", "Green", "Black", "White"]
        self.set_color_field = ttk.Combobox(self.mainframe, values=color_options)
        self.set_color_field.grid(row=2, column=0, sticky="NWES", pady=10)
        set_color_button = ttk.Button(
            self.mainframe, text="Set Color", command=self.set_color
        )
        set_color_button.grid(row=2, column=1, pady=10)

        # create and position reverse text button
        self.reverse_text = ttk.Button(
            self.mainframe, text="Reverse Text", command=self.reverse
        )
        self.reverse_text.grid(row=3, column=0, sticky="NWES", pady=10)
        self.root.mainloop()
        return

    # functions to perform the button actions: set text, set color, reverse text
    def set_text(self):
        newText = self.set_text_field.get()
        self.text.config(text=newText)

    def set_color(self):
        newColor = self.set_color_field.get()
        self.text.config(foreground=newColor)

    def reverse(self):
        newText = self.text.cget("text")
        reversed = newText[::-1]
        self.text.config(text=reversed)


if __name__ == "__main__":
    App()
