#!/usr/bin/env python
# coding: utf-8

# ### 국가별 백신 접종률 정보 가져오기

# ### 정보 수집 사이트 
# * bloomberg.com
#   * https://www.bloomberg.com/graphics/covid-vaccine-tracker-global-distribution/
# 
# ### 기타 참고 통계 사이트
# * our world in data
#   * https://ourworldindata.org/covid-vaccinations
# 

# In[1]:


from IPython.display import display, Image
import os, warnings
import re
warnings.filterwarnings(action='ignore')


# ### 01 웹 브라우저 띄우기
#  *  만약 chrome 브라우저와 chromedirver의 버전이 안 맞을 경우, 버전을 맞는 것으로 변경해야 함.(가끔 이 부분에서 에러 발생)
#    * 'chrome driver download'로 검색 후, 사이트에 접근 후, 다운로드 가능(window, linux, mac 버전 있음)

# In[2]:


from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver_91')

url = 'https://www.bloomberg.com/graphics/covid-vaccine-tracker-global-distribution/'
driver.get(url)


# In[3]:


import time
time.sleep(3)  # 홈페이지 로딩 시간 3초


# ### 전체 데이터 보기
#  * 나라가 여러나라가 있어, 더 보기 버튼을 2번 정도 눌러준다.

# In[4]:


# //*[@id="dvz-table-global-vaccination"]/div[2]/div[2]/button
# //*[@id="dvz-table-global-vaccination"]/div[2]/div[2]/button
sel_more1 = driver.find_element_by_xpath('//*[@id="dvz-table-global-vaccination"]/div[2]/div[2]/button')
sel_more1.click()
time.sleep(1)


# In[5]:


# //*[@id="dvz-table-usa-vaccination"]/div[2]/div[2]/button
sel_more2 = driver.find_element_by_xpath('//*[@id="dvz-table-global-vaccination"]/div[2]/div[2]/button')
sel_more2.click()


# ### TABLE 선택 후, 데이터 가져오기

# #### Countries and regions 
#  * //*[@id="dvz-table-global-vaccination"]/div[2]/div[1]/table/tbody/tr[1]/td[1]
#  * ..
#  * //*[@id="dvz-table-global-vaccination"]/div[2]/div[1]/table/tbody/tr[3]/td[1]
#  
# #### Doses administered
#  * //*[@id="dvz-table-global-vaccination"]/div[2]/div[1]/table/tbody/tr[1]/td[2]
#  
# #### Enough for % of people
#  * //*[@id="dvz-table-global-vaccination"]/div[2]/div[1]/table/tbody/tr[1]/td[3]
#  
# #### given 1+ dose
#  * //*[@id="dvz-table-global-vaccination"]/div[2]/div[1]/table/tbody/tr[1]/td[4]
#  
# #### fully vaccinated
#  * //*[@id="dvz-table-global-vaccination"]/div[2]/div[1]/table/tbody/tr[1]/td[5]
#  
# #### Daily rate of doses administered
#  * //*[@id="dvz-table-global-vaccination"]/div[2]/div[1]/table/tbody/tr[1]/td[6]
#  

# In[ ]:


all_data = []

for i in range(1, 7, 1):
    data_col = []
    xpath = '//*[@id="dvz-table-global-vaccination"]/div[2]/div[1]/table/tbody/tr/td[%s]' % str(i) 
    sel_data = driver.find_elements_by_xpath(xpath)
    
    for dat in sel_data:
        #print(dat)
        data_col.append(dat.text)
    print(data_col)
    all_data.append(data_col)


# In[ ]:


import pandas as pd


# ### 데이터 확인 
#  * Countries and regions : 나라 및 지역 / country 컬럼
#  * Doses administered : 접종 수 / Doses_administered 컬럼
#  * Enough for % of people : 접종률 / percent_of_people 컬럼
#  * given 1+ dose : 1차 접종 / 1_percent 컬럼
#  * fully vaccinated : 2차 접종 / 2_percent 컬럼
#  * Daily_rate_of_doses_administered : 일일 투여 용량 / Daily_rate_of_doses 컬럼

# In[ ]:


pd.set_option("display.max_rows", 40)

dat_dict = {'country':all_data[0],
            'Doses_administered':all_data[1],
            'percent_of_people:':all_data[2],
            '1_percent':all_data[3],
            '2_percent':all_data[4],
            'Daily_rate_of_doses':all_data[5]
           }

dat_df = pd.DataFrame(dat_dict)
dat_df


# In[ ]:


dat_df.info()


# ### 데이터 전처리
#  * 데이터가 없거나 제대로 얻어지지 못한 부분. 그리고 추가 컬럼 등을 생성

# In[ ]:


### 공백행을 삭제
dat_df['country'].str.len()


# ### 한나라의 중복 행의 존재로 이 부분은 정보 취득 못함

# In[ ]:


dat_df.loc[ dat_df['country'].str.len() <1, : ]


# In[ ]:


sel_index = dat_df[ dat_df['country'].str.len() <1 ].index
print(sel_index)
dat_df.drop (sel_index, axis=0, inplace=True  )


# In[ ]:


dat_df = dat_df.reindex()
dat_df.shape


# In[ ]:


dat_df.loc[dat_df['Doses_administered'] == '–']


# In[ ]:


dat_df.loc[dat_df['Daily_rate_of_doses'] == '–']


# In[ ]:


dat_df.columns


# In[ ]:


col_all = dat_df.columns
for one in col_all:
    print("col name : ", one)
    print( dat_df.loc[dat_df[one] == '–', one].count() )
    print("\n")


# ### 결측치(비어 있는 값)를 -999로 처리한다.

# In[ ]:


col_all = dat_df.columns
for one in col_all:
    print("col name : ", one)
    print( dat_df.loc[dat_df[one] == '–', one].count() )
    dat_df.loc[dat_df[one] == '–', one] = "-999"      # -은 이상치 -999로 치환
    dat_df.loc[dat_df[one] == '<0.1', one] = "0.05"   # <0.1은 0.05로 치환
    
    print("\n")


# ### 확인

# In[ ]:


col_all = dat_df.columns
for one in col_all:
    print("col name : ", one)
    print( dat_df.loc[dat_df[one] == '–', one].count() )


# ### ','을 처리

# In[ ]:



dat_df['Doses_administered'] = dat_df['Doses_administered'].str.replace(',', '')
dat_df['Daily_rate_of_doses'] = dat_df['Daily_rate_of_doses'].str.replace(',', '')


# In[ ]:


dat_df.head(10)


# ### 데이터 전처리 후, 확인

# In[ ]:


dat_df.info()


# In[ ]:


dat_df.Doses_administered.unique()


# In[ ]:


dat_df.isnull().sum()


# In[ ]:


dat_df['Doses_administered'].unique()


# In[ ]:


dat_df['Doses_administered'].head(30)


# In[ ]:


dat_df.loc[dat_df['Doses_administered'].isna() , : ] 


# In[ ]:


dat_df.iloc[ 15:25, :]


# In[ ]:


dat_df_num = dat_df.iloc[:, 1:]
dat_df_num.columns


# In[ ]:


sel_col = dat_df_num.columns
for one in sel_col:
    print("col name :", one)
    dat_df[one] = dat_df[one].astype('float32')
    
dat_df.info()


# ### 파일 만들기

# In[ ]:


from datetime import datetime
import os

now = datetime.now()
file_make_time = "%04d%02d%02d_%02d" % (now.year, now.month, now.day, now.hour)
print(now.day - 1)
now_day = now.day
now_hour = now.hour

print( file_make_time )


# In[ ]:


print( os.getcwd() )
path_dir = os.getcwd() + "\\data\\"
path_file = path_dir + file_make_time
print( path_dir,  path_file, sep="\n" )


# In[ ]:


dat_df.to_csv( path_file + "_vaccine_bloomberg.csv", index=False)
dat_df.to_excel( path_file + "_vaccine_bloomberg.xlsx", index=False)
os.listdir(path_dir)


# * history 
#  * 2021.08.08 version 01
# * 출처를 밝히시고 위의 내용에 대해 자유롭게 사용 가능합니다.

# In[ ]:




