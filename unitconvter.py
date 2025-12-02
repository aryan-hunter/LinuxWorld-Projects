print("\n--- UNIT CONVERTER ---")

print("1. Km → Miles")
print("2. Miles → Km")
print("3. Celsius → Fahrenheit")
print("4. Fahrenheit → Celsius")

ch = input("Choose option: ")
n = float(input("Enter value: "))

if ch == "1":
    print(f"{n} km = {n*0.621:.2f} miles")

elif ch == "2":
    print(f"{n} miles = {n/0.621:.2f} km")

elif ch == "3":
    print(f"{n}°C = {(n*1.8)+32:.1f}°F")

elif ch == "4":
    print(f"{n}°F = {(n-32)/1.8:.1f}°C")

else:
    print("Invalid choice!")
