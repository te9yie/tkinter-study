import tkinter


def main():
    root = tkinter.Tk()
    root.geometry("320x240")

    tkinter.Label(root, text="LABEL 1", borderwidth=1, relief="raised").grid(
        row=0, column=0
    )
    tkinter.Label(root, text="LABEL 2", borderwidth=1, relief="raised").grid(
        row=0, column=1, sticky=tkinter.EW
    )
    tkinter.Label(root, text="LABEL 3", borderwidth=1, relief="raised").grid(
        row=0, column=2
    )
    tkinter.Label(root, text="LABEL 4", borderwidth=1, relief="raised").grid(
        row=1, column=0, columnspan=2, sticky=tkinter.EW
    )
    tkinter.Label(root, text="LABEL 5", borderwidth=1, relief="raised").grid(
        row=2, column=1, sticky=tkinter.NSEW
    )

    root.grid_columnconfigure(0, weight=0)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=0)
    root.grid_rowconfigure(0, weight=0)
    root.grid_rowconfigure(1, weight=0)
    root.grid_rowconfigure(2, weight=1)

    root.mainloop()


if __name__ == "__main__":
    main()
