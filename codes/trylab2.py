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
#import sys
# insert at 1, 0 is the script path (or '' in REPL)
#from main import *

def get_courses_info(pref_sems):
    IDs = [Sems_info[1] for Sems_info in pref_sems]
    courses = []
    for ID in IDs:
        if not driver.find_element_by_xpath("//div[@id='{}']/ul/li/a".format(ID)).text:
            driver.find_element_by_id("afor"+ID).click()
            #put a flag?
        courses += driver.find_elements_by_xpath("//div[@id='{}']/ul/li/a".format(ID))
#        courses_info = [(course.text,course.get_attribute("href")) for course in courses]
        print("\n".join([i.text for i in courses]))
    return [(course.text,course.get_attribute("href")) for course in courses]

from codes.main import *
driver = loginBD(redirect())
sems_info = get_sems_info()
sems_info = pref_sems_info(sems_info)
#may change to arrange according to sem
courses_info = get_courses_info(sems_info)



driver.get(courses_info[0][1])
cols = driver.find_elements_by_xpath("//ul[@id='courseMenuPalette_contents']/li/a")
cols_info = [(col.find_element_by_css_selector("span").get_attribute("title"),col.get_attribute("href")) for col in cols]
##visualize info
#print("\n".join(["{}: {}".format(i,j) for i,j in cols_info]))

#k = ["Content","Tools"]
#useless_set_name = [i for i,j in cols_info if i not in k]
#hard code it
useless_set_name = ['Tools','Home Page', 'Announcements', 'Calendar', 'Contacts', 'Discussions', 'Groups', 'Help', 'What if you have trouble viewing the Math symbols and formulas?', 'How to access useful resources in the following 3 E-Books?', 'Foundation Statistics', 'Foundation Mathematics', 'Engineering Mathematics', 'Mathematics Learning Support Centre', 'Library Resources']
useful_set_info = [(i,j) for i,j in cols_info if i not in useless_set_name]

import os
import builtins

col_info = useful_set_info[0]

#it can crawl folder and col in panel
#input one tuple as (name,href)
#output list of tuple as (type,name,href)
def crawl_folder(folder_info):
    driver.get(folder_info[1])
    items = driver.find_elements_by_xpath("//ul[@id='content_listContainer']/li")
    return [(item.find_element_by_css_selector("img").get_attribute("alt"),item.text,item.find_element_by_css_selector("a").get_attribute("href")) for item in items]
download_url = "{0}/{1}/{2}".format(file_to_url,sem_name,col_name)
os.makedirs(download_url)
#It can download multiple folders and files, inputs as list of tuple (type,name,href)
def download(infos,prior_dir="/download",download_pack=[]):
    for info in infos:
        if info[0] =="Content Folder":
            os.mkdir(prior_dir+"/"+info[1])
            download_pack += download(crawl_folder(info[1:]),prior_dir+"/"+info[1])
        if info[0] =="File":
            download_pack.append((prior_dir+"/"+info[1],info[2]))
    return download_pack

for i in range(1,11):
    try:
        download_url = f"download{i}"
        os.makedirs(download_url)
        break
    if i ==10:
        print("remove some download files")
        break


from codes.main import *
driver = loginBD(redirect())
sems_info = get_sems_info()
sems_info = pref_sems_info(sems_info)
#may change to arrange according to sem
courses_info = get_courses_info(sems_info)
driver.get(courses_info[0][1])
cols = driver.find_elements_by_xpath("//ul[@id='courseMenuPalette_contents']/li/a")
cols_info = [(col.find_element_by_css_selector("span").get_attribute("title"),col.get_attribute("href")) for col in cols]
useless_set_name = ['Tools','Home Page', 'Announcements', 'Calendar', 'Contacts', 'Discussions', 'Groups', 'Help', 'What if you have trouble viewing the Math symbols and formulas?', 'How to access useful resources in the following 3 E-Books?', 'Foundation Statistics', 'Foundation Mathematics', 'Engineering Mathematics', 'Mathematics Learning Support Centre', 'Library Resources']
useful_set_info = [(i,j) for i,j in cols_info if i not in useless_set_name]
col_info = useful_set_info[0]
download_url = "/".join([f"download{i}",courses_info[0][0],col_info[0]])
a = download(crawl_folder(col_info),prior_dir=download_url)
