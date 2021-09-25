#!/usr/bin/env python
# coding: utf-8

# ### 두개의 데이터 셋을 합치고 처리하기

# ### 데이터 참고 사이트 
# * our world in data
#   * https://ourworldindata.org/covid-vaccinations
# * bloomberg.com
#   * https://www.bloomberg.com/graphics/covid-vaccine-tracker-global-distribution/
#   
# * 코로나 19(COVID-19) 실시간 상황판
#   * https://coronaboard.kr/

# In[1]:


from IPython.display import display, Image
import os, warnings
import re
warnings.filterwarnings(action='ignore')


# ### 01 파일 불러오기

# In[2]:


os.listdir(os.getcwd())


# In[3]:


import pandas as pd

# excel 데이터 셋도 pd.read_excel로 가져올 수 있음.
corona = pd.read_csv("./data/2021-09-20_corona.csv")
vaccine = pd.read_csv("./data/20210920_00_vaccine_bloomberg.csv")
country_code = pd.read_excel("./data/country.xlsx")

corona.shape, vaccine.shape, country_code.shape


# In[4]:


corona.head()


# In[5]:


vaccine.head()


# In[6]:


country_code.head()


# ### 코로나에 나라명이 있으면 해당되는 열을 붙여라

# In[7]:


corona['국가'].str.extract('([ㄱ-ㅣ가-힣]+)')


# In[8]:


corona['hangul_code'] = corona['국가'].str.extract('([ㄱ-ㅣ가-힣]+)', expand=False)
corona.columns


# In[9]:


col = ['국가', 'hangul_code', '위중증', '치명(%)', '완치(%)', '발생률', '인구수', '확진자_합계', '확진자1일', '사망자합계',
       '사망자1일', '완치합계', '완치1일']
new_corona = corona[col].copy()
new_corona


# ### 두 데이터 셋 연결

# In[10]:


new_corona.head()


# In[11]:


country_code.head()


# In[12]:


country_code.columns = ['han_code', 'eng_code', 'country', 'etc']
country_code.head()


# In[13]:


df_corona = new_corona.merge(country_code, left_on='hangul_code', 
                             right_on='han_code')
df_corona.head()


# In[14]:


df_corona.drop(['국가', 'han_code', 'country', 'etc'], axis=1, inplace=True)
df_corona.head()


# In[15]:


vaccine.head()


# In[16]:


df_corona_all = df_corona.merge(vaccine, left_on='eng_code', right_on='country')
df_corona_all.head()


# In[17]:


df_corona_all.drop(['country'], axis=1, inplace=True)
df_corona_all


# In[18]:


df_corona_all.columns


# In[19]:


sel = ['hangul_code', 'eng_code', '위중증', '치명(%)', '완치(%)', '발생률', '인구수', '확진자_합계', '확진자1일',
       '사망자합계', '사망자1일', '완치합계', '완치1일', 'Doses_administered',
       'percent_of_people:', '1_percent', '2_percent',  'Daily_rate_of_doses' ]
df_corona_all_n = df_corona_all[sel].copy()
df_corona_all_n


# In[20]:


df_corona_all_n.columns


# In[21]:


df_corona_all_n.columns = ['국가명', 'eng_code', '위중증', '치명(%)', '완치(%)', '발생률', '인구수', '확진자_합계',
       '확진자1일', '사망자합계', '사망자1일', '완치합계', '완치1일','백신접종', '접종률(인구)', '1차접종', '2차접종',
       '접종비율(일간)']
df_corona_all_n


# In[22]:


df_corona_all_n.sort_values(['접종률(인구)'], ascending=False)


# In[23]:


df_corona_all_n.info()


# In[24]:


df_corona_all_n['발생률'] = df_corona_all_n['발생률'].astype(int)
df_corona_all_n.info()


# In[25]:


df_corona_all_n['발생률_순위'] = df_corona_all_n['발생률'].rank(ascending=False) # ascending=False : 내림차순
df_corona_all_n['접종률_순위'] = df_corona_all_n['접종률(인구)'].rank(ascending=False) # ascending=False : 내림차순
df_corona_all_n


# In[26]:


df_corona_all_n.sort_values(['접종률_순위'], ascending=True)


# In[27]:


df_corona_all_n.columns


# In[28]:


sel = [ '국가명', 'eng_code', '발생률', '인구수', '백신접종', 
       '접종률(인구)', '발생률_순위', '접종률_순위', '1차접종', '2차접종', 
       '위중증', '치명(%)', '완치(%)', '확진자_합계',
       '확진자1일', '사망자합계', '사망자1일', '완치합계', 
       '완치1일', '접종비율(일간)']

df_corona_all_n = df_corona_all_n[sel]
df_corona_all_n


# In[29]:


df_corona_all_n.sort_values(['발생률_순위'])


# ### 인구당 확진자 비율

# In[30]:


df_corona_all_n['확진자비율_전체인구'] = df_corona_all_n['확진자_합계'].astype(int)/df_corona_all_n['인구수'].astype(int)
df_corona_all_n


# In[31]:


df_corona_all_n.columns


# In[32]:


sel = ['국가명', 'eng_code', '발생률', '인구수', '확진자_합계', '백신접종', '접종률(인구)', '발생률_순위', '접종률_순위',
       '확진자비율_전체인구', '1차접종', '2차접종', '위중증', '치명(%)', '완치(%)',  '확진자1일', '사망자합계',
       '사망자1일', '완치합계', '완치1일', '접종비율(일간)']
df_corona_all_n =  df_corona_all_n[sel]
df_corona_all_n


# In[33]:


from datetime import datetime
import os

now = datetime.now()
file_make_time = "%04d%02d%02d_%02d" % (now.year, now.month, now.day, now.hour)
print( file_make_time )

path_dir = os.getcwd() + "\\data\\"
path_file = path_dir + file_make_time
print( path_dir,  path_file, sep="\n" )


# In[34]:


df_corona_all_n.to_csv(path_file + "_datamerge.csv", index=False)
df_corona_all_n.to_excel(path_file + "_datamerge.xlsx", index=False)


# In[35]:


import seaborn as sns


# ### 백신 접종률과 인구당 확진자 비율의 상관관계

# In[36]:


from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import platform
import matplotlib


# In[37]:


path = "C:/Windows/Fonts/malgun.ttf"
if platform.system() == "Windows":
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system()=="Darwin":
    rc('font', family='AppleGothic')
else:
    print("Unknown System")
    
matplotlib.rcParams['axes.unicode_minus'] = False


# In[38]:


df_corona_all_n.columns


# In[39]:


df_corona_all_n.head()


# ### 확진자 비율과 백신 접종률 상관관계 확인해 보기

# In[40]:


sns.lmplot(x='접종률(인구)', y='확진자비율_전체인구', data=df_corona_all_n)
plt.show()


# ### 인구당 확진자 발생 비율과 백신 접종률 상관관계 그래프 그려보기

# In[41]:


sns.lmplot(x='접종률(인구)', y='발생률', data=df_corona_all_n)
plt.show()


# In[42]:


df_corona_all_n.corr()['접종률(인구)']['발생률']


# In[43]:


df_corona_all_n.corr()['접종률(인구)']['확진자비율_전체인구']


# ### 01 현재까지의 누적된 데이터로 확인 결과 백신 접종률과 인구당 확진지 비율은 양의 상관관계를 갖는다.
# ### 02 현재까지의 누적된 데이터로 확인 결과 백신 접종률과 확진자 발생 비율은 양의 상관관계를 갖는다.
