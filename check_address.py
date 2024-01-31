import re

def validate_bank_card_format(str):
	pattern = r"[0-9]+"
	
	res = re.findall(pattern, str)
	
	if sum(list(map(len, res))) == 16 :
		print('номер карты ', ''.join(res) , ' корректен' )
		return 0
	else:
		print('вы ввели некорректный номер карты')
		return 1
		
		
		
def validate_crypto_address_format(crypto_address):

					#BTC
	# первый символ 1 , затем любая латинская буква (большая или маленькая), цифра, + это любое их количество
	res = re.findall(r"[1][A-Z a-z 0-9]+" , crypto_address)

	if len(res) != 0 and len(res[0]) == len(crypto_address):
		print('адрес валидный')
		return 0

	
	res = re.findall(r"[3][A-Z a-z 0-9]+" , crypto_address)		# начинается с 3

	if len(res) != 0 and len(res[0]) == len(crypto_address):
		print('адрес валидный')
		return 0

	
	res = re.findall(r"[b][c][1][q][A-Z a-z 0-9]+" , crypto_address)		#  начинается с bc1q

	if len(res) != 0 and len(res[0]) == len(crypto_address):
		print('адрес валидный')
		return 0


	res = re.findall(r"[b][c][1][p][A-Z a-z 0-9]+"  , crypto_address)		#  начинается с bc1p

	if len(res) != 0 and len(res[0]) == len(crypto_address):
		print('адрес валидный')
		return 0


				#	ETC					
	res = re.findall(r"[0][x][A-Z a-z 0-9]+"  , crypto_address)		#  начинается с 0x , длина адреса 42

	if len(res) != 0 and len(res[0]) == len(crypto_address) and len(res[0]) == 42:
		print('адрес валидный')
		return 0


				#	XMR
	res = re.findall(r"[4 8][A-Z a-z 0-9]+"  , crypto_address)		#  начинается с 4 или 8

	if len(res) != 0 and len(res[0]) == len(crypto_address) and len(res[0]) == 95:
		print('адрес валидный')
		return 0


				#	USDT
	res = re.findall(r"[0][x][A-Z a-z 0-9]+"  , crypto_address)		#  ERC20, BEP20
 
	if len(res) != 0 and len(res[0]) == len(crypto_address) and len(res[0]) == 95:
		print('адрес валидный')
		return 0


	res = re.findall(r"[T][A-Z a-z 0-9]+"  , crypto_address)		#  TRC20

	if len(res) != 0 and len(res[0]) == len(crypto_address):
		print('адрес валидный')
		return 0

	else:
		print('адрес не валиден')
		return 1

	
	

def main():
	card_num = input("введите номер карты: ")

	while(1):
		if validate_bank_card_format(card_num) != 0:
			card_num = input("введите номер карты еще раз: ")
		else:
			break

	crypto_address = input("введите крипто адрес : ")

	while(1):
		if validate_crypto_address_format(crypto_address) != 0:
			crypto_address = input("введите адрес еще раз : ")
		else:
			break
 

 
if __name__ == "__main__": 
    main()
