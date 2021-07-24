from typing import Collection
from classes import*
from tkinter import * 
from tkinter import ttk
app = Tk()

#FUNÇOES------------------------------------------------------------------------------------------------------------------------------------------------------------------

def  salvar_dados():
        global nome_recuperado

        nome_recuperado = ent_produto.get()


def recuperar_dados():
        global nome_recuperado
        lbl_salvo['text'] = nome_recuperado
        
#LAYOUT------------------------------------------------------------------------------------------------------------------------------------------------------------------

app.title('CADASTRO DE PRODUTOS')
app.geometry("500x300")
app.configure(background="#D2EBEF")


#WIDGETS------------------------------------------------------------------------------------------------------------------------------------------------------------------

lbl_epaco = Label(app)
lbl_nomeprod = Label(app,text='Nome  ',background='#D2EBEF')
ent_produto = Entry()
lbl_categoria = Label(app,text='Categoria  ',background='#D2EBEF')
ent_produto = Entry()
lbl_salvo =  Label(app, text="nome do produto vai aparecer aqui")
cbb_categoria = ttk.Combobox(app,values=["padaria", "açougue","cereais","higiene","limpeza","biscoitos"])
lbl_preco = Label(app,text='Preço')
ent_preco = Entry()


#btn_enviar = Button(app,text="enviar",command=salvar_dados)

#btn_recuperar = Button(app,text="recuperar",command=recuperar_dados)

#GRID------------------------------------------------------------------------------------------------------------------------------------------------------------------

lbl_nomeprod.grid(column=0,row=1,sticky=W)
ent_produto.grid(column=1,row=1,sticky=W,padx=10,pady=10)
lbl_categoria.grid(column=0,row=3,sticky=W)
cbb_categoria.grid(column=1,row=3,sticky=W,padx=10,pady=10)
lbl_preco.grid(column=0,row=3,sticky=W)
#btn_enviar.grid(column=1,row=3)
#btn_recuperar.grid(column=1,row=5)
#lbl_salvo.grid(column=1,row=4)




app.mainloop()