import random
import math

starting_p = {'Sunny': 0.45, 'Cloudy': 0.15, 'Rainy': 0.4}
weather = ["Sunny", "Cloudy", "Rainy"]
act = ["Picnic", "Exercise", "Home"]
weather_mood = {
    "Sunny":
        {
            "Good": 0.6,
            "Moderate": 0.2,
            "Bad": 0.2
        },

    "Cloudy":
        {
            "Good": 0.4,
            "Moderate": 0.4,
            "Bad": 0.2},

    "Rainy":
        {
            "Good": 0,
            "Moderate": 0.5,
            "Bad": 0.5
        }
}

weather_weather = {
    "Sunny": {
        "Sunny": 0.4,
        "Cloudy": 0.35,
        "Rainy": 0.25,
    },
    "Cloudy": {
        "Sunny": 0.2,
        "Cloudy": 0.35,
        "Rainy": 0.45,
    },
    "Rainy": {
        "Sunny": 0.2,
        "Cloudy": 0.3,
        "Rainy": 0.5,
    }
}

weather_act = {
    "Good": {
        "Picnic": 0.4,
        "Exercise": 0.4,
        "Home": 0.2
    },
    "Moderate": {
        "Picnic": 0.2,
        "Exercise": 0.4,
        "Home": 0.4
    },
    "Bad": {
        "Picnic": 0,
        "Exercise": 0.4,
        "Home": 0.6
    }
}


def trans_probility(weather1, weather2):
    return weather_weather[weather1][weather2]


def find_weather_mood_prob(weather1, mood1):
    return weather_mood[weather1][mood1]


def find_mood_behavior(mood1, act1):
    return weather_act[mood1][act1]


def find_emission(w, b):
    prob = 0
    for m in mood:
        prob += find_weather_mood_prob(w, m) * find_mood_behavior(m, b)
    return prob


make_up = [random.choices(weather, weights=[0.45, 0.15, 0.4], k=1)[0]]
co_behavior = []
mood = ["Good", "Moderate", "Bad"]

temp_mood = random.choices(mood, weights=[0.434, 0.4, 0.166], k=1)[0]
if temp_mood == "Good":
    pos3 = [0.4, 0.4, 0.1]
elif temp_mood == "Moderate":
    pos3 = [0.2, 0.4, 0.4]
else:
    pos3 = [0, 0.4, 0.6]
co_behavior.append(random.choices(act, weights=pos3, k=1)[0])

for x in range(365):
    last = make_up[len(make_up) - 1]
    if last == "Sunny":
        pos = [0.4, 0.35, 0.25]
    elif last == "Cloudy":
        pos = [0.2, 0.35, 0.45]
    else:
        pos = [0.2, 0.3, 0.5]
    chosen = random.choices(weather, weights=pos, k=1)[0]
    make_up.append(chosen)
    if chosen == "Sunny":
        pos2 = [0.6, 0.2, 0.2]
    elif chosen == "Cloudy":
        pos2 = [0.4, 0.4, 0.2]
    else:
        pos2 = [0, 0.5, 0.5]
    chosen_mood = random.choices(mood, weights=pos2, k=1)[0]
    if chosen_mood == "Good":
        pos3 = [0.4, 0.4, 0.2]
    elif chosen_mood == "Moderate":
        pos3 = [0.2, 0.4, 0.4]
    else:
        pos3 = [0, 0.4, 0.6]
    co_behavior.append(random.choices(act, weights=pos3, k=1)[0])

for i in make_up:
    print(i)
print("-------------------------------------------")


# for i in co_behavior:
#   print(i)
def starting_b():
    startb = {'Sunny': 0, 'Cloudy': 0, 'Rainy': 0}
    for w in weather:
        startb[w] = math.log(starting_p[w], 10)
    return startb


def calculateAccuracy(a, b):
    if len(a) != len(b):
        raise ValueError("input should have same length")
    i = 0
    correct = 0
    while i < len(a):
        i = i + 1
        if a[i] == b[i]:
            correct += 1
    return correct / i
