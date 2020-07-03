import re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# redirect to the correct login page
def redirect():
    sess = requests.session()
    sess.headers = {'user-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    url = 'https://learn.polyu.edu.hk/'
    front_page = sess.get(url)
    bs_front_page = BeautifulSoup(front_page.text,'html.parser')
    k = bs_front_page.find_all(href = True)
    Iwant = re.findall('[^\"]*(?:saml|SAML)[^\"]*',k.__str__())[0]
    print("Redirected to {}".format(url+Iwant))
    return url+Iwant

#login blackboard
def loginBD(login_url):
#    from selenium import webdriver
#    from webdriver_manager.chrome import ChromeDriverManager
    global driver
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    except:
        print("error in loading driver")
        exit()
    #driver = webdriver.Chrome("chromedriver_win32/chromedriver.exe")
    driver.get(login_url)
    consent_cookie = {'name':'COOKIE_CONSENT_ACCEPTED','value':'true','Domain':'learn.polyu.edu.hk','expires':'2030-06-19T19:49:48.000Z'}
    print("Make sure you can log in blackboard as in your browser.\nThe program can only crawl the courses included in \"My Course\".")
    print(f"If you wish to crawl last few sem courses, please add the courses into \"My Course\" manually (or you can pay me to code more:D).\nThis program is like automating the manual downloading from BC in browser.\nIt is slow sorry.:( ")
    #Lots more improvement can be made especially in finding the target
    while True:
        #username = input("enter student ID: ")
        #password = input("enter password: ")
        driver.find_element_by_id("userNameInput").send_keys("16061778d")
        driver.find_element_by_id("passwordInput").send_keys("Azxiop123")
        driver.find_element_by_id("submitButton").click()
        if driver.title.find('Welcome') != -1:
            driver.add_cookie(consent_cookie)
            driver.refresh()
            print('Logged in')
            break
        else:
            print("Failed to log in")

#a = driver.find_elements_by_class_name("termToggleLink itemHead")

#+ driver.find_elements_by_partial_link_text('sem')
#///ava_sem_text = [SEM.text for SEM in sem ]
#///sem_id = [SEM.get_attribute("id")[4:] for SEM in sem ]
#get courses of a particular sem link ///need to be def and incoperate
#return sems info
def get_sems_info():
    sems = driver.find_elements_by_partial_link_text('Sem')
    sems_info = [(SEM.text,SEM.get_attribute("id")[4:]) for SEM in sems ]
    print("\n".join([i+": "+j for i,j in sems_info]))
#    print("\n".join(str(i)+": "+j for i,j in enumerate([i[0] for i in sems_info])))
    return sems_info

#pop unwanted sem
#///print("\n".join(str(i)+": "+j for i,j in enumerate([i[0] for i in sems_info])))
def pref_sems_info(sems_info):
    print("\n".join(str(i) + ": " + j for i, j in enumerate([i[0] for i in sems_info])))
    while True:
        index = input("Enter UNWANTED sem index(space separated if multiple): ")
        swi = input("Confirmed?(Y/N)")
        if (swi=="Y"):
            try:
                k = [int(i) for i in list(index.split())]
                if not ((max(k) <= len(sems_info)-1) and (min(k)>=0) and (len(k)==len(set(k)))):
                    raise ValueError
                break
            except ValueError:
                print("Invalid entry. Try again")
    return [sems_info[i] for i in range(len(sems_info)) if i not in k]


#get the courses names and urls in triple form
#####sems_info = pref_sems_info(sems_info)
def find_courses_info(pref_sems):
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

def find_all_materials(courses_info):
    for cname,curl in courses_info:






















driver.close()
