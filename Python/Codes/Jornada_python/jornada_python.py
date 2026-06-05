'''
passo 1: entrar no sistema da empresa
passo 2: Fazer login
passo 3: Importar a base de dados
passo 4: cadastrar 1 produto
passo 5: repetir passo 4 ate acabar
'''
import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5 # Da pausa de 0.5s entre comandos do pyautogui
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
User = 'Wallace'
password = "password"
tabela = pandas.read_csv(r'C:\Users\Usuario\Desktop\Wallace\Study\Programing\Python\produtos.csv')

pyautogui.press('win')
pyautogui.write('brave')
pyautogui.press('enter')
# pyautogui.hotkey('ctrl', 'c')
time.sleep(5) #pausa o programa pro 5s

pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=468, y=368)
pyautogui.write(User)
pyautogui.press('tab')
pyautogui.write(password)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

pyautogui.press('tab')

for linha in tabela.index: # cria uma variavel com o nome linha e inicia um loop colocando o valor da linha na variavel linha

    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs): # check if empty
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter')

    pyautogui.scroll(5000)
    pyautogui.click(x=465, y=257)

    #for _ in range(10): #first solution to the problem. given a better one (pyautogui.scroll)

        #pyautogui.press('tab')
