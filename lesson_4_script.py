def salary():
    try:
        hours, cash_per_hour, extra_cash = map(float, argv[1:])
        print(f" Salary = {time * rate + bonus}")
    except ValueError:
        print("Enter all 3 numbers -- not str etc")

salary()