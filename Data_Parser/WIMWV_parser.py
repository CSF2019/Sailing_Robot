
class wind_tp:
    def __init__(self,type) -> None:
        if type == 'T':
            self.tp = 'True wind '
        else:
            self.tp = 'Relative wind '



class wind_ut:
    def __init__(self,unit) -> None:
        if unit == 'K':
            self.ut = 'km/h'
        elif unit == 'M':
            self.ut = 'm/s'
        elif unit == 'N':
            self.ut = 'kn'
        elif unit == 's':
            self.ut = 'mile/h'
        else:
            self.ut = ''


def wimwv_parser(data):
    getdata = data.split(",")
    global wind_type
    wind_type = wind_tp(getdata[2])
    global wind_direction
    wind_direction = wind_type.tp+getdata[1]+'°'
    global wind_unit
    wind_unit = wind_ut(getdata[4])
    global wind_speed
    wind_speed = wind_type.tp+getdata[3]+wind_unit.ut




def getwind_direction(data):
    wimwv_parser(data)
    print(wind_direction+'\n')
    return wind_direction


def getwind_speed(data):
    wimwv_parser(data)
    print(wind_speed+'\n')
    return wind_speed


if __name__ == '__main__':
    str="$WIMWV,,T,,,V*7C"
    getwind_direction(str)
    getwind_speed(str)
