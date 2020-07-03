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
from selenium.webdriver.common.keys import Keys
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
print("\n".join([i+": "+j for i,j in zip(ava_sem_text,sem_id)]))


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com/search?q=hi&oq=hi&aqs=chrome.0.69i59.413j0j8&sourceid=chrome&ie=UTF-8")
point = driver.find_element_by_partial_link_text("hi - Urban Dictionary")
point.get_attribute('href')



ID = [Sems_info[1] for Sems_info in sems_info][2] #particular id: 2
courses = driver.find_elements_by_xpath("//div[@id='{}']/ul/li/a".format(ID))
courses_info = [(course.text,course.get_attribute("href")) for course in courses ]
print("\n".join([i.text for i in courses]))



pref_sems = sems_info.copy()
for i in k:
    print(i)
    pref_sems.pop(i-1)




driver.find_element_by_tag_name("body")
driver.refresh()

pref_sems = sems_info.copy()
IDs = [Sems_info[1] for Sems_info in pref_sems]
courses = []
for ID in IDs:
    if not driver.find_element_by_xpath("//div[@id='{}']/ul/li/a".format(ID)).text:
        driver.find_element_by_id("afor"+ID).click()
        #flag = True
        print("clicked {}".format(ID))
    courses += driver.find_elements_by_xpath("//div[@id='{}']/ul/li/a".format(ID))
#z    if flag:       driver.find_element_by_id("afor" + ID).click()flag = Falseprint("closed")
#        courses_info = [(course.text,course.get_attribute("href")) for course in courses]
print("\n".join([i.text for i in courses]))
i = [(course.text,course.get_attribute("href")) for course in courses]





driver.get(i[0][1])
# id = puller
header = driver.find_element_by_id("puller")
if header.get_attribute("class"):
    header.click()
header = driver.find_element_by_css_selector('div.navPaletteContent')
cols = driver.find_elements_by_xpath("//ul[@id='courseMenuPalette_contents']/li/a")
cols_name = [col.find_element_by_css_selector("span").get_attribute("title") for col in cols]
cols_info = [(col.find_element_by_css_selector("span").get_attribute("title"),col.get_attribute("href")) for col in cols]

#1. find a object to download
#2. try create a download file, with correct name: courses, file name
#3. download the file
#4. loop for each courses
#5. loop for each sem
#bonus crab videos from ultra

