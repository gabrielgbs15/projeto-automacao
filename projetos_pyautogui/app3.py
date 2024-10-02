# Como pegar e "Arrastar" algo para outro lugar 
import pyautogui

for i in range(5):
    # mover para a cordenada
    pyautogui.moveTo(2223,224,duration=1)
    #selecionar e arrastar
    pyautogui.dragTo(3018,360,button='left',duration=1)