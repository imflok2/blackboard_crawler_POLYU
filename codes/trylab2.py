import re
from bs4 import BeautifulSoup
import requests
#https://www.rexegg.com/regex-quickstart.html
#https://regexr.com/
sess = requests.session()
sess.headers = {'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
url = 'https://learn.polyu.edu.hk/'
front_page = sess.get(url)
bs_front_page = BeautifulSoup(front_page.text,'html.parser')
k = bs_front_page.find_all(href = True)
#l = re.findall('https[^\"]*',k.__str__())
Iwant = re.findall('[^\"]*(?:saml|SAML)[^\"]*',k.__str__())[0]
form_payload= {
    'UserName': r'16061778d@hh',
    'Password': 'Azxiop123',
    'Kmsi':[],
    'AuthMethod': "FormsAuthentication"
}
redir_page = sess.get(url+Iwant)
logining_page = sess.post(url+Iwant,data= form_payload)
#soup = bs_front_page
#hrefs = [href for href in soup]
next_url_3 = re.findall('action="(.+?)">', logining_page.text)[0]
SAMLResponse = re.findall('name="SAMLResponse" value="(.+?)" />', logining_page.text)[0]
logined_page = sess.post(next_url_3, data = {'SAMLResponse': SAMLResponse})

from robobrowser import RoboBrowser
br = RoboBrowser()
br.open(url+Iwant)
form = br.get_form()
for key in list(form_payload.keys()):
    form[key] = form_payload[key]
br.submit_form()
src = str(br.parsed())

redir_page = sess.get(url+Iwant,data= form_payload)
bs_redir_page = BeautifulSoup(redir_page.text)
bs_redir_page.find_all(id = True)


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome("chromedriver_win32/chromedriver.exe")
driver.get(url+Iwant)
a = driver.find_element_by_id("passwordInput")
driver.find_element_by_id("userNameInput").send_keys("16061778d")
driver.find_element_by_id("passwordInput").send_keys("Azxiop123")
driver.find_element_by_id("submitButton").click()



find_some = list(enumerate(a_text))
enu_sem_text = list(enumerate(ava_sem_text))
#all - crawl all avalible sem  ///do it later
#latest - crawl the latest sem ///do it later
#string separated by spacebar
for i,j in enu_sem_text:
    print("{0} : {1}".format(i,j))
sele_sem = []









