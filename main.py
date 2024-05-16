# Body Mass Index (BMI) from a user's weight and height.

# Ask for 1st input: enter the height in meters
height = input("Enter your height in meters: ")

# Ask for 2nd input: enter the weight in kg
weight = input("Enter your weight in kg: ")

# Convert the height to a float
height_as_float = float(height)

# Convert the weight to a integer
weight_as_int = int(weight)

# Caclulate the BMI
bmi = weight_as_int / (height_as_float * height_as_float)

# Convert the BMI to a integer
bmi_as_int = int(bmi)

# Print the integer BMI
print(bmi_as_int)
