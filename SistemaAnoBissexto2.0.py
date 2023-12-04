import tkinter as tk
from tkinter import messagebox

def bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def verificar_bissexto():
    try:
        ano = int(entry_ano.get())
        if bissexto(ano):
            messagebox.showinfo("Resultado", f"{ano} é um ano bissexto.")
        else:
            messagebox.showinfo("Resultado", f"{ano} não é um ano bissexto.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um ano válido.")

# Configuração da janela principal
root = tk.Tk()
root.title("Verificador de Ano Bissexto")
root.geometry("300x150")
root.configure(bg='#e6f7ff') # Cor de fundo

# Widgets
label_ano = tk.Label(root, text="Digite um ano:", bg='#e6f7ff') # Cor de fundo
label_ano.pack(pady=10)

entry_ano = tk.Entry(root, bg='#f2f2f2') # Cor de fundo
entry_ano.pack(pady=10)

btn_verificar = tk.Button(root, text="Verificar", command=verificar_bissexto, bg='#4CAF50', fg='white') # Cores de fundo e texto
btn_verificar.pack(pady=10)

# Inicia o loop principal
root.mainloop()