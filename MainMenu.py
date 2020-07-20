from  tkinter import *
from tkinter import messagebox
from SortingAlgorithm import *
from Backtrack.Knights_Tour import *
from Backtrack.N_queen import *
algotype=""
class second:
    def __init__(self,root):
        self.root = root
        self.root.geometry("650x300")
        self.root.resizable(False, False)
        self.root.title("Algorithm Visualizer")
        self.root.iconbitmap("hnet.com-image.ico")

        self.AlgoTypeLabel = Label(self.root, text='  Select Algorithm Type:-', font=("Courier", 10))
        self.AlgoTypeLabel.grid(row=0, column=0 ,pady=15)

        self.AlgoTypeVar = StringVar()
        self.AlgoTypeVar.set("Select Algorithm Type")
        self.AlgoTypeList = ["Select Algorithm Type", "Sorting Algorithm","Backtracking Algorithms"]
        self.AlgoTypeDrop = OptionMenu(self.root, self.AlgoTypeVar, *self.AlgoTypeList)
        self.AlgoTypeDrop.grid(row=1, column=0)

        self.StartButton = Button(self.root, text="Choose Algorithim Name", padx=5,command=self.run)
        self.StartButton.grid(row=8,column=1)
    def run(self):
        if self.AlgoTypeVar.get() == "Select Algorithm Type":
            messagebox.showerror("Incomplete Data!", "Please fill all the Fields to Start Visualization.")
        elif self.AlgoTypeVar.get() == "Sorting Algorithm":
            algotype="Sorting Algorithm"
            #print("Sorting Algorithm")
            self.root.destroy()
            me=Tk()
            temp=front(me,algotype)
        elif self.AlgoTypeVar.get() == "Backtracking Algorithms":
            algotype="Backtracking Algorithms"
            self.root.destroy()
            me=Tk()
            temp=front(me,algotype)
            return
