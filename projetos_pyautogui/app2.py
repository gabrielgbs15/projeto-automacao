# Como usar a função click.
import pyautogui

# Click pessonalizado
pyautogui.click(x=2575,y=731,clicks=100,interval=0.2,button='left',duration=1)

# Click na posição atual(Com os botões do mouse)
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='middle')

# Click x vezes na mesma posição
pyautogui.click(clicks=10)

# Funções prontas para clicks
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
pyautogui.tripleClick()