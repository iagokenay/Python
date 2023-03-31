from tkinter import *
class janela:
    def __init__(self, toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()

        self.texto = Label(self.fr1,text='informe seu nome:')
        self.texto.pack()

        self.campo = Entry()
        self.campo.pack()

        self.botao = Button(self.fr1, text='okay', background= 'green', command=self.imprimir)
        self.botao.pack()

    def imprimir(self):
        print('####')
        print(self.campo.get())

       


raiz=Tk()
raiz.geometry('600x600')
janela(raiz)
raiz.mainloop()


