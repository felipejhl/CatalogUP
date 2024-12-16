import pyautogui
import time

# Passo 1: Abrir o navegador e entrar no sistema da empresa (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
pyautogui.PAUSE = 0.5

# Abrindo o Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter") 

# Entrando no Sistema
time.sleep(2)
pyautogui.click(x=209, y=59) # Clicar na barra de pesquisa
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Passo 2: Fazer login no sistema
time.sleep(2)
pyautogui.click(x=395, y=408) # Clicar no campo de E-mail
pyautogui.write("administrador@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=390, y=291) # Clicar no campo de Código do Produto 

    # Codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # Preco Unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # Custo 
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # OBS
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # Enviar o cadastro
    pyautogui.press("enter")

    pyautogui.scroll(1920)

# Passo 5: Repetir o processo de cadastro até o ultimo produto