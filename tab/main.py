import tkinter
import tkinter.ttk


def create_frame(parent, text):
    frame = tkinter.Frame(parent)
    label = tkinter.Label(frame, text=text)
    label.pack()
    return frame


def main():
    root = tkinter.Tk()
    root.geometry("320x240")

    notebook = tkinter.ttk.Notebook(root)
    notebook.pack(fill=tkinter.BOTH, expand=True)

    frame1 = create_frame(notebook, "Frame 1")
    frame2 = create_frame(notebook, "Frame 2")

    notebook.add(frame1, text="Tab 1")
    notebook.add(frame2, text="Tab 2")

    root.mainloop()


if __name__ == "__main__":
    main()
