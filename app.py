# 1. As a valued customer at the Bank of Honolulu, you make a deposit of $1000. Your savings account balance prior to the deposit has an amount of $8000. Calculate the new savings account balance. Print the new savings account balance and concatenate the dollar sign.

original_balance = 8000
deposit = 1000
def add(num1, num2):
    return num1 + num2
add(original_balance, deposit)
new_balance = add(original_balance, deposit)
print("$" + str(new_balance))


# 2.You need to pay taxes on the $500 cash prize that you won to the IRS ( The tax rate is 30%). Calculate the tax amount and subtract this from your savings balance. Print the updated savings account balance and concatenate the dollar sign.

cash_prize = 500
tax = 0.3
def subtract(num1, num2, num3):
    return num1 - num2 * num3
subtract(new_balance, cash_prize, tax)
taxed_total = subtract(new_balance, cash_prize, tax)
print("$" + str(taxed_total))


# 3. The savings account accrues an annual interest rate of 2%. Calculate the interest earned for the first quarter of 2018, using the original account balance from Question 1. Print the interst earned in the first quarter and concatenate the dollar sign.

interest = .2
def multiply(num1, num2):
    return num1 * num2 
multiply(original_balance, interest)
interest_earned = multiply(original_balance, interest)
print("$" + str(interest_earned))


# 4. Function add
# Create a function that will take two parameters named num1 and num2. This function will add two numbers. Print your result.

french_fries = 6
additional_fries = 4
def addition(num1, num2):
    return num1 + num2
addition(french_fries, additional_fries)
new_fry_amount = addition(french_fries, additional_fries)
print(new_fry_amount)


# 5. Function subtract
# Create a function that will take two parameters named num1 and num2. This function will subtract two numbers. Print your result.

reeses_cups = 4
eaten_cups = 4
def subtraction(num1, num2):
        return num1 - num2
subtraction(reeses_cups, eaten_cups)
new_reeses_amount = subtraction(reeses_cups, eaten_cups)
print(new_reeses_amount)

# 6. Function add-then-subtract
# Create a function that will take in three parameters named num1, num2 and num3. The function will sum up the first two parameters (num1 and num2) and subtract it from the third parameter (num3). Please use your previous functions (i.e. add or subtract) for this exercise. Print your result.

stripping_tips = 1500
coin_jar = 1000
truck_payment = 615
def subtract2(num1, num2, num3):
    return num1 + num2 - num3
subtract2(stripping_tips, coin_jar, truck_payment)
remaining_balance = subtract2(stripping_tips, coin_jar, truck_payment)
print("$" + str(remaining_balance))

# 7. Function shoe size
#  Create a function that will take in a parameter named inches. This function will convert inches to centimeters(cm). Print your result. 

inches = 9
def shoe_size(inches):
    return inches * 2.54
size_in_cm = shoe_size(9) * 2.54
print(str(size_in_cm) - ' cm')

# 8. Create a function that will take in a parameter named cel. The function will convert Celsius into Fahrenheit. Print your result.

# 9. Function all caps
#  Create a function that will take in a parameter named str. This function will capitalize all the letters in the string. Print your result. 

# 10. Function one cap
#  Create a function that will take in a parameter named str. The function will capitalize only the first letter in the string. Print your result.

# 11. Use the extend method to combine the following lists together. Print your result.

east_side = ['Biggie', 'Nas', 'Wu-Tang Clan']
west_side = ['Tupac', 'Dre', 'Snoop']

# 12. Use the clear method to remove all items from the following list. If you are using Python 2 or 3.2, use the del operator instead. Print your result.

haters = ['Keyshia Cole', 'Wendy Williams', '50 Cent', 'Lil Kim']












