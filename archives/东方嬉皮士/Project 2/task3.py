from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats
import os
plt.rcParams['savefig.dpi'] = 300  # 图片像素
plt.rcParams['figure.dpi'] = 300  # 分辨率

def plot_box(dataframe, number):
    df = dataframe[:number]
    x1 = df['Temp__F_']  # 温度
    x2 = df['Humidity____']
    x3 = df['Pressure__mbar_']
    x4 = df['PM_2_5_30_Minute_Avg_']
    x5 = df['PM_2_5_1_Hour_Avg_']
    path = './task3.1/'
    if not os.path.exists(path):
        os.mkdir(path)
    plt.boxplot(x1, labels=['Temp__F_'])
    plt.savefig(path+'x1.jpg')
    plt.show()
    plt.boxplot(x2, labels=['Humidity____'])
    plt.savefig(path+'x2.jpg')
    plt.show()
    plt.boxplot(x3, labels=['Pressure__mbar_'])
    plt.savefig(path+'x3.jpg')
    plt.show()
    plt.boxplot(x4, labels=['PM_2_5_30_Minute_Avg_'])
    plt.savefig(path+'x4.jpg')
    plt.show()
    plt.boxplot(x5, labels=['PM_2_5_1_Hour_Avg_'])
    plt.savefig(path+'x5.jpg')
    plt.show()


def plot_scatter(dataframe, number):
    df = dataframe[:number]
    x1 = df['Temp__F_']  # 温度
    x2 = df['Humidity____']
    x3 = df['Pressure__mbar_']
    x4 = df['PM_2_5_30_Minute_Avg_']
    x5 = df['PM_2_5_1_Hour_Avg_']
    y = df['PM_2_5_24_Hour_Avg_']
    path = './task3.2/' + str(number) + '/'
    if not os.path.exists('./task3.2/'):
        os.mkdir('./task3.2/')
    if not os.path.exists(path):
        os.mkdir(path)
    plt.scatter(x1, y, label='Temp__F_ and PM_2_5_24_Hour_Avg_')
    plt.xlabel('Temp__F_')
    plt.ylabel('PM_2_5_24_Hour_Avg_')
    plt.savefig(path+'x1_y.jpg')
    plt.show()
    plt.scatter(x2, y, label='Humidity____ and PM_2_5_24_Hour_Avg_')
    plt.xlabel('Humidity____')
    plt.ylabel('PM_2_5_24_Hour_Avg_')
    plt.savefig(path+'x2_y.jpg')
    plt.show()
    plt.scatter(x3, y, label='Pressure__mbar_ and PM_2_5_24_Hour_Avg_')
    plt.xlabel('Pressure__mbar_')
    plt.ylabel('PM_2_5_24_Hour_Avg_')
    plt.savefig(path+'x3_y.jpg')
    plt.show()
    plt.scatter(x4, y, label='PM_2_5_30_Minute_Avg_ and PM_2_5_24_Hour_Avg_')
    plt.xlabel('PM_2_5_30_Minute_Avg_')
    plt.ylabel('PM_2_5_24_Hour_Avg_')
    plt.savefig(path+'x4_y.jpg')
    plt.show()
    plt.scatter(x5, y, label='PM_2_5_1_Hour_Avg_ and PM_2_5_24_Hour_Avg_')
    plt.xlabel('PM_2_5_1_Hour_Avg_')
    plt.ylabel('PM_2_5_24_Hour_Avg_')
    plt.savefig(path+'x5_y.jpg')
    plt.show()


def task3_3(dataframe,number):
    df = dataframe[:number]
    y = df['PM_2_5_24_Hour_Avg_']
    path = './task3.2/' + str(number) + '/'
    if not os.path.exists('./task3.2/'):
        os.mkdir('./task3.2/')
    if not os.path.exists(path):
        os.mkdir(path)
    sns.distplot(y, hist=False, kde=False, fit=stats.norm,
                 fit_kws={'color': 'black', 'label': 'u=0,s=1', 'linestyle': '-'})
    plt.savefig(path+'density curve of PM_2_5_24_Hour_Avg_.png')
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('air-quality.csv')
    number = 1000
    plot_box(df, number)
    plot_scatter(df, number)
    task3_3(df, number)
