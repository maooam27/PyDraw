import tkinter as tk


class App(tk.Tk):

    def new_file(self):
        self.destroy()
        app = App()
        app.mainloop()

    def __init__(self):
        super().__init__()
        self.title("PyDraw")
        self.geometry("1000x700")
        self.resizable(False, False)

        self.frame = tk.Frame(self, width=1000, height=150, bg="white")
        self.frame.grid(row=0, column=0)

        # Create a canvas
        self.holder = tk.Frame(self.frame, height=120, width=900, bg="white", padx=6, pady=10)
        self.holder.grid(row=0, column=0, sticky=tk.NW)
        self.holder.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.holder.columnconfigure(0, minsize=120)
        self.holder.columnconfigure(1, minsize=120)
        self.holder.columnconfigure(2, minsize=120)
        self.holder.columnconfigure(3, minsize=120)
        self.holder.columnconfigure(4, minsize=120)

        self.holder.rowconfigure(0, minsize=30)

        # Create a label for the tools
        self.label123 = tk.Label(self.holder, text="TOOLS", borderwidth=1, relief=tk.SOLID, width=15)
        self.label123.grid(row=0, column=0)

        self.label456 = tk.Label(self.holder, text="TOOLS", borderwidth=1, relief=tk.SOLID, width=15)
        self.label456.grid(row=0, column=1)

        self.label789 = tk.Label(self.holder, text="TOOLS", borderwidth=1, relief=tk.SOLID, width=15)
        self.label789.grid(row=0, column=2)

        # Create menubar
        self.menubar = tk.Menu(self)

        # Add menus
        self.file_menu = tk.Menu(self.menubar, tearoff=False)

        # Add menu items
        self.file_menu.add_command(
            label="New",
            accelerator="Ctrl+N",
            command=self.new_file
        )

        self.file_menu.add_separator()
        self.file_menu.add_command(
            label="Quit",
            accelerator="Ctrl+Q",
            command=self.destroy
        )

        # Keybindings
        self.bind_all("<Control-n>", lambda e: self.new_file())
        self.bind_all("<Control-N>", lambda e: self.new_file())

        self.bind_all("<Control-q>", lambda e: self.destroy())
        self.bind_all("<Control-Q>", lambda e: self.destroy())

        self.menubar.add_cascade(label="File", menu=self.file_menu)

        self.config(menu=self.menubar)


if __name__ == "__main__":
    app = App()
    app.mainloop()
