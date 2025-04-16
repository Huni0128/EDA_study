import pandas as pd
from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = "NanumGothic"

def seoul_population():
    seoul_pop_data = pd.read_excel("./data/seoul_population.xlsx", header=2, usecols="B,D,G,J,N") # 구, 전체인구, 한국인, 외국인, 고령자 칼럼만 가져오기
    seoul_pop_data = seoul_pop_data.rename(columns={seoul_pop_data.columns[0]:"구별",
                                                    seoul_pop_data.columns[1]:"전체인구",
                                                    seoul_pop_data.columns[2]:"한국인",
                                                    seoul_pop_data.columns[3]:"외국인",
                                                    seoul_pop_data.columns[4]:"고령자"}) # B,D,G,J,N 칼럼명 변경

    seoul_pop_data = seoul_pop_data.replace(',','', regex=True) # 데이터 내부의 ',' (쉼표) 제거
    seoul_pop_data = seoul_pop_data.replace(' ','', regex=True) # 데이터 내부의 공백 제거
    seoul_pop_data = seoul_pop_data.drop(index=[0]) # 총합계 열 삭제
    
    seoul_pop_data["외국인비율"] = seoul_pop_data["외국인"] / seoul_pop_data["전체인구"] * 100
    seoul_pop_data["고령자비율"] = seoul_pop_data["고령자"] / seoul_pop_data["전체인구"] * 100
    
    return seoul_pop_data


def seoul_cctv():
    
    seoul_cctv_data = pd.read_excel("./data/seoul_cctv_data.xlsx", engine="openpyxl") # xlsx 파일 변수에 집어넣기

    seoul_cctv_data = seoul_cctv_data.drop(columns=["순번"]) # 순번칼럼 삭제
    seoul_cctv_data = seoul_cctv_data.drop(index=[0]) # 총합계 열 삭제
    seoul_cctv_data = seoul_cctv_data.reset_index(drop=True) # 행 삭제로 인한 행 번호 초기화
    seoul_cctv_data = seoul_cctv_data.replace(',','', regex=True) # 데이터 내부의 ',' (쉼표) 제거
    seoul_cctv_data = seoul_cctv_data.replace(' ','', regex=True) # 데이터 내부의 공백 제거
    seoul_cctv_data = seoul_cctv_data.rename(columns={"구분":"구별"})
    
    seoul_cctv_data['2021년 이전'] = seoul_cctv_data.iloc[:,2:-3].sum(axis=1)
    seoul_cctv_data['2022년 이후'] = seoul_cctv_data.iloc[:,9:12].sum(axis=1)
    seoul_cctv_data['최근3년 증가율'] = seoul_cctv_data['2022년 이후'] / seoul_cctv_data["2021년 이전"] * 100
    
    seoul_cctv_data = seoul_cctv_data.sort_values(by='최근3년 증가율', ascending=False) # 증가율 높은 순으로 정렬
    
    return seoul_cctv_data
    
def org_data():
    seoul_merge = pd.merge(seoul_cctv(),seoul_population(), on='구별', how="left") #cctv_df, population_df 합치기
    cols_to_drop = seoul_merge.columns[seoul_merge.columns.get_loc("2015년 이전 설치된 CCTV "):seoul_merge.columns.get_loc("2022년 이후") + 1] # 필요없는 칼럼 저장
    global seoul_data
    seoul_data = seoul_merge.drop(columns=cols_to_drop) # 필요없는 칼럼 삭제
    
    seoul_data["CCTV비율"] = seoul_data["총 계"] / seoul_data["전체인구"] * 100
    seoul_data = seoul_data.set_index("구별") #기본 index가 이미지에 출력되서 변경
    
    return seoul_data

def drawGraph():
    seoul_data["총 계"].sort_values().plot(
        kind="barh", grid=True, title="가장 CCTV가 많은 구", figsize=(10,6))
    plt.savefig("CCTV_graph.png")

def drawPlot():
    plt.figure(figsize=(10,6))
    plt.scatter(x=seoul_data["전체인구"], y=seoul_data["총 계"], label="CCTV 개수", color="blue")
    line = np.polyfit(seoul_data["전체인구"], seoul_data["총 계"], 1) # 경향선을 위한 1차 함수 만들기
    trend_line = np.poly1d(line)
    plt.plot(seoul_data["전체인구"], trend_line(seoul_data["전체인구"]), color="red", label="Trend Line") # x축방향으로 경향선 그리기

    for i, name in enumerate(seoul_data.index):
        plt.annotate(name, (seoul_data["전체인구"].iloc[i], seoul_data["총 계"].iloc[i]),
                     textcoords="offset points", xytext=(-10,5), ha="center", fontsize=9) #각 plot에 해당하는 구 이름 작성하기

    plt.title("인구 수에 따른 CCTV 개수")
    plt.xlabel("인구수")
    plt.ylabel("CCTV 개수")
    plt.legend()
    plt.grid(True)
    plt.savefig("CCTV_plot.png")

org_data()
drawGraph()
drawPlot()

