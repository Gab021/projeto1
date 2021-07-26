from typing import Collection
from classes import*
from tkinter import * 
from tkinter import ttk


#LAYOUT------------------------------------------------------------------------------------------------------------------------------------------------------------------
app = Tk()
app.title('CADASTRO DE PRODUTOS')
app.geometry("500x500")
app.configure(background="#D2EBEF")



global nome

#FUNÇOES------------------------------------------------------------------------------------------------------------------------------------------------------------------

def salvar_arquivo(): 
        print(ent_produto.get())
        '''with open('Produtos.txt','w+') as arquivo:
                arquivo.write(str(nome))'''



#WIDGETS------------------------------------------------------------------------------------------------------------------------------------------------------------------

ent_produto = Entry() ##

btn_salvar = Button(app, text ="Salvar", command = salvar_arquivo)


#print(nome)
#

#btn_enviar = Button(app,text="enviar",command=salvar_dados)

#btn_recuperar = Button(app,text="recuperar",command=recuperar_dados)

#GRID------------------------------------------------------------------------------------------------------------------------------------------------------------------





ent_produto.grid(column=1,row=1,sticky=W,padx=10,pady=10)#

btn_salvar.grid(column=4,row=20,sticky=W)

#btn_enviar.grid(column=1,row=3)
#btn_recuperar.grid(column=1,row=5)
#lbl_salvo.grid(column=1,row=4)




app.mainloop()