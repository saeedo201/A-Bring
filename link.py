#!/usr/bin/python 2.7.16
import bs4  
import requests
print  "----------------------------------"
print      "========>Z.O.A.L<========"
print          "===>ZoalKtoom<===="
print            "--------------\n"
print "  [1] Bring a links	 [2] Exit"
print "\n"
choose =raw_input("[Chose Number]~#:")
if choose == '1':
	user = raw_input("Please Enter a Url \n")
	print "proccessing...\n"
	url = requests.get('https://{0}'.format(user)) 
	Soup = bs4.BeautifulSoup(url.text,"html.parser")
	print "Here It Is :\n" 
	for link in Soup.findAll('a' , href=True):
	    	print link['href']
if choose == '2':
	print "Thanks For Usage"
