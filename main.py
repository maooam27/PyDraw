import tkinter as tk
from tkinter import colorchooser


class App(tk.Tk):
    prevPoint = [0, 0]
    currentPoint = [0, 0]

    penColor = "black"
    stroke = 1

    canvas_data = []

    # Stroke size
    def stroke_increment(self):
        if self.stroke < 10:
            self.stroke += 1

    def stroke_decrement(self):
        if self.stroke > 1:
            self.stroke -= 1

    def stroke_default(self):
        self.stroke = 1

    def canvas_delete_all(self):
        self.canvas.delete("all")

    # Pencil
    def pencil(self):
        self.penColor = "black"
        self.canvas["cursor"] = "pencil"

    # Eraser
    def eraser(self):
        self.penColor = "white"
        self.canvas["cursor"] = tk.DOTBOX

    # Pencil Choose Color
    def color_choice(self):
        color = colorchooser.askcolor(title="Select a Color")
        self.canvas["cursor"] = "pencil"

        if color[1]:
            self.penColor = color[1]

        else:
            pass

    # Paint Function
    def paint(self, event):
        x = event.x
        y = event.y

        self.currentPoint = [x, y]

        if self.prevPoint != [0, 0]:
            self.canvas.create_polygon(
                self.prevPoint[0],
                self.prevPoint[1],
                self.currentPoint[0],
                self.currentPoint[1],
                fill=self.penColor,
                outline=self.penColor,
                width=self.stroke,
            )

        self.prevPoint = self.currentPoint

        if event.type == "5":
            self.prevPoint = [0, 0]

    def new_file(self):
        self.destroy()
        new_app = App()
        new_app.mainloop()

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

        self.holder.rowconfigure(0, minsize=30)

        # Create a label for the tools
        self.label123 = tk.Label(self.holder, text="TOOLS", borderwidth=1, relief=tk.SOLID, width=15)
        self.label123.grid(row=0, column=0)

        self.pencil_button = tk.Button(self.holder, text="Pencil", width=15, command=self.pencil)
        self.pencil_button.grid(row=1, column=0)
        self.eraser_button = tk.Button(self.holder, text="Eraser", width=15, command=self.eraser)
        self.eraser_button.grid(row=2, column=0)
        self.color_button = tk.Button(self.holder, text="Select Color", width=15, command=self.color_choice)
        self.color_button.grid(row=3, column=0)

        self.other_label = tk.Label(self.holder, text="OTHER", borderwidth=1, relief=tk.SOLID, width=15)
        self.other_label.grid(row=0, column=1)

        self.new_button = tk.Button(self.holder, text="New", width=15, command=self.new_file)
        self.new_button.grid(row=1, column=1)
        self.clear_button = tk.Button(self.holder, text="Clear", width=15, command=self.canvas_delete_all)
        self.clear_button.grid(row=2, column=1)
        self.exit_button = tk.Button(self.holder, text="Exit", width=15, command=self.destroy)
        self.exit_button.grid(row=3, column=1)

        self.stroke_label = tk.Label(self.holder, text="Stroke Size", borderwidth=1, relief=tk.SOLID, width=15)
        self.stroke_label.grid(row=0, column=2)

        self.increment_button = tk.Button(self.holder, text="Increment", width=15, command=self.stroke_increment)
        self.increment_button.grid(row=1, column=2)
        self.decrement_button = tk.Button(self.holder, text="Decrement", width=15, command=self.stroke_decrement)
        self.decrement_button.grid(row=2, column=2)
        self.default_button = tk.Button(self.holder, text="Default", width=15, command=self.stroke_default)
        self.default_button.grid(row=3, column=2)

        # Create a canvas
        self.frame2 = tk.Frame(self, height=500, width=1100)
        self.frame2.grid(row=1, column=0)

        # Making a Canvas
        self.canvas = tk.Canvas(self.frame2, height=450, width=1000, bg="white")
        self.canvas.grid(row=0, column=0, padx=50)
        self.canvas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.canvas.config(cursor="pencil")

        # Event Binding
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.paint)
        self.canvas.bind("<Button-1>", self.paint)

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
