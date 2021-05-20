#Naeemah Davis
#Easy Ticket- Ticket Sales
from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("600x700")
root.title("Ticket Sales")
root.config(bg= "black")
variable=StringVar(root)

class TicketSales():
    #variable going to be used as default value in  drop down menu
    variable.set("Select your choice")
    def __init__(self, window):
        #creating label on window
        self.lblCell = Label(window, text="Enter CellNumber: ", font="Arial 15", fg="white", bg="black")
        self.lblCell.place(x=40, y=60)
        self.lblCategory = Label(window, text="Select Ticket Category: ", font="Arial 15", fg="white", bg="black")
        self.lblCategory.place(x=40, y=120)
        self.lblTicket = Label(window, text="Number of Tickets Bought", font="Arial 15", bg="black", fg="white")
        self.lblTicket.place(x=40, y=180)
        #label that is going to be used to display the output
        self.Display = Label(window, bg="black", fg="light blue", font="Arial 15")
        self.Display.place(x=150, y=400, width=300, height=200)
        
        #creating an entry on window
        self.entry1 = Entry(window, bg="light blue")
        self.entry1.place(x=350, y=60, width= 200)
        
        #creating a menu thats going to display the options that can be selected in the menu
        self.menuCat = OptionMenu(window, variable, "Soccer", "Movies", "Theater")
        self.menuCat.place(x=350, y=120, width=200)
        
        #creating a spinbox so that the user can only choose from certain numbers # avoiding 
        self.spnbox = Spinbox(window, from_ =1, to= 500, bg="light blue")
        self.spnbox.place(x=400, y=180, width= 70, height= 30)
        
        self.btnCalc = Button(window, text= "Calculate Amount", font="Arial 15 ", command= self.Calculate)
        self.btnCalc.place(x=60, y=250)
        self.btnClear = Button(window, text="Clear", font= "Arial 15", bg="blue", fg="white", command= self.Clear)
        self.btnClear.place(x=400, y=250, width= 100)
#function that will calculate ticket prices and display them
    def Calculate(self):
        # option = self.Display['text'] =
        number = self.spnbox.get()
        try:

            if variable.get() == "Soccer":
                num = self.entry1.get()
                if len(self.entry1.get()) == 10 or num[0] == 0:
                    total = int(self.spnbox.get()) * 40
                    self.Display.config(text="Amount Payable: R" + str(total + (0.14 * total)) + "\n" +
                                             "Reservation for " + f' {variable.get()} ' + " for " + number + "\n" +
                                             "was done by " + self.entry1.get())
                else:
                    messagebox.showinfo("Error", "Input proper Cell Number!!")
                    self.entry1.delete(0, END)
                    self.spnbox.delete(0, END)
                    self.Display.config(text=" ")
            elif variable.get() == "Movies":
                num = self.entry1.get()
                if len(self.entry1.get()) == 10 or num[0] == 0:
                    total = int(self.spnbox.get()) * 75
                    self.Display.config(text="Amount Payable: R" + str(total + (0.14 * total)) + "\n" +
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
                    self.Display.config(text="Amount Payable: R" + str(total + (0.14 * total)) + "\n" +
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
        self.Display.config( text = " ")

objectSales = TicketSales(root)
root.mainloop()
