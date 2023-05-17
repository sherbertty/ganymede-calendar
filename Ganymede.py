import datetime
# Code writen by Sherbert
# Astronomy aided by SuperZtar64 
# To use, input an earth date after the discovery of the moon.
# Repr to get out YY-MM-DD HH:MM:SS  

class Sol:
    'Parent Class of Moons'

    def __init__(self,year = 0 , month = 1,day = 1, hour = 0, min = 0, sec =0):
        self.earthTime = datetime.datetime(year,month,day,hour,min,sec)
    
    def printEarthDay(self):
        print(self.earthTime)

class Ganymede(Sol):
    "Moon Ganymede"
    
    def __init__(self,year = 0 , month = 1,day = 1, hour = 0, min = 0, sec =0):
        self.earthTime = datetime.datetime(year,month,day,hour,min,sec)
        self.timeSinceStart = self.earthTime - datetime.datetime(1610, 1, 7, 0, 0, 0, 0)
        self.totalCercads = self.timeSinceStart / datetime.timedelta(hours=21.49916)
        self.year = self.findYear(self.totalCercads)
        self.month = self.currentMonth(self.totalCercadsInYear)
        self.day = self.currentDay(self.month,self.totalCercadsInYear)
        self.findHourMinSec()
        self.day = int(self.day)

    def isShortYear(self,year):
        for y in range(1, year//28 + 1):
            x = (year - 28*y) // 400
            if 400*x + 28*y == year:
                return True
        return False
    
    def findYear(self,totalCercads):
        year = 1
        while totalCercads > 400:
            if self.isShortYear(year):
                totalCercads -= 400
                year += 1
            elif(totalCercads > 408):
                totalCercads -= 408
                year += 1
        self.totalCercadsInYear = totalCercads
        return year

    def currentMonth(self,totalCercadsInYear):
        month = 1
        cercad = totalCercadsInYear
        while (cercad > 32 and month != 7):
            cercad -= 32
            month += 1
        if (month == 7 and cercad <= 24):
            return month
        elif(cercad >= 24 and month >= 6):
            month +=1
            cercad -= 24
        while(cercad > 32):
            cercad -= 32
            month += 1
        return month
    
    def currentDay(self,month,totalCercadsInYear):
        if month <= 7:
            return (totalCercadsInYear - ((month - 1) *32))
        elif month > 7:
            return (totalCercadsInYear - ((month - 2) *32) - 24)


    def findHourMinSec(self):
        particalCercad = self.totalCercadsInYear - int(self.totalCercadsInYear)
        self.hour = (particalCercad * 21.49916)
        self.minute = (self.hour - int(self.hour)) * 60
        self.second = (self.minute - int(self.minute)) * 60
        self.hour = int(self.hour)
        self.minute = int(self.minute)
        self.second = int(self.second) 
         
    def __repr__(self):
        return f'''{self.year}-{self.month}-{self.day} {self.hour}:{self.minute}:{self.second}'''


print('-------------------------') #Ganymede Tests
x = Ganymede(2000,6,1)
print(x)
x = Ganymede(2000,7,1)
print(x)
x = Ganymede(2000,7,17)
print(x)
x = Ganymede(1800,1,1)
print(x)
x = Ganymede(2001,12,28)
print(x)
x = Ganymede(2002,1,4)
print(x)
x = Ganymede(2002,1,1)
print(x)
print('-------------------------')
