#bank balance
balance = 10000

deposit = 5000
balance += deposit

print("After Deposit:", balance)

withdraw = 2000
balance -= withdraw

print("After Withdraw:" , balance)

#comparison operators
a = 10
b =20

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

#age eligibility checker
age = int(input("Enter your age:"))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#pass or fail checker
marks = int(input("Enter your marks:"))

print("Pass" if marks >= 35 else "Fail")


#loging validation
correct_username = "admin"
correct_password = "password123"

username = input("Enter your username:")
password = input("Enter your password:")

print("Login successful!" if username == correct_username and password == correct_password else "Invalid username or password.")
print("Login successful!" if username == correct_username and password == correct_password else "Invalid username or password.")


is_logged_in = True

print(not is_logged_in)

#atm eligility checker
balane = 10000
withdraw = 5000

print(withdraw > 0 and withdraw <= balance)

#student scholarship eligibility checker
marks = float(input("Enter your marks:"))
attendance = float(input("Enter your attendance percentage:"))

eligible = marks >= 85 and attendance >= 75

print("Eligible for scholarship:", eligible)

