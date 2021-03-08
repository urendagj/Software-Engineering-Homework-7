def Leapyear(year):
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        else:
            return False