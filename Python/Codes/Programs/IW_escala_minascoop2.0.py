nome_paciente = 'BENEDITA ROSA MONTEIRO'
data_inicio = '01/05/2024'
data_fim = '31/05/2024'

enfermeiras = ['LUIZA ALICIA', 'NATHIELE DE CASSIA', 'CREUZA PEREIRA', 'CREUSA SERAPI']
loop_enfermeiras = [
    (528, 376,enfermeiras[0]), # enfermeira1, impar dia
    (514, 395,enfermeiras[1]), # enfermeira2, impar noite
    (433, 412,enfermeiras[2]), # enfermeira3, par dia
    (431, 432,enfermeiras[3]) # enfermeira4, par noite
    ]

# IW tem que ser o primeiro aplicativo na barra de ferramentas
# resolução da tela 1360x768
import time
import pyautogui

pyautogui.PAUSE = 3

# 0 clicar IW

pyautogui.click(x=418, y=754)

# 1 clicar na lupa

pyautogui.click(x=173, y=204)
time.sleep(2)

# 2 clicar em paciente

pyautogui.click(x=479, y=297)

# 3 digitar nome paciente

pyautogui.write(nome_paciente)

# 4 clicar pesquisar

pyautogui.press('enter')
pyautogui.click(x=589, y=624)

# 5 clicar paciente

pyautogui.click(x=641, y=247)

# 6 clicar adicionar

pyautogui.click(x=616, y=629)

# 7 clicar equipe

pyautogui.click(x=32, y=572)

# 8 clicar escala enfermagem domiciliar

pyautogui.click(x=391, y=205)

# 9 clicar pesquisar e selecionar periodo

pyautogui.click(x=500, y=694)
pyautogui.click(x=525, y=624)

# 10 clicar 2x em data 1

pyautogui.doubleClick(x=723, y=308)

# 11 digitar data 1

pyautogui.write(data_inicio)

# 12 clicar 2x em data 2

pyautogui.doubleClick(x=709, y=321)

# 13 digitar data 2

pyautogui.write(data_fim)

# 14 clicar ok

pyautogui.click(x=643, y=497)

def ate_nome(): # função para cada enfermeiro
    # 15.1 clicar turnos, selecionar 1 em 4
    pyautogui.click(x=919, y=695)
    pyautogui.click(x=984, y=533)
    pyautogui.click(x=767, y=279) # 16 clicar selecionar
    pyautogui.click(x=950, y=697) # 16.1 clicar limpar
    # 17 clicar cooperativa e selecionar cooperativa
    pyautogui.click(x=236, y=215)
    pyautogui.click(x=211, y=234)
    pyautogui.click(x=333, y=162) # 18 clicar nome

def depois_nome():
    # 19 clicar pesquisar, enfermeira e selecionar
    pyautogui.click(x=418, y=695)
    pyautogui.click(x=418, y=695)
    pyautogui.click(x=411, y=345)
    pyautogui.click(x=332, y=697)
    # 20 clicar profissional e escalar profissional
    pyautogui.click(x=652, y=695)
    pyautogui.click(x=726, y=425)
    # 21 clicar ok e limpar
    pyautogui.click(x=679, y=391)
    pyautogui.click(x=776, y=306)

for x, y, enfermeira in loop_enfermeiras: # 22 loopar 15 ao 24 trocando impar/par dia/noite
    pyautogui.click(x=x, y=y) # 15 clicar impar/par dia/noite,
    ate_nome()
    pyautogui.write(enfermeira)# 18.1 digitar nome
    depois_nome()

# 23 finalizar cilcando no x e em prontuario

pyautogui.click(x=1342, y=86)
pyautogui.click(x=535, y=320)