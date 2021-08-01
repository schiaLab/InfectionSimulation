import random
import pandas as pd

def read_network(route="socfb-American75.mtx"):
    data = open(route)

    n = 0

    result = {}

    for line in data:

        aList = []

        if n == 0:

            n += 1
            continue

        else:

            line = line.split(" ")

            for num in line:
                aList.append(int(num))

            n += 1


            result[aList[0]] = result.get(aList[0], []) + [aList[1]]
            result[aList[1]] = result.get(aList[1], []) + [aList[0]]


        if n % 50000 == 0:

            print(f"{n}번째 연결선 처리 완료")



    return result, n-1

def sample(array, p):

    result = []

    for ele in array:

        if random.random() < p:

            result.append(ele)

    return result




def propergation(map, infection_p):

    already = []

    key0 = random.choice(list(map.keys()))

    infectionTimeSeries = []

    infectionTimeSeries.append(1)

    already.append(key0)

    array = select(already, map, [key0], infection_p)

    infectionTimeSeries.append(len(array))

    already += array


    while True:

        array1 = select(already, map, array, infection_p)

        infectionTimeSeries.append(len(array))

        already += array1

        array = array1

        if len(array) == 0:

            break

        #print(f"{len(array)}명 감염")




    return infectionTimeSeries





def select(already, map, array, infection_p):

    result = []


    for key in array:

        for ele in sample(map[key], infection_p):

            if ele in already:
                continue

            else:

                result.append(ele)


    result = pd.Series(result)

    result = list(result.drop_duplicates())


    return result

