# Login no site da Amazon
import pyautogui
from time import sleep
# Pegar as coordenadas da tela de login e clicar
pyautogui.click(933,281,duration=1.5)
sleep(1)
# Digitar o email
pyautogui.typewrite('email@gmail.com')
sleep(1)
# Apertar tab para mudar para o botão de continuar
pyautogui.press('tab')
sleep(1)
# Apertar enter
pyautogui.press('enter')
sleep(5)
# Digitar a senha
pyautogui.typewrite('senha')
sleep(1)
# Apertar tab novamente para mudar para botão de fazer login
pyautogui.press('tab')
sleep(1)
# Apertar enter novamente
pyautogui.press('enter')