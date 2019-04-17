import os
from pathlib import Path
from google_images_download import google_images_download
from argparse import ArgumentParser
import json

def download_sections(requests, amount, store_path):
	response = google_images_download.googleimagesdownload()
	
	key = ','.join(requests)
	
	arguments = {'keywords' : key, 'limit' : amount, 'output_directory' : store_path}
	response.download(arguments)

	
if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument("-a", "--amount", 	dest="amount", 				help="amount of pictures to download", 		required=True)
	parser.add_argument("-d", "--dir", 		dest="directory", 			help="root directory to collect pictures", 	required=True)
	parser.add_argument("-r", "--requests", dest="requests_filename", 	help="file with requests", 					required=True)
	
	args = None
	
	try:
		args = parser.parse_args()
	except Exception as exc:
		print(exc)
		exit()

	requests = None
	
	try:
		with open(args.requests_filename, 'r') as reqFd:
			lines = reqFd.readlines()
			requests = [l.strip('\n\r') for l in lines]
			
	except Exception as exc:
		print(exc)
		exit()
		
	download_sections(requests, args.amount, args.directory)