import datetime
  
class Date: 
    def __init__(self, d, m, y): 
        self.d = d 
        self.m = m 
        self.y = y 
  
    # To store number of days in 
    # all months from January to Dec. 
    monthDays = [31, 28, 31, 30, 31, 30, 
                31, 31, 30, 31, 30, 31] 
    
    def countLeapYears(self): 
        years = self.y 
        # Check if the current year needs to be considered for the count of leap years or not
        if (self.m <= 2): 
            years -= 1
    
        # An year is a leap year if it is a multiple of 4, multiple of 400 and not a multiple of 100
        ans = int(years / 4) 
        ans -= int(years / 100) 
        ans += int(years / 400) 
        return ans 

    
    def days_since_ever(self):
        # COUNT TOTAL NUMBER OF DAYS BEFORE FIRST DATE 'dt1' 
        # initialize count using years and day 
        n1 = self.y * 365 + self.d 
  
        # Add days for months in given date 
        for i in range(0, self.m - 1): 
            n1 += self.monthDays[i] 
  
        # Since every leap year is of 366 days, add a day for every leap year
        n1 += self.countLeapYears() 
        return n1
    
# This function returns number of 
# days between two given dates 
  
  
# Driver Code 
if __name__ == "__main__":
    dt1 = Date(1, 9, 2014) 
    dt2 = Date(28, 9, 2014) 
    zero_time = Date(0,0,0)
    days_count1 = dt1.days_since_ever()
    days_count2 = dt2.days_since_ever()
    diff = abs(days_count1 - days_count2)
    print(f"Difference between two dates is {diff}")

# print(f"First date ")
# year = int(input('Enter a year: '))
# month = int(input('Enter a month: '))
# day = int(input('Enter a day: '))
# date1 = Date(year, month, day)
# d1 = datetime.datetime(year, month, day)

# print(f"Second date ")
# year = int(input('Enter a year: '))
# month = int(input('Enter a month: '))
# day = int(input('Enter a day: '))
# date2 = Date(year, month, day)
# d2 = datetime.datetime(year, month, day)
 
# Function call 
# print(f"Diff between {d1.date()} and {d2.date()} is {getDifference(date1, date2)} days")
# print(f"{getDifference(zero_time, date1)} days passed since 0") 