import pyautogui

# mover o mouse até a onde você quer escrever 
pyautogui.moveTo(835,320,duration=1)
# Clicar no campo a onde quer digitar
pyautogui.click()
# Digitar a mensagem
pyautogui.typewrite('Bom dia Mundo!')