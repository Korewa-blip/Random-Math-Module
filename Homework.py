import math

print("Trigonometric Angle Finder")
print("---------------------------")
print("1. Find angle using sine (sin⁻¹)")
print("2. Find angle using cosine (cos⁻¹)")
print("3. Find angle using tangent (tan⁻¹)")

choice = input("Enter your choice (1/2/3): ")

# Ask the user for the trig value
value = float(input("Enter the trigonometric value (between -1 and 1 for sin/cos): "))

if choice == '1':
    angle_rad = math.asin(value)  # Inverse sine
elif choice == '2':
    angle_rad = math.acos(value)  # Inverse cosine
elif choice == '3':
    angle_rad = math.atan(value)  # Inverse tangent
else:
    print("Invalid choice.")
    exit()

# Convert from radians to degrees
angle_deg = math.degrees(angle_rad)

print(f"The angle is approximately {angle_deg:.2f} degrees.")
