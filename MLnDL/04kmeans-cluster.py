# -*- coding: utf-8 -*-
# !/usr/bin/python

import sys
import csv

import pylab
from pylab import plot, show
from numpy import array
from numpy import vstack
from numpy import genfromtxt
import numpy as np
from scipy.cluster.vq import kmeans
from scipy.cluster.vq import vq

def readData(filename, columns):
    csv = genfromtxt(filename, delimiter=",",
                     usecols=(map(int, columns.split(","))))
    return csv

def writeResult(filename, idx):
    w = open(filename, 'w', encoding="utf-8")

    for i in range(len(idx)):
        w.write("{}\n".format(idx[i]))
    w.close()

if __name__ == "__main__":
    k = sys.argv[1]
    data_filename = sys.argv[2]
    columns = sys.argv[3]
    centroid_filename = sys.argv[4]
    out_filename = sys.argv[5]

    # 데이터 파일에서 읽어오기 (1)
    read_data = readData(data_filename, columns)

    # kmeans 학습 수행하기 (2)
    centroids, _ = kmeans(read_data, int(k))

    # 각 예제를 군집에 할당 (3)
    idx, _ = vq(read_data, centroids)
    writeResult(out_filename, idx)

    np.savetxt(centroid_filename, centroids, delimiter=",")

    # 결과 차트 출력 (4)
    for i in range(int(k)):
        plot(read_data[idx == i, 0], read_data[idx == i, 1], 'o', markersize=3)
        plot(centroids[i:, 0], centroids[i:, 1], '^r', markersize=10)

    filename = data_filename.split("/")[len(data_filename.split("/"))-1]
    pylab.savefig("04kmeans-cluster_" + filename + ".png")
    # show()
    # python 04kmeans-cluster.py 3 ./practice/chapter04/iris.data "0,1,2,3" iris-centroid.csv 04iris_result.txt
    # python 04kmeans-cluster.py 3 iris.data "0,1,2,3" iris-centroid.csv 04iris_result.txt
    # python 04kmeans-cluster.py 3 ./practice/chapter04/wine.data "1,2,3,4,5,6,7,8,9,10,11,12,13" wine-centroid.csv 04wine_result.txt
    # python 04kmeans-cluster.py 3 wine.data "1,2,3,4,5,6,7,8,9,10,11,12,13" wine-centroid.csv 04wine_result.txt