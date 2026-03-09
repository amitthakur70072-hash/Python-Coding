units_consumed = int(input("Enter units consumed: "))

if units_consumed > 0 and units_consumed <= 100:
    print(units_consumed * 1.5)

elif units_consumed >= 101 and units_consumed <= 200:
    print((100 * 1.5) + (units_consumed - 100) * 2.5)

elif units_consumed >= 201 and units_consumed <= 300:
    print((100 * 1.5) + (100 * 2.5) + (units_consumed - 200) * 4)

elif units_consumed >= 301:
    print((100 * 1.5) + (100 * 2.5) + (100 * 4) + (units_consumed - 300) * 6)

else:
    print("Invalid entry")
