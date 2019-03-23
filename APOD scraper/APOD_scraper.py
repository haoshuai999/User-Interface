# coding=UTF-8
import csv
import socket
import requests
#import pandas as pd
import lxml
from lxml.html import fromstring
from APOD_url import urls

# Id =[]
# Title = []
# Poster = []
# Year = []
# Month = []
# Day = []
# Explanation = []
# Copyright = []
# Authors = []
# Editors = []

def scrape(urls):
	photo_id = 0 
	csv_writer = csv.writer(open("APOD.csv","w", encoding="utf-8", newline=''))
	csv_writer.writerow(["Id","Title", "Poster","Year","Month","Day","Explanation","Copyright","PageAuthor","PageEditor"])
	for url in urls:
		try:
			response = requests.get(url)
			page_html_text = response.text
			page_html = fromstring(page_html_text)

			photo_id += 1
			title = page_html.cssselect("center:nth-child(2) b")[0].text_content().strip()
			poster = 'https://apod.nasa.gov/apod/' + page_html.cssselect("p:nth-child(3) a")[0].get('href')
			date = page_html.cssselect("p:nth-child(3)")[0].text_content().strip()
			year = date.split()[0]
			if date.split()[1] == 'February':
				month = 2
			elif date.split()[1] == 'March':
				month = 3
			day = date.split()[2]
			paras = page_html.cssselect("p")[2].text_content().strip().replace('\n',' ').replace('Explanation: ','')
			copyright = page_html.cssselect("center")[1].text_content().strip().replace(title,'')
			copyright_text = copyright.split(":")[-1].replace('\n',' ')
			bottom = page_html.cssselect("center p")[3]
			bottom_text = [p.text_content() for p in bottom]
			author = bottom_text[1]
			editor = bottom_text[3]

			print("processing:", url)
			result_row = [photo_id,title,poster,year,month,day,paras,copyright_text,author,editor]
			csv_writer.writerow(result_row)

		except (socket.gaierror, requests.ConnectionError) as e:
			if e.errno != 10054:
				continue

			reconnect()
		# Id.append(photo_id)
		# Title.append(title)
		# Poster.append(poster)
		# Year.append(year)
		# Month.append(month)
		# Day.append(day)
		# Explanation.append(paras)
		# Copyright.append(copyright)
		# Authors.append(author)
		# Editors.append(editor)

	# print(photo_id)
	# print(title)
	# print(poster)
	# print(month)
	# print(paras)
	# print(copyright)
	# print(editor)

if __name__ == '__main__':
	scrape(urls)
