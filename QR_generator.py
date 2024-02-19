import qrcode

class myQR:
	def __init__(self,size,padding):
		self.qr = qrcode.QRCode(box_size=size, border=padding)


	def create_qr(self, filename:str, fg:str,bg:str):
		user_input = input('Enter text: ')

		try:
			self.qr.add_data(user_input)
			qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
			qr.image.save(filename)

			print(f'Successful created ({filename})')
		except Exception as e:
			print(f'Error: {e}')



def main():
	myqr = myQR(size=30,padding=2)
	myqr.create_qr('sample.png', fg='black', bg='white')


if __name__ == '__main__':
	main()



