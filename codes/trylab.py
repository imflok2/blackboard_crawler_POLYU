#class HIWO:
#        self['a'] = 'yes'
#
#
#y = HIWO.a

from bs4 import BeautifulSoup
import requests
import re
sess = requests.session()
sess.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
blackboard_main_resp = sess.get('https://adfs.polyu.edu.hk/adfs/ls/?SAMLRequest=fVLLbsIwEPwVa%2B%2BJ45ACsUgQLUJFogKR0EMvyAlOsRps6nVQ%2B%2FdNeai0UrlYWnt2xjuzg%2BHHriYHaVEZnQDzAyBSl2aj9GsCq3zi9WGYDlDs6nDPR43b6qV8byQ60jZq5KeXBBqruRGokGuxk8hdybPR04yHfsD31jhTmhrICFFa10o9GI3NTtpM2oMq5Wo5S2Dr3B45pbUUVvt7U382vtw0%2FvaNilbY%2B5aixyPL5lTUSiBdx71eb82AjNsvKS3ccYwLk9hU%2BIeovaE1UiATY0t5HCiBStQogUzHCYgoLO5YJy6rigWR6nZUXHTZpscqFYedogXhQiCqg%2FxpQ2zkVKMT2iUQBmHgBV2PxTnr807IWehHQfQCZHG24V7pk723PCtOIOSPeb7wFvMsB%2FJ8iakFwDkUflS312ncJhaXCCD93%2FABvSZPz%2BXvBUi%2FAA%3D%3D&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=G%2F9K8dn96FtodeE2Ml%2BTzhxEWPDvQGCi7tOjcRCE%2FeKt%2FqZbDrQsucHuX47OPoapa%2F%2Fh7MJJ00%2Bccomad4xFxMiBKT2qKPhcPLBBOkozuG2bd2U29NgooZzSQRYwWkwCKnS7d%2FAeLmkpDSE5hE7948gjOdx0Goit3VuP8e6tGdnhTFvmrHSmnsTidtKNyOa4fzPUyVdmbDPh6xpQ4%2F%2B0EvLMhEfT9LMiG6DHVDBsLCuXerU0w7dIBhMfsq6Vd%2BLONjdYy%2FstGU22MWQL31vZkF%2BeTfimcR7CVbT4ANw%2Bop0vmxohxSGUe4%2Bk0iOFRbPP78L2VuHhjVX%2F2rJMXmECUA%3D%3D')
login_page_url = 'https://adfs.polyu.edu.hk/adfs/ls/?SAMLRequest=fVLLbsIwEPwVa%2B%2BJ45ACsUgQLUJFogKR0EMvyAlOsRps6nVQ%2B%2FdNeai0UrlYWnt2xjuzg%2BHHriYHaVEZnQDzAyBSl2aj9GsCq3zi9WGYDlDs6nDPR43b6qV8byQ60jZq5KeXBBqruRGokGuxk8hdybPR04yHfsD31jhTmhrICFFa10o9GI3NTtpM2oMq5Wo5S2Dr3B45pbUUVvt7U382vtw0%2FvaNilbY%2B5aixyPL5lTUSiBdx71eb82AjNsvKS3ccYwLk9hU%2BIeovaE1UiATY0t5HCiBStQogUzHCYgoLO5YJy6rigWR6nZUXHTZpscqFYedogXhQiCqg%2FxpQ2zkVKMT2iUQBmHgBV2PxTnr807IWehHQfQCZHG24V7pk723PCtOIOSPeb7wFvMsB%2FJ8iakFwDkUflS312ncJhaXCCD93%2FABvSZPz%2BXvBUi%2FAA%3D%3D&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=G%2F9K8dn96FtodeE2Ml%2BTzhxEWPDvQGCi7tOjcRCE%2FeKt%2FqZbDrQsucHuX47OPoapa%2F%2Fh7MJJ00%2Bccomad4xFxMiBKT2qKPhcPLBBOkozuG2bd2U29NgooZzSQRYwWkwCKnS7d%2FAeLmkpDSE5hE7948gjOdx0Goit3VuP8e6tGdnhTFvmrHSmnsTidtKNyOa4fzPUyVdmbDPh6xpQ4%2F%2B0EvLMhEfT9LMiG6DHVDBsLCuXerU0w7dIBhMfsq6Vd%2BLONjdYy%2FstGU22MWQL31vZkF%2BeTfimcR7CVbT4ANw%2Bop0vmxohxSGUe4%2Bk0iOFRbPP78L2VuHhjVX%2F2rJMXmECUA%3D%3D'
blackboard_main_resp.apparent_encoding
root = BeautifulSoup(blackboard_main_resp.text,'html.parser')


len(blackboard_main_resp.text)
form_auth_payload = {
    'UserName': r'16061778d@hh',
    'Password': 'Azxiop123',
    'AuthMethod': "FormsAuthentication"
}
#login
blackboard_login = sess.post(login_page_url,data =form_auth_payload )
next_url_3 = re.findall('action="(.+?)">',blackboard_login.text)[0]
SAMLResponse = re.findall('name="SAMLResponse" value="(.+?)" />', blackboard_login.text)[0]
resp4 = sess.post(next_url_3, data={'SAMLResponse': SAMLResponse})

f = open("login_resp_text.txt",'w')
for i in blackboard_login.text.split('<'):
    f.write("<{}\n".format(i))
f.close()

f = open("resp4.txt",'w')
for i in resp4.text.split('<'):
    f.write("<{}\n".format(i))
f.close()



bb_main_page = sess.get('https://blackboard.cuhk.edu.hk')
next_url_1 = re.findall('url=(.+)', bb_main_page.text)[0]
print(next_url_1)

#~  git clone https://github.com/.../... .git
#~  cd bootstrap
#~  git checkout -b test-pr
#~  git add . && git commit -m "test-pr"
#~  git push origin test-pr










