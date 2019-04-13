from PIL import Image, ImageDraw, ImageFont
from stegano import lsb

blank = 'images/meme.jpg'
temp = 'images/temp.png'
leet = 'images/leet.png'

def openFont(sz):
	return ImageFont.truetype('fonts/Roboto-Bold.ttf', size=sz)	 	

def genImage(x, y, message, font):
	draw.text((x,y), message, font=font)

def genMeme():
	global draw

	top = ['ME','GOOGLE']
	middle = ['PICTURE', 'SYMPTOM']
	bottom = ['IS THIS A MEME?', 'IS THIS CANCER?']
	 
	image = Image.open(blank)
	 
	draw = ImageDraw.Draw(image)

	from random import randint
	pos = randint(0, len(top) - 1)

	genImage(150, 150, top[pos], font=openFont(90))
	genImage(600, 250, middle[pos], font=openFont(60))
	genImage(10, 700, bottom[pos], font=openFont(90))
 
	image.save(temp, optimize=True, quality=20)

def hideLSB(message):
	genMeme()
	secret = lsb.hide(temp, message)
	secret.save(leet)
	print(lsb.reveal(leet))

while True:
	hideLSB(message = input('$ '))