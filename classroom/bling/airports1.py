def main():

    airports = ['LAX','DBX','IST','DEL']

    port = input('Enter desination airport: ')

    while port not in airports:
        print('NOT available')
        port = input('Enter desination airport: ')
        
    print('Available')
        
main()
