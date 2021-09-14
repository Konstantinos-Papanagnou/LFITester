#!/usr/bin/env python3

# CAUTION this script doesn't check for Remote File Inclusion (RFI)

# DISCLAIMER
# ONLY test this in a server you have permission to do it!!!!!!!

from ArgumentHandler import ArgumentHandler
from termcolor import colored
import PayloadManager
import sys
from pyfiglet import Figlet
from proxies_list import clean_proxies
from Crawler import webcrawler
	
def main():
	try:
		ascii_art = Figlet(font='big')
		print(colored(ascii_art.renderText('LFITester'), 'yellow'))
		arghandler = ArgumentHandler()
		if not arghandler.url:
			arghandler.parser.print_help(sys.stderr)
			exit(1)
		if arghandler.enable_proxies:
			print(colored("Detected Enabled Proxies. Setting up proxy list...",'green'))
			clean_proxies()
		print(colored("This script doesn't check for Remote File Inclusion (RFI)", 'blue'))
		print(colored("If it doesn't show any results that means it didn't find anything!!!", 'blue'))
		if type(arghandler.url) is not list:
			if arghandler.crawler:
				test_urls = webcrawler(arghandler.url)
				for url in test_urls:
					print(colored(f"Testing: {url}\n\n", 'green'))
					PayloadManager.Payload(url, arghandler.outfile, verbosity=arghandler.verbosity)
			else:
				print(colored(f"Testing: {arghandler.url}\n\n", 'green'))
				PayloadManager.Payload(arghandler.url, arghandler.outfile, verbosity=arghandler.verbosity)
		else:
			if arghandler.crawler:
				for url in arghandler.url:
					test_urls = webcrawler(url)
					for endpoint in test_urls:
						print(colored(f"Testing: {endpoint}\n\n", 'green'))
						PayloadManager.Payload(endpoint, arghandler.outfile, verbosity = arghandler.verbosity)
			else:
				for url in arghandler.url:
					print(colored(f"Testing: {url}\n\n", 'green'))
					PayloadManager.Payload(url, arghandler.outfile, verbosity = arghandler.verbosity)
	except KeyboardInterrupt:
		print('\nGracefully Exiting...\n')
	
	
	
	
if __name__ == '__main__':
	main()

