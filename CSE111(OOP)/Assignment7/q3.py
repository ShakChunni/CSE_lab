# question3
from datetime import date


class Dates:
    def __init__(self, n1):
        self.date = n1

    def getDate(self):
        return self.date

    @classmethod
    def toDashDate(cls, n1):
        cls.date = n1.replace('/', '-')
        object = Dates(cls.date)
        return object


date1 = Dates("05-09-2020")
dateFromDB = "05/09/2020"
date2 = Dates.toDashDate(dateFromDB)
if (date1.getDate() == date2.getDate()):
    print("Equal")
else:
    print("Unequal")
print("4. It shows equal because the string in both date1 and date2 are same.")
