import os
import requests

def get_extension(imageURL):
	extensions = ['.png' , '.jpg' , '.jpeg' , '.gif' , '.svg']
	for ext in extensions:
		if ext in imageURL:
			return ext


def download_image(imageURL , name , folder=None):
	if ext := get_extension(imageURL):
		if folder:
			image_name = f'{folder}/{name}{ext}'
		else:
			image_name = f'{name}{ext}'
	else:
		raise Exception('Image extension could not be located.')


	if os.path.isfile(image_name):
		raise Exception('file name already exists')


	# download image
	try:
		iamge_content = requests.get(imageURL).content
		with open(iamge_name,'wb') as handler:
			handler.write(iamge_content)
			print(f'Downloaded: "{iamge_name}" successfully!')
	except Exception as e:
		print(f'Error: {e}')



if __name__ == '__main__':
	input_url = input('Enter a url: ')
	input_name = input('What would you like to name it: ')
	folder = '' # Enter folder you want to store image

	print('Downloading....')
	download_image(input_url,name = input_name , folder = folder)