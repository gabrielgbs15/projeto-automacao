import pyautogui
import pyperclip

# Criar a tela de login onde vai digitar o email
email = pyautogui.prompt(text='Digite o seu email',title='Tela de login')
# Criar a tela de login pnde vai digitar a senha
senha = pyautogui.password(text='Digite a sua senha',title='Tela de login',mask='*')
# Criar a automação onde vai copiar e colar o email
pyperclip.copy(email)
pyautogui.click(840,113,duration=0.5)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
# Criar a automação onde vai copiar e colar a senha
pyperclip.copy(senha)
pyautogui.hotkey('ctrl','v')