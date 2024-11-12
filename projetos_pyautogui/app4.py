import pyautogui

# mover o mouse até a onde você quer escrever 
pyautogui.moveTo(746,93,duration=1)
# Clicar no campo a onde quer digitar
pyautogui.click()
# Digitar a mensagem
pyautogui.typewrite('Bom dia Mundo!')