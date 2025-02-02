import pyautogui
import webbrowser
from time import sleep

# DESAFIO 🥇
# 1) Navegue até o site https://cursoautomacao.netlify.app/
webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(1)
# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
pyautogui.moveTo(1196,260,duration=1)
sleep(1)
pyautogui.scroll(-15)
sleep(1)
pyautogui.click(935,311,duration=1)
sleep(1)
pyautogui.typewrite('Gabriel Borges de Souza')
sleep(1)
# 3) Clique em alerta, para gerar a alerta
pyautogui.click(921,352,duration=1)
sleep(1)
# 4) Feche a alerta
pyautogui.click(1274,237,duration=1)
sleep(1)
# 5) Suba a página totalmente para cima
pyautogui.scroll(15)
sleep(1)
# 6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
pyautogui.scroll(-20)
sleep(1)
pyautogui.click(966,587,duration=1)
sleep(1)
pyautogui.click(1309,177,duration=1)
sleep(1)
pyautogui.click(966,705,duration=1)
sleep(1)
pyautogui.click(1309,177,duration=1)
sleep(1)
# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
pyautogui.alert(text='VOCÊ TERMINOU',title='Automação',button='OK')
