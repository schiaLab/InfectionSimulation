import model as m
import numpy as np
import pandas as pd
from itertools import combinations
import random

infection_p = 1 / 1000
isRandom = True

if not isRandom:
    map, n  = m.read_network()

else:
    map, n = m.read_network()
    V = set([v for v in range(len(map.keys()))])
    map2 = {}

    p = n / ((len(V) * (len(V) -1)) / 2)

    for combination in combinations(V, 2):

        if random.random() < p:

            map2[combination[0]] = map2.get(combination[0], []) + [combination[1]]
            map2[combination[1]] = map2.get(combination[1], []) + [combination[0]]

    map = map2
    map2 = None
indices = []

simul = []

for n in range(20):

    indices.append(infection_p)

    print(infection_p)

    sumResult = []
    meanResult = []
    lenResult = []

    for n in range(1000):


        result = m.propergation(map, infection_p)

        sumResult.append(np.sum(result))
        meanResult.append(np.mean(result))
        lenResult.append(len(result))

    sumResult = np.mean(sumResult)
    meanResult = np.mean(meanResult)
    lenResult = np.mean(lenResult)

    print(f"열람확률 {infection_p}일 때 총 {sumResult}명 감염")

    row = [sumResult/len(map.keys()), sumResult, meanResult, lenResult]

    simul.append(row)


    infection_p += 1 / 1000


results = pd.DataFrame(simul, index=indices,
                       columns=["평균 감염률", "평균 총 감염자수", "평균 순간 감염자수", "평균 감염 종료 시점"])


results.to_csv("결과 데이터2.csv", index=True, encoding="cp949")