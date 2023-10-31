import tkinter


class Canvas(tkinter.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.canvas = tkinter.Canvas(self, bg="#222")
        self.canvas.pack(fill=tkinter.BOTH, expand=True)

        self.line = self.canvas.create_line(100, 0, 100, 200, fill="#eb2")

        self.canvas.bind("<Motion>", self.on_motion)

    def on_motion(self, e):
        self.canvas.moveto(self.line, e.x, 0)


def main():
    root = tkinter.Tk()
    root.geometry("320x240")

    canvas = Canvas(root)
    canvas.pack(fill=tkinter.BOTH, expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
