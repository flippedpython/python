def main():

    ages = [12,45,34,67,12,7,39,49,17]

    totalAge = calculateTotal(ages)
    averageAge = calculateAverageAge(ages)

    print('Total Age is ',totalAge)
    print('Average Age is ',averageAge)

    print('There are %d items in the list' % len(ages))
    
def calculateTotal(someList):
    total = 0
    for num in someList:
        total += num

    return total

def calculateAverageAge(someList):
    t = calculateTotal(someList)
    return t/len(someList)

main()

        
