import datetime

class Time:
    def __init__(self):
        currentTime = datetime.datetime.now()
        self.__h = currentTime.hour
        self.__m = currentTime.minute
        self.__s = currentTime.second

    def getHour(self):
        return self.__h

    def getMinute(self):
        return self.__m

    def getSecond(self):
        return self.__s

    def setTime(self, elapsedTime):
        totalSeconds = elapsedTime % (24 * 3600)
        self.__h = totalSeconds // 3600
        self.__m = (totalSeconds % 3600) // 60
        self.__s = totalSeconds % 60

timeOb = Time()
print(f"Current Time: {timeOb.getHour()}:{timeOb.getMinute()}:{timeOb.getSecond()}")
elapsed_time = int(input("Enter elapsed time in seconds: "))

timeOb.setTime(elapsed_time)
print(f"Updated Time: {timeOb.getHour()}:{timeOb.getMinute()}:{timeOb.getSecond()}")

