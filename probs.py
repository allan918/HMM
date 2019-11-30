import random
import numpy as np

weather_mood = {
    "Sunny":
        {
            "Good": 0.7,
            "Moderate": 0.2,
            "Bad": 0.1
        },

    "Cloudy":
        {
            "Good": 0.4,
            "Moderate": 0.4,
            "Bad": 0.2},

    "Rainy":
        {
            "Good": 0.2,
            "Moderate": 0.4,
            "Bad": 0.4
        },

    "Storm":
        {"Good": 0,
         "Moderate": 0.2,
         "Bad": 0.8}

}

weather_weather = {
    "Sunny": {
        "Sunny": 0.5,
        "Cloudy": 0.3,
        "Rainy": 0.15,
        "Storm": 0.05
    },
    "Cloudy": {
        "Sunny": 0.15,
        "Cloudy": 0.5,
        "Rainy": 0.25,
        "Storm": 0.1
    },
    "Rainy": {
        "Sunny": 0.15,
        "Cloudy": 0.3,
        "Rainy": 0.4,
        "Storm": 0.15
    },
    "Storm": {
        "Sunny": 0.05,
        "Cloudy": 0.2,
        "Rainy": 0.5,
        "Storm": 0.25
    }
}

weather_act = {
    "Good": {
        "Picnic": 0.4,
        "Exercise": 0.3,
        "Homework": 0.1,
        "Home": 0.2
    },
    "Moderate": {
        "Picnic": 0.1,
        "Exercise": 0.3,
        "Homework": 0.3,
        "Home": 0.3
    },
    "Bad": {
        "Picnic": 0,
        "Exercise": 0.2,
        "Homework": 0.3,
        "Home": 0.5
    }
}


def trans_probility(weather, weather2):
    return weather_weather[weather][weather2]


def find_weather_mood_prob(weather, mood):
    return weather_mood[weather][mood]


def find_mood_behavior(mood, act):
    return weather_act[mood][act]


make_up = []
make_up.append("Sunny")
weather = ["Sunny", "Cloudy", "Rainy", "Storm"]

for x in range(999):
    last = make_up[len(make_up) - 1]
    if last == "Sunny":
        pos = [0.15, 0.5, 0.25, 0.1]
    elif last == "Cloudy":
        pos = [0.15, 0.5, 0.25, 0.1]
    elif last == "Rainy":
        pos = [0.15, 0.3, 0.4, 0.15]
    else:
        pos = [0.05, 0.2, 0.5, 0.25]
    make_up.append(random.choices(weather, weights=pos, k=1))
for i in make_up:
    print(i)
