def main():
    
    yearsSmoking = float(input("enter years smoking 1 to 40? "))
    
    cigsPerDay = float(input("enter daily intake? "))

    minutesDeleted = minutesLost(cigsPerDay, yearsSmoking)
    daysDeleted = daysLost(cigsPerDay,yearsSmoking)

    printSummary(cigsPerDay,yearsSmoking, minutesDeleted, daysDeleted)

def minutesLost(cigs, years):
    minutes = cigs * 365 * 11 * years
    return minutes

def daysLost(cigs, years):
    days = cigs * 11 * 365 * years / (60 * 24)
    return days

def printSummary(cigs, years, minutes, days):
    print('Smoking ',cigs,' per day for ',years,'years')
    print('You have lost ',minutes,' minutes from your life')
    print('or ',days,' days')

main()





