def main():
    appName = 'Smoking App'
    doctorsSay = 'On average 11 minutes of life is lost for each cigarette'
    print(appName+doctorsSay)
    
    yearsSmoking = getYearsSmoking()
    cigsPerDay = getCigsPerDay();
    daysLost = calcDaysLost(yearsSmoking,cigsPerDay)

    print('Days Lost ',daysLost)
        
def getYearsSmoking():
    ys = 0
    while (ys < 1 or ys > 40):
        ys = int(input("enter years smoking 1 to 40? "))
    return ys

def getCigsPerDay():
    cig = 0
    while (cigs < 1 or cigs > 100):
        cigs = int(input("enter daily intake? "))
    return cigs

def calcDaysLost(ys, cigs):
    daysLost = cigs * 11 * 365 * ys / (60 * 24)
    return daysLost


if __name__ == '__main__':
    main()

