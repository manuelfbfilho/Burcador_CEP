import tkinter as tk
import requests
import re



# Função para realizar a pesquisa do CEP
def pesquisar_cep():
    cep = cep_entry.get()

    # Validação do CEP (exemplo: verificar se possui 8 dígitos)
    if not re.match(r"^\d{8}$", cep):
        resultado_label.config(text="CEP inválido.")
        return
    else:
        resultado_label.config(text="")  # Limpa o texto de resultado

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    data = response.json()

    if "erro" in data:
        resultado_label.config(text="CEP não encontrado.")
    else:
        endereco_label.config(text=f"{data['logradouro']}")
        bairro_label.config(text=f"{data['bairro']}")
        cidade_label.config(text=f"{data['localidade']}")
        estado_label.config(text=f"{data['uf']}")
        ddd_label.config(text=f"{data['ddd']}")

# Configurações da janela principal
root = tk.Tk()
root.title("Buscador de CEP")
root.title("Botão Personalizado")
root.geometry("500x350")

# Carregue a imagem de fundo (Colocar o endereço de onde está sua imagem)
bg_image = tk.PhotoImage(file="C:\\Users\\Dell\\Downloads\\Aulas_Python\\BuscaCEP\\BuscadorCEP.png")

# Crie um canvas para exibir a imagem de fundo
canvas = tk.Canvas(root, width=500, height=350)
canvas.pack()

# Exiba a imagem no canvas
canvas.create_image(0, 0, anchor="nw", image=bg_image)

# Caixa de texto para digitar o CEP
cep_entry = tk.Entry(root, width=19, bg="#007c8a", relief="flat", font=("Helvetica", 10))
cep_entry.place(x=283, y=76)

# Carregue a imagem do botão (Colocar o endereço de onde está sua imagem do botão)
button_image = tk.PhotoImage(file="C:\\Users\\Dell\\Downloads\\BotaoPeq.png")

# Crie um rótulo para exibir a imagem como botão
custom_button = tk.Button(root, image=button_image, command=pesquisar_cep, bd=0, highlightthickness=0, activebackground="#001c30")
custom_button.place(x=440, y=68)

# Resto do seu código (rótulos para informações sobre o CEP)
resultado_label = tk.Label(root, font=("Helvetica", 11), fg="red", bg="#001c30")
resultado_label.place(x=310, y=105)

endereco_label = tk.Label(root, font=("Helvetica", 10), fg="#d7b317", bg="#001c30")
endereco_label.place(x=35, y=200)

bairro_label = tk.Label(root, font=("Helvetica", 10), fg="#d7b317", bg="#001c30")
bairro_label.place(x=350, y=200)

cidade_label = tk.Label(root, font=("Helvetica", 10), fg="#d7b317", bg="#001c30")
cidade_label.place(x=35, y=270)

estado_label = tk.Label(root, font=("Helvetica", 10), fg="#d7b317", bg="#001c30")
estado_label.place(x=250, y=270)

ddd_label = tk.Label(root, font=("Helvetica", 10), fg="#d7b317", bg="#001c30")
ddd_label.place(x=400, y=270)

root.mainloop()

