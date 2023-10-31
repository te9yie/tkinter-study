import tkinter
import tkinter.ttk


def main():
    root = tkinter.Tk()

    tree = tkinter.ttk.Treeview(root, columns=["Visible"])
    tree.heading("#0", text="TREE")
    tree.heading("#1", text="Visible")

    top = tree.insert("", tkinter.END, text="TOP", open=True, values=["True"])
    child1 = tree.insert(top, tkinter.END, text="CHILD #1", values=["True"])
    child2 = tree.insert(top, tkinter.END, text="CHILD #2", values=["False"])

    tree.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
