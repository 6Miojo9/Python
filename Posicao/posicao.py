import pyautogui as ag
import time 

total = list()
while True:
    a = str(input("Digite o botão: "))
    if a == "0":
        break
    elif a == " ":
        total.append(a)
    else:
        time.sleep(3)
        total.append(a + " " + str(ag.position()))

with open('posicoes.txt', 'w') as arquivos:
    for valor in total:
        arquivos.write(str(valor) + '\n')