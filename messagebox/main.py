import tkinter
import tkinter.messagebox


def hello():
    tkinter.messagebox.showinfo(title="Greeting", message="Hello")


def main():
    root = tkinter.Tk()

    button = tkinter.Button(root, text="Click Me", command=hello)
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
