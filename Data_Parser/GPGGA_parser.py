


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


def gpgga_parser(data):
    getdata=data.split(",")
    global time
    time=cur_time(getdata[1][0:2],getdata[1][2:4],getdata[1][4:6])
    global latitude
    latitude=cur_latitude(getdata[3],getdata[2][0:2],getdata[2][2:4])
    global longitude
    longitude=cur_longitude(getdata[5],getdata[4][0:3],getdata[4][3:5])
    global GPS_status
    GPS_status=getdata[6]


def gettime(data):
    gpgga_parser(data)
    print(time.t+'\n')
    return time


def getlatitude(data):
    gpgga_parser(data)
    print(latitude.la+'\n')
    return latitude


def getlongitude(data):
    gpgga_parser(data)
    print(longitude.lo+'\n')
    return longitude


def getGPSstatus(data):
    gpgga_parser(data)
    print(GPS_status+'\n')
    return GPS_status


if __name__ == '__main__':
    str="$GPGGA,092204.999,4250.5589,S,14718.5084,E,1,04,24.4,19.7,M,,,0000*1F"
    gettime(str)
    getlatitude(str)
    getlongitude(str)
    getGPSstatus(str)
