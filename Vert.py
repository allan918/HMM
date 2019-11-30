import math
import opreator

lastweather = {'Sunny': 0, 'Cloudy': 0, 'Rainy': 0, 'Storm': 0}


def vertib(A1, A2, tp, behavior, lastw):
    global lastweather
    for w in weather:
        lastweather[w] = lastweather[w] + math.log(tp(lastw, w), 10)
    maxw = max(lastweather.items(), key=operator.itemgetter(1))[0]

    maxweather = ''
    p = 0
    prob = lastweather[maxw]
    for m in mood:
        prob = prob + math.log(A1(next, m), 10) + math.log(A2(m, behavior), 10)
        if prob > p:
            p = prob
            maxweather = weather
    return maxweather
