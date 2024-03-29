# Micro LED 분석
---
## 1. 프로그램 소개
Micro_LED에 대한 PL(Photoluminescence) 검사 데이터를 활용하여 EL(Electroluminescence) 데이터를 예상하는 프로그램입니다. \
표와 그래프를 통해 각 데이터 간의 상관관계를 분석 및 근사할 수 있습니다.

#### - 개발자 : 문의사항 있을 시, 아래 메일로 연락주시기 바랍니다.

 - 박승민 (psm401@hanyang.ac.kr)
 - 김강석 (ddol410@hanyang.ac.kr)
---

## 2. 프로그램 정보
 #### 
 + **상세 내용**

     주요 목표는 PL 데이터에서 EL 데이터의 예상값을 도출하여 불량품을 확인하는 것이다.

     주요 과제는 PL 세기 데이터에 대한 EL 데이터의 상관관계를 분석을 진행한다

     - PL 세기 데이터
     - EL 데이터

  - 두가지이며, 먼저 분석에 용이하도록 데이터를 가공한다. 
  - 그 다음 Seaborn을 통해 상관관계를 분석하고 Pandas와 Matplotlib를 이용하여 표와 그래프를 각각 도출한다. 
  - 마지막으로 불량 데이터를 필터링 후 데이터 추출 및 근사하여 그래프로 표시한다.

---

## 3. 설치 및 실행

####
 * 시작할 때
    + 터미널로 들어가서, 하기의 문구를 입력한다.\
 ``pip install -r requirements.txt``


 * 실행 방법
   + 사용자가 분석하기 원하는 미가공 데이터 폴더를 지정한다.

---

## 4. 모듈 설명

#### 그래프 피팅(Fitting)

   * 엑셀에서 미가공 PL과 EL 데이터를 추출하여 그래프로 나타낸다.   
   
       - 첫번째 그래프는 각각의 축에 따라 데이터 간의 상관관계를 나타내며 1과 -1에 가까울수록 데이터 간의 상관관계가 있음을 의미한다.
       - 두번째 그래프는 각각의 축에 따른 데이터 간의 산포도를 나타내며 이를 통해 군집 위치을 알 수 있다.
       - 데이터 값을 필터링 진행한 후 상위 두 그래프를 재도출한다.
       - PL 세기 데이터와 EL 전력 데이터 간의 상관관계를 도출하고 이를 바탕으로 근사식을 구할 수 있다.
       - 최종적으로 PL 데이터를 기반으로 하여 EL 데이터를 추출하여 불량률을 예측할 수 있다

---

## 5. 결과 

#### 최조 결과를 Jupyter notebook 을 이용하여 Python code 기반으로 문서화 함. 
* [최종 결과 문서](https://github.com/YKgroup-HYU/micro_led_analysis/blob/main/doc/Final%20Document.ipynb)
