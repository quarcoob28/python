def zeller(day, month, year):

    if (month >= 1 and month <=2 ):
        A = month +10
        corrected_year = year - 1


    elif (month >= 3 and month <=12):
        A = month - 2
        corrected_year = year


    year_to_cList = list(str(corrected_year))

    yearOfCentury = year_to_cList[2] + year_to_cList[3]


    current_century = year_to_cList[0] + year_to_cList[1]

    B = day
    C = int(yearOfCentury)
    D = int(current_century)

    W = (13 * int(A) - 1) / 5
    X = C/ 4
    Y = D / 4

    Z = int(W) + int(X) + int(Y) + (B) + (C) - 2 * (D)
    R = int(Z) % 7

    days = { 0 : "Sunday", 1 : "Monday", 2 : "Tuesday" , 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday" }

    return days[R]


print (zeller (16,3,1990))
