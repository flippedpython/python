def main():

    ages = [32,56,18,34,12,16,17]

    print('There are ',len(ages),' items in the list')

    ageTotal = 0.0
    
    for age in ages:
        ageTotal += age

    print('Age Total ',ageTotal)
    print('Average age is ',ageTotal/len(ages))
    

main()
