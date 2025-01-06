# Tela para pedir a senha
import pyautogui

senha = pyautogui.password(text='Digite a sua senha',title='Dados de login',mask='*')
print(senha)