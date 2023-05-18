import requests
from os import path
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help=' [+] Ingresar un Dominio ')
parser = parser.parse_args()

def noc():
    if parser.target:
        if path.exists('subdominios.txt'):
            wordlist = open('subdominios.txt','r')
            wordlist = wordlist.read().split('\n')
            
            for subdominio in wordlist:
                url = "http://"+subdominio+"."+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("[+] Subdominio Encontrado: " + url)
            
            for subdominio in wordlist:
                url = "https://"+subdominio+"."+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("[+] Subdominio Encontrado: " + url)
            
                
    else:
        print("[-] Ingresar un Dominio")  
                

if __name__ == '__main__':
    try:
        noc()
    except KeyboardInterrupt:
        sys.exit()