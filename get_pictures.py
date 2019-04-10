import os
from pathlib import Path
from google_images_download import google_images_download
from configparser import ConfigParser
import json

CONFIG_FILE = 'picture_download.ini'

def download_sections(sections, amount, color, size, store_path):
	response = google_images_download.googleimagesdownload()
	
	key = ','.join(sections)
	
	arguments = {'keywords' : key, 'limit' : amount, 'color' : color, 'size' : size, 'output_directory' : store_path}
	response.download(arguments)

def download_section(section, amount, color, size, store_path):
	response = google_images_download.googleimagesdownload()
	
	arguments = {'keywords' : section, 'limit' : amount, 'color' : color, 'size' : size, 'output_directory' : store_path}
	response.download(arguments)	
	
if __name__ == '__main__':
	config = ConfigParser()
	config.read(CONFIG_FILE)
	
	store_path = None
	
	try:
		store_path = config['Search']['store_path']
	
		if not os.path.exists(store_path):
			os.makedirs(store_path)
	except:
		pass
	
	amount = None
	
	try:
		amount = config['Search']['amount']
	except Exception as exc:
		print(exc)
		
	size = None
	
	try:
		size = config['Search']['size']
	except Exception as exc:
		print(exc)
		
	color = None
	
	try:
		color = config['Search']['color']
	except Exception as exc:
		print(exc)
	
	sections = json.loads(config['Search']['sections'])
	
	if type(sections) is list:
		if not amount:
			print('Количество изображений для скачивания не определено')
			exit()
		
		download_sections(sections, amount, color, size, store_path)
		
	elif type(sections) is dict:
		for key in sections:
			download_section(key, sections[key], color, size, store_path)
	else:
		exit()