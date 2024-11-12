import pyautogui as ag
import time 

total = []
while True:
    a = str(input("Digite o botão: "))
    if a == "0":
        break
    time.sleep(3)
    total.append(a + ag.position())

print(total)
# with open('Posicoes.txt', 'w') as arquivos:
#     pass