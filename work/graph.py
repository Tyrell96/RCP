import pandas as pd
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy.interpolate import interp1d
import numpy as np

data_sn = pd.read_excel('C:\\Users\\JH\\Desktop\\sn_curve.xlsx')

def du_find(data0): #중복된 값 찾기
    DFU = data_sn[data_sn.duplicated(data0,keep=False)]
    return DFU

def du_avgN(data1): #중복된 값의 평균값 구하기
    data = data1['N']
    out = round(np.mean(data))
    return out


x = du_find('S') #S 열에서 중복 값 찾기
A_data = data_sn.drop_duplicates('S',keep=False).copy() #중복 값 다 삭제해서 A_data에 저장
xx = x.iloc[1]['S'] # 중복값의 S 값 찾기
yy = du_avgN(du_find('S')) # 중복값의 N 평균값
A_data.loc[len(A_data)] = [xx, yy] #해당열에 S와 N의 평균값 집어넣음

x_ori = A_data['S'] #정리된 S 값
y_ori = A_data['N'] #정리된 N 값

ix = np.linspace(59, 2000, 300) #해당 사이의 값 300개를 일정한 간격으로 생성

f = interpolate.interp1d(y_ori,x_ori, kind='cubic') # S,N값을 가져와 cubic형태로 보간함
plt.plot(ix,f(ix), label='data') #f에 300개의 임의의 값을 s,n갑 사이에서 대략적인 보간법을 이용하여 값을 나타냄
plt.legend()
plt.title("S/N Curve")
plt.xlabel('N data')
plt.ylabel('S data')
plt.show()