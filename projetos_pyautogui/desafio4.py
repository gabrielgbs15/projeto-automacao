import pyautogui
import pyperclip

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

# Mover o mouse até a onde vai escrever
pyautogui.moveTo(746,93,duration=1)
# Clicar no locar onde vai ser colocado o texto
pyautogui.click()
# Escrever a mensagem
escrever_frase('Altomação é Imcrível!')