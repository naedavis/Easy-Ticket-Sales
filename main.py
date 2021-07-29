#Naeemah Davis
#Easy Ticket- Ticket Sales
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("600x700")
root.title("Ticket Sales")
root.config(bg= "purple")
variable=StringVar(root)

class TicketSales():

    variable.set("Select your choice")
    def __init__(self, window):
        # self.default = StringVar()
        # self.lbltitle = Label(window, text="Ticket Booth ", font="Purisa 30", fg="white", bg="purple")
        # self.lbltitle.place(x=170, y=50)
        self.Display = Label(window,text="Ticket Booth", bg="purple", fg="white", font="Purisa 30")
        self.Display.place(x=100, y=70, width=400, height=200)
        self.lblCell = Label(window, text="Enter CellNumber: ", font="Arial 15", fg="white", bg="purple")
        self.lblCell.place(x=40, y=360)
        self.entry1 = Entry(window, bg="white")
        self.entry1.place(x=350, y=360, width= 200)
        self.lblCategory = Label(window, text="Select Ticket Category: ", font="Arial 15", fg="white", bg="purple")
        self.lblCategory.place(x=40, y=420)
        self.menuCat = OptionMenu(window, variable, "Soccer", "Movies", "Theater")
        self.menuCat.place(x=350, y=420, width=200)

        self.lblTicket = Label(window, text="Number of Tickets Bought", font="Arial 15", bg="purple", fg="white")
        self.lblTicket.place(x=40, y=480)
        self.spnbox = Spinbox(window, from_ =1, to= 500, bg="white")
        self.spnbox.place(x=400, y=480, width= 70, height= 30)
        self.btnCalc = Button(window, text= "Calculate Amount", font="Arial 15 ",fg="purple", bg="white", command= self.Calculate)
        self.btnCalc.place(x=60, y=550)
        self.btnClear = Button(window, text="Clear", font= "Arial 15",fg="purple", bg="white", command= self.Clear)
        self.btnClear.place(x=400, y=550, width= 100)


    def menOp(self):
        self.default.get()

    def Calculate(self):
        # option = self.Display['text'] =
        number = self.spnbox.get()
        try:

            if variable.get() == "Soccer":
                num = self.entry1.get()
                if len(self.entry1.get()) == 10 or num[0] == 0:
                    total = int(self.spnbox.get()) * 40
                    self.Display.config(font="Arial 20", text="Amount Payable: R" + str(total + (0.14 * total)) + "\n" +
                                             "Reservation for " + f' {variable.get()} ' + " for " + number + "\n" +
                                             "was done by " + self.entry1.get())
                else:
                    messagebox.showinfo("Error", "Input proper Cell Number!!")
                    self.entry1.delete(0, END)
                    self.spnbox.delete(0, END)
                    self.Display.config(text=" Ticket Booth ")
            elif variable.get() == "Movies":
                num = self.entry1.get()
                if len(self.entry1.get()) == 10 or num[0] == 0:
                    total = int(self.spnbox.get()) * 75
                    self.Display.config(font="Arial 20",text="Amount Payable: R" + str(total + (0.14 * total)) + "\n" +
                                             "Reservation for " + f' {variable.get()} ' + " for " + number + "\n" +
                                             "was done by " + self.entry1.get())
                else:
                    messagebox.showinfo("Error", "Input proper Cell Number!!")
                    self.entry1.delete(0, END)
                    self.spnbox.delete(0, END)
                    self.Display.config(text=" ")

            else:
                num = self.entry1.get()
                if len(self.entry1.get()) == 10 or num[0] == 0:
                    total = int(self.spnbox.get()) * 100
                    self.Display.config(font="Arial 20",text="Amount Payable: R" + str(total + (0.14 * total)) + "\n" +
                                             "Reservation for " + f' {variable.get()} ' + " for " + number + "\n" +
                                             "was done by " + self.entry1.get())
                else:
                    messagebox.showinfo("Error", "Input proper Cell Number!!")
                    self.entry1.delete(0, END)
                    self.spnbox.delete(0, END)
                    self.Display.config(text=" ")

        except ValueError:
            messagebox.showinfo("Error", "make sure all values are entered ")

    def Clear(self):
        self.entry1.delete(0,END)
        self.spnbox.delete(0, END)
        self.Display.config( text = " Ticket Booth ")


objectSales = TicketSales(root)
root.mainloop()
