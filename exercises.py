# Exercise 1: Calculate Area of a Triangle
def calculate_area_triangle(base, height):
    return (base * height) / 2


print("Exercise 1:", calculate_area_triangle(10, 5))
print("Exercise 1:", calculate_area_triangle(7, 3))


# Exercise 2: Calculate Simple Interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


print("Exercise 2:", simple_interest(1000, 5, 2))


# Exercise 3: Apply a Discount
def apply_discount(price, discount):
    return price - (price * (discount / 100))


print("Exercise 3:", apply_discount(100, 25))


# Exercise 4: Convert Temperature
def convert_temperature(temperature, unit):
    if unit.lower() == "c":
        return (temperature * 9 / 5) + 32
    elif unit.lower() == "f":
        return (temperature - 32) * 5 / 9.0


print("Exercise 4: Convert 0°C to Fahrenheit:", convert_temperature(0, "C"))
print("Exercise 4: Convert 32°F to Celsius:", convert_temperature(32, "F"))


# Exercise 5: Sum to N
def sum_to(n):
    return n * (n + 1) / 2


print("Exercise 5:", sum_to(10))


# Exercise 6: Find the Largest Number
def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c


print("Exercise 6:", largest(1, 2, 3))


# Exercise 7: Calculate a Tip
def calculate_tip(bill, tip):
    return bill * (tip / 100)


print("Exercise 7:", calculate_tip(50, 20))


# Exercise 8: Calculate Product of Numbers
def product(num1, num2, *nums):
    pNum = num1 * num2

    for num in nums:
        pNum = pNum * num

    return pNum


print("Exercise 8:", product(2, 5, 5))


# Exercise 9: Basic Calculator
def basicCalculator(num1, num2, operation):
    # ..I tryed to put (num1, num2, **kwargs) ,but it didn't work.. for now this works
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2


print("Exercise 9 Result:", basicCalculator(10, 5, "add"))
