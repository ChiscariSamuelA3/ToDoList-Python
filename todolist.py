from tkinter import *
from time import *

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do-List")
        self.root.geometry('750x450+450+150')
        self.root.config(background = "yellow")

        self.label = Label(self.root, text = "To-Do-List",
                           font = 'Arial, 25 bold', width = 10, bd = 5, bg = 'blue', fg = 'orange')
        self.label.pack(side = 'top', fill = BOTH)

        self.label2 = Label(self.root, text = "Task control",
                           font = 'Arial, 15 bold', width = 10, bd = 5, bg = 'grey', fg = 'pink')
        self.label2.place(x = 65, y = 54)

        self.label3 = Label(self.root, text = "Tasks",
                            font = 'Arial, 15 bold', width = 10, bd = 5, bg = 'grey', fg = 'pink')
        self.label3.place(x=470, y = 54)

        self.listed_tasks = Listbox(self.root, height = 10, width = 25, bd = 5, font = 'ariel, 20 bold')
        self.listed_tasks.place(x = 340, y = 100)

        self.add_text = Text(self.root, height = 2, width = 30, bd = 5, font = 'ariel, 10 bold italic')
        self.add_text.place(x = 20, y = 120)

        #add task function

        def add_function():
            task = self.add_text.get(1.0, END)
            self.listed_tasks.insert(END, task)

            with open('savedlist.txt', 'a') as file:
                file.write(task)
                file.seek(0)
                file.close()

            self.add_text.delete(1.0, END)

        #delete task function

        def delete_function():
            delete_item = self.listed_tasks.curselection()
            selected_item = self.listed_tasks.get(delete_item)
            with open('savedlist.txt', 'r+') as file:
                lines = file.readlines()
                file.seek(0)
                task = str(selected_item)

                formatted_task = ""
                for i in task:
                    if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') or i == ' ':
                        formatted_task = formatted_task + i
                print(formatted_task)

                file.truncate(0)
                for line in lines:
                    if formatted_task not in line:
                        file.write(line)

            self.listed_tasks.delete(delete_item)

        with open('savedlist.txt', 'r') as file:
            lines = file.readlines()
            for i in lines:
                line = i.split()
                self.listed_tasks.insert(END, line)
            file.close()

        self.add_button = Button(self.root, text = "Add task",font = 'sarif, 15 bold',
                                 width = 9, bd = 5, bg = 'green', fg = 'white', command=add_function)
        self.add_button.place(x = 65, y = 180)

        self.delete_button = Button(self.root, text="Delete task", font='sarif, 15 bold',
                                 width=9, bd=5, bg='green', fg='white', command=delete_function)
        self.delete_button.place(x=65, y=390)


root = Tk()

time_label = Label(root, font=("Arial", 20), fg="black", bg="yellow")
time_label.place(x=45, y=250)

day_label = Label(root, font=("Ink Free", 20), bg="yellow")
day_label.place(x=64, y=280)

date_label = Label(root, font=("Arial bold", 15), bg="yellow")
date_label.place(x=31, y=315)

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    time_label.after(1000,update)

def main():

    ui = todo(root)

    update()

    root.mainloop()

if __name__ == "__main__":
    main()
