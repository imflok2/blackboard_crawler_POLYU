import re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# redirect to the correct login page
sess = requests.session()
sess.headers = {'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
url = 'https://learn.polyu.edu.hk/'
front_page = sess.get(url)
bs_front_page = BeautifulSoup(front_page.text,'html.parser')
k = bs_front_page.find_all(href = True)
Iwant = re.findall('[^\"]*(?:saml|SAML)[^\"]*',k.__str__())[0]
print("Redirected to {}".format(url+Iwant))
consent_cookie = {'name':'COOKIE_CONSENT_ACCEPTED','value':'true','Domain':'learn.polyu.edu.hk','expires':'2030-06-19T19:49:48.000Z'}


#login blackboard
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except:
    print("error in loading driver")
    exit()
#driver = webdriver.Chrome("chromedriver_win32/chromedriver.exe")
driver.get(url+Iwant)
driver.add_cookie(consent_cookie)
print("Make sure you can log in blackboard as in your browser.\nThe program can only crawl the courses included in \"My Course\".")
print(f"If you wish to crawl last few sem courses, please add the courses into \"My Course\" manually (or you can pay me to code more:D).\nThis program is like automating the manual downloading from BC in browser.\nIt is slow sorry.:( ")
#Lots more improvement can be made especially in finding the target
while True:
    username = input("enter student ID: ")
    password = input("enter password: ")
    driver.find_element_by_id("userNameInput").send_keys("16061778d")
    driver.find_element_by_id("passwordInput").send_keys("Azxiop123")
    driver.find_element_by_id("submitButton").click()
    if driver.title.find('Welcome') != -1:
        print('Logged in')
        break
    else:
        print("Failed to log in")

#a = driver.find_elements_by_class_name("termToggleLink itemHead")
sem = driver.find_elements_by_partial_link_text('Sem') + driver.find_elements_by_partial_link_text('sem')
ava_sem_text = [SEM.text for SEM in sem ]
sem_id = [SEM.get_attribute("id")[4:] for SEM in sem ]
#get courses of a particular sem link ///need to be def and incoperate
ID = sem_id[2]
courses = driver.find_elements_by_xpath("//div[@id='{}']/ul/li".format(ID))
courses[1].click()



a = driver.find_elements_by_css_selector('a')
a_text = [A.text for A in a]
#open close
li = driver.find_elements_by_css_selector('ul.portletList-img')
[SEM.click() for SEM in sem]
li = li + driver.find_elements_by_css_selector('ul.portletList-img')
[SEM.click() for SEM in sem]
li_text = [LI.text for LI in li]
sem[0].get_attribute("id")



















driver.close()
