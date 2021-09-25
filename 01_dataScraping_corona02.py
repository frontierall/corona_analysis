#!/usr/bin/env python
# coding: utf-8

# ### 코로나 데이터 웹 데이터 수집

# ### 학습내용
# * 추가적인 내용을 수집한다.(인구수, 위중증 추가)
# * 금일 정보가 아닌 어제기준 완료된 데이터를 가져와 본다.

# * 코로나 19(COVID-19) 실시간 상황판
# * url : https://coronaboard.kr/

# In[1]:


from IPython.display import display, Image
import os, warnings
import re
warnings.filterwarnings(action='ignore')


# ### 01 웹 브라우저 띄우기

# In[2]:


from selenium import webdriver
from bs4 import BeautifulSoup


# In[5]:


driver = webdriver.Chrome('./chromedriver_91')

## https://www.amazon.com/
url = 'https://coronaboard.kr/'
driver.get(url)

import time
time.sleep(3)  # 홈페이지 로딩 시간 3초


# ### 02 더보기 버튼 찾기

# In[6]:


from selenium.webdriver import ActionChains

some_tag = driver.find_element_by_id('show-more')
ActionChains(driver).move_to_element(some_tag).perform()
some_tag.click()


# In[7]:


some_tag = driver.find_element_by_id('show-more')
ActionChains(driver).move_to_element(some_tag).perform()
some_tag.click()


# ### 03 추가정보선택
#  * 콤보박스 : //*[@id="global-slide"]/div/div[2]/div/div/button/div/div/div

# In[8]:


some_tag = driver.find_element_by_xpath('//*[@id="global-slide"]/div/div[2]/div/div/button/div/div/div')
ActionChains(driver).move_to_element(some_tag).perform()
some_tag.click()


# * //*[@id="bs-select-1-5"]

# ### 인구수 추가

# In[9]:


sel_menu = driver.find_element_by_xpath('//*[@id="bs-select-1-5"]')
sel_menu.click()


# ### 위중증 추가

# In[10]:


sel_menu = driver.find_element_by_xpath('//*[@id="bs-select-1-1"]')
sel_menu.click()


# In[11]:


some_tag.click()


# ### 국가 정보 가져오기

# * //*[@id="country-table"]/div/div/table/tbody/tr[1]/td[2]/a
# * //*[@id="country-table"]/div/div/table/tbody/tr[2]/td[2]/a
# * //*[@id="country-table"]/div/div/table/tbody/tr[4]/td[2]/a

# In[12]:


sel_country = driver.find_elements_by_xpath('//*[@id="country-table"]/div/div/table/tbody/tr/td[2]')
len(sel_country)


# In[13]:


for one in sel_country:
    print(one.text)


# ### 확진자 정보
#  * //*[@id="country-table"]/div/div/table/tbody/tr[1]/td[3]
#  * //*[@id="country-table"]/div/div/table/tbody/tr[2]/td[3]
#  * ..
#  * //*[@id="country-table"]/div/div/table/tbody/tr[5]/td[3]
#  
# ### 위중증
#  * //*[@id="country-table"]/div/div/table/tbody/tr[1]/td[4]
#  * //*[@id="country-table"]/div/div/table/tbody/tr[3]/td[4]
#  * ..
#  
# ### 사망자 정보
#  * //*[@id="country-table"]/div/div/table/tbody/tr[1]/td[5]
#  * //*[@id="country-table"]/div/div/table/tbody/tr[2]/td[5]
#  * ...
#  
# ### 완치
#  * //*[@id="country-table"]/div/div/table/tbody/tr[1]/td[6]
#  * //*[@id="country-table"]/div/div/table/tbody/tr[2]/td[6]
#  * ..
#  
# ### 치명(%)
#  * //*[@id="country-table"]/div/div/table/tbody/tr[1]/td[7]
#  * //*[@id="country-table"]/div/div/table/tbody/tr[2]/td[7]
#  * ...
#  
# ### 완치(%)
#  * //*[@id="country-table"]/div/div/table/tbody/tr[2]/td[8]
#  
#  
# ### 발생률
#  * //*[@id="country-table"]/div/div/table/tbody/tr[1]/td[9]
#  * //*[@id="country-table"]/div/div/table/tbody/tr[2]/td[9]
#  * ...
#  
# ### 인구수
#  * //*[@id="country-table"]/div/div/table/tbody/tr[1]/td[10]
#  * //*[@id="country-table"]/div/div/table/tbody/tr[2]/td[10]
#  * ...

