#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1


def findAdmin():
	f = open("list.txt","r");
	link = raw_input("\033[1;34mEnter Site Name \n(ex : example.com or www.example.com ):\033[1;32m ")
	print "\n\n\033[1;33mAvilable links : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "\033[91mOK => ",req_link

def Credit():
	Space(9); print "\033[1;34m____ ____ _  _ \033[91m.\033[1;34m _  _"
	Space(9); print "\033[1;34m|__| |  | |\/| | |\ |"
	Space(9); print "\033[1;34m|  | |__| |  | | | \|"
	Space(9); print "\033[37mtwitter \033[91m@\033[37mAHuxlr\033[1;m"
	Space(9); print "\033[1;31m---------------------\033[1;m\n"

Credit()
findAdmin()
