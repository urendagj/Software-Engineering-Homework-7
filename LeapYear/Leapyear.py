def Leapyear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    #if year is not divisible by 100
    if year % 4 == 0:
        return True
    return False