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
    #variable going to be used as default value in  drop down menu
    variable.set("Select your choice")
    def __init__(self, window):
<<<<<<< HEAD
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

=======
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
        
        #creating a spinbox so that the user can only choose from numbers # avoiding any incorrect input from the user 
        self.spnbox = Spinbox(window, from_ =1, to= 500, bg="light blue")
        self.spnbox.place(x=400, y=180, width= 70, height= 30)
        
        #button that will call the function that will calculate the cost of tickets and display it 
        self.btnCalc = Button(window, text= "Calculate Amount", font="Arial 15 ", command= self.Calculate)
        self.btnCalc.place(x=60, y=250)
        
        # button used to clear all input from the user
        self.btnClear = Button(window, text="Clear", font= "Arial 15", bg="blue", fg="white", command= self.Clear)
        self.btnClear.place(x=400, y=250, width= 100)
    #function that will calculate ticket prices and display them
>>>>>>> origin/main
    def Calculate(self):
        #defining a variable that will take in the value selected in the spinbox by the user
        number = self.spnbox.get()
        #making use of try except method to make sure the values inserted by the user are of correct type
        try:
            #if statement with what should happen when soccer is chosen by user
            if variable.get() == "Soccer":
                #variable that gets the value of the entry from user
                num = self.entry1.get()
                #if statement that will allow for if the number entered does begin with 0 and the length of the number enterd is a valid cell phone number
                if len(self.entry1.get()) == 10 or num[0] == 0:
                    #calculation for soccer tickets
                    total = int(self.spnbox.get()) * 40
<<<<<<< HEAD
                    self.Display.config(font="Arial 20", text="Amount Payable: R" + str(total + (0.14 * total)) + "\n" +
=======
                    #making the label created equal to the amount payable and the chosen values by the user
                    self.Display.config(text="Amount Payable: R" + str(total + (0.14 * total)) + "\n" +
>>>>>>> origin/main
                                             "Reservation for " + f' {variable.get()} ' + " for " + number + "\n" +
                                             "was done by " + self.entry1.get())
                else:
                    #if the number enterd isnt 10digits long or doesnt begin with 0 then the following will happen
                    #message box pop up 
                    messagebox.showinfo("Error", "Input proper Cell Number!!")
                    #clear the values enterd ny the user
                    self.entry1.delete(0, END)
                    self.spnbox.delete(0, END)
<<<<<<< HEAD
                    self.Display.config(text=" Ticket Booth ")
=======
                    self.Display.config(text=" ")
            # if the user chooses movies
>>>>>>> origin/main
            elif variable.get() == "Movies":
                #value of entry to be stored in num variable 
                num = self.entry1.get()
                ##if statement that will allow for if the number entered does begin with 0 and the length of the number enterd is a valid cell phone number
                if len(self.entry1.get()) == 10 or num[0] == 0:
                    #calculation for movie tickets
                    total = int(self.spnbox.get()) * 75
<<<<<<< HEAD
                    self.Display.config(font="Arial 20",text="Amount Payable: R" + str(total + (0.14 * total)) + "\n" +
=======
                     #making the label created equal to the amount payable and the chosen values by the user
                    self.Display.config(text="Amount Payable: R" + str(total + (0.14 * total)) + "\n" +
>>>>>>> origin/main
                                             "Reservation for " + f' {variable.get()} ' + " for " + number + "\n" +
                                             "was done by " + self.entry1.get())
                else:
                    #if the number entered isnt 10digits long or doesnt begin with 0 then the following will happen
                    #message box pop up 
                    messagebox.showinfo("Error", "Input proper Cell Number!!")
                    #clear the values enterd ny the user
                    self.entry1.delete(0, END)
                    self.spnbox.delete(0, END)
                    self.Display.config(text=" ")

            else:
                num = self.entry1.get()
                #if statement that will allow for if the number entered does begin with 0 and the length of the number enterd is a valid cell phone number
                if len(self.entry1.get()) == 10 or num[0] == 0:
                    #calculation for theater tickets
                    total = int(self.spnbox.get()) * 100
<<<<<<< HEAD
                    self.Display.config(font="Arial 20",text="Amount Payable: R" + str(total + (0.14 * total)) + "\n" +
=======
                    #making the label created equal to the amount payable and the chosen values by the user
                    self.Display.config(text="Amount Payable: R" + str(total + (0.14 * total)) + "\n" +
>>>>>>> origin/main
                                             "Reservation for " + f' {variable.get()} ' + " for " + number + "\n" +
                                             "was done by " + self.entry1.get())
                else:
                    #if the number entered isnt 10digits long or doesnt begin with 0 then the following will happen
                    #message box pop up
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
