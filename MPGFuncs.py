def calculate_miles_per_gallon(miles_driven, gallons):
    mpg = miles_driven / gallons
    mpg = round(mpg, 1)
    return mpg

def input_validate_miles():
    miles_driven = float(input("Enter miles traveled? "))
    while (miles_driven <= 0):

        print("Miles cannot be less than or = zero - pls enter a positive non-zero value")
        miles_driven = float(input("Enter miles traveled? "))

    return miles_driven

def input_validate_gallons():
    gallons = float(input("Enter gallons used? "))

    while (gallons <= 0):
        print("Gallons cannot be less than or equal to zero! please enter a positive non-zero value")
        gallons = float(input("Enter gallons used? "))
    return gallons

miles_driven = input_validate_miles()

# if miles_driven == 0:
#     print("Miles cannot be 0!")
#else: # miles are valid
gallons = input_validate_gallons()
print("MPG: ", calculate_miles_per_gallon(miles_driven,gallons ))