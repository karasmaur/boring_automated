## mauricio_karas u68uuqpewKwnhddix  PROBLEMA 'https://usd.sicredi.net/CAisd/pdmweb.exe?OP=SEARCH+FACTORY=pr+SKIPLIST=1+QBE.EQ.ref_num=8457681'

from selenium import webdriver
browser = webdriver.Firefox()

browser.get('https://usd.sicredi.net/CAisd/pdmweb.exe?OP=SEARCH+FACTORY=chg+SKIPLIST=1+QBE.EQ.chg_ref_num=195081')
# TODO: Handle the User/Pass NTLM auth

try:
    elem = browser.find_element_by_id('id=df_5_0')
    print elem.text
except:
    print('Was not able to find what you were looking for.')
    #and I still haven't found