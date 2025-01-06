# Criando uma janela para pedir informções
import pyautogui

email = pyautogui.prompt(text='Digite o seu e-mail', title='Informação Obrigatória')
print(f'Você digitou {email}')