# Passo 1: Entrar no sistema da empresa
# pip install pyautogui
import pyautogui
import time

# pyautogui.write -> escreve um texto
# pyautogui.click -> clica com o mouse
# pyautogui.press -> aperta uma tecla
# pyautogui.hotkey -> aperta um atalho de teclado (Ctrl, C)

pyautogui.PAUSE = 0.5

# abrir o navegador
# apertar a tecla win
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Passo 2: Fazer login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# quero dar uma pausa de 3 segundos
time.sleep(3)
pyautogui.click(x=710, y=408)
pyautogui.write("coolemail.contato@gmail.com")

# passar para o próximo campo
pyautogui.press("tab")
pyautogui.write("senha12345")

# apertar no botão de login
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

# Passo 3: Importar base de dados
# pip install pandas
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto

# Para cada linha da minha tabela
for linha in tabela.index:
  # selecionar o 1º campo
  pyautogui.click(x=702, y=292)
  # texto = string = str()

  # código
  codigo = tabela.loc[linha, "codigo"]
  pyautogui.write(str(codigo))
  pyautogui.press("tab")

  # marca
  marca = tabela.loc[linha, "marca"]
  pyautogui.write(str(marca))
  pyautogui.press("tab")

  # tipo
  tipo = tabela.loc[linha, "tipo"]
  pyautogui.write(str(tipo))
  pyautogui.press("tab")

  # categoria
  categoria = tabela.loc[linha, "categoria"]
  pyautogui.write(str(categoria))
  pyautogui.press("tab")

  # preço unitário
  preco = tabela.loc[linha, "preco_unitario"]
  pyautogui.write(str(preco))
  pyautogui.press("tab")

  # custo
  custo = tabela.loc[linha, "custo"]
  pyautogui.write(str(custo))
  pyautogui.press("tab")

  # obs
  # nan = Not a number = vazio
  obs = tabela.loc[linha, "obs"]
  # se o campo estiver vazio, vai passar para o próximo
  if not pandas.isna(obs):
    pyautogui.write(str(obs))
  pyautogui.press("tab")

  # clicar no botão enviar
  pyautogui.press("enter")
  pyautogui.press("home")

# Passo 5: Repetir o processo de cadastro até os produtos acabarem