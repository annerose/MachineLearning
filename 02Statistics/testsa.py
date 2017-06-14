# -*- coding: utf-8 -*-

__author__ = 'dddd'

import math

# 求平均值
def calcMean(arr):
    return sum(arr) / float(len(arr))



# 平方差总和
def calcSumSquarDiff (arr):

    mean = calcMean(arr)
    squartsum = 0
    for i in arr:
        squartsum += (i - mean) **2

    return squartsum

# 标准差
def calcSamleStandDevia (arr):
    return math.sqrt(calcSumSquarDiff(arr)  / (len(arr) - 1))

# 求均值标准差
def calcStandErrorMean(arr1, arr2):
    s1 = calcSamleStandDevia(arr1)
    s2 = calcSamleStandDevia(arr2)

    sem = math.sqrt( (s1 ** 2) / len(arr1) + (s2 **2) / len(arr2))

    print 'StandErrorM =', sem

    return sem

# discard...
def calcPoolVal(arr1, arr2):
    return (calcSumSquarDiff(arr1) + calcSumSquarDiff(arr2)) / (len(arr1) + len(arr2) - 2)

# discard...
def calcStandErrorbyPool (arr1, arr2):
    sp2 = calcPoolVal(arr1, arr2)
    se = math.sqrt(sp2 / len(arr1) + sp2 / len(arr2))
    print 'StandErrorbyPool = ', se

#  求t-test 统计值
def calcTSat(arr1, arr2):

    # 均值标准差
    standErrMean = calcStandErrorMean(arr1, arr2)
    # standErrMeanByPool = calcStandErrorbyPool(arr1, arr2)
    return  (calcMean(arr1) -  calcMean(arr2)) / standErrMean







# 文字和颜色一致的识别时间
arrCongruent   = [12.079,16.791,9.564,8.63,14.669,12.238,14.692,8.987,9.401,14.48,22.328,15.298,15.073,16.929,18.2,12.13,18.495,10.639,11.344,12.369,12.944,14.233,19.71,16.004]

# 文字和颜色不一致的识别时间
arrIncongruent = [19.278,18.741,21.214,15.687,22.803,20.878,24.572,17.394,20.762,26.282,24.524,18.644,17.51,20.33,35.255,22.158,25.139,20.429,17.425,34.288,23.894,17.96,22.058,21.157]




# t test 统计值
tSta = calcTSat(arrCongruent, arrIncongruent)

print 't test sats =', tSta

# 自由度
df = len(arrCongruent) + len(arrIncongruent) - 2;

print 'df =', df

# t test 临界值 alpha = 0.05, one tail, df46, tc = 1.684 ~ 1.676
tCrictal = -1.676

# null hypothesis
h0 = (tSta <  tCrictal)
print 'h0 =', h0