import time
from codes.BC import *
driver = loginBD(redirect())
sems_info = get_sems_info()
sems_info = pref_sems_info(sems_info)
ult_download_pack = init_download(sems_info)






#may change to arrange according to sem
courses_info = get_courses_info(sems_info)
i = 0
driver.get(courses_info[i][1])
course_cols = get_course_cols(courses_info[i])
course_cols = pref_course_cols(course_cols)
download_url = "/".join([f"download{i}",courses_info[0][0],col_info[0]])
a = download(crawl_folder(col_info),prior_dir=download_url)


import os
import numpy as np
items_list = [ re.search("([A-Z]{2,4}\w+)",i).group(0) for i,j in ult_download_pack]
last = None
see = ["start"]
for i in items_list:
    if i == last:
        continue
    else:
        see.append(i)
        last = i
del last
print("\n".join(see))





