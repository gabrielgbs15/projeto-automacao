# Como tirar print da tela inteira, ou de uma parte dela
import pyautogui

# Tirado print da tela inteira
pyautogui.screenshot('tela.jpg')

# Tirando print só da calculadora
pyautogui.screenshot('calculadora.jpg',region=(815,140,345,486))