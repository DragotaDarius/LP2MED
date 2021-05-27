
from tkinter import *
import tkinter.ttk as ttk
import base64
import enigma
import Swap_chars

#define main application
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (PageOne, PageTwo,PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='NSEW')
        self.show_frame(PageOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#create page_one interface
class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    #create items (buttons, labels, forms)
    def make_widget(self):
        self.cvs = Canvas(self, width="500", height="140")
        ttk.Label(self, text='ENCODE DECODE', font='arial 20 bold').pack()
        ttk.Label(self, text='Dragota & Dumitrescu', font='arial 20 bold').pack(side=BOTTOM)
        self.cvs.pack() #show canvas

        # define variables of first algorithm
        Text = StringVar()
        private_key = StringVar()
        mode = StringVar()
        Result = StringVar()

        #######define function#####

        # function to encode - first agorithm
        def Encode(key, message):
            enc = []
            for i in range(len(message)):
                key_c = key[i % len(key)]
                enc.append(chr((ord(message[i]) + ord(key_c)) % 256))

            return base64.urlsafe_b64encode("".join(enc).encode()).decode()

        # function to decode
        def Decode(key, message):
            dec = []
            message = base64.urlsafe_b64decode(message).decode()
            for i in range(len(message)):
                key_c = key[i % len(key)]
                dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

            return "".join(dec)

        # Function to reset
        def Reset():
            Text.set("")
            private_key.set("")
            mode.set("")
            Result.set("")


        def encode_button():
            Result.set(Encode(private_key.get(), Text.get()))


        def decode_button():
            Text.set(Result.get())
            Result.set(Decode(private_key.get(), Text.get()))

        #################### Label and Button #############

        # Message
        Label(self, font='arial 12 bold', text='MESSAGE:').place(x=60, y=60)
        Label(self, font='arial 15 bold', text='BASE64').place(x=200, y=30)
        Entry(self, font='arial 10', textvariable=Text, bg='ghost white').place(x=290, y=60)

        # key
        Label(self, font='arial 12 bold', text='KEY:').place(x=60, y=90)
        Entry(self, font='arial 10', textvariable=private_key, bg='ghost white').place(x=290, y=90)

        # mode
        Label(self, font='arial 12 bold', text='MODE:').place(x=60, y=120)

        # result
        Entry(self, font='arial 10 bold', textvariable=Result, bg='ghost white').place(x=290, y=150)

        # encode button
        Button(self, font='arial 10 bold', text='ENCODE', padx=2, bg='deepskyblue', command=encode_button).place(x=290, y=115)

        # decode button
        Button(self, font='arial 10 bold', text='DECODE', padx=2, bg='deepskyblue', command=decode_button).place(x=370, y=115)

        # reset button
        Button(self, font='arial 10 bold', text='RESET', width=6, command=Reset, bg='salmon2', padx=2).pack(side=BOTTOM)

        # result label
        Label(self, font='arial 12 bold', text='RESULT:').place(x=60, y=150)

        Button(self, font='arial 10 bold', text="Enigma", fg="black", width="6", height="1", command=lambda: self.controller.show_frame(PageTwo)).place(x=0, y=0)
        Button(self, font='arial 10 bold', text="Swap", fg="black", width="6", height="1",command=lambda: self.controller.show_frame(PageThree)).place(x=60, y=0)


class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.make_widget()
    def make_widget(self):
        ttk.Label(self, text='ENCODE DECODE', font='arial 20 bold').pack()
        ttk.Label(self, text='Dragota & Dumitrescu', font='arial 20 bold').pack(side=BOTTOM)

        # define variables of second algorithm
        Text = StringVar()
        Result = StringVar()

        #pages
        Button(self, font='arial 10 bold', text="Base64", fg="black", width="5", height="1", command=lambda: self.controller.show_frame(PageOne)).place(x=0, y=0)
        Button(self, font='arial 10 bold', text="Swap", fg="black", width="6", height="1", command=lambda: self.controller.show_frame(PageThree)).place(x=52, y=0)

        #----BUTTONS-----
        # result
        Label(self, font='arial 12 bold', text='RESULT:').place(x=60, y=90)
        Entry(self, font='arial 10 bold', textvariable=Result, bg='ghost white').place(x=290, y=90)

        def encode_button():
            Result.set(enigma.enigma(Text.get()))

        def decode_button():
            Text.set(Result.get())
            Result.set(enigma.enigma(Text.get()))

        def Reset():
            Text.set("")
            Result.set("")

        # encode button
        Button(self, font='arial 10 bold', text='ENCODE', padx=2, bg='deepskyblue', command=encode_button).place(x=290, y=115)

        # decode button
        Button(self, font='arial 10 bold', text='DECODE', padx=2, bg='deepskyblue', command=decode_button).place(x=370, y=115)
        Label(self, font='arial 12 bold', text='MODE:').place(x=60, y=120)

        #result
        Button(self, font='arial 10 bold', text='RESET', width=6, command=Reset, bg='salmon2', padx=2).pack(side=BOTTOM)

        #Message
        Label(self, font='arial 12 bold', text='MESSAGE:').place(x=60, y=60)
        Label(self, font='arial 15 bold', text='ENIGMA').place(x=200, y=30)
        Entry(self, font='arial 10', textvariable=Text, bg='ghost white').place(x=290, y=60)

class PageThree(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.make_widget()

    def make_widget(self):
        ttk.Label(self, text='ENCODE DECODE', font='arial 20 bold').pack()
        ttk.Label(self, text='Dragota & Dumitrescu', font='arial 20 bold').pack(side=BOTTOM)

        # define variables of third algorithm
        Text = StringVar()
        Result = StringVar()

        # pages
        Button(self, font='arial 10 bold', text="Base64", fg="black", width="5", height="1", command=lambda: self.controller.show_frame(PageOne)).place(x=0, y=0)
        Button(self, font='arial 10 bold', text="Enigma", fg="black", width="6", height="1", command=lambda: self.controller.show_frame(PageTwo)).place(x=52, y=0)

        # ----BUTTONS-----
        # result
        Label(self, font='arial 12 bold', text='RESULT:').place(x=60, y=90)
        Entry(self, font='arial 10 bold', textvariable=Result, bg='ghost white').place(x=290, y=90)

        def encode_button():
            Result.set(Swap_chars.swap(Text.get()))

        def decode_button():
            Text.set(Result.get())
            Result.set(Swap_chars.swap(Text.get()))

        def Reset():
            Text.set("")
            Result.set("")

        # encode button
        Button(self, font='arial 10 bold', text='ENCODE', padx=2, bg='deepskyblue', command=encode_button).place(x=290, y=115)

        # decode button
        Button(self, font='arial 10 bold', text='DECODE', padx=2, bg='deepskyblue', command=decode_button).place(x=370, y=115)
        Label(self, font='arial 12 bold', text='MODE:').place(x=60, y=120)

        # result
        Button(self, font='arial 10 bold', text='RESET', width=6, command=Reset, bg='salmon2', padx=2).pack(side=BOTTOM)

        # Message
        Label(self, font='arial 12 bold', text='MESSAGE:').place(x=60, y=60)
        Label(self, font='arial 15 bold', text='SWAP').place(x=200, y=30)
        Entry(self, font='arial 10', textvariable=Text, bg='ghost white').place(x=290, y=60)



if __name__ == '__main__':
    app = App()
    app.title("Message Encode and Decode")
    app.mainloop()