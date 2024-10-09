# Automatização de Tarefas

Projeto que automatiza processos repetitivos, cuja finalidade é o cadastramento de uma base de dados em um sistema, feito durante a primeira aula da Jornada Python da Hashtag Treinamentos com a linguagem python. 
Pode ser aplicado em projetos pessoais, empresas e mais. Para teste, foi utilizado o Sistema Python Power Up de cadastros da hashtag: https://dlp.hashtagtreinamentos.com/python/intensivao/login.

## 🚀 Passo a passo do que foi feito

* Passo 1: Entrar no sistema específico - fazer a máquina abrir o navegador, pressionar a tecla Win e entrar no link [Python Power Up](https://dlp.hashtagtreinamentos.com/python/intensivao/login). Nesse processo,
  cada comando deve ter uma pequena pausa com pyautogui.PAUSE = 0.5 para dar tempo das informações carregarem.
  
* Passo 2: Fazer login - fazer a máquina pausar por mais ou menos 3 segundos para que o site possa carregar antes dos comandos serem executados, digitar cada informação (e-mail e senha) e passar para a próxima até
  o botão de login para enviar.
  
* Passo 3: Importar base de dados - importa a base de dados do projeto com a biblioteca pandas e printar as informações no terminal para consultas.
  
* Passo 4: Cadastrar 1 produto - definir todas as informações da tabela, selecionar o primeiro campo e cadastrar o primeiro produto.

* Passo 5: Repetir o processo de cadastro até os produtos acabarem - comando de repetição for, condicional if e localização de informações específicas na tabela com tabela.loc[linha, coluna] para que, assim, o projeto
  seja automatizado.

## 📋 Ferramentas/Linguagens utilizadas

* [Python](https://www.python.org/doc/) - Linguagem de programação back-end utilizada.
* [Pyautogui](https://pyautogui.readthedocs.io/en/latest/) - Biblioteca utilizada para automatização de processos repetitivos.
* [Pandas](https://pandas.pydata.org/docs/) - Biblioteca utilizada para a importação e visualização da base de dados.

---

Feito com 💜 by Juliana Morais! :)
