import requests
import urllib.request as urllib2
from utils import mkdir, directory_flatten, title_print
from bs4 import BeautifulSoup
class BCPrefs(object):



class BlackboardCrawler:
    def __init__(self, username, password, parent):
        self.username = username
        self.password = password
        self.parent = parent

    def BC_login(self):
        self._BC_init_bb_session()
        self._BC_login()
        self.userid = self._BC_get_bb_userid()
        mkdir('Blackboard')

  def _BC_init_bb_session(self):
    sess = requests.session()
    # fake header, otherwise they wont care
    sess.headers['User-Agent']='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    # go to starting page
    blackboard_main_resp = sess.get(self.prefs.blackboard_url)
    next_url_1 = re.findall('url=(.+)', blackboard_main_resp.text)[0]
    # redirected to login page
    next_url_1 = urllib2.unquote(next_url_1)
    login_page_resp = sess.get(next_url_1)
    self.login_page_url = login_page_resp.url
    self.sess = sess


AuthMethod