a = int(input("Enter a number: "))
series = [2*i + 1 for i in range(a)]
print("Output:", ", ".join(map(str, series)))
