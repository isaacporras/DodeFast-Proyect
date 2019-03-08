from tkinter import *




class Gui:

    def __init__(self):
        self.MainWindow = Tk()

        ####################################  Centra la ventana  #######################################################

        w = 1003
        h = 773

        ws = self.MainWindow.winfo_screenwidth()
        hs = self.MainWindow.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)



        self.MainWindow.geometry('%dx%d+%d+%d' % (w, h, x, y))

        ################################################################################################################

        self.MainWindow.title("Dode Fast IDE")
        self.MainWindow.geometry("1003x773")

        # Inserta las dos areas de texto

        self.CodeTextArea = Text(self.MainWindow)
        self.CodeTextArea.place(x=21, y=84, width=748, height=423)

        self.OutputTextArea = Text(self.MainWindow)
        self.OutputTextArea.place(x=21, y=514, width=748, height=243)





        self.FileLabel = Label(self.MainWindow, text= "FILE")
        self.FileLabel.place(x=27, y=41)

        self.FileTextField = Entry(self.MainWindow)
        self.FileTextField.place(x=62, y=41, width=707,height=26)

        self.CompileButton = Button(self.MainWindow,text="COMPILE", command = self.compileButtonClick)
        self.CompileButton.place(x=798, y=84)

        self.MainWindow.mainloop()

    def compileButtonClick(self):

        print("Compile was clicked")

        self.setOutputText("hola\n'")

    def setOutputText(self, output):

        self.OutputTextArea.insert(END, output)

IDE = Gui()