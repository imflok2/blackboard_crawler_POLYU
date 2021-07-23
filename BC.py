import re
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import os
import shutil

delay = 10


# redirect to the correct login page
def redirect():
    sess = requests.session()
    sess.headers = {
        'user-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    url = 'https://learn.polyu.edu.hk/'
    front_page = sess.get(url)
    bs_front_page = BeautifulSoup(front_page.text, 'html.parser')
    k = bs_front_page.find_all(href=True)
    Iwant = re.findall('[^\"]*(?:saml|SAML)[^\"]*', k.__str__())[0]
    print("Redirected to {}".format(url + Iwant))
    return url + Iwant


def init_chrome_options(headless=False):
    global download_home
    for i in range(1, 11):
        try:
            download_home = f"download{i}"
            os.makedirs(download_home)
            break
        except:
            if i == 10:
                print("remove some download files")
                exit()
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--verbose')
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": os.path.abspath(download_home),

        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False,
        "plugins.always_open_pdf_externally": True
    })
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-software-rasterizer')
    if headless:
        chrome_options.add_experimental_option()
        chrome_options.add_argument("--headless")
    return chrome_options


# login blackboard
def loginBD(login_url,init_driver_options = init_chrome_options(headless=False)):
    global driver
    global home_page
    try:

        driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=init_driver_options)
    except:
        print("error in loading driver. Please try install chrome browser.")
        exit()
    # driver = webdriver.Chrome("chromedriver_win32/chromedriver.exe")
    driver.get(login_url)
    time.sleep(2)
    consent_cookie = {'name': 'COOKIE_CONSENT_ACCEPTED', 'value': 'true', 'Domain': 'learn.polyu.edu.hk',
                      'expires': '2030-06-19T19:49:48.000Z'}
    print(
        "Make sure you can log in blackboard as in your browser.\nThe program can only crawl the courses included in \"My Course\".")
    print(
        f"If you wish to crawl last few sem courses, please add the courses into \"My Course\" manually (or you can pay me to code more:D).\nThis program is like automating the manual downloading from BC in browser.\nIt is slow sorry.:( ")
    # Lots more improvement can be made especially in finding the target
    while True:
        # username = input("enter student ID: ")
        # password = input("enter password: ")
        print("Logging in")
        driver.find_element_by_id("userNameInput").send_keys("16061778d")
        driver.find_element_by_id("passwordInput").send_keys("Azxiop123")
        driver.find_element_by_id("submitButton").click()
        try:
            WebDriverWait(driver, delay).until(EC.title_contains("Welcome"))
            #        if driver.title.find('Welcome') != -1:
            driver.add_cookie(consent_cookie)
            driver.refresh()
            print('Logged in')
            time.sleep(5)
            home_page = driver.current_url
            break
        except:
            print("Failed to log in")
    # thats tentative for trylab
    return driver


# a = driver.find_elements_by_class_name("termToggleLink itemHead")

# + driver.find_elements_by_partial_link_text('sem')
# ///ava_sem_text = [SEM.text for SEM in sem ]
# ///sem_id = [SEM.get_attribute("id")[4:] for SEM in sem ]
# get courses from a particular sem link ///need to be def and incoperate
# return sems info
def get_sems_info():
    sems = driver.find_elements_by_partial_link_text('Sem')
    sems_info = [(SEM.text, SEM.get_attribute("id")[4:]) for SEM in sems]
    print("\n".join([i + ": " + j for i, j in sems_info]))
    #    print("\n".join(str(i)+": "+j for i,j in enumerate([i[0] for i in sems_info])))
    return sems_info


# pop unwanted sem
# ///print("\n".join(str(i)+": "+j for i,j in enumerate([i[0] for i in sems_info])))
def pref_sems_info(sems_info):
    print("\n".join(str(i) + ": " + j for i, j in enumerate([i[0] for i in sems_info])))
    if not sems_info:
        print("No semester found")
        return 0
    while True:
        index = input("Enter UNWANTED sem index(space separated if multiple): ")
        swi = input("Confirm?(Y/N)")
        if (swi == "Y"):
            try:
                k = [int(i) for i in list(index.split())]
                if k:
                    if (not ((max(k) <= len(sems_info) - 1) and (min(k) >= 0) and (len(k) == len(set(k))))):
                        raise ValueError
                break
            except ValueError:
                print("Invalid entry. Try again")
    return [sems_info[i] for i in range(len(sems_info)) if i not in k]


# get the courses names and urls in triple form
#####sems_info = pref_sems_info(sems_info)
def get_courses_info(pref_sems):
    #    IDs = [Sems_info[1] for Sems_info in pref_sems]
    driver.get(home_page)
    time.sleep(2)
    ID = pref_sems[1]
    courses = []
    #    for Sem_Name,ID in pref_sems:
    if not driver.find_element_by_xpath("//div[@id='{}']/ul/li/a".format(ID)).text:
        driver.find_element_by_id("afor" + ID).click()
        # put a flag?
    courses += driver.find_elements_by_xpath("//div[@id='{}']/ul/li/a".format(ID))
    #        courses_info = [(course.text,course.get_attribute("href")) for course in courses]
    print(pref_sems[0])
    print("\n".join([i.text for i in courses]))
    return [(course.text, course.get_attribute("href")) for course in courses]


def get_course_cols(course_info):
    driver.get(course_info[1])
    #    WebDriverWait(driver, delay).until(EC.presence_of_element_located(driver.find_element_by_xpath("//ul[@id='courseMenuPalette_contents']/li/a")))
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'courseMenuPalette_contents')))
        cols = driver.find_elements_by_xpath("//ul[@id='courseMenuPalette_contents']/li/a")
    except:
        print("Error when crawling Course's content panel: ", course_info[0])
        return []
    return [(col.find_element_by_css_selector("span").get_attribute("title"), col.get_attribute("href")) for col in
            cols]


def pref_course_cols(cols_info):
    useless_set_name = ['Tools', 'Home Page', 'Announcements', 'Calendar', 'Contacts', 'Discussions', 'Groups', 'Help',
                        'What if you have trouble viewing the Math symbols and formulas?',
                        'How to access useful resources in the following 3 E-Books?', 'Foundation Statistics',
                        'Foundation Mathematics', 'Engineering Mathematics', 'Mathematics Learning Support Centre',
                        'Library Resources']
    pref_course = [(i, j) for i, j in cols_info if i in ["Content"]]
    # may implement functions for choosing pref cols
    return pref_course

#(name,href)
def crawl_folder(folder_info):
    #    WebDriverWait(driver, delay).until(EC.presence_of_element_located(driver.find_element_by_xpath("//ul[@id='content_listContainer']/li")))
    try:
        driver.get(folder_info[1])
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'content_listContainer')))
        items = driver.find_elements_by_xpath("//ul[@id='content_listContainer']/li")
        infos = [(item.find_element_by_css_selector("img").get_attribute("alt"), item.text,
                  item.find_element_by_css_selector("a").get_attribute("href")) for item in items]
        new = [(info[0], re.findall('^.+', info[1])[0], driver.current_url) for info in infos if info[0] in ["Item", "Assignment"]]
        infos = new + [info for info in infos if info[0] not in ["Item", "Assignment"]]
    except:
        print("error when crawling folder: ", folder_info[0])
        infos = []
    return infos


def crawl_ass_Item(info):
    driver.get(info[1])
    try:
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'content_listContainer')))
        items = driver.find_elements_by_xpath("//*[contains(text(), '{}')]/../../..//a".format(info[0]))
        infos=[]
        for item in items:
            try:
                if item.text:
                    infos.append((item.find_element_by_css_selector("img").get_attribute("alt"), item.text, item.get_attribute("href")))
            except:
                print("error when crawling Ass/Item: ", item.text,"\nNot a file under the item",info[0])
    except:
        print("error when crawling Ass/Item: ", info[0])
        infos = []
        if infos:
            print("item {} is non-empty".format(info[0]))
    return infos


#   It can download multiple folders and files from multiple folders, inputs as list of tuple (type,name,href)

def download(infos, prior_dir=os.path.abspath("download"), download_pack=[]):

    for info in infos:
        if info[0] == "Content Folder":
            #print("Content Folder")
#            os.makedirs(prior_dir + "/" + info[1])
            download(crawl_folder(info[1:]), prior_dir + "/" + info[1])
        if info[0] == "File":
            #print("File")
            download_pack.append((prior_dir, info[2], info[1]))
        if info[0] in ["Item", "Assignment"]:
            #print("ass")
#            os.makedirs(prior_dir + "/" + info[1])
            download(crawl_ass_Item(info[1:]), prior_dir + "/" + info[1])
        if info[0] not in ["Item", "Assignment", "Content Folder", "File"]:
            print("unexpected file type exists in: {}, file type: {}".format(prior_dir, info))
    return download_pack


def init_download(sems_info):
    download_packs = []
    for sem_info in sems_info:
#        os.makedirs("{}\\{}".format(download_home, sem_info[0].replace("/", "-")))
        print("make dir:","{}\\{}".format(download_home, sem_info[0].replace("/", "-")))
        courses_info = get_courses_info(sem_info)
        for course_info in courses_info:
            print(course_info[0])
            cols_info = pref_course_cols(get_course_cols(course_info))
            for col_info in cols_info:
                print(sem_info[0], course_info[0], col_info[0])
                download_path = "/".join(
                    [download_home, sem_info[0].replace("/", "-"), course_info[0].replace(":", ""), col_info[0]])
#                download_packs += [download(crawl_folder(col_info), prior_dir=download_path)]
                download_packs = download(crawl_folder(col_info), prior_dir=download_path,download_pack=download_packs)
                print("Finish")
            if input("Continue?(Y/N):") == "N":
                return download_packs
    return download_packs