class front:
    def sortmenu(self):
        self.AlgoNameLabel = Label(self.root, text=' Select Algorithm Name:-', font=("Courier", 10))
        self.AlgoNameLabel.grid(row=1, column=1)
        self.AlgoNameVar.set("Select Algorithm Name")
        self.AlgoNameList = ["Select Algorithm Name", "Bubble Sort","Insertion Sort","Selection Sort"]
        self.AlgoNameDrop = OptionMenu(self.root,self.AlgoNameVar,*self.AlgoNameList)
        self.AlgoNameDrop.grid(row=2, column=1)

        self.fill6 = Label(self.root, text="")
        self.fill6.grid(row=2, column=0)

        self.NoOfElementsLabel1 = Label(self.root, text="   Select Number of Elements:-", font=("Courier", 10))
        self.NoOfElementsLabel1.grid(row=3, column=0)
        self.NoOfElementsLabel2 = Label(self.root, text="(from 5 to 160)")
        self.NoOfElementsLabel2.grid(row=4, column=0)

        self.NoOfElementsSlider = Scale(self.root, from_= 5, to = 160, orient=HORIZONTAL, sliderlength=20, width=10)
        self.NoOfElementsSlider.grid(row=5, column=0)

        self.SpeedLabel1 = Label(self.root, text="Select Speed of Visualization:-", font=("Courier", 10))
        self.SpeedLabel1.grid(row=3, column=2)
        self.SpeedLabel2 = Label(self.root, text="(in Operations per sec.)")
        self.SpeedLabel2.grid(row=4,column=2)
        
        self.StartButton = Button(self.root, text="Back", padx=5,command=self.back)
        self.StartButton.grid(row=6,column=1)
        
        self.SpeedSlider = Scale(self.root, from_ = 1, to = 400, orient=HORIZONTAL, sliderlength=20, width=10)
        self.SpeedSlider.grid(row=5, column=2)

        self.fill1 = Label(self.root, text="")
        self.fill1.grid(row=6,column=0)
        self.fill2 = Label(self.root, text="")
        self.fill2.grid(row=7,column=0)

        self.StartButton = Button(self.root, text="::  Start Visualization  ::", padx=5,command=self.run)
        self.StartButton.grid(row=8,column=1)
    def backmenu(self):
        self.AlgoNameLabel = Label(self.root, text=' Select Algorithm Name:-', font=("Courier", 10))
        self.AlgoNameLabel.grid(row=1, column=1)

        self.AlgoNameVar = StringVar()
        self.AlgoNameVar.set("Select Algorithm Name")
        self.AlgoNameList = ["Select Algorithm Name","N- Queens","Knight's Tour"]
        self.AlgoNameDrop = OptionMenu(self.root,self.AlgoNameVar,*self.AlgoNameList)
        self.AlgoNameDrop.grid(row=2, column=1)

        self.fill6 = Label(self.root, text="")
        self.fill6.grid(row=2, column=0)

        self.NoOfElementsLabel1 = Label(self.root, text="   Select Grid Size:-", font=("Courier", 10))
        self.NoOfElementsLabel1.grid(row=3, column=0)
        self.NoOfElementsLabel2 = Label(self.root, text="(from 4 to 60)")
        self.NoOfElementsLabel2.grid(row=4, column=0)

        self.NoOfElementsSlider = Scale(self.root, from_= 4, to = 60, orient=HORIZONTAL, sliderlength=20, width=10)
        self.NoOfElementsSlider.grid(row=5, column=0)

        self.SpeedLabel1 = Label(self.root, text="Select Speed of Visualization:-", font=("Courier", 10))
        self.SpeedLabel1.grid(row=3, column=2)
        self.SpeedLabel2 = Label(self.root, text="(Slow(1) to Fast(10))")
        self.SpeedLabel2.grid(row=4,column=2)

        self.SpeedSlider = Scale(self.root, from_ = 1, to = 10, orient=HORIZONTAL, sliderlength=20, width=10)
        self.SpeedSlider.grid(row=5, column=2)
        
        self.StartButton = Button(self.root, text="Back", padx=5,command=self.back)
        self.StartButton.grid(row=6,column=1)
        
        self.fill1 = Label(self.root, text="")
        self.fill1.grid(row=6,column=0)
        self.fill2 = Label(self.root, text="")
        self.fill2.grid(row=7,column=0)

        self.StartButton = Button(self.root, text="::  Start Visualization  ::", padx=5,command=self.run)
        self.StartButton.grid(row=8,column=1)
    def back(self):
        self.root.destroy()
        me=Tk()
        se=second(me)
    def __init__(self,root,algotype=""):
        
        if(algotype==""):
            se=second(root)
        self.root=root
        self.algo=algotype
        self.root.geometry("650x300")
        self.root.resizable(False, False)
        self.root.title("Algorithm Visualizer")
        self.root.iconbitmap("hnet.com-image.ico")
        #me=Tk()
        self.AlgoNameVar = StringVar()
        self.NoOfElementsSlider=0
        self.SpeedSlider=0
        #print(algotype)
        if(algotype=="Sorting Algorithm"):
            self.sortmenu()
        if(algotype=="Backtracking Algorithms"):
            self.backmenu()

    def run(self):
        if self.algo == "Select Algorithm Type" or self.AlgoNameVar.get()=="Select Algorithm Type" :
            messagebox.showerror("Incomplete Data!", "Please fill all the Fields to Start Visualization.")

        elif self.algo == "Sorting Algorithm":
            self.temp1=self.NoOfElementsSlider.get()
            self.temp2=self.SpeedSlider.get()
            self.root.destroy()
            Sorting(self.temp1, self.temp2,self.AlgoNameVar.get())
        elif self.algo =="Backtracking Algorithms":
            if(self.AlgoNameVar.get()=="N- Queens"):
                temp=N_queen(self.NoOfElementsSlider.get(),1000//self.SpeedSlider.get())
            elif(self.AlgoNameVar.get()=="Knight's Tour"):
                temp=Knight(self.NoOfElementsSlider.get(),1000//self.SpeedSlider.get())