# ### 어제 오늘 선택

# In[14]:


# 어제 : //*[@id="global-slide"]/div/div[2]/ul/li[2]/a
flag_today = False # False : 어제, Today : 오늘


# In[15]:


if flag_today==False:
    sel_yesterday = driver.find_element_by_xpath('//*[@id="global-slide"]/div/div[2]/ul/li[2]/a')
    sel_yesterday.click()


# In[ ]:


all_data = []
for i in range(2, 11):
    tmp = '//*[@id="country-table"]/div/div/table/tbody/tr/td[{}]'.format(i)
    # print(tmp)
    sel_ele = driver.find_elements_by_xpath(tmp)
    
    
    column_data = []
    for one in sel_ele:
        # print(one.text)
        column_data.append(one.text)
    
    print( len(sel_ele) )
    all_data.append(column_data)
    print(column_data)
    print()
    
all_data


# In[ ]:


for i in range(9):
    print(len( all_data[i]) )


# In[ ]:


import pandas as pd

dict_dat = { "국가":all_data[0], 
             "확진자":all_data[1],
             "위중증":all_data[2],
             "사망자":all_data[3],
             "완치":all_data[4],
             "치명(%)":all_data[5],
             "완치(%)":all_data[6],
             "발생률":all_data[7],
             "인구수":all_data[8]
           }

dat = pd.DataFrame(dict_dat)
dat


# ### 주어진 데이터를 좀 더 사용하기 쉽게 전처리한다.

# In[ ]:


### 확진자를 총 확진자와, 일일 확진자로
dat['확진자_합계'] = dat['확진자'].str.split('\n').str[0]
dat['확진자1일'] = dat['확진자'].str.split('\n').str[1]

dat['사망자합계'] = dat['사망자'].str.split('\n').str[0]
dat['사망자1일'] = dat['사망자'].str.split('\n').str[1]

dat['완치합계'] = dat['완치'].str.split('\n').str[0]
dat['완치1일'] = dat['완치'].str.split('\n').str[1]

dat = dat.drop( [ '확진자', '사망자', '완치'], axis=1)

dat.head()


# In[ ]:


dat['위중증'] = dat['위중증'].str.replace(pat=r'[,()]', repl=r'', regex=True)
dat['발생률'] = dat['발생률'].str.replace(pat=r'[,]', repl=r'', regex=True)
dat['인구수'] = dat['인구수'].str.replace(pat=r'[,]', repl=r'', regex=True)

dat['확진자_합계'] = dat['확진자_합계'].str.replace(pat=r'[,]', repl=r'', regex=True)
dat['확진자1일'] = dat['확진자1일'].str.replace(pat=r'[,()]', repl=r'', regex=True)

dat['사망자합계'] = dat['사망자합계'].str.replace(pat=r'[,]', repl=r'', regex=True)
dat['사망자1일'] = dat['사망자1일'].str.replace(pat=r'[,()]', repl=r'', regex=True)

dat['완치합계'] = dat['완치합계'].str.replace(pat=r'[,]', repl=r'', regex=True)
dat['완치1일'] = dat['완치1일'].str.replace(pat=r'[,()]', repl=r'', regex=True)
dat.head()


# In[ ]:


from datetime import datetime
from datetime import date
import datetime
import os

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)

# print(today)
# print(yesterday)
if flag_today == True:
    file_make_time = today
else:
    file_make_time = yesterday

print( file_make_time )

print( os.getcwd() )
path_dir = os.getcwd() + "\\data\\"
path_file = path_dir + str(file_make_time)
print( path_dir,  path_file, sep="\n" )


# In[ ]:


dat.to_csv(path_file + "_corona.csv", index=False)
dat.to_excel(path_file + "_corona.xlsx", index=False)
os.listdir( path_dir )


# ### 추가 과제
#  * 위증증 - 총 합계와 일일 합계 나누기
#  * 확진자/총인구 값 구하기

# * history 
#  * 2021.08.08 version 01
# * 출처를 밝히시고 위의 내용에 대해 자유롭게 사용 가능합니다.
