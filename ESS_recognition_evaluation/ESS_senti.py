import pandas as pd
import json
import numpy as np
import random
from matplotlib import pyplot as plt
import seaborn as sns
import sys
sys.path.append('D:\情绪-建成环境\编程\sentiment')  #将路径添加进来，方便调用自己编写的函数
import dzddqx as dzdp


# with open('D:\情绪-建成环境\自制景观情感词典\要素生态系统服务\\生态系统服务词.json', 'r')as o:
#     ESS = dict(json.load(o))


index1='生态系统服务频率'
index2='生态系统服务得分'
index3='公园名称'
index4='情绪得分标准值'

"""读取所有评论数据"""
# df=pd.read_excel('北京公园ess.xlsx')
# indexs=list(df.columns) #5-20,21-36

"""将公园名称保存到本地"""
# parks=df['公园名称']
# parks=sorted(set(list(parks)),key=list(parks).index)
# with open ('park_names.txt','a') as o:
#     o.write('\n'.join(parks))
parks=dzdp.read_txt('park_names.txt',encoding='ANSI')   #读取公园名称

'''文件中读取数据，加载为向量，并本地保存'''
# ESS_portion_matrix=np.asarray([df[index1].apply(lambda x:[int(x) for x in str(x).split(',')])])   #从本地文件读取频率
# ESS_senti_matrix = np.asarray([df[index2].apply(lambda x:[int(x) for x in str(x).split(',')])])   #从本地文件读取得分
# np.save('ESS_portion_matrix',ESS_portion_matrix)   #保存
# np.save('ESS_senti_matrix',ESS_senti_matrix)   #保存
# ESS_portion_matrix=np.load('ESS_portion_matrix.npy')    #读取频率矩阵

"""读取公园的平均评论数据"""
df=pd.read_excel('统计.xlsx')
indexs=list(df.columns) #1-16;17-32
for i in range(17,33):
    sns.boxplot([i-16 for j in range(50)],df[indexs[i]],
                order=[j for j in range(1,17)])
plt.xticks([j for j in range(0,16)],[index[3:].replace(' portion','').replace(' senti','') for index in indexs[17:33]],rotation=15,fontsize=10)
plt.xlabel('Ecosystem Service Category',fontsize=15)
plt.ylabel('Sentiment Score',fontsize=15)
plt.title('ES Performance Boxplot',fontsize=20)
plt.grid()
plt.show()