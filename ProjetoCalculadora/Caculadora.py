
import tkinter as tk
from tkinter import messagebox

# Funções com ERROS propositalmente (para aluno corrigir)
def somar():
    try:
        a = int(entrada1.get())
        b = int(entrada2.get())
        resultado['text'] = a + b  
    except:
        messagebox.showerror("Erro", "Verifique os valores digitados.")

def subtrair():
    try:
        a = int(entrada1.get())
        b = int(entrada2.get())
        resultado['text'] = a - b  
    except:
        messagebox.showerror("Erro", "Verifique os valores digitados.")

def multiplicar():
    try:
        a = int(entrada1.get())
        b = int(entrada2.get())
        resultado['text'] = a * b  
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Não é possível dividir por zero.")
    except:
        messagebox.showerror("Erro", "Verifique os valores digitados.")

def dividir():
    try:
        a = int(entrada1.get())
        b = int(entrada2.get())
        if b == 0:
            messagebox.showerror("Erro", "Não é possível dividir por zero.")
        else:
            resultado['text'] = a / b  
    except:
        messagebox.showerror("Erro", "Verifique os valores digitados.")

def divisao_inteira():
    try:
        resultado['text'] = int(entrada1.get()) // int(entrada2.get())  
    except:
        messagebox.showerror("Erro", "Verifique os valores digitados.")

def resto_divisao():
    try:
        resultado['text'] = int(entrada1.get()) / int(entrada2.get())  
    except:
        messagebox.showerror("Erro", "Verifique os valores digitados.")

def potencia():
    try:
        resultado['text'] = int(entrada1.get()) ** int(entrada2.get())  
    except:
        messagebox.showerror("Erro", "Verifique os valores digitados.")

def limpar_campos():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    resultado['text'] = ""

# Entrada ativa
entrada_ativa = 1

def inserir_numero(numero):
    campo = entrada1 if entrada_ativa == 1 else entrada2
    campo.insert(tk.END, str(numero))

def selecionar_entrada1(_=None):
    global entrada_ativa
    entrada_ativa = 1

def selecionar_entrada2(_=None):
    global entrada_ativa
    entrada_ativa = 2

# Janela
janela = tk.Tk()
janela.title("Calculadora Visual")
janela.geometry("320x500")
janela.configure(bg="#f0f4f7")

tk.Label(janela, text="Calculadora", font=("Helvetica", 20), bg="#f0f4f7").pack(pady=10)

entrada1 = tk.Entry(janela, font=("Helvetica", 14), justify="right")
entrada1.pack(padx=10, pady=5, fill='x')
entrada1.bind("<FocusIn>", selecionar_entrada1)

entrada2 = tk.Entry(janela, font=("Helvetica", 14), justify="right")
entrada2.pack(padx=10, pady=5, fill='x')
entrada2.bind("<FocusIn>", selecionar_entrada2)

# Frame geral para botoes numeros + operacoes
frame_geral = tk.Frame(janela, bg="#f0f4f7")
frame_geral.pack(pady=10)

# Botões numéricos
frame_numeros = tk.Frame(frame_geral, bg="#f0f4f7")
frame_numeros.grid(row=0, column=0, padx=10)

botoes = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for i, linha in enumerate(botoes):
    for j, num in enumerate(linha):
        tk.Button(
            frame_numeros, text=str(num), width=5, height=2,
            font=("Helvetica", 12), bg="white", command=lambda n=num: inserir_numero(n)
        ).grid(row=i, column=j, padx=4, pady=4)

# Botões de operações
frame_operacoes = tk.Frame(frame_geral, bg="#f0f4f7")
frame_operacoes.grid(row=0, column=1, sticky='n')

estilo_botao = {"width": 5, "height": 2, "font": ("Helvetica", 12)}

operacoes = [
    ("+", somar, "#a8d5ff"),
    ("-", subtrair, "#91c788"),
    ("×", multiplicar, "#ffb347"),
    ("÷", dividir, "#ff6961"),
    ("//", divisao_inteira, "#cba0ff"),
    ("%", resto_divisao, "#ffb6c1"),
    ("^", potencia, "#8dd3c7"),
    ("C", limpar_campos, "#ff6666")
]

for i, (texto, funcao, cor) in enumerate(operacoes):
    tk.Button(
        frame_operacoes, text=texto, command=funcao, bg=cor, **estilo_botao
    ).grid(row=i, column=0, pady=3)

# Resultado
resultado = tk.Label(janela, text="", font=("Helvetica", 18), bg="#f0f4f7", fg="#333")
resultado.pack(pady=20, fill='x')

tk.Label(janela, text="Versão com erros – Corrija as funções!", bg="#f0f4f7", fg="gray").pack(side="bottom", pady=5)

janela.mainloop()