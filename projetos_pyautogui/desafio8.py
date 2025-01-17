import pyautogui

captcha = pyautogui.locateCenterOnScreen('/home/gabrielborges/Documentos/Curso_python_automacao/projeto-automacao/projetos_pyautogui/quadrado.png')

pyautogui.click(captcha,duration=2)
