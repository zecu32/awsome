# -*- coding: utf-8 -*- 
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
#from urllib.parse import urlparse
import requests

url = "http://urx2.nu/Ot7A"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html,"lxml")
#print(soup.prettify())
k = soup.find("a",class_="c-pagination__num")
a2 = str(k.get("href"))
a1 = re.sub(r"/\d/","/1/",str(a2))
a3 = re.sub(r"/\d/","/3/",str(a2))
a4 = re.sub(r"/\d/","/4/",str(a2))
a5 = re.sub(r"/\d/","/5/",str(a2))
urllist=[a1,a2,a3,a4,a5]
#tmp3 = [print(n) for n in urllist]

list =[]
df = pd.DataFrame({},index=["店舗名","郵便番号","住所","電話番号","オープン日"])

def ver3():
	for url in urllist:
		print(url)
		html = urllib.request.urlopen(url)
		soup = BeautifulSoup(html,"lxml")
		for atag in soup.find_all("a",target="_blank"):
			txet = atag.get_text()
			txet = str(txet).split(r"\u")
			txet = re.sub(r"\\u"," ",str(txet))
			txet = re.sub(r"(\[|\]|\"|\||\n|\'|：)","",str(txet))
			#print(txet)
			href = atag.get("href")
			#print(href)
			list.append([txet,href])
		del list[-1]
#del list[-1]
ver3()
#print("test")
#tmp =[ print(i) for i in list]

def var2(name,url):
	print(name,url)
	html =urllib.request.urlopen(url)
	soup =BeautifulSoup(html,"lxml")
	#print(soup.prettify())
	address = soup.find("p",class_="rstinfo-table__address")
	address = str(address.get_text())
	print(address)
	tel = soup.find("p",class_="rstdtl-side-yoyaku__tel-number")
	tel = str(tel.get_text())
	tel = re.sub(r"(\[|\]|\"|\||\n|\'|：)","",str(tel))
	tel = re.sub(r" {2}","",str(tel))
	print(tel)
	opendate =soup.find("p",class_="rstinfo-opened-date")
	opendate =re.sub(r"<[^>]*?>","",str(opendate))
	print(opendate)
	tmp = address.split(" ")
	tmp = tmp[0]
	#print(tmp)
	url = "https://yubin.senmon.net/search?q="+str(tmp)
	#print(url)
	url = requests.get(url)
	url = url.url
	#print(url2)
	html =urllib.request.urlopen(url)
	#print(html)
	soup =BeautifulSoup(html,"lxml")
	#print(soup.prettify())
	zipcode = soup.find("a",class_="z")
	zipcode = re.sub(r"<[^>]*?>","",str(zipcode))
	print(zipcode)
	line.append([name,zipcode,address,tel,opendate])
	#print(name)
#name ="test"
#url = "https://tabelog.com/aichi/A2305/A230501/23067844/"
line = []
#print("test",list)
tmp = [var2(i[0],i[1]) for i in list]
#tmp2 = [print(j) for j in line]
#url = "https://tabelog.com/aichi/A2301/A230103/23039690/"
#var2("name",url)
df = pd.DataFrame(line)
print(df)
path = os.getcwd()+ "/result.csv"
df.to_csv(path,encoding="shift_jis")