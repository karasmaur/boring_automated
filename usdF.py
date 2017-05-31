import requests
from requests_ntlm import HttpNtlmAuth
try:
    incNumber = '8457681' #pyperclip.paste()
    typeNumber = 'pr' #implement a verification system to check which type the number informed is
    link = 'https://usd.sicredi.net/CAisd/pdmweb.exe?OP=SEARCH+FACTORY='+typeNumber+'+SKIPLIST=1+QBE.EQ.ref_num='+incNumber

    res = requests.get(link, verify=False, auth=HttpNtlmAuth('SICREDI\\mauricio_karas', 'u68uuqpewKwnhddix'))

    problem = open('problem.txt', 'wb')


    for chunk in res.iter_content(1000000):
        problem.write(chunk)
    res.raise_for_status()

except Exception as exc:
    print('There was a problem: %s' % (exc))