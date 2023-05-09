# Micro_LED 분석
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

 #### 
+ **Run file description**

   First, extract only the file named 'LMZ' from the file that the customer gave us.\
   Then, after analyzing the raw data given by the customer using various modules, make a csv file.

---

## 3. Install and Run

####
* Getting Stared
   + Entered the Terminal, write down 'pip install -r requirements.txt' and download it. \
``(base) C:\Download\PE02_A02_SBBFU-1>pip install -r requirements.txt``

* How to Run
  + Choose the raw data folder customer want to analyze.
   
  + After select the data you want to analyze, select various options such as wafer, die option, figure shape (show figure, save figure, save csv) and press run button.

---

## 4. Description of the module file feature

* Fitting module
   + The graph is drawn by parsing the raw data of Wavelengthsweep, IL, Current, and Voltage in the xml file.
   + The fitting of parsing a raw data and displays the data value y-axis corresponding to x-axis by the customer and the desired R-squared, etc. and stored in the graph to visualize the image.

* CSV module
  + It contains a variety of data information, including Lot, Wafer, and Operator etc.
  + Create a dataframe so that the meausured information in the xml file can be viewed at a glance.
  + Save this data frome in csv format in the 'Result' folder.
 
 ---
## 5. Run file algorithm
* First of all 
   + Please select options such as Data location, Analyze folder, Figure shape, Colum & Row, Save figure mode, Show figure mode, Save CSV in the run.py. 
   

* And then
  + The 'run' function in the runfile.py is executed.
* Next
   + Depending on the option initially selected, ivfitting.py, measured_spectra.py, processed_spectra.py, process.py, ref_fitting.py are executed. 
 ---

![image](https://user-images.githubusercontent.com/77437180/132507266-4615ae28-653f-494b-85aa-2b714852021e.png)
 
### :warning:precautions

 1) You must select all the options in the 'Checkbox'. If you don't, you'll make a error.
 2) When fitting sometimes doesn't work, it keeps running until fitting is done well.
 3) If you choose the All option when Wafer is selected, you must not choose any other option.
