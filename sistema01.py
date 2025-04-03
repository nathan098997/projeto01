from PIL import Image, ImageTk
import  customtkinter
from tkinter import ttk
import os
import sqlite3
from tkinter import END
 
item_selecionado= None
#-----------------------------------------------------------------import imagem (lixeira)----------------------------------------------------------------------------------
file_path=os.path.dirname(os.path.realpath(__file__))
image1=customtkinter.CTkImage(Image.open(fp="c:/Users/978776/OneDrive - SENAC em Minas - EDU/Imagens/images-removebg-preview.png"), size=(25,25))
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
 
#-------------------------------------------------------------------banco de dados-----------------------------------------------------------------------------
def criar_banco():
    conexao=sqlite3.connect("projeto.db")
    terminal_sql= conexao.cursor()
    terminal_sql.execute("CREATE TABLE IF NOT EXISTS tabela (nome text,preco float ,desc text,quantidade integer)")
    conexao.commit()
    conexao.close()
 
def salvar_dados():
    conexao=sqlite3.connect("projeto.db")
    entrada_nome = entrada_nome_produto_frame_cadastro.get()
    entrada_preco = entrada_preco_frame_cadastro.get()
    entrada_descricao= textbox_descricao_frame_cadastro.get("1.0","end")
    quant_cadastro ="0"
    terminal_sql= conexao.cursor()
    terminal_sql.execute(f"INSERT INTO tabela VALUES ('"+entrada_nome+"','"+entrada_preco+"','"+entrada_descricao+"','"+quant_cadastro+"')")
    conexao.commit()
    conexao.close()
    entrada_nome_produto_frame_cadastro.delete(0,END)
    entrada_preco_frame_cadastro.delete(0,END)
    textbox_descricao_frame_cadastro.delete("1.0","end")
 
def ler_dados():
    conexao=sqlite3.connect("projeto.db")
    terminal_sql= conexao.cursor()
    terminal_sql.execute("SELECT * FROM tabela ")
    recebe_dados=terminal_sql.fetchall()
 
    estoque_relatorio_estoque.delete(*estoque_relatorio_estoque.get_children())    
 
    nome =""
    preco =""
    descricao =""
    quantidade =""
 
    for i in recebe_dados:
 
        nome = str(i[0])
        preco = str(i[1])
        descricao = str(i[2])
        quantidade = str(i[3])
       
        estoque_relatorio_estoque.insert("","end", values=(nome,quantidade,preco,descricao))    
 
    conexao.close()
criar_banco()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 
 
#--------------------------------funções---------------------------------
def cadastro():
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_entrada.grid_forget()
    frame_saida.grid_forget()
    frame_editar.grid_forget()
    frame_cadastro.grid(row = 0, column = 1, padx = 10, pady=10)
    frame_cadastro.grid_propagate(False)
 
def editar():
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_entrada.grid_forget()
    frame_saida.grid_forget()
    frame_cadastro.grid_forget()
    frame_editar.grid(row = 0, column = 1, padx = 10, pady=10)
    frame_editar.grid_propagate(False)
    editar_banco_dados()
 
def saida():
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_entrada.grid_forget()
    frame_cadastro.grid_forget()      
    frame_editar.grid_forget()
    frame_saida.grid(row = 0, column = 1, padx = 10, pady=10)
    frame_saida.grid_propagate(False)
    saida_banco_dados()
 
def entrada():
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_saida.grid_forget()
    frame_cadastro.grid_forget()      
    frame_editar.grid_forget()
    frame_entrada.grid(row = 0, column = 1, padx = 10, pady=10)
    frame_entrada.grid_propagate(False)
    entrada_banco_dados()
 
def relatorio_estoque():
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_saida.grid_forget()
    frame_cadastro.grid_forget()      
    frame_editar.grid_forget()
    frame_relatorio_estoque.grid(row = 0, column = 1, padx = 10, pady=10)
    frame_relatorio_estoque.grid_propagate(False)
    ler_dados()
 
def relatorio_saida():
    frame_relatorio_entrada.grid_forget()
    frame_entrada.grid_forget()
    frame_saida.grid_forget()
    frame_cadastro.grid_forget()      
    frame_editar.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_saida.grid(row = 0, column = 1, padx = 10, pady=10)
    frame_relatorio_saida.grid_propagate(False)
 
def relatorio_entrada():
    frame_relatorio_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_saida.grid_forget()
    frame_cadastro.grid_forget()      
    frame_editar.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_entrada.grid(row = 0, column = 1, padx = 10, pady=10)
    frame_relatorio_entrada.grid_propagate(False)
 
#------------------------------------------------------------------------------------------------------------------------------------------------------------
 
def editar_banco_dados():
    global items, check_var
    conexao = sqlite3.connect("projeto.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"SELECT nome FROM tabela")
    items = terminal_sql.fetchall()
    check_var = customtkinter.StringVar(value="on")
    for item in scrollable_frame_editar.winfo_children():
        item.destroy()
 
    for item in items:
        nome = str(item[0])
        itens = []
        itens.append(nome)
 
 
        for item in itens:
           
            box = customtkinter.CTkCheckBox(scrollable_frame_editar, text=item, command=lambda: seleciona_item() if
            check_var.get() else None, variable=check_var, onvalue=item, offvalue="")
            box.pack(pady=5, padx=5, fill="x")
    conexao.close()
#------------------------------------------------------------------------------------------------------------------------------------------------------------
 
def saida_banco_dados():
    global items, check_var
    conexao = sqlite3.connect("projeto.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"SELECT nome FROM tabela")
    items = terminal_sql.fetchall()
    check_var = customtkinter.StringVar(value="on")
    for item in scrollable_buscar_produto_frame_saida.winfo_children():
        item.destroy()
 
    for item in items:
        nome = str(item[0])
        itens = []
        itens.append(nome)
        for item in itens:
           
            box_saida = customtkinter.CTkCheckBox(scrollable_buscar_produto_frame_saida, text=item, command=lambda: seleciona_item() if
            check_var.get() else None, variable=check_var, onvalue=item, offvalue="")
            box_saida.pack(pady=5, padx=5, fill="x")
    conexao.close()
#------------------------------------------------------------------------------------------------------------------------------------------------------------
 
def entrada_banco_dados():
    global items, check_var
    conexao = sqlite3.connect("projeto.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"SELECT nome FROM tabela")
    items = terminal_sql.fetchall()
    check_var = customtkinter.StringVar(value="on")
    for item in scrollable_buscar_produto_frame_entrada.winfo_children():
        item.destroy()
 
    for item in items:
        nome = str(item[0])
        itens = []
        itens.append(nome)
        for item in itens:
       
            box_entrada = customtkinter.CTkCheckBox(scrollable_buscar_produto_frame_entrada, text=item, command=lambda: seleciona_item()
            if check_var.get() else None, variable=check_var, onvalue=item, offvalue="")
            box_entrada.pack(pady=5, padx=5, fill="x")
 
    conexao.close()
#-------------------------------------------------------------selecionar checkbox item da tela editar-----------------------------------------------------------------------------------------------
nome_antigo_editar=None
 
def seleciona_item():
    global nome_antigo_editar
    valor_checkbox = check_var.get()
 
    conexao = sqlite3.connect("projeto.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"SELECT * FROM tabela WHERE nome = '{valor_checkbox}'")
    receber_dados_produtos = terminal_sql.fetchall()
    entrada_nome_produto_frame_editar.delete(0, 'end')
    entrada_preco_frame_editar.delete(0, 'end')
    textbox_descricao_frame_editar.delete("1.0", 'end')
 
    entrada_nome_produto_frame_editar.insert(0, receber_dados_produtos[0][0])
    entrada_preco_frame_editar.insert(0, receber_dados_produtos[0][1])
    textbox_descricao_frame_editar.insert("0.0", receber_dados_produtos[0][2])
 
    nome_antigo_editar = receber_dados_produtos[0][0]
#------------------------------------------------------funcionalidades dos 3 botes da tela editar------------------------------------------------------------------------------------------------------
def excluir (valor_checkbox):
    conexao = sqlite3.connect("projeto.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"DELETE FROM tabela WHERE nome = '{valor_checkbox}'")
    conexao.commit()
    conexao.close()
    entrada_nome_produto_frame_editar.delete(0,"end")
    entrada_preco_frame_editar.delete(0,"end")
    textbox_descricao_frame_editar.delete("1.0","end")
    editar_banco_dados()
 
def salvar_edicao(nome_produto,preco_produto,descricao):
    global nome_antigo_editar
    conexao = sqlite3.connect("projeto.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"UPDATE tabela SET nome ='{nome_produto}', preco ='{preco_produto}', desc ='{descricao}' WHERE nome = '{nome_antigo_editar}'")
    conexao.commit()
    conexao.close()
    entrada_nome_produto_frame_editar.delete(0,"end")
    entrada_preco_frame_editar.delete(0,"end")
    textbox_descricao_frame_editar.delete("1.0","end")
    editar_banco_dados()
 
def cancelar_edicao():
    entrada_nome_produto_frame_editar.delete(0,"end")
    entrada_preco_frame_editar.delete(0,"end")
    textbox_descricao_frame_editar.delete("1.0","end")
#--------------------------------------------------------------------------------------------------------
#---------------------------------------------funcionalidades da tela entrada----------------------------------------------------
#--------------------------------------------------------------------------------------------------------
 
 
 
#-----------------------------------janela do botão exportar--------------------------------------------------------
def exportar():
    janela_exportar = customtkinter.CTkToplevel()
    janela_exportar.attributes('-topmost',True)
    janela_exportar.title("")
    janela_exportar.geometry('500x252')
#------------------------------------------------frame da janela exportar--------------------------------------------------
    frame_exportar =customtkinter.CTkFrame(janela_exportar, width=500, height=250, corner_radius= 20, border_color= '#0070ff', border_width=2 )
    frame_exportar.grid(pady=0, padx=0,row=0,column=0, rowspan = 5)
    frame_exportar.grid_propagate(False)
 
    titulo_escolha_relatorio_frame_exportar=customtkinter.CTkLabel(frame_exportar, text="Escolher relatório(s):", font=("arial",20,"bold"))
    titulo_escolha_relatorio_frame_exportar.grid(row=0,pady=10, padx=20, column=0, sticky="w")
 
    titulo_escolha_extencao_frame_exportar=customtkinter.CTkLabel(frame_exportar, text="Escolher extensão:", font=("arial",20,"bold"))
    titulo_escolha_extencao_frame_exportar.grid(row=0, pady=10, padx=20, column=1, sticky="w")
 
    box_exportar_estoque_janela_exportar = customtkinter.CTkCheckBox(frame_exportar, text="exportar estoque")
    box_exportar_estoque_janela_exportar.grid(row=1, pady=10, padx=20, column=0, sticky="w")
 
    box_exportar_saida_janela_exportar = customtkinter.CTkCheckBox(frame_exportar, text="Exportar saida")
    box_exportar_saida_janela_exportar.grid(row=2, pady=10, padx=20, column=0, sticky="w")
 
    box_exportar_entrada_janela_exportar = customtkinter.CTkCheckBox(frame_exportar, text="Exportar entrada")
    box_exportar_entrada_janela_exportar.grid(row=3, pady=10, padx=20, column=0, sticky="w")
 
    box_extencao_word_janela_exportar = customtkinter.CTkCheckBox(frame_exportar, text="Word")
    box_extencao_word_janela_exportar.grid( row=1,pady=10, padx=20, column=1, sticky="w")
 
    box_extencao_pdf_janela_exportar = customtkinter.CTkCheckBox(frame_exportar, text="PDF")
    box_extencao_pdf_janela_exportar.grid( row=2,pady=10, padx=20, column=1, sticky="w")
 
    box_extencao_excel_janela_exportar = customtkinter.CTkCheckBox(frame_exportar, text="Excel")
    box_extencao_excel_janela_exportar.grid( row=3,pady=10, padx=20, column=1, sticky="w")
 
    botao_cancelar_janela_exportar=customtkinter.CTkButton(frame_exportar, text="cancelar", width=80, corner_radius= 20,fg_color="#0070ff")
    botao_cancelar_janela_exportar.grid(row=4,pady=10, padx=20, column=1, sticky="w" )
 
    botao_salvar_janela_exportar=customtkinter.CTkButton(frame_exportar, text="salvar", width=80, corner_radius= 20,fg_color="#0070ff")
    botao_salvar_janela_exportar.grid(row=4,pady=10, padx=20, column=1 , sticky="e")
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 
 
#----------------------------------------------------------------------------imagem da lixeira------------------------------------------------------------------------
def delete_itens(linhas, botoes):
    linhas.grid_forget()
    botoes.grid_forget()
 
linha=0
def adicionar_item():
    global linha
    item_vet=str(entrada_quantidade_frame_saida.get())
    linha += 1
 
    if item_vet in items:
        try:    
            label = customtkinter.CTkLabel(scrollable_adicionar_frame_saida, text=item_vet, anchor="w")            
            label.grid(row=linha, column=0, pady=5, padx=5)    
            lixeira = customtkinter.CTkButton(scrollable_adicionar_frame_saida, width=25, height=25, text="", image=image1, command=lambda: delete_itens(label, lixeira))
            lixeira.grid(row=linha, column=1, pady=5, padx=80, sticky="e")
        except ValueError:
            return
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
 
 
 
#-----------------------------janela principal----------------------------
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
 
janela =customtkinter.CTk()
janela.title("")
janela.geometry('820x420')
#-------------------------------------------------------------------------
 
 
 
#------------------------------------------------------------cor das tabelas--------------------------------------------------------------------
style = ttk.Style(master=janela)
style.theme_use('clam')
style.configure("Treeview", background="#3484F0", fieldbackground="#393939", foreground="white",rowheight=25,bordercolor="white", )
style.configure("Treeview.Heading",background="#565b5e",foreground="white",relief="flat")
style.map("Treeview.Heading",background=[('active', '#323232')])
#------------------------------------------------------------------------------------------------------------------------------------------------
 
 
 
#--------------------------------------------------------------frame do menu------------------------------------------------------------------
frame_menu =customtkinter.CTkFrame(master=janela, width=190, height=400, corner_radius= 20, border_color= '#0070ff', border_width=2 )
frame_menu.grid(row = 0, column = 0,padx = 10, pady=10)
frame_menu.pack_propagate(False)
 
nome_do_siatema_frame_menu = customtkinter.CTkLabel(frame_menu, text="Micael bozó", font=("arial",20,"bold"))
nome_do_siatema_frame_menu.pack(pady=40)
 
botao_cadastro_frame_menu = customtkinter.CTkButton(frame_menu, corner_radius= 20, text='cadastrar',fg_color="#0070ff", command=cadastro)
botao_cadastro_frame_menu.pack(pady=5)
 
botao_editar_frame_menu =customtkinter.CTkButton(frame_menu, corner_radius= 20, text='editar',fg_color="#0070ff", command = editar )
botao_editar_frame_menu.pack(pady=5)
 
botao_saida_frame_menu = customtkinter.CTkButton(frame_menu, corner_radius= 20,text='saída',fg_color="#0070ff", command= saida)
botao_saida_frame_menu.pack(pady=5)
 
botao_entrada_frame_menu =customtkinter.CTkButton(frame_menu, corner_radius= 20, text='entrada',fg_color="#0070ff", command=entrada)
botao_entrada_frame_menu.pack(pady=5)
 
botao_relatorio_frame_menu =customtkinter.CTkButton(frame_menu, corner_radius= 20,text='relatorio',fg_color="#0070ff", command=relatorio_estoque)
botao_relatorio_frame_menu.pack(pady=5)
#----------------------------------------------------------------------------------------------------------------------------------------------
 
 
 
#------------------------------------------------------------------frame do cadastro------------------------------------------------------------------
frame_cadastro =customtkinter.CTkFrame(master=janela, width=590, height=400, corner_radius= 20, border_color= '#0070ff', border_width=2 )
frame_cadastro.grid(row = 0, column = 1, padx = 10, pady=10)
frame_cadastro.grid_propagate(False)
 
titulo_frame_cadastro = customtkinter.CTkLabel(frame_cadastro, text="Cadastro do produto", font=("arial",20,"bold"))
titulo_frame_cadastro.grid(row = 0, column = 1, padx = 10, pady=10)
 
texto_nome_produto_frame_cadastro = customtkinter.CTkLabel(frame_cadastro, text="Nome do produto:")
texto_nome_produto_frame_cadastro.grid(row = 1, column = 0, padx = 10, pady=10)
 
texto_preco_frame_cadastro = customtkinter.CTkLabel(frame_cadastro, text="Preço(R$):")
texto_preco_frame_cadastro.grid(row = 2, column = 0, padx = 10, pady=10 ,  sticky ="e")
 
texto_descricao_frame_cadastro = customtkinter.CTkLabel(frame_cadastro, text="Descrição:")
texto_descricao_frame_cadastro.grid(row = 3, column = 0, padx = 10, pady=10,  sticky ="e,n")
 
entrada_nome_produto_frame_cadastro=customtkinter.CTkEntry(frame_cadastro, placeholder_text="informe o nome do produto:", width=300, border_color= '#0070ff', border_width=2)
entrada_nome_produto_frame_cadastro.grid(row = 1, column = 1, padx = 10, pady=10)
 
entrada_preco_frame_cadastro=customtkinter.CTkEntry(frame_cadastro, placeholder_text="R$:", width=80, border_color= '#0070ff', border_width=2)
entrada_preco_frame_cadastro.grid(row = 2, column = 1, padx = 10, pady=10, sticky ="w")
 
textbox_descricao_frame_cadastro=customtkinter.CTkTextbox(master=frame_cadastro,  width=300, height=80, border_color= '#0070ff', border_width=2)
textbox_descricao_frame_cadastro.grid(row = 3, column = 1, padx = 10, pady=10)
 
botao_salvar_frame_cadastro = customtkinter.CTkButton(master=frame_cadastro,  corner_radius= 20, text='Salvar',fg_color="#0070ff", command=salvar_dados)
botao_salvar_frame_cadastro.grid(row = 4, column = 1, padx = 10, pady=10, sticky ="e")
#----------------------------------------------------------------------------------------------------------------------------------------------
 
 
 
#------------------------------------------------------------------frame do editar------------------------------------------------------------------
frame_editar =customtkinter.CTkFrame(master=janela, width=590, height=400, corner_radius= 20, border_color= '#0070ff', border_width=2 )
frame_editar.grid_propagate(False)
 
scrollable_frame_editar = customtkinter.CTkScrollableFrame(frame_editar)
scrollable_frame_editar.grid(pady=17, padx=10,row=2,column=0, rowspan = 5, sticky ="w")
 
titulo_frame_editar = customtkinter.CTkLabel(frame_editar, text="Editar", font=("arial",20,"bold"))
titulo_frame_editar.grid(row = 0, column = 0, padx = 10, pady=10, columnspan=4)
 
entrada_buscar_produto_frame_editar=customtkinter.CTkEntry(frame_editar, placeholder_text="Buscar produto:", width=223, border_color= '#0070ff', border_width=2)
entrada_buscar_produto_frame_editar.grid(row = 1, column = 0, padx = 10, pady=0, sticky ="w,s")
 
entrada_nome_produto_frame_editar=customtkinter.CTkEntry(frame_editar, placeholder_text="Nome do produto:", width=300, border_color= '#0070ff', border_width=2)
entrada_nome_produto_frame_editar.grid(row = 2, column = 1, padx = 5, pady=15, sticky ="sw")
 
entrada_preco_frame_editar=customtkinter.CTkEntry(frame_editar, placeholder_text="R$:", width=80, border_color= '#0070ff', border_width=2)
entrada_preco_frame_editar.grid(row = 3, column = 1, padx = 5, pady=0, sticky ="nw")
 
textbox_descricao_frame_editar=customtkinter.CTkTextbox(frame_editar,  width=300, height=80, border_color= '#0070ff', border_width=2)
textbox_descricao_frame_editar.grid(row = 4, column = 1, padx = 5, pady=0, sticky ="sw")
 
botao_salvar_frame_editar = customtkinter.CTkButton(frame_editar,width=90,  corner_radius= 20, text='Salvar',fg_color="#0070ff",command=lambda: salvar_edicao(entrada_nome_produto_frame_editar.get(),entrada_preco_frame_editar.get(),textbox_descricao_frame_editar.get('1.0', 'end')))
botao_salvar_frame_editar.grid(row = 5, column = 1, padx = 5, pady=0, sticky ="e")
 
botao_excluir_frame_editar = customtkinter.CTkButton(frame_editar,width=90,  corner_radius= 20, text='Excluir',fg_color="#ff0000", command=lambda: excluir(entrada_nome_produto_frame_editar.get()))
botao_excluir_frame_editar.grid(row = 5, column = 1, padx = 5, pady=0, sticky ="w")
 
botao_cancelar_frame_editar = customtkinter.CTkButton(frame_editar,width=90,  corner_radius= 20, text='Cancelar',fg_color="#0070ff", command=cancelar_edicao)
botao_cancelar_frame_editar.grid(row = 5, column = 1, padx = 5, pady=0)
#----------------------------------------------------------------------------------------------------------------------------------------------
 
 
 
#------------------------------------------------------------------frame da saida------------------------------------------------------------------
frame_saida = customtkinter.CTkFrame(master=janela, width=590, height=400, corner_radius= 20, border_color= '#0070ff', border_width=2 )
frame_saida.grid_propagate(False)
 
scrollable_buscar_produto_frame_saida = customtkinter.CTkScrollableFrame(frame_saida)
scrollable_buscar_produto_frame_saida.grid(pady=17, padx=30,row=3,column=0, rowspan = 5, sticky ="e")
 
titulo_frame_saida = customtkinter.CTkLabel(frame_saida, text="Saída de produto", font=("arial",20,"bold"))
titulo_frame_saida.grid(row = 0, column = 0, padx = 5, pady=5,columnspan=4)
 
entrada_buscar_produto_frame_saida=customtkinter.CTkEntry(frame_saida, placeholder_text="Buscar produto:", width=223, border_color= '#0070ff', border_width=2)
entrada_buscar_produto_frame_saida.grid(row = 3, column = 0, padx = 30, pady=5,sticky="w")
 
entrada_preenchida_produto_frame_saida=customtkinter.CTkEntry(frame_saida, placeholder_text="Buscar produto:", width=223, border_color= '#0070ff', border_width=2)
entrada_preenchida_produto_frame_saida.grid(row = 2, column = 1, padx = 30, pady=5, sticky ="w")
 
entrada_quantidade_frame_saida=customtkinter.CTkEntry(frame_saida, placeholder_text="Quantidade:", width=80, border_color= '#0070ff', border_width=2)
entrada_quantidade_frame_saida.grid(row = 3, column = 1, padx = 30, pady=5, sticky ="w")
 
botao_adicionar_produto_frame_saida= customtkinter.CTkButton(frame_saida, text="Adicionar produto" ,width=90,  corner_radius= 20,fg_color="#0070ff", command=adicionar_item)
botao_adicionar_produto_frame_saida.grid(row = 3, column = 1, padx = 30, pady=5,sticky="e")
 
botao_salvar_frame_saida= customtkinter.CTkButton(frame_saida, text="Salvar" ,width=90,  corner_radius= 20,fg_color="#0070ff")
botao_salvar_frame_saida.grid(row = 5, column = 1, padx = 30, pady=5,sticky="e")
 
botao_cancelar_frame_saida= customtkinter.CTkButton(frame_saida, text="Cancelar" ,width=90,  corner_radius= 20,fg_color="#0070ff")
botao_cancelar_frame_saida.grid(row = 5, column = 1, padx = 30, pady=5, sticky ="w")
 
scrollable_adicionar_frame_saida = customtkinter.CTkScrollableFrame(frame_saida)
scrollable_adicionar_frame_saida.grid(pady=5, padx=30,row=4,column=1, sticky ="w")
items = ["Produto 1", "Produto 2", "Produto 3", "Produto 4","Produto 5", "Produto 6", "Produto 7", "Produto 8"]
#----------------------------------------------------------------------------------------------------------------------------------------------
 
 
 
#------------------------------------------------------------------frame da entrada------------------------------------------------------------------
frame_entrada = customtkinter.CTkFrame(master=janela, width=590, height=400, corner_radius= 20, border_color= '#0070ff', border_width=2 )
frame_entrada.grid_propagate(False)
 
scrollable_buscar_produto_frame_entrada = customtkinter.CTkScrollableFrame(frame_entrada)
scrollable_buscar_produto_frame_entrada.grid(pady=17, padx=30,row=3,column=0, rowspan = 5, sticky ="e")
 
titulo_entrada_frame_entrada = customtkinter.CTkLabel(frame_entrada, text="Entrada", font=("arial",20,"bold"))
titulo_entrada_frame_entrada.grid(row = 0, column = 0, padx = 5, pady=5,columnspan=4)
 
entrada_buscar_produto_frame_entrada=customtkinter.CTkEntry(frame_entrada, placeholder_text="Buscar produto:", width=223, border_color= '#0070ff', border_width=2)
entrada_buscar_produto_frame_entrada.grid(row = 3, column = 0, padx = 30, pady=5,sticky="w")
 
entrada_preenchida_produto_frame_entrada=customtkinter.CTkEntry(frame_entrada, placeholder_text="produto:", width=130, border_color= '#0070ff', border_width=2)
entrada_preenchida_produto_frame_entrada.grid(row = 2, column = 1, padx = 30, pady=5, sticky ="w")
 
entrada_preenchida_quantidade_frame_entrada=customtkinter.CTkEntry(frame_entrada, placeholder_text="quantidade:", width=90, border_color= '#0070ff', border_width=2)
entrada_preenchida_quantidade_frame_entrada.grid(row = 2, column = 1, padx = 30, pady=5, sticky ="e")
 
entrada_quantidade_frame_entrada=customtkinter.CTkEntry(frame_entrada, placeholder_text="Quantidade:", width=80, border_color= '#0070ff', border_width=2)
entrada_quantidade_frame_entrada.grid(row = 3, column = 1, padx = 30, pady=5, sticky ="w")
 
botao_adicionar_produto_frame_entrada= customtkinter.CTkButton(frame_entrada, text="Adicionar produto" ,width=90,  corner_radius= 20,fg_color="#0070ff", command=adicionar_item)
botao_adicionar_produto_frame_entrada.grid(row = 3, column = 1, padx = 30, pady=5,sticky="e")
 
botao_salvar_frame_entrada= customtkinter.CTkButton(frame_entrada, text="Salvar" ,width=90,  corner_radius= 20,fg_color="#0070ff")
botao_salvar_frame_entrada.grid(row = 5, column = 1, padx = 30, pady=5,sticky="e")
 
botao_cancelar_frame_entrada= customtkinter.CTkButton(frame_entrada, text="Cancelar" ,width=90,  corner_radius= 20,fg_color="#0070ff")
botao_cancelar_frame_entrada.grid(row = 5, column = 1, padx = 30, pady=5,sticky="w")
 
scrollable_adicionar_frame_entrada = customtkinter.CTkScrollableFrame(frame_entrada)
scrollable_adicionar_frame_entrada.grid(pady=5, padx=10,row=4,column=1)
items_adicionar_frame_entrada = ["Produto 1", "Produto 2", "Produto 3", "Produto 4","Produto 5", "Produto 6", "Produto 7", "Produto 8"]
#----------------------------------------------------------------------------------------------------------------------------------------------
 
 
 
#-----------------------------------------------------------------frame dos relatorios------------------------------------------------------------------
#-----------------------------------------------------------------relatorio de estoque-----------------------------------------------------------------
frame_relatorio_estoque=customtkinter.CTkFrame(janela, width=590, height=400, corner_radius= 20, border_color= '#0070ff', border_width=2)
frame_relatorio_estoque.grid_propagate(False)
 
titulo_frame_relatorio_estoque = customtkinter.CTkLabel(frame_relatorio_estoque, text="Relatorio do estoque", font=("arial",20,"bold"))
titulo_frame_relatorio_estoque.grid(row = 0, column = 0, padx = 10, pady=10)
 
entrada_pesquisa_frame_relatorio_estoque = customtkinter.CTkEntry(frame_relatorio_estoque, placeholder_text="Barra de pesquisa",width=200)
entrada_pesquisa_frame_relatorio_estoque.grid(row = 1, column = 0, padx = 30, pady=5,sticky="w")
#-------------------------------------------------tabela do freme relatorio de eestoque-----------------------------------------------------------------
columns_relatorio_estoque = ('nome','quantidade','preço','descrição')
estoque_relatorio_estoque = ttk.Treeview(frame_relatorio_estoque,columns=columns_relatorio_estoque,show='headings',height=8)
estoque_relatorio_estoque.grid(row = 2, column = 0, padx = 30, pady=10,sticky="w")
estoque_relatorio_estoque.heading('nome',text='nome')
estoque_relatorio_estoque.heading('quantidade',text='quantidade')
estoque_relatorio_estoque.heading('preço',text='preço')
estoque_relatorio_estoque.heading('descrição',text='descrição')
estoque_relatorio_estoque.column('nome',width=128, anchor="center")
estoque_relatorio_estoque.column('quantidade',width=127, anchor="center")
estoque_relatorio_estoque.column('preço',width=127, anchor="center")
estoque_relatorio_estoque.column('descrição',width=128, anchor="center")
#-----------------------------------------------------------------------------------------------------------------------------------------------------
botao_exportar_frame_relatorio_estoque=customtkinter.CTkButton(frame_relatorio_estoque, text="Exportar",fg_color="#0070ff",command=exportar, corner_radius= 20)
botao_exportar_frame_relatorio_estoque.grid(row=1, column=0, padx = 30, pady=5, sticky="e")
 
botao_estoque_frame_relatorio_estoque=customtkinter.CTkButton(frame_relatorio_estoque, text="Estoque",fg_color="#0070ff",command=relatorio_estoque, corner_radius= 20)
botao_estoque_frame_relatorio_estoque.grid(row=3, column=0, padx = 30, pady=5, sticky="w")
 
botao_saida_frame_relatorio_estoque=customtkinter.CTkButton(frame_relatorio_estoque, text="Saída",fg_color="#0070ff",command=relatorio_saida, corner_radius= 20)
botao_saida_frame_relatorio_estoque.grid(row=3, column=0, padx = 30, pady=5)
 
botao_entrada_frame_relatorio_estoque=customtkinter.CTkButton(frame_relatorio_estoque, text="Entrada",fg_color="#0070ff",command=relatorio_entrada, corner_radius= 20)
botao_entrada_frame_relatorio_estoque.grid(row=3, column=0, padx = 30, pady=5, sticky="e")
#----------------------------------------------------------------------------------------------------------------------------------------------
 
 
 
#-----------------------------------------------------------------relatorio de saida-----------------------------------------------------------------
frame_relatorio_saida=customtkinter.CTkFrame(master=janela, width=590, height=400, corner_radius= 20, border_color= '#0070ff', border_width=2)
frame_relatorio_saida.grid_propagate(False)
 
titulo_frame_relatorio_saida = customtkinter.CTkLabel(frame_relatorio_saida, text="Relatorio de saida", font=("arial",20,"bold"))
titulo_frame_relatorio_saida.grid(row = 0, column = 0, padx = 10, pady=10)
 
entrada_pesquisa_frame_relatorio_saida = customtkinter.CTkEntry(frame_relatorio_saida, placeholder_text="Barra de pesquisa",width=200)
entrada_pesquisa_frame_relatorio_saida.grid(row = 1, column = 0, padx = 30, pady=5,sticky="w")
#-------------------------------------------------tabela do freme relatorio de saida-----------------------------------------------------------------
columns_relatorio_saida = ('nome','quantidade','data/hora')
estoque_relatorio_saida = ttk.Treeview(frame_relatorio_saida,columns=columns_relatorio_saida,show='headings',height=8)
estoque_relatorio_saida.grid(row = 2, column = 0, padx = 30, pady=10,sticky="w")
estoque_relatorio_saida.heading('nome',text='nome')
estoque_relatorio_saida.heading('quantidade',text='quantidade')
estoque_relatorio_saida.heading('data/hora',text='data/hora')
estoque_relatorio_saida.column('nome',width=170, anchor="center")
estoque_relatorio_saida.column('quantidade',width=170, anchor="center")
estoque_relatorio_saida.column('data/hora',width=170, anchor="center")
#--------------------------------------------------------------------------------------------------------------------------------------------------------
botao_exportar_frame_relatorio_saida=customtkinter.CTkButton(frame_relatorio_saida, text="Exportar",fg_color="#0070ff",command=exportar, corner_radius= 20)
botao_exportar_frame_relatorio_saida.grid(row=1, column=0, padx = 30, pady=5, sticky="e")
 
botao_estoque_frame_relatorio_saida=customtkinter.CTkButton(frame_relatorio_saida, text="Estoque",fg_color="#0070ff",command=relatorio_estoque, corner_radius= 20)
botao_estoque_frame_relatorio_saida.grid(row=3, column=0, padx = 30, pady=5, sticky="w")
 
botao_saida_frame_relatorio_saida=customtkinter.CTkButton(frame_relatorio_saida, text="Saída",fg_color="#0070ff",command=relatorio_saida, corner_radius= 20)
botao_saida_frame_relatorio_saida.grid(row=3, column=0, padx = 30, pady=5)
 
botao_entrada_frame_relatorio_saida=customtkinter.CTkButton(frame_relatorio_saida, text="Entrada",fg_color="#0070ff",command=relatorio_entrada, corner_radius= 20)
botao_entrada_frame_relatorio_saida.grid(row=3, column=0, padx = 30, pady=5, sticky="e")
#----------------------------------------------------------------------------------------------------------------------------------------------
 
 
 
#-----------------------------------------------------------------relatorio de entrada-----------------------------------------------------------------
frame_relatorio_entrada=customtkinter.CTkFrame(master=janela, width=590, height=400, corner_radius= 20, border_color= '#0070ff', border_width=2)
frame_relatorio_entrada.grid_propagate(False)
 
titulo_frame_relatorio_entrada = customtkinter.CTkLabel(frame_relatorio_entrada, text="Relatorio de entrada", font=("arial",20,"bold"))
titulo_frame_relatorio_entrada.grid(row = 0, column = 0, padx = 10, pady=10)
 
entrada_pesquisa_frame_relatorio_entrada = customtkinter.CTkEntry(frame_relatorio_entrada, placeholder_text="Barra de pesquisa",width=200)
entrada_pesquisa_frame_relatorio_entrada.grid(row = 1, column = 0, padx = 30, pady=5,sticky="w")
#-------------------------------------------------tabela do freme relatorio de entrada-----------------------------------------------------------------
columns_relatorio_entrada = ('nome','quantidade','data/hora')
estoque_relatorio_entrada = ttk.Treeview(frame_relatorio_entrada,columns=columns_relatorio_entrada,show='headings',height=8)
estoque_relatorio_entrada.grid(row = 2, column = 0, padx = 30, pady=10,sticky="w")
estoque_relatorio_entrada.heading('nome',text='nome')
estoque_relatorio_entrada.heading('quantidade',text='quantidade')
estoque_relatorio_entrada.heading('data/hora',text='data/hora')
estoque_relatorio_entrada.column('nome',width=170, anchor="center")
estoque_relatorio_entrada.column('quantidade',width=170, anchor="center")
estoque_relatorio_entrada.column('data/hora',width=170, anchor="center")
#------------------------------------------------------------------------------------------------------------------------------------------------------
botao_exportar_frame_relatorio_entrada=customtkinter.CTkButton(frame_relatorio_entrada, text="Exportar",fg_color="#0070ff",command=exportar, corner_radius= 20)
botao_exportar_frame_relatorio_entrada.grid(row=1, column=0, padx = 30, pady=5, sticky="e")
 
botao_estoque_frame_relatorio_entrada=customtkinter.CTkButton(frame_relatorio_entrada, text="Estoque",fg_color="#0070ff",command=relatorio_estoque, corner_radius= 20)
botao_estoque_frame_relatorio_entrada.grid(row=3, column=0, padx = 30, pady=5, sticky="w")
 
botao_saida_frame_relatorio_entrada=customtkinter.CTkButton(frame_relatorio_entrada, text="Saída",fg_color="#0070ff",command=relatorio_saida, corner_radius= 20)
botao_saida_frame_relatorio_entrada.grid(row=3, column=0, padx = 30, pady=5)
 
botao_entrada_frame_relatorio_entrada=customtkinter.CTkButton(frame_relatorio_entrada, text="Entrada",fg_color="#0070ff",command=relatorio_entrada, corner_radius= 20)
botao_entrada_frame_relatorio_entrada.grid(row=3, column=0, padx = 30, pady=5, sticky="e")
#----------------------------------------------------------------------------------------------------------------------------------------------
janela.mainloop()