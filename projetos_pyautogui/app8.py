# Comfirmar se algo vai acontecer ou não.
import pyautogui

resposta = pyautogui.confirm(text='Continuar rodando essa automção?',title='Confimações',buttons=['sim','nao','cancelar'])

if resposta == 'sim':
    print('Continuar a automação!')
elif resposta == 'não':
    print('Encerrando a automação!')
else:
    print('Automação cancelada!')