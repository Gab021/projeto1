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
        with open('Produtos.txt','a') as arquivo:
                arquivo.write(str(ent_produto.get()+';'))
                arquivo.write(str(cbb_categoria.get()+';'))
                arquivo.write(str(ent_preco.get()+';'))
                arquivo.write(str(ent_quantidade.get()+'\n'))

                


        arquivo.close      

def  salvar_dados():
        global nome_recuperado

        nome_recuperado = ent_produto.get()


def recuperar_dados():
        global nome_recuperado
        lbl_salvo['text'] = nome_recuperado
        

#WIDGETS------------------------------------------------------------------------------------------------------------------------------------------------------------------
lbl_espaco = Label(app)
lbl_nomeprod = Label(app,text='Nome  ',background='#D2EBEF')
ent_produto = Entry() ##
lbl_categoria = Label(app,text='Categoria  ',background='#D2EBEF')
lbl_salvo =  Label(app, text="nome do produto vai aparecer aqui")
cbb_categoria = ttk.Combobox(app,values=["padaria", "açougue","cereais","higiene","limpeza","biscoitos"])
lbl_preco = Label(app,text='Preço',background='#D2EBEF')
ent_preco = Entry()
lbl_quantidade = Label(app,text='Quantidade ',background='#D2EBEF')
ent_quantidade = Entry()
lbl_unidade = Label(app,text='Unidade ',background='#D2EBEF')
ent_unidade = Entry()
btn_salvar = Button(app, text ="Salvar", command = salvar_arquivo)


#print(nome)
#

#btn_enviar = Button(app,text="enviar",command=salvar_dados)

#btn_recuperar = Button(app,text="recuperar",command=recuperar_dados)

#GRID------------------------------------------------------------------------------------------------------------------------------------------------------------------




lbl_nomeprod.grid(column=0,row=1,sticky=W)
ent_produto.grid(column=1,row=1,sticky=W,padx=10,pady=10)#
lbl_categoria.grid(column=0,row=3,sticky=W)
cbb_categoria.grid(column=1,row=3,sticky=W,padx=10,pady=10)
lbl_preco.grid(column=0,row=6,sticky=W)
ent_preco.grid(column=1,row=6,sticky=W,padx=10,pady=10)
lbl_quantidade.grid(column=0,row=9,sticky=W)
ent_quantidade.grid(column=1,row=9,sticky=W,padx=10,pady=10)
lbl_unidade.grid(column=0,row=12,sticky=W)
ent_unidade.grid(column=1,row=12,sticky=W,padx=10,pady=10)
btn_salvar.grid(column=4,row=20,sticky=W)

#btn_enviar.grid(column=1,row=3)
#btn_recuperar.grid(column=1,row=5)
#lbl_salvo.grid(column=1,row=4)




app.mainloop()