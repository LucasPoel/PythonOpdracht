import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.yes_button = tk.Button(self, text="Yes", command=self.on_yes)
        self.no_button = tk.Button(self, text="No", command=self.on_no)

        self.yes_button.pack()
        self.no_button.pack()

    def on_yes(self):
        YesWindow(self)

    def on_no(self):
        NoWindow(self)

class YesWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.yes_button = tk.Button(self, text="Yes", command=self.on_yes)
        self.yes_button.pack()

    def on_yes(self):
        # Do something when the yes button is pressed
        pass

class NoWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        self.no_button = tk.Button(self, text="No", command=self.on_no)
        self.no_button.pack()

    def on_no(self):
        # Do something when the no button is pressed
        pass

if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
