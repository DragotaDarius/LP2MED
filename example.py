
from tkinter import *
import tkinter.ttk as ttk


class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='NSEW')
        self.show_frame(PageOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def make_widget(self):
        self.cvs = Canvas(self, width="800", height="600", background="#7ce577")
        """
        FIRST ROW BUTTONS
        """
        self.cvs.create_oval(50, 65, 250, 265, fill="#a0ccda", outline="#a0ccdb")
        self.cvs.create_text(148, 161, text="L", font="Arial 60 bold", state="normal")
        btnScott = Button(self.cvs, text="Lee", font="Arial 16", command="scott", bg="#a0ccda")
        btnScott.place(x=100, y=275, width="100", height="50")

        self.cvs.create_oval(295, 65, 495, 265, fill="#a0ccda", outline="#a0ccdb")
        self.cvs.create_text(395, 161, text="W", font="Arial 60 bold", state="normal")
        btnMan = Button(self.cvs, text="Wei Hong", font="Arial 16", command="man", bg="#a0ccda")
        btnMan.place(x=345, y=275, width="100", height="50")

        self.cvs.create_oval(540, 65, 740, 265, fill="#a0ccda", outline="#a0ccdb")
        self.cvs.create_text(640, 161, text="R", font="Arial 60 bold", state="normal")
        btnRof = Button(self.cvs, text="Rofieq", font="Arial 16", command="rof", bg="#a0ccda")
        btnRof.place(x=590, y=275, width="100", height="50")

        """
        SECOND ROW BUTTONS
        """
        self.cvs.create_oval(170, 340, 370, 540, fill="#a0ccda", outline="#a0ccdb")
        self.cvs.create_text(270, 435, text="E", font="Arial 60 bold", state="normal")
        btnYang = Button(self.cvs, text="En Yang", font="Arial 16", command="yang", bg="#a0ccda")
        btnYang.place(x=220, y=550, width="100", height="50")

        self.cvs.create_oval(420, 340, 620, 540, fill="#a0ccda", outline="#a0ccdb")
        self.cvs.create_text(520, 435, text="S", font="Arial 60 bold", state="normal")
        btnYun = Button(self.cvs, text="Sze Yun", font="Arial 16", command="yun", bg="#a0ccda")
        btnYun.place(x=470, y=550, width="100", height="50")

        # demo button to change page
        btnChange = Button(self.cvs, text="Change", font="Arial 16",
                           command=lambda: self.controller.show_frame(PageTwo),
                           bg="#a0ccda")
        btnChange .place(x=600, y=550, width="100", height="50")

        self.cvs.pack()

        def change_page(self):
            pass

class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def make_widget(self):
        ttk.Label(self, text='This is page two').grid(padx=(20,20), pady=(20,20))
        button1 = ttk.Button(self, text='Previous Page',
                             command=lambda: self.controller.show_frame(PageOne))
        button1.grid()


if __name__ == '__main__':
    app = MyApp()
    app.title('Multi-Page Test App')
    app.mainloop()