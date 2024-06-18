def sum_of_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total

number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))
