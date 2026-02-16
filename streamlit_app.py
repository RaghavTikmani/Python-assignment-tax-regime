
print("Unemployment status checjer")
print(" ")
age = int(input("Enter your age: "))
education = input("Enter your education level: ")
if age < 15 or age > 59:
    status = "Not in Labour Force"
else:
    worked = input("Did you work during the reference period? (Yes/No): ")
    if worked.lower() == "yes":
        status = "Employed"
    else:
        seeking = input("Are you actively seeking a job? (Yes/No): ")
        available = input("Are you available for work? (Yes/No): ")

        if seeking.lower() == "yes" and available.lower() == "yes":
            status = "Unemployed"
        else:
            status = "Not in Labour Force"
print("Result")
print("Age:", age)
print("Education:", education)
print("Employment Status:", status)
