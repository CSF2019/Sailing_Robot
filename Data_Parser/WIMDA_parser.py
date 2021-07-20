


def wimda_parser(data):
    getdata = data.split(",")
    global wind_direction
    wind_direction = getdata[13]+'°'
    global wind_speed
    wind_speed = getdata[17]+'kn'
    global wind_speed2
    wind_speed2 = getdata[19]+'m/s'







def getwind_direction(data):
    wimda_parser(data)
    print(wind_direction+'\n')
    return wind_direction



def getwind_speed(data):
    wimda_parser(data)
    print(wind_speed+'\n')
    return wind_speed


def getwind_speed2(data):
    wimda_parser(data)
    print(wind_speed2+'\n')
    return wind_speed2


if __name__ == '__main__':
    str="$WIMDA,29.6865,I,1.0053,B,27.0,C,,,56.1,,17.4,C,,,,,,,,*77"
    getwind_direction(str)
    getwind_speed(str)
    getwind_speed2(str)