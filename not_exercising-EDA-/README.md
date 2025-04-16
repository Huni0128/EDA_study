# Reasons for Not Exercising

[![Python](https://img.shields.io/badge/Python-3.12.3-blue.svg)](https://www.python.org/)

이 프로젝트는 **서울시 운동을 하지 않는 이유** 데이터를 활용한 탐색적 데이터 분석(Exploratory Data Analysis, EDA) 프로젝트입니다.  
성별에 따른 운동 비실천 주요 원인을 비교 분석하고, 파이 차트를 활용해 남성과 여성의 운동 비실천 이유 분포를 시각화합니다.

---

## 📁 데이터
-**서울시 운동을 하지 않는 이유**[서울시 운동을 하지 않는 이유](https://data.seoul.go.kr/dataList/10280/C/2/datasetView.do)

---

## 🔧 사용 기술

| **카테고리**           | **기술 스택**                                                                                                                                                                                     |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **OS & Editor**        | ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=Ubuntu&logoColor=white) &nbsp; ![VS Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=flat-square&logo=Visual%20Studio%20Code&logoColor=white)                |
| **Language & Library** | ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white) &nbsp; ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=Pandas&logoColor=white) &nbsp; ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=NumPy&logoColor=white) &nbsp; ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=Matplotlib&logoColor=white) |
| **Version Control**    | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=GitHub&logoColor=white) &nbsp; ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=Git&logoColor=white)                                                |

---

## 📊 분석 내용

- **데이터 전처리**: 결측치 처리, 이상치 탐지, 데이터 정규화 등의 전처리 과정 수행
- **데이터 시각화**: 파이차트를 통해 데이터의 분포와 상관관계 분석

### 예시 결과

<div align="center">
  <img src="images/man_women.png" alt="남자,여자 운동하지 않는 이유" width="500"/>
  <br/>
  <em>남자,여자 운동하지 않는 이유</em>
  <br/>
</div>

---

## 🔍 주요 분석 결과

- **남성 vs 여성 운동 비실천 이유**: 남성과 여성의 운동 비실천 이유를 비교 분석한 결과, 남성은 주로 시간 부족과 체력 저하를, 여성은 안전 문제와 환경적 요인을 주요 원인으로 꼽았습니다.
- **성별 패턴**: 파이 차트를 통해 각 성별의 운동 비실천 이유 분포를 시각화함으로써, 성별에 따른 차이를 명확히 확인할 수 있었습니다.
- **데이터 기반 인사이트**: 이 분석을 통해 남녀 각각의 운동 비실천 이유에 특화된 맞춤형 건강 증진 전략 수립의 필요성을 도출할 수 있었습니다.

---

## 🚀 실행 방법

1. **데이터 다운로드**: 데이터셋을 프로젝트에 포함시키거나 외부 링크를 통해 다운로드합니다.
2. **필수 라이브러리 설치**:
   ```bash
   pip install pandas numpy matplotlib
