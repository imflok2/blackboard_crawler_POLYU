import requests
import os
import requests
os.makedirs('tryfolder_download')
url = ''
open('tryfolder/mac_chrome_dri.zip','wb').write(requests.get(url))


