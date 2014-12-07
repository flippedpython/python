def main():
    appName = 'Smoking App'
    doctorsSay = 'On average 11 minutes of life is lost for ech cigarette'
    print(appName+doctorsSay)
    
    yearsSmoking = 0
    while (yearsSmoking < 1 or yearsSmoking > 40):
        yearsSmoking = int(input("enter years smoking 1 to 40? "))

    cigs = 0
    while (cigs < 1 or cigs > 100):
        cigs = int(input("enter daily intake? "))

    daysLost = cigs * 11 * 365 * yearsSmoking / (60 * 24)

    print('You have lost ' + str(daysLost) + ' from you life')


if __name__ == '__main__':
    main()

