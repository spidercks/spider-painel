import socket, random, time, http.client, json, os, subprocess
from colorama import Fore, Back, Style 
startTime = time.time()

def painel():
  print(Fore.RED + """  	
 
╭━━━╮╱╱╱╱╱╭╮╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱┃┃╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱┃┃
┃╰━━┳━━┳┳━╯┣━━┳━╮┃╰━╯┣━━┳┳━╮╭━━┫┃
╰━━╮┃╭╮┣┫╭╮┃┃━┫╭╯┃╭━━┫╭╮┣┫╭╮┫┃━┫┃
┃╰━╯┃╰╯┃┃╰╯┃┃━┫┃╱┃┃╱╱┃╭╮┃┃┃┃┃┃━┫╰╮
╰━━━┫╭━┻┻━━┻━━┻╯╱╰╯╱╱╰╯╰┻┻╯╰┻━━┻━╯
╱╱╱╱┃┃
╱╱╱╱╰╯)
  
  
  """)
  print('')

painel()
print('1 - GERADOR CC \n2 - SPIDER BROWSER \n3 - PAINEL DE CONSULTAS')
select = int(input('\nEscolha uma opção: '))

if select == 1:
  os.system('cls' if os.name == 'nt' else 'clear')
  
  exec(open("cc.py").read())
    

if select ==2:
  os.system('cls' if os.name == 'nt' else 'clear')

  exec(open("browser.py").read())

elif select ==3:
  os.system('cls' if os.name == 'nt' else 'clear')
  
  exec(open("SpiderPainel.py").read())
  
