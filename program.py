ap = {}

print("\nAirport Database")
print("1. Add a new airport")
print("2. Fetch airport information")
print("3. Quit")


ch = input("write your choice: ")

while ch != '3':
    if ch == '1':
        c = input("Enter the ICAO code: ")
        n = input("write airport name: ")
        ap[c] = n
        print(f"Airport {c} - {n} added successfully.")
    elif ch == '2':
        c = input("write the ICAO code of the airport to fetch information: ")
        print(f"The name of the airport with ICAO code {c} is {ap.get(c, 'not found')}.")
    else:
        print("Invalid choice.")

    ch = input("Enter your choice: ")

print("Exit program.")
