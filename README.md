# corona_analysis

### 웹 사이트 URL
 * https://frontierall.github.io/corona_analysis/


## 프로젝트 하나 - 백신 접종률과 인구당 확진자의 비율의 관계
### 01 데이터 수집
 * 코로나19 실시간 상황판 : https://coronaboard.kr/
 * Bloomberg Covid-19 Tracker : https://www.bloomberg.com/graphics/covid-vaccine-tracker-global-distribution/
 
#### 수집된 데이터 
 * https://github.com/frontierall/corona_analysis/tree/main/data
   * xxx_corona_xx : 코로나 수집 데이터
   * xxx_vaccine_xx : 백신 수집 데이터
   * xxx_datamerge_xxx_ : 수집 데이터 전처리 및 병합 데이터 셋 

### 02 데이터 수집 후, 기본 분석 - 상관관계 확인
#### 2-1 실행 코드 - 데이터 수집하기 - 웹
 * 데이터 수집 [html](https://frontierall.github.io/corona_analysis/html_pdf/01_dataScraping_corona02.html) 
 * 데이터 수집 [html](https://frontierall.github.io/corona_analysis/html_pdf/02_dataScraping_bloomberg.html) 
 * 데이터 처리 및 병합 - 상관관계 확인 [html](https://frontierall.github.io/corona_analysis/html_pdf/03_corona_vaccine_merge.html) 
 * 나라별 백신 접종률과 인구당확진자비율/사망률/위중증률 상관관계 확인 [html](https://frontierall.github.io/corona_analysis/html_pdf/06_corona_analysis.html) 
 
### 확인 결과
 * (2021/09/21 기준)지금까지의 백신 접종률과 인구당 확진자 비율은 0.58정도(2021/09 기준)으로 양의 상관관계를 갖는다.
   * 왜 그런지 추가 확인 필요.
 * (2021/09/21 기준) 위중증의 값이 없는 것을 제외한 131개국의 확인 결과 
   * 백신 접종률과 인구당 확진자 비율은 0.27정도 으로 양의 상관관계를 갖는다.
    * 왜 그런지 추가 확인 필요.
 * (2021/09/21 기준) 인구 200만 이상의 나라 확인 결과
   

### 03. 왜 상관관계가 양의 상관관계일까? 
 * 데이터로 이해할 수 없는 통계에 대한 자료를 수집 후, 다각도 알아보기

### 04. 의문에 대한 자료 리서치 및 추가 상세 분석 [이동하기](https://github.com/frontierall/corona_analysis/tree/main/project01_01)

## 관련 자료
### 지난 팀 코로나 관련 자료
### 지난 팀 프로젝트 github [Link](https://github.com/LDJWJ/LikeLion_10th_DataCourse/tree/main/00_TeamProject_First_Corona)

## 기타 정보 사이트
 * 코로나19 실시간 상황판 [Link](https://coronaboard.kr/)
 * Bloomberg Covid-19 Tracker [Link](https://www.bloomberg.com/graphics/covid-vaccine-tracker-global-distribution/)
 * 질병관리청 보도자료 09/15 [Link](https://www.kdca.go.kr/board/board.es?mid=a20501010000&bid=0015&list_no=716965&cg_code=&act=view&nPage=1)

### [부작용 관련]
   * 국민 청원 모음 (크베어 댕큰 코리아) [https://cafe.naver.com/querdenkenkorea/9525)
   * 국민 청원 (보건복지) [Link](https://www1.president.go.kr/petitions/?c=41&only=1&page=1&order=1)
   * 코로나 백신 부작용 극복 (Link](https://cafe.naver.com/blue0bum4) - 코로나 백신 부작용 사례
   * 코로나 백신 부작용 피해자 모임 [Link](https://cafe.naver.com/covid2021) - 코로나 백신 피해자 모임

### 해외
   * CDC (Centers for Disease Control and Prevention) [Link](https://www.cdc.gov/nchs/data_access/ftp_data.htm)
   * U.S. CDC Public Health datasets
   * Who (World Health Organization) [Link](https://www.who.int/)
   * HealthData.gov [Link](https://healthdata.gov/)
   * U.S. Food and Drug Administration (FDA) - [Link](https://open.fda.gov/)
 
### Dataset
 * Awesome Public Datasets [Link](https://github.com/awesomedata/awesome-public-datasets#machinelearning)
 * kaggle dataset - Novel Corona Virus 2019 Dataset
   [Link](https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset)
 * kaggle dataset - COVID-19 Corona Virus India Dataset
   [Link](https://www.kaggle.com/imdevskp/covid19-corona-virus-india-dataset/code)
 * 공공 데이터 포털 [Link](https://www.data.go.kr/index.do)
   * (1) 서울특별시_코로나19 자치구별 확진자 발생동향 [Link](https://www.data.go.kr/data/15081054/fileData.do)
   * (2) 건강보험심사평가원_코로나19병원정보(국민안심병원 외)서비스 [Link](https://www.data.go.kr/data/15043078/openapi.do)
 * 서울 열린데이터 광장 [Link](https://data.seoul.go.kr/) - 코로나 등의 키워드 검색
 * 경기도 데이터 드림 [Link](https://data.gg.go.kr/portal/data/dataset/searchDatasetPage.do) 




#### 이곳의 자료는 자유롭게 사용 편집이 가능합니다.


