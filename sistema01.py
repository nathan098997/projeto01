# Criação do codigo_____________________________________________________________________________________________________
import customtkinter
from tkinter import ttk
import sqlite3
import tkinter as tk
customtkinter.set_appearance_mode('dark')
aba = customtkinter.CTk()
aba.title('')
aba.geometry('800x400')
 
 
# Criação de defs ______________________________________________________________________________________________________
 
def troca_Cadastro():
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_Cadastrar.grid_propagate(False)
    frame_Cadastrar.grid(row=0, column=1, pady=10, padx=10)
 
 
def criar_banco():
    conexao = sqlite3.connect("dados_cadastro.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("CREATE TABLE IF NOT EXISTS pessoas (nome text, preco decimal, desc text)")
    conexao.commit()
    conexao.close()
 
 
def salvar_dados():
    conexao = sqlite3.connect("dados_cadastro.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"INSERT INTO pessoas (nome, preco, desc) VALUES ('{Colocar_Nome_Cadastrar.get()}',"
                         f"'{float(Colocar_Preco_Cadastrar.get())}', '{TextBox_Descricao_Cadastrar.get('1.0', 'end')}')"
                         )
    Colocar_Nome_Cadastrar.delete(0, 'end')
    Colocar_Preco_Cadastrar.delete(0, 'end')
    TextBox_Descricao_Cadastrar.delete(1.0, 'end')
    conexao.commit()
    conexao.close()
 
 
def ler_dados():
    conexao = sqlite3.connect("dados_cadastro.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"SELECT * FROM pessoas")
    recebe_dados = terminal_sql.fetchall()
    for item in Trivel_Relatorio_Estoque.get_children():
        Trivel_Relatorio_Estoque.delete(item)
 
    for i in recebe_dados:
        nomes = str(i[0])
        quantidade = 0
        preco = float(i[1])
        desc = str(i[2])
        Trivel_Relatorio_Estoque.insert('', tk.END, values=(nomes, quantidade, preco, desc))
        conexao.close()
 
 
def ler_dados_lista_editar():
    global items, check_var
    conexao = sqlite3.connect("dados_cadastro.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"SELECT nome FROM pessoas")
    items = terminal_sql.fetchall()
    check_var = customtkinter.StringVar(value="on")
    for item in scrollable_frame_Editar.winfo_children():
        item.destroy()
 
    for item in items:
        nome = str(item[0])
        itens = []
        itens.append(nome)
 
 
        for item in itens:
            labeal_edicao_dados.configure(text=item)
            box = customtkinter.CTkCheckBox(scrollable_frame_Editar, text=item, command=lambda: seleciona_item() if
            check_var.get() else None, variable=check_var, onvalue=item, offvalue="")
            box.pack(pady=5, padx=5, fill="x")
    conexao.close()
 
 
def ler_dados_lista_saida():
    global items, check_var
    conexao = sqlite3.connect("dados_cadastro.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"SELECT nome FROM pessoas")
    items = terminal_sql.fetchall()
    check_var = customtkinter.StringVar(value="on")
    for item in Lista_produtos_saida.winfo_children():
        item.destroy()
 
    for item in items:
        nome = str(item[0])
        itens = []
        itens.append(nome)
        for item in itens:
            labeal_saida_dados.configure(text=item)
            box_saida = customtkinter.CTkCheckBox(Lista_produtos_saida, text=item, command=lambda: seleciona_item() if
            check_var.get() else None, variable=check_var, onvalue=item, offvalue="")
            box_saida.pack(pady=5, padx=5, fill="x")
    conexao.close()
 
 
def ler_dados_lista_entrada():
    global items, check_var
    conexao = sqlite3.connect("dados_cadastro.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"SELECT nome FROM pessoas")
    items = terminal_sql.fetchall()
    check_var = customtkinter.StringVar(value="on")
    for item in Lista_Produtos_Entrada.winfo_children():
        item.destroy()
 
    for item in items:
        nome = str(item[0])
        itens = []
        itens.append(nome)
        for item in itens:
            labeal_entrada_dados.configure(text=item)
            box_entrada = customtkinter.CTkCheckBox(Lista_Produtos_Entrada, text=item, command=lambda: seleciona_item()
            if check_var.get() else None, variable=check_var, onvalue=item, offvalue="")
            box_entrada.pack(pady=5, padx=5, fill="x")
 
    conexao.close()
 
 
def seleciona_item():
    valor_checkbox = check_var.get()
 
    conexao = sqlite3.connect("dados_cadastro.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"SELECT * FROM pessoas WHERE nome = '{valor_checkbox}'")
    receber_dados_produtos = terminal_sql.fetchall()
    print(receber_dados_produtos)
    Editar_Nome_Produto.delete(0, 'end')
    Editar_preco_Produto.delete(0, 'end')
    Editar_Descricao_Produto.delete(0, 'end')
 
    Editar_Nome_Produto.insert(0, receber_dados_produtos[0][0])
    Editar_preco_Produto.insert(0, receber_dados_produtos[0][1])
    Editar_Descricao_Produto.insert(0, receber_dados_produtos[0][2])
 
 
def delet_item():
    Editar_Nome_Produto.delete(0, "end")
    Editar_preco_Produto.delete(0, "end")
    Editar_Descricao_Produto.delete(0, "end")
 
 
def troca_editar():
    frame_Cadastrar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_editar.grid_propagate(False)
    frame_editar.grid(row=0, column=1, pady=10, padx=10)
    ler_dados_lista_editar()
 
 
def troca_saida():
    frame_Cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_saida.grid_propagate(False)
    frame_saida.grid(row=0, column=1, pady=10, padx=10)
    ler_dados_lista_saida()
 
 
def troca_entrada():
    frame_Cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_entrada.grid_propagate(False)
    frame_entrada.grid(row=0, column=1, pady=10, padx=10)
    ler_dados_lista_entrada()
 
 
def troca_relatorio_estoque():
    frame_Cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_estoque.grid_propagate(False)
    frame_relatorio_estoque.grid(row=0, column=1, pady=10, padx=10)
    ler_dados()
 
 
def troca_relatorio_entrada():
    frame_Cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_saida.grid_forget()
    frame_relatorio_entrada.grid_propagate(False)
    frame_relatorio_entrada.grid(row=0, column=1, pady=10, padx=10)
 
 
def troca_relatorio_saida():
    frame_Cadastrar.grid_forget()
    frame_editar.grid_forget()
    frame_saida.grid_forget()
    frame_entrada.grid_forget()
    frame_relatorio_estoque.grid_forget()
    frame_relatorio_entrada.grid_forget()
    frame_relatorio_saida.grid_propagate(False)
    frame_relatorio_saida.grid(row=0, column=1, pady=10, padx=10)
 
 
def deletar_item(index):
    items_entrada.pop(index)
    atualizar()
 
 
def atualizar():
    for botaozinho in Lista_Excluir_Produtos_Saida.winfo_children():
        botaozinho.destroy()
 
    for i, item in enumerate(items_entrada):
        box = customtkinter.CTkCheckBox(Lista_Excluir_Produtos_Saida, text=item)
        box.grid(row=i, column=0, pady=5, padx=10, sticky="w")
        deletar_botao = customtkinter.CTkButton(Lista_Excluir_Produtos_Saida, text="🗑️", fg_color="red", width=40,
                                                command=lambda index=i: deletar_item(index))
        deletar_botao.grid(row=i, column=1, padx=10, pady=5)
 
 
def abrir_pop_up():
    customtkinter.set_appearance_mode("dark")
    pop_up = customtkinter.CTk()
    pop_up.geometry("470x400")
    pop_up.title("pop_up")
    # criação das funções do pop-up_________________________________________________________________________________________
 
    impressão = customtkinter.CTkLabel(pop_up, text="Impressora", font=("Open sans", 30, "bold"))
    impressão.grid(row=0, column=0, padx=0, pady=5, sticky="nsew")
 
    escolher_relatorio = customtkinter.CTkLabel(pop_up, text="Escolher relatório", font=("Open sans", 20, "bold"))
    escolher_relatorio.grid(row=1, column=0, padx=5, pady=30, sticky="w")
 
    exportar_estoque = customtkinter.CTkCheckBox(pop_up, text="exportar estoque")
    exportar_estoque.grid(row=2, column=0, padx=5, pady=20, sticky="w")
 
    exportar_saida = customtkinter.CTkCheckBox(pop_up, text="exportar saída")
    exportar_saida.grid(row=3, column=0, padx=5, pady=20, sticky="w")
 
    exportar_entrada = customtkinter.CTkCheckBox(pop_up, text="exportar entrada")
    exportar_entrada.grid(row=4, column=0, padx=5, pady=20, sticky="w")
 
    escolher_extensao = customtkinter.CTkLabel(pop_up, text="Escolher extensão", font=("Open sans", 20, "bold"))
    escolher_extensao.grid(row=1, column=1, padx=50, pady=30, sticky="w")
 
    word = customtkinter.CTkCheckBox(pop_up, text="Word")
    word.grid(row=2, column=1, padx=50, pady=20, sticky="w")
 
    PDF = customtkinter.CTkCheckBox(pop_up, text="PDF")
    PDF.grid(row=3, column=1, padx=50, pady=20, sticky="w")
 
    excel = customtkinter.CTkCheckBox(pop_up, text="Excel")
    excel.grid(row=4, column=1, padx=50, pady=20, sticky="w")
 
    # criação dos botões do pop-up__________________________________________________________________________________________
 
    pop_up_salvar = customtkinter.CTkButton(pop_up, text="salvar", fg_color="green", width=90, height=30)
    pop_up_salvar.grid(row=5, column=1, padx=5, pady=20, sticky="e")
 
    pop_up_cancelar = customtkinter.CTkButton(pop_up, text="cancelar", fg_color="red", width=90, height=30)
    pop_up_cancelar.grid(row=5, column=1, padx=70, pady=20, sticky="w")
 
    pop_up.mainloop()
 
 
def on_click(i):
    pass
 
 
# criaçao de frames ____________________________________________________________________________________________________
criar_banco()
 
frame_menu = customtkinter.CTkFrame(aba, width=190, height=390, corner_radius=0)
frame_menu.pack_propagate(False)
frame_menu.grid(row=0, column=0)
 
frame_Cadastrar = customtkinter.CTkFrame(aba, width=590, height=390, corner_radius=0)
frame_Cadastrar.grid_propagate(False)
frame_Cadastrar.grid(row=0, column=1, pady=10, padx=10)
 
frame_editar = customtkinter.CTkFrame(aba, width=590, height=390, corner_radius=0)
frame_editar.grid_propagate(False)
 
frame_saida = customtkinter.CTkFrame(aba, width=590, height=390, corner_radius=0)
frame_saida.grid_propagate(False)
 
frame_entrada = customtkinter.CTkFrame(aba, width=590, height=390, corner_radius=0)
frame_entrada.grid_propagate(False)
 
frame_relatorio_estoque = customtkinter.CTkFrame(aba, width=590, height=390, corner_radius=0)
frame_relatorio_estoque.grid_propagate(False)
 
frame_relatorio_entrada = customtkinter.CTkFrame(aba, width=590, height=390, corner_radius=0)
frame_relatorio_entrada.grid_propagate(False)
 
frame_relatorio_saida = customtkinter.CTkFrame(aba, width=590, height=390, corner_radius=0)
frame_relatorio_saida.grid_propagate(False)
 
# Menu _________________________________________________________________________________________________________________
 
Titulo_Menu = customtkinter.CTkLabel(frame_menu, text=f' Nome do \nSistema', font=('comic sans', 20, 'bold'))
Titulo_Menu.pack(pady=15)
 
Botao_Cadastrar = customtkinter.CTkButton(frame_menu, text='Cadastrar', command=troca_Cadastro)
Botao_Cadastrar.pack(pady=5)
 
Botao_Editar = customtkinter.CTkButton(frame_menu, text='Editar', command=troca_editar)
Botao_Editar.pack(pady=5)
 
Botao_Saida = customtkinter.CTkButton(frame_menu, text='Saida', command=troca_saida)
Botao_Saida.pack(pady=5)
 
Botao_Entrada = customtkinter.CTkButton(frame_menu, text='Entrada', command=troca_entrada)
Botao_Entrada.pack(pady=5)
 
Botao_Relatorio = customtkinter.CTkButton(frame_menu, text='Relatorio', command=troca_relatorio_estoque)
Botao_Relatorio.pack(pady=5)
 
# Cadastrar ____________________________________________________________________________________________________________
 
Titulo_Cadastrar = customtkinter.CTkLabel(frame_Cadastrar, text='Cadastro de Produto', font=('comic sans', 30, 'bold'))
Titulo_Cadastrar.grid(pady=15, padx=15, row=0, column=1, sticky='n')
 
Nome_Produto_Cadastrar = customtkinter.CTkLabel(frame_Cadastrar, text='Nome do Produto :')
Nome_Produto_Cadastrar.grid(pady=5, padx=5, row=1, column=0, sticky="e")
 
Preco_Produto_Cadastrar = customtkinter.CTkLabel(frame_Cadastrar, text='preço (R$) :')
Preco_Produto_Cadastrar.grid(pady=5, padx=5, row=2, column=0, sticky="e")
 
Descricao_Produto_Cadastrar = customtkinter.CTkLabel(frame_Cadastrar, text='Descrição :')
Descricao_Produto_Cadastrar.grid(pady=5, padx=5, row=3, column=0, sticky="e")
 
Colocar_Nome_Cadastrar = customtkinter.CTkEntry(frame_Cadastrar, placeholder_text='digite o nome do produto', width=300,
                                                height=30)
Colocar_Nome_Cadastrar.grid(pady=5, padx=10, row=1, column=1, sticky="w")
 
Colocar_Preco_Cadastrar = customtkinter.CTkEntry(frame_Cadastrar, placeholder_text='0.00', height=30, width=80)
Colocar_Preco_Cadastrar.grid(pady=5, padx=10, row=2, column=1, sticky="w")
 
TextBox_Descricao_Cadastrar = customtkinter.CTkTextbox(frame_Cadastrar, height=80, width=300)
TextBox_Descricao_Cadastrar.grid(pady=5, padx=5, row=3, column=1)
 
botao_salvar_frame_Cadastrar = customtkinter.CTkButton(frame_Cadastrar, text='salvar', width=80, command=salvar_dados)
botao_salvar_frame_Cadastrar.grid(pady=5, padx=15, row=4, column=1, sticky="e")
 
# Editar _______________________________________________________________________________________________________________
 
scrollable_frame_Editar = customtkinter.CTkScrollableFrame(frame_editar)
scrollable_frame_Editar.grid(row=2, column=0, rowspan=4, pady=5, padx=5, stick="w")
 
labeal_edicao_dados = customtkinter.CTkLabel(frame_editar)
 
 
Titulo_Editar = customtkinter.CTkLabel(frame_editar, text='Editar produto cadastrado', font=('Courier', 25, 'bold'))
Titulo_Editar.grid(row=0, column=0, pady=5, padx=140, stick="w")
 
Buscar_Produto_Editar = customtkinter.CTkEntry(frame_editar, placeholder_text='Buscar produto', width=222, height=30)
Buscar_Produto_Editar.grid(row=1, column=0, pady=2, padx=5, stick='w')
 
Editar_Nome_Produto = customtkinter.CTkEntry(frame_editar, placeholder_text='Nome do produto', width=300, height=30)
Editar_Nome_Produto.grid(row=2, column=0, pady=0, padx=250, stick='w')
 
Editar_preco_Produto = customtkinter.CTkEntry(frame_editar, placeholder_text='0.00', width=50, height=30)
Editar_preco_Produto.grid(row=3, column=0, pady=5, padx=250, stick='w')
 
Editar_Descricao_Produto = customtkinter.CTkEntry(frame_editar, width=300, height=100)
Editar_Descricao_Produto.grid(row=4, column=0, pady=0, padx=250, stick="w")
 
Botao_Salvar_Frame_Editar = customtkinter.CTkButton(frame_editar, text='salvar', width=80, height=30)
Botao_Salvar_Frame_Editar.grid(row=5, column=0, pady=5, padx=370, stick="w")
 
Botao_Cancelar_Frame_Editar = customtkinter.CTkButton(frame_editar, text='cancelar', width=80, height=30)
Botao_Cancelar_Frame_Editar.grid(row=5, column=0, pady=5, padx=480, stick="w")
 
Botao_Excluir_Frame_Editar = customtkinter.CTkButton(frame_editar, text='excluir', fg_color='red', width=80, height=30)
Botao_Excluir_Frame_Editar.grid(row=5, column=0, pady=5, padx=260, stick="w")
 
# Saida _________________________________________________________________________________________________________________
 
Titulo_saida = customtkinter.CTkLabel(frame_saida, text="Saída Produto:", font=("Arial", 30))
Titulo_saida.grid(row=0, column=0, pady=20, padx=200, sticky="w")
 
Lista_produtos_saida = customtkinter.CTkScrollableFrame(frame_saida)
Lista_produtos_saida.grid(pady=5, padx=20, sticky="w", row=2, column=0, rowspan=5)
 
labeal_saida_dados = customtkinter.CTkLabel(frame_saida)
 
Quantidade_Produtos_Saida = customtkinter.CTkEntry(frame_saida, placeholder_text="Quantidades de items no estoque",
                                                   width=280)
Quantidade_Produtos_Saida.grid(pady=5, padx=290, row=1, column=0, sticky="w")
 
Botao_Adicionar_Saida = customtkinter.CTkButton(frame_saida, text='Adicionar item', width=120, fg_color="green", )
Botao_Adicionar_Saida.grid(pady=1, padx=450, row=2, column=0, sticky="w", columnspan=2)
 
Busca_Produto_Saida = customtkinter.CTkEntry(frame_saida, placeholder_text="Campo de Busca:", width=225)
Busca_Produto_Saida.grid(row=1, column=0, pady=2, padx=20, sticky="w", columnspan=2)
 
Busca_Estoque_Saida = customtkinter.CTkEntry(frame_saida, placeholder_text="", width=140)
Busca_Estoque_Saida.grid(pady=1, padx=290, row=2, column=0, sticky="w", columnspan=2)
 
Lista_Excluir_Produtos_Saida = customtkinter.CTkScrollableFrame(frame_saida, width=260)
Lista_Excluir_Produtos_Saida.grid(row=3, column=0, pady=1, padx=290, sticky="w")
items_saida = ["Produto 1", "Produto 2", "Produto 3", "Produto 4", "Produto 5", "Produto 6", "Produto 7", "Produto 8"]
 
for item in items_saida:
    box_excluir_saida = customtkinter.CTkCheckBox(Lista_Excluir_Produtos_Saida, text=item)
    box_excluir_saida.pack(pady=5, padx=10)
 
Botao_Cancelar_Saida = customtkinter.CTkButton(frame_saida, text="Cancelar", width=80, fg_color="red")
Botao_Cancelar_Saida.grid(row=4, column=0, pady=5, padx=290, sticky="w")
 
Botao_Salvar_Saida = customtkinter.CTkButton(frame_saida, text="Salvar", width=80, fg_color="green")
Botao_Salvar_Saida.grid(row=4, column=0, pady=5, padx=490, sticky="e")
 
# Entrada_______________________________________________________________________________________________________________
 
Titulo_Entrada = customtkinter.CTkLabel(frame_entrada, text="Entrada Produtos:", font=("arial", 30))
Titulo_Entrada.grid(row=0, column=1, pady=20, sticky="w")
 
Busca_Entrada = customtkinter.CTkEntry(frame_entrada, placeholder_text="campo de busca:", width=150)
Busca_Entrada.grid(row=1, column=0, pady=5, padx=15, stick="w", columnspan=2)
 
Nome_Quantidade_Campo = customtkinter.CTkEntry(frame_entrada, placeholder_text="Quantidade de itens no estoque:",
                                               width=300)
Nome_Quantidade_Campo.grid(row=1, column=1, pady=5, padx=5, stick="w")
 
Descricao_Entrada = customtkinter.CTkEntry(frame_entrada, placeholder_text="", width=100)
Descricao_Entrada.grid(row=2, column=1, pady=5, padx=10, stick="w")
 
Adicionar_Entrada = customtkinter.CTkButton(frame_entrada, text="Adicionar item", width=120, fg_color="green")
Adicionar_Entrada.grid(row=2, column=1, pady=5, padx=10, stick="e")
 
Cancelar_Entrada = customtkinter.CTkButton(frame_entrada, text="cancelar", width=80, fg_color="red")
Cancelar_Entrada.grid(row=7, column=1, pady=5, padx=5, sticky="w")
 
Salvar_Entrada = customtkinter.CTkButton(frame_entrada, text="salvar", width=80, fg_color="green")
Salvar_Entrada.grid(row=7, column=1, pady=5, padx=5, sticky="e")
 
Lista_Produtos_Entrada = customtkinter.CTkScrollableFrame(frame_entrada)
Lista_Produtos_Entrada.grid(pady=5, padx=20, stick="we", row=2, column=0, rowspan=5)
 
labeal_entrada_dados = customtkinter.CTkLabel(frame_saida)
 
items_entrada = ["Produto 1", "Produto 2", "Produto 3", "Produto 4", "Produto 5", "Produto 6", "Produto 7", "Produto 8"]
 
for item in items_entrada:
    box_entrada = customtkinter.CTkCheckBox(Lista_Produtos_Entrada, text=item)
    box_entrada.grid(pady=5, padx=10)
 
Lista_Items_Entrada_Posicao = customtkinter.CTkFrame(frame_entrada, width=300, height=180)
Lista_Items_Entrada_Posicao.grid(padx=5, pady=5, row=3, column=1, stick="nwes")
 
# Relatorio Estoque ____________________________________________________________________________________________________
 
Titulo_Frame_estoque = customtkinter.CTkLabel(frame_relatorio_estoque, text='Relatorio Estoque',
                                              font=('comic sans', 30, 'bold'))
Titulo_Frame_estoque.grid(pady=10, padx=5, row=0, column=0, sticky='nsew', columnspan=4)
 
Entrada_Nome_Frame_Estoque = customtkinter.CTkEntry(frame_relatorio_estoque, placeholder_text="Barra de Pesquisa:",
                                                    width=150)
Entrada_Nome_Frame_Estoque.grid(row=1, column=0, pady=5, padx=5, stick="w")
 
Coluna_Relatorio_Estoque = ["Produtos", "Quantidade", "Preço", "Descrição"]
Trivel_Relatorio_Estoque = ttk.Treeview(frame_relatorio_estoque, columns=Coluna_Relatorio_Estoque, show="headings")
Trivel_Relatorio_Estoque.grid(row=2, column=0, columnspan=5, padx=5, pady=5)
 
Trivel_Relatorio_Estoque.heading("Produtos", text="Produtos")
Trivel_Relatorio_Estoque.heading("Quantidade", text="Quantidade")
Trivel_Relatorio_Estoque.heading("Preço", text="Preço")
Trivel_Relatorio_Estoque.heading("Descrição", text="Descrição")
 
Trivel_Relatorio_Estoque.column("Produtos", width=140, anchor="center")
Trivel_Relatorio_Estoque.column("Quantidade", width=140, anchor="center")
Trivel_Relatorio_Estoque.column("Preço", width=140, anchor="center")
Trivel_Relatorio_Estoque.column("Descrição", width=140, anchor="center")
 
 
Botao_Exportar = customtkinter.CTkButton(frame_relatorio_estoque, text="exportar", command=abrir_pop_up,
                                         fg_color="green")
Botao_Exportar.grid(row=1, column=3, padx=0, pady=5, sticky="e")
 
Botao_Saida = customtkinter.CTkButton(frame_relatorio_estoque, text="saida", width=100, command=troca_relatorio_saida)
Botao_Saida.grid(padx=10, row=3, column=1, sticky="w")
 
Botao_Estoque = customtkinter.CTkButton(frame_relatorio_estoque, text="estoque", width=100, command=troca_relatorio_estoque,fg_color="green")
Botao_Estoque.grid(padx=10, row=3, column=0, sticky="e")
 
Botao_Entrada = customtkinter.CTkButton(frame_relatorio_estoque, text="entrada", width=100, command=troca_relatorio_entrada)
Botao_Entrada.grid(padx=10, row=3, column=2, sticky="w")
 
# Relatorio Entrada ____________________________________________________________________________________________________
 
Titulo_Relatorio_Entrada = customtkinter.CTkLabel(frame_relatorio_entrada, text='Relatorio Entrada',
                                                  font=('comic sans', 30, 'bold'))
Titulo_Relatorio_Entrada.grid(pady=10, padx=5, row=0, column=0, sticky='nsew', columnspan=4)
 
Entrada_Nomeframe_Relatorio_Entrada = customtkinter.CTkEntry(frame_relatorio_entrada,
                                                             placeholder_text="Barra de Pesquisa:", width=150)
Entrada_Nomeframe_Relatorio_Entrada.grid(row=1, column=0, pady=5, padx=5, stick="w")
 
Coluna_Relatorio_Entrada = ["Produtos", "Quantidade", "Data/Hora"]
Trivel_Relatorio_Entrada = ttk.Treeview(frame_relatorio_entrada, columns=Coluna_Relatorio_Entrada, show="headings")
Trivel_Relatorio_Entrada.grid(row=2, column=0, columnspan=5, padx=5, pady=5)
 
Trivel_Relatorio_Entrada.heading("Produtos", text="Produtos")
Trivel_Relatorio_Entrada.heading("Quantidade", text="Quantidade")
Trivel_Relatorio_Entrada.heading("Data/Hora", text="Data/Hora")
 
 
Trivel_Relatorio_Entrada.column("Produtos", width=140, anchor="center")
Trivel_Relatorio_Entrada.column("Quantidade", width=140, anchor="center")
Trivel_Relatorio_Entrada.column("Data/Hora", width=140, anchor="center")
 
Trivel_Relatorio_Entrada.insert("", "end", values=("Produto 1"))
Trivel_Relatorio_Entrada.insert("", "end", values=("Produto 2"))
Trivel_Relatorio_Entrada.insert("", "end", values=("Produto 3"))
Trivel_Relatorio_Entrada.insert("", "end", values=("Produto 4"))
Trivel_Relatorio_Entrada.insert("", "end", values=("Produto 5"))
Trivel_Relatorio_Entrada.insert("", "end", values=("Produto 6"))
Trivel_Relatorio_Entrada.insert("", "end", values=("Produto 7"))
Trivel_Relatorio_Entrada.insert("", "end", values=("Produto 8"))
Trivel_Relatorio_Entrada.insert("", "end", values=("Produto 9"))
Trivel_Relatorio_Entrada.insert("", "end", values=("Produto 10"))
Trivel_Relatorio_Entrada.insert("", "end", values=("Produto 11"))
 
Botao_Exportar = customtkinter.CTkButton(frame_relatorio_entrada, text="exportar", command=abrir_pop_up,
                                         fg_color="green")
Botao_Exportar.grid(row=1, column=3, padx=0, pady=5, sticky="e")
 
Botao_Saida_Relatorio = customtkinter.CTkButton(frame_relatorio_entrada, text="saida", width=100, command=troca_relatorio_saida)
Botao_Saida_Relatorio.grid(padx=10, row=3, column=1, sticky="w")
 
Botao_Estoque_Relatorio = customtkinter.CTkButton(frame_relatorio_entrada, text="estoque", width=100, command=troca_relatorio_estoque)
Botao_Estoque_Relatorio.grid(padx=10, row=3, column=0, sticky="e")
 
Botao_Entrada_Relatorio = customtkinter.CTkButton(frame_relatorio_entrada, text="entrada", width=100, command=troca_relatorio_entrada,
                                                  fg_color="green")
Botao_Entrada_Relatorio.grid(padx=10, row=3, column=2, sticky="w")
 
# menu do relatorio saida ______________________________________________________________________________________________
 
Titulo_Relatorio_Saida = customtkinter.CTkLabel(frame_relatorio_saida, text='Relatorio Saida',
                                                font=('comic sans', 30, 'bold'))
Titulo_Relatorio_Saida.grid(pady=10, padx=5, row=0, column=0, sticky='nsew', columnspan=4)
 
Pequisa_relatorio_saida = customtkinter.CTkEntry(frame_relatorio_saida, placeholder_text="Barra de Pesquisa:",
                                                 width=150)
Pequisa_relatorio_saida.grid(row=1, column=0, pady=5, padx=5, stick="w")
 
Coluna_Relatorio_Saida = ["Produtos", "Quantidade", "Data/Hora"]
Trivel_Relatorio_Saida = ttk.Treeview(frame_relatorio_saida, columns=Coluna_Relatorio_Saida, show="headings")
Trivel_Relatorio_Saida.grid(row=2, column=0, columnspan=5, padx=5, pady=5)
 
Trivel_Relatorio_Saida.heading("Produtos", text="Produtos")
Trivel_Relatorio_Saida.heading("Quantidade", text="Quantidade")
Trivel_Relatorio_Saida.heading("Data/Hora", text="Data/Hora")
 
Trivel_Relatorio_Saida.column("Produtos", width=140, anchor="center")
Trivel_Relatorio_Saida.column("Quantidade", width=140, anchor="center")
Trivel_Relatorio_Saida.column("Data/Hora", width=140, anchor="center")
 
Trivel_Relatorio_Saida.insert("", "end", values=("Produto 1"))
Trivel_Relatorio_Saida.insert("", "end", values=("Produto 2"))
Trivel_Relatorio_Saida.insert("", "end", values=("Produto 3"))
Trivel_Relatorio_Saida.insert("", "end", values=("Produto 4"))
Trivel_Relatorio_Saida.insert("", "end", values=("Produto 5"))
Trivel_Relatorio_Saida.insert("", "end", values=("Produto 6"))
Trivel_Relatorio_Saida.insert("", "end", values=("Produto 7"))
Trivel_Relatorio_Saida.insert("", "end", values=("Produto 8"))
Trivel_Relatorio_Saida.insert("", "end", values=("Produto 9"))
Trivel_Relatorio_Saida.insert("", "end", values=("Produto 10"))
Trivel_Relatorio_Saida.insert("", "end", values=("Produto 11"))
 
Botao_Exportar = customtkinter.CTkButton(frame_relatorio_saida, text="exportar", command=abrir_pop_up, fg_color="green")
Botao_Exportar.grid(row=1, column=3, padx=0, pady=5, sticky="e")
 
Botao_Saida = customtkinter.CTkButton(frame_relatorio_saida, text="saida", width=100, command=troca_relatorio_saida, fg_color="green")
Botao_Saida.grid(padx=10, row=3, column=1, sticky="w")
 
Botao_Estoque = customtkinter.CTkButton(frame_relatorio_saida, text="estoque", width=100, command=troca_relatorio_estoque)
Botao_Estoque.grid(padx=10, row=3, column=0, sticky="e")
 
Botao_Entrada = customtkinter.CTkButton(frame_relatorio_saida, text="entrada", width=100, command=troca_relatorio_entrada)
Botao_Entrada.grid(padx=10, row=3, column=2, sticky="w")
 
# Pop-up  ______________________________________________________________________________________________________________
 
 
atualizar()
 
aba.mainloop()