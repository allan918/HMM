import math
import operator
import dataFunction as p

lastweather = p.starting_b()
behavior = p.act
weather = p.weather


def v(behaviors):
    maxtrans = max(lastweather.items(), key=operator.itemgetter(1))[0]
    mostlikelyW = [maxtrans]
    for b in behaviors:
        mostlikelyW.append(viterbi(b, mostlikelyW[-1]))
    return mostlikelyW


def viterbi(behav, lastw):
    global lastweather
    print(lastweather)
    for w in weather:
        lastweather[w] = lastweather[w] + math.log(p.trans_probility(lastw, w), 10) + math.log(
            p.find_emission(w, behav), 10)
    maxweather = max(lastweather.items(), key=operator.itemgetter(1))[0]
    return maxweather
