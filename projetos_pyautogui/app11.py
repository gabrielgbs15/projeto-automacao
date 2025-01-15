# Reconhecimento de imagem simples com pyautogui
import pyautogui

numero = pyautogui.locateCenterOnScreen('/home/gabrielborges/Documentos/Curso_python_automacao/projeto-automacao/projetos_pyautogui/numero4.png')
pyautogui.moveTo(numero,duration=2)