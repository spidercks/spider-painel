import sys
import requests 
import json
from bs4 import BeautifulSoup
from pyfiglet import Figlet 
import colorama
import time
import asyncio
import os
import bin

def detect_os():
    if "win" in sys.platform:
        return "windows"
    else:
        return "linux"


rd = colorama.Fore.RED
cv = colorama.Fore.WHITE
mag = colorama.Fore.MAGENTA
bl = colorama.Fore.BLUE
gn = colorama.Fore.GREEN
yl = colorama.Fore.YELLOW
cy = colorama.Fore.CYAN
gg = colorama.Fore.LIGHTCYAN_EX


def logo():
    figlet = Figlet(font="standard").renderText("Spider CC")
    return (gn + figlet)
print (logo())
print (bl + "[-] GERADOR DE CC")
print (gn + "[+] Gerador kibado por spiderckz ")

opr = input (mag + "\n[x] 1) Gerar uma cc\n[x] 2) Checkar\n[x] 3) Gerar com bin \n\n[^] Escolha uma das opções:  ")

def genscard():
    cookies = {"csrftoken":"8b56rI96TwUH0X7dOT86JmPMBbUVYEpX3EI7ZKp3ZXHWnrRySD9ORyNaAaRXnW7i","_ga":"GA1.2.1579916434.1654760883","_gid":"GA1.2.1410860416.1654760883","_gads":"ID=d4f0fe2265535514-2243e178fad30069:T=1654760893:RT=1654760893:S=ALNI_MaIzJo5Kmg3rKoLXSuvDGnQkyW3uw","_gpi":"UID=0000087f297f7f43:T=1654760893:RT=1654760893:S=ALNI_MbnajBnRWmSHW7vrpR-U1w2uMwyVw",'FCNEC':'[["AKsRol_6etCde6kaPNd_o13SF2anvKLy0qaXvN6Kz0O_d9YbYS_KOfZ-j0xDjsEXL_4Otx5R38juHOOwfg0JShy5DHGmgAw2R6ZN4KZyI3qGimMjR0mQ0SEgj2ncvV4jQ32pssYst9ml2ptS_Ip2XyPbrLivgKXjIQ=="],null,[]]'}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36","content-type":"application/x-www-form-urlencoded","x-csrftoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj","x-requested-with":"XMLHttpRequest"}
    payload = {"brand":"VISA","country":"UNITED STATES","bank":"121 FINANCIAL C.U.","cvv":"","date":"","year":"","range":"500 - 1000","amount":"10","dataformat":"TEXT","pin":"on","ctoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj"}
    sitex = "https://www.vccgenerator.org/fetchdata/generate-home-credit-card/"
    rs = requests.post(sitex , headers=headers , cookies=cookies,data=payload)
    data = json.loads(rs.text)
    card = data['creditCard'][1]
    return (gn + "[-] Bandeira: %s\n[-] Numero: %s\n[-] Banco: %s\n[-] Nome: %s\n[-] Endereço: %s\n[-] País: %s\n[-] dinheiro: %s\n[-] CVV: %s\n[-] Validade: %s\n[-] Senha: %s\n============================\n[*] Telegram: t.me/spiderckz" % (card['IssuingNetwork'] , card['CardNumber'] , card['Bank'] , card['Name'] , card['Address'] , card['Country'] , card['MoneyRange'] , card['CVV'] , card['Expiry'] , card['Pin']) + cv)

def genmcard():
    cookies = {"csrftoken":"8b56rI96TwUH0X7dOT86JmPMBbUVYEpX3EI7ZKp3ZXHWnrRySD9ORyNaAaRXnW7i","_ga":"GA1.2.1579916434.1654760883","_gid":"GA1.2.1410860416.1654760883","_gads":"ID=d4f0fe2265535514-2243e178fad30069:T=1654760893:RT=1654760893:S=ALNI_MaIzJo5Kmg3rKoLXSuvDGnQkyW3uw","_gpi":"UID=0000087f297f7f43:T=1654760893:RT=1654760893:S=ALNI_MbnajBnRWmSHW7vrpR-U1w2uMwyVw",'FCNEC':'[["AKsRol_6etCde6kaPNd_o13SF2anvKLy0qaXvN6Kz0O_d9YbYS_KOfZ-j0xDjsEXL_4Otx5R38juHOOwfg0JShy5DHGmgAw2R6ZN4KZyI3qGimMjR0mQ0SEgj2ncvV4jQ32pssYst9ml2ptS_Ip2XyPbrLivgKXjIQ=="],null,[]]'}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36","content-type":"application/x-www-form-urlencoded","x-csrftoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj","x-requested-with":"XMLHttpRequest"}
    payload = {"brand":"VISA","country":"UNITED STATES","bank":"121 FINANCIAL C.U.","cvv":"","date":"","year":"","range":"500 - 1000","amount":"10","dataformat":"TEXT","pin":"on","ctoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj"}
    sitex = "https://www.vccgenerator.org/fetchdata/generate-home-credit-card/"
    rs = requests.post(sitex , headers=headers , cookies=cookies,data=payload)
    data = json.loads(rs.text)
    open("generated_card.txt","w").write("")
    for i in range(1,10):
        card = data['creditCard'][i]
        f = open("generated_card.txt","a")
        f.write("[-] Bandeira: %s\n[-] Numero: %s\n[-] Banco: %s\n[-] Nome: %s\n[-] Endereco: %s\n[-] País: %s\n[-] Dinheiro: %s\n[-] CVV: %s\n[-] Validade: %s\n[-] Senha: %s\n===================================\n" % (card['IssuingNetwork'] , card['CardNumber'] , card['Bank'] , card['Name'] , card['Address'] , card['Country'] , card['MoneyRange'] , card['CVV'] , card['Expiry'] , card['Pin']))
    return (gn + "[$] Sucesso!\n[+] Salvo em generated_card.txt" + cv)

def ccvalidator(number , type):
    site = "https://www.tools4noobs.com/"
    payload = {"action":"ajax_credit_card_validate","text":number,"cc":type}
    result = requests.post(site , data=payload)
    soup = BeautifulSoup(result.text ,"html.parser")
    return (bl + soup.text + cv)

if opr == "1":
    print (cy + "[&] Carregando... \n\n")
    time.sleep(1)
    print (genscard())
elif opr == "2":
    print (mag + "[&] Carregando...\n\n")
    number = input(yl + "[$] Insira o número do cartão: ")
    if detect_os() == "windows":
        popen = os.popen("node core\\val.js " + number).read()
        print (bl + popen + cv)
    else:
        popen = os.popen("node core/val.js " + number).read()
        print (bl + popen + cv)
elif opr == "3":
    print (bl + "[&] Carregando...")
    time.sleep(0.3)
    number = input(gn + "[-] Bin -  > ")
    round = input(cy + "[+] Quantidade ex: (10) - > ")
    print (rd)
    bin.bin_generator(number , round)
    print ("Salvo em bin_generated.txt !")
    print (mag + "[$] Telegram: t.me/spiderckz" + cv)
