class cur_time:
    def __init__(self,hh,mm,ss):
        self.t=hh+':'+mm+':'+ss


class cur_latitude:
    def __init__(self,NS,dd,mm):
        if NS=='N':
            ns='north latitude '
        else:
            ns='south latitude '
        self.la=ns+dd+'.'+mm


class cur_longitude:

    def __init__(self,EW,ddd,mm) -> None:
        if EW=='E':
            ew='east longitude '
        else:
            ew='west longitude '
        self.lo=ew+ddd+'.'+mm



def gprmc_parser(data):
    getdata = data.split(",")
    global time
    time = cur_time(getdata[1][0:2], getdata[1][2:4], getdata[1][4:6])
    global latitude
    latitude = cur_latitude(getdata[4], getdata[3][0:2], getdata[3][2:4])
    global longitude
    longitude = cur_longitude(getdata[6], getdata[5][0:3], getdata[5][3:5])
    global speed
    speed = getdata[7]+'kn'
    global angle
    angle = getdata[8]+'°'



def gettime(data):
    gprmc_parser(data)
    print(time.t + '\n')
    return time


def getlatitude(data):
    gprmc_parser(data)
    print(latitude.la + '\n')
    return latitude


def getlongitude(data):
    gprmc_parser(data)
    print(longitude.lo + '\n')
    return longitude


def getspeed(data):
    gprmc_parser(data)
    print(speed+'\n')
    return speed


def getangle(data):
    gprmc_parser(data)
    print(angle+'\n')
    return angle


if __name__ == '__main__':
    str="$GPRMC,024813.640,A,3158.4608,N,11848.3737,E,10.05,324.27,150706,,,A*50"
    gettime(str)
    getlatitude(str)
    getlongitude(str)
    getspeed(str)
    getangle(str)

