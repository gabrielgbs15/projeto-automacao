# Login site da amanzon (copiando e colando)
import pyautogui
from time import sleep
# Mover o mouse até a onde está o email
pyautogui.tripleClick(839,560,duration=1)
# Copiar o email
pyautogui.hotkey('ctrl','c')
# Mover e clicar no campo de login a onde eu coloco o email
pyautogui.click(954,282,duration=1)
# Colar o email
pyautogui.hotkey('ctrl','v')
# Apertar tab
pyautogui.press('tab')
# Apertar enter
pyautogui.press('enter')
sleep(4)
# Mover o mouse até a onde está a senha
pyautogui.tripleClick(756,596,duration=1)
# Copiar a senha
pyautogui.hotkey('ctrl','c')
# Mover e clicar no campo de senha
pyautogui.click(913,309,duration=1)
# Colar a senha
pyautogui.hotkey('ctrl','v')
# Apertar tab
pyautogui.press('tab')
# Apertar enter
pyautogui.press('enter')
