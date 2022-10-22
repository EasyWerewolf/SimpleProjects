def celsius_to_fahrenheit():
    
    city = input('Enter the name of the city you are visiting: ')
    cels = input(('Enter a temp in degrees Celsius: '))

    print('The temperature in ' + city + ' is likely to be:')
    print('Celsius\t\tFahrenheit')
    
    temp = range(int(cels), int(cels) + 10)
    tbl = []
    tbl2 = []

    if int(cels) <= 15:
        for i in temp:
            cel = i - 9
            tbl.append(cel)
            fah = ((i - 9) * 9/5) + 32
            tbl2.append(fah)
            print(str(cel), "\t\t ", str(fah))
    elif int(cels) >= 16:
        for i in temp:
            cel = i
            tbl.append(cel)
            fah = (i * 9/5) + 32
            tbl2.append(fah)
            print(str(cel), "\t\t ", str(fah))
        
celsius_to_fahrenheit()