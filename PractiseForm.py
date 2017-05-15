from tkinter import ttk
from tkinter import *

class Login(Tk):
    def __init__(self):
        super().__init__()
        self.uname_var = StringVar()
        self.pword_var = StringVar()
        self.init_widgets()

    def init_widgets(self):
        
        mainframe = ttk.Frame(self, padding='5 5')
        mainframe.grid(row=0, column=0, sticky=(N, E, S, W))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        
        ttk.Label(mainframe, text='Ime: ').grid(row=0, column=0, sticky=W)
        ttk.Label(mainframe, text='Sifra: ').grid(row=1, column=0, sticky=W)

        
        uname_entry = ttk.Entry(mainframe, width=20, textvariable=self.uname_var)
        uname_entry.grid(row=0, column=1, sticky=(E, W))
        pword_entry = ttk.Entry(mainframe, width=20, textvariable=self.pword_var, show = "*")
        pword_entry.grid(row=1, column=1, sticky=(E, W))

      
        ttk.Button(mainframe, text='Uloguj se ', command=self.check_login).grid(row=2, column=1, sticky=E,pady = 20)

        ttk.Button(mainframe, text='Novi nalog ', command=self.regObrazac).grid(row=2, column=0, sticky=E,pady = 20)

        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        uname_entry.focus()
        self.bind('<Return>', self.check_login)

    def check_login(self, *args):
        
        uname = self.uname_var.get()
        pword = self.pword_var.get()
        fajl = open(uname, "r")
        sadrzaj = fajl.read()
        fajl.close()
        pristup = "pristup"
        privilegija1 =  uname + pristup
        if  pword == sadrzaj:
            fajl3 = open(privilegija1, "r")
            pristup1 = fajl3.read()
            fajl3.close()
            if pristup1 == "Admin":
                noviPr2 = AdminForm()
                noviPr2.title("Admin")
                noviPr2.geometry("200x150")
            if pristup1 == "Gost":
                noviPr = GostForm()
                noviPr.title("Gost")
                noviPr.geometry("200x150")
            if pristup1 == "Korisnik":
                noviPr1 = KorisnikForm()
                noviPr1.title("Korisnik")
                noviPr1.geometry("200x150")
        else:
            print("Pogresili ste ime ili sifru.")

    def regObrazac(self,*args):
        noviPr1 = RegForma()
        noviPr1.title("Registracija ")
        noviPr1.geometry("250x200")

class RegForma(Toplevel):
    def __init__(self):
        super().__init__()
        self.novoI = StringVar()
        self.novaS = StringVar()
        self.radio1 = IntVar()
        self.radio2 = IntVar()
        self.init_widgets()

    def init_widgets(self):
        mainframe = ttk.Frame(self)
        mainframe.grid(column=0, row=0)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        
        ttk.Label(mainframe, text='Izaberite ime: : ').grid(row=0, column=0, sticky=W,pady = 5)
        ttk.Label(mainframe, text='Izaberite sifru : ').grid(row=1, column=0, sticky=W,pady = 5)

        
        novoIme = ttk.Entry(mainframe, width=20, textvariable=self.novoI)
        novoIme.grid(row=0, column=1 ,pady = 5)
        
        novaSifra = ttk.Entry(mainframe, width=20, textvariable=self.novaS)
        novaSifra.grid(row=1, column=1,pady = 5)
        
        ttk.Label(mainframe, text='Gost ').grid(row=2, column=0,sticky = E)
        ttk.Checkbutton(mainframe,variable = self.radio1).grid(row= 2,column = 1,sticky = W)

        ttk.Label(mainframe, text='Korisnik').grid(row=3, column=0,sticky = E)
        ttk.Checkbutton(mainframe,variable = self.radio2).grid(row= 3,column = 1,sticky = W)
         
        ttk.Button(mainframe, text='Registruj se ', command=self.save_Reg).grid(row=4, column=1, sticky=W,pady = 13)

    
           
          
    def save_Reg(self,*args):
        nI = self.novoI.get()
        nS = self.novaS.get()
        fajl1 = open(nI, "w")
        fajl1.write(nS)
        fajl1.close()

        pristup = "pristup"
        privG = self.radio1.get()
        privK = self.radio2.get()
        
        privilegija = nI + pristup
        
        if privG == 1 and privK == 0:
            fajl2 = open(privilegija, "w")
            fajl2.write("Gost")
            fajl2.close()
        if privG == 0 and privK == 1:
            fajl2 = open(privilegija, "w")
            fajl2.write("Korisnik")
            fajl2.close()
        
        noviPr4 = UspesnoReg()
        
        noviPr4.geometry("200x150")

class UspesnoReg(Toplevel):
    def __init__(self):
        super().__init__()
        self.init_widgets()
        

    def init_widgets(self):
        mainframe = ttk.Frame(self)
        mainframe.grid(column=0, row=0, sticky=(N, E, S, W))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        ttk.Label(mainframe, text='Uspesno ste se registrovali. ').grid(column=0, row=0,pady = 10 )
        ttk.Button(mainframe, text='Izadjite ', command = self.izadji).grid(column=0, row=1,pady = 30 )         

    def izadji(self):
        UspesnoReg.destroy(self)
        
         
         

class AdminForm(Toplevel):
    def __init__(self):
        super().__init__()
        self.init_widgets()

    def init_widgets(self):
        mainframe = ttk.Frame(self)
        mainframe.grid(column=0, row=0, sticky=(N, E, S, W))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        ttk.Label(mainframe, text='Ulogovali ste se kao admin. ').grid(column=0, row=0,pady = 10 )        
        
            

class GostForm(Toplevel):
    def __init__(self):
        super().__init__()
        self.init_widgets()

    def init_widgets(self):
        mainframe = ttk.Frame(self)
        mainframe.grid(column=0, row=0, sticky=(N, E, S, W))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        ttk.Label(mainframe, text='Ulogovali ste se kao gost. ').grid(column=0, row=0, pady = 10)

class KorisnikForm(Toplevel):
    def __init__(self):
        super().__init__()
        self.init_widgets()

    def init_widgets(self):
        mainframe = ttk.Frame(self)
        mainframe.grid(column=0, row=0, sticky=(N, E, S, W))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        ttk.Label(mainframe, text='Ulogovali ste se kao korisnik. ').grid(column=0, row=0, pady = 10 )


def main():
    root = Login()
    root.title("Login")
    root.mainloop()

if __name__ == '__main__': main()
