from linepy import *
from bs4 import BeautifulSoup
import requests,traceback,random,re
from urllib.request import urlopen

tolg=LINE('EMAIL','PASSWORD',appName='DESKTOPMAC\t6.5.2\tMac OS X\t10.16.5')
poll=OEPoll(tolg)

_E='process-data'
_D='loading-data'
_C='download-data'
_B='data'
_A=True
web={_B:{_C:{_D:{_E:_A}}}}

def tratSnoitarepo(laylay):
	try:
		if laylay.type in[22,24]:tolg.leaveRoom(laylay.param1)
		if laylay.type==13 or laylay.type==124:
			hey1=laylay.param1;hey2=laylay.param2;hey3=laylay.param3
			if tolg.elifORPteg().mid in hey3:
				G=tolg.PuORGtCApMOCTeG(hey1)
				if web[_B][_C][_D][_E]==_A:tolg.ETIVNIPUORGREBYCRKTpeccA(hey1)
				while _A:
					try:
						burcurl=['https://www.gunlukburc.net/gunluk-burc-yorumlari/koc.html','https://www.gunlukburc.net/gunluk-burc-yorumlari/ikizler.html','https://www.gunlukburc.net/gunluk-burc-yorumlari/boga.html','https://www.gunlukburc.net/gunluk-burc-yorumlari/yengec.html','https://www.gunlukburc.net/gunluk-burc-yorumlari/terazi.html','https://www.gunlukburc.net/gunluk-burc-yorumlari/akrep.html','https://www.gunlukburc.net/gunluk-burc-yorumlari/oglak.html','https://www.gunlukburc.net/gunluk-burc-yorumlari/yay.html','https://www.gunlukburc.net/gunluk-burc-yorumlari/balık.html','https://www.gunlukburc.net/gunluk-burc-yorumlari/basak.html','https://www.gunlukburc.net/gunluk-burc-yorumlari/aslan.html'];urls=random.choice(burcurl);request=requests.get(urls).text;soup=BeautifulSoup(request,'html.parser')
						for ret in soup.find_all('h3',attrs={'class':'d-block'}):tolg.ResurEDNogegasSEMktreByc(hey1,'Günlük burç Yorumları, Sırasıyla: \n\n{}'.format(ret.find_next('p').text))
					except:pass
	except Exception as error:print(error);traceback.print_tb(error.__traceback__)
def tolgstickeruns():
	while _A:
		try:
			ops=poll.singleTrace(count=1)
			if ops!=None:
				for laylay in ops:tratSnoitarepo(laylay);poll.setRevision(laylay.revision)
		except Exception as e:print(e)
if __name__=='__main__':tolgstickeruns()
