ans = input("If you want to use our data, enter 'Y' or 'y', enter anything else, you will generate your own data with prompt")
list = []
if not (ans == "Y" or ans == "y"):
    while True:
        val = input("Please enter 0 represents Sunny, 1 represents Rainy, 2 represents Cloudy, other to finish\n")
        if val == "0":
            list.append("Sunny")
        elif val == "1":
            list.append('Rainy')
        elif val == "2":
            list.append('Cloudy')
        else:
            break
    for i in list:
        print(i)
else:
    print("here")
