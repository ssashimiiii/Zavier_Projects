#Tan Jun Yu Zavier S10255651D P09

# Part 1 - This part reads the data from 'carpark-information.csv'.
list_of_dict = []
carpark_list = []
information_list = []
f1 = open('carpark-information.csv', 'r')
lines = f1.readlines()
title = lines[0].strip().split(',')
for line in lines[1:]:
    data = line.strip().split(',', 3)
    data[3] = data[3].strip('"')
    dictionary = {}
    for i in range(len(title)):
        dictionary[title[i]] = data[i]
    list_of_dict.append(dictionary)
    carpark_list.append(data[0])
    information_list.append(data[1:])
f1.close()
# End of Part 1

# Part 2 - This part will display the total number of carparks in 'carpark-information.csv'.
def total_no_carparks():
    print("Option 1: Display Total Number of Carparks in 'carpark-information_list'")
    print("Total Number of carparks in 'carpark-information.csv':{}.".format(len(list_of_dict)))
# End of Part 2

# Part 3 - This part will display all the basement carparks in 'carpark-information.csv'.
count = 0
def all_basement_carpark():
    global count
    print("Option 2: Display All Basement Carparks in 'carpark-information.csv'")
    print('Carpark No Carpark Type       Address')
    for i, info in enumerate(information_list):
        if info[0] == 'BASEMENT CAR PARK':
            count += 1
            print('{:<10} {:<18} {}'.format(carpark_list[i], info[0], info[2]))
    print('Total number: {}'.format(count))
# End of part 3

# Part 4 - This part will read the data from carpark-availability file the user puts in.
def read_carpark_availability():
    print("Option 3: Read Carpark Availability Data File")
    file_name = input("Enter the filename for carpark availability data (e.g., carpark-availability-v1.csv): ")
    try:
        f2 = open(file_name, 'r')
    except FileNotFoundError:
        print("File not found. Please make sure the file exists in the current directory.")
        return [], []

    global carpark_no, carpark_availability
    carpark_no = []
    carpark_availability = []
    timestamp = f2.readline().strip()
    print("Timestamp:", timestamp)
    f2.readline()  # Skip the header line
    for line1 in f2:
        data = line1.strip().split(',')
        carpark_no.append(data[0])
        carpark_availability.append(data[1])
    f2.close()
    return carpark_no, carpark_availability
# End of Part 4

# Part 5 - This part will print the total no of carparks in carpark availability data file
def display_carpark_count():
    if carpark_availability:
        print("Option 4: Print Total Number of Carparks in the File Read in [3]")
        print('Total Number of Carparks in the File: {}'.format(len(carpark_no)))
    else:
        print('You may only continue after option 3 is done!')
# End of Part 5

# Part 6 - This part displays the carparks without available lots
def display_carparks_without_available_lots():
    global count
    if carpark_availability:
        print('Option 5: Display Carparks without Available lots')
        count = 0
        for i in range(len(carpark_availability)):
            if len(carpark_availability[i]) >= 2 and carpark_availability[i][1] == '0':
                count += 1
                print('Carpark Number: {}'.format(carpark_no[i]))
        print('Total number: {}'.format(count))
    else:
        print('You may only continue after option 3 is done!')
# End of Part 6

# Part 7 - This part displays carpark with at least x% available lots.
def min_available_lots():
    global count
    if carpark_availability:
        print('Option 6: Display Carparks With At Least x% Available Lots')
        try:
            percentage_input = int(input('Enter the percentage required: '))
        except ValueError:
            print('Please enter a valid integer!')
            return min_available_lots()

        if percentage_input < 0 or percentage_input > 100:
            print('Please enter an integer between 0 and 100 (inclusive)')
            return min_available_lots()

        print('Carpark No  Total Lots  Lots Available  Percentage')
        count = 0
        for i in range(len(carpark_availability)):
            if len(carpark_availability[i]) >= 2 and carpark_availability[i][1] != '0':
                total_lots = float(carpark_availability[i][0])
                available_lots = float(carpark_availability[i][1])
                percentage = (available_lots / total_lots) * 100
                if percentage >= percentage_input:
                    count += 1
                    print('{:<10} {:<12} {:<15} {:.2f}%'.format(carpark_no[i], int(total_lots), int(available_lots),
                                                                percentage))
        print('Total number: {}'.format(count))
    else:
        print('You may only continue after option 3 is done!')
# End of Part 7

# Part 8 - This part displays the addresses of carparks with at least x% available lots.
def add_of_carpark_with_min_lots():
    global count
    if carpark_availability:
        print('Option 7: Display Addresses of Carparks With At Least x% Available Lots')
        try:
            percentage_input = int(input('Enter the percentage required: '))
        except ValueError:
            print('Please enter a valid integer')
            return add_of_carpark_with_min_lots()

        if percentage_input < 0 or percentage_input > 100:
            print('Please enter an integer between 0 and 100 (inclusive)')
            return add_of_carpark_with_min_lots()

        print('{:10} {:10} {:14} {:10} {:7}'.format('Carpark No', 'Total Lots', 'Lots Available', 'Percentage', 'Address'))
        count = 0
        for i in range(len(carpark_availability)):
            if len(carpark_availability[i]) >= 2 and carpark_availability[i][1] != '0':
                total_lots = float(carpark_availability[i][0])
                available_lots = float(carpark_availability[i][1])
                percentage = (available_lots / total_lots) * 100
                if percentage >= percentage_input:
                    count += 1
                    print('{:<10} {:>10} {:>14} {:>10.1f} {:<7}'.format(carpark_no[i], carpark_availability[i][0],
                                                                        carpark_availability[i][1], percentage,
                                                                        information_list[i][2]))
        print('Total Number: {}'.format(count))
    else:
        print('You may only continue after option 3 is done!')
# End of Part 8

# Advanced Feature - Part 9 - Display All Carparks at Given Location
option_3_done = False  # Global variable to track if Option 3 has been executed

def display_carparks_at_location():
    global count
    if option_3_done:
        print('Option 8: Display All Carparks at Given Location')
        location_input = input("Enter the location: ").upper()
        count = 0

        print('{:10} {:18} {:18} {}'.format('Carpark No', 'Carpark Type', 'Type of Parking System', 'Address'))
        for carpark in list_of_dict:
            if carpark['Address'].upper().find(location_input) != -1:
                carpark_no = carpark['Carpark Number']
                carpark_type = carpark['Carpark Type']
                parking_system = carpark['Type of Parking System']
                address = carpark['Address']
                print('{:<10} {:<18} {:<18} {}'.format(carpark_no, carpark_type, parking_system, address))
                count += 1

        if count == 0:
            print('No carpark found at the given location.')
        else:
            print('Total Number of Carparks found at the given location: {}'.format(count))
    else:
        print('Please read carpark availability data file first by selecting Option 3!')

# End of Part 9

# Advanced Feature - Part 10 - Display Carpark with the Most Parking Lots
def display_carpark_with_most_lots():
    global carpark_no, carpark_availability
    if carpark_availability:
        print("Option 9: Display Carpark with the Most Parking Lots")

        most_lots = 0
        carpark_with_most_lots = []

        for i in range(len(carpark_availability)):
            total_lots = int(carpark_availability[i][0])
            if total_lots > most_lots:
                most_lots = total_lots
                carpark_with_most_lots = [carpark_no[i]]
            elif total_lots == most_lots:
                carpark_with_most_lots.append(carpark_no[i])

        if carpark_with_most_lots:
            print("Carpark with the Most Parking Lots:")
            for carpark_number in carpark_with_most_lots:
                print("Carpark Number: {}".format(carpark_number))
                for carpark in list_of_dict:
                    if carpark.get('CARPARK NO') == carpark_number:
                        print("Carpark Type: {}".format(carpark.get('CARPARK TYPE', '')))
                        print("Type of Parking System: {}".format(carpark.get('TYPE OF PARKING SYSTEM', '')))
                        print("Address: {}".format(carpark.get('ADDRESS', '')))
                        print()  # Adding a blank line for readability between each carpark
                        break
        else:
            print("No carpark information available.")
    else:
        print('You may only continue after option 3 is done!')
# End of Part 10

# Main Part - This part is to display the menu
def display_menu():
    global option_3_done
    while True:
        print('Menu')
        print('====')
        print("[1] Display Total Number of Carparks in 'carpark-information.csv'")
        print("[2] Display All Basement Carparks in 'carpark-information.csv'")
        print('[3] Read Carpark Availability Data File')
        print('[4] Print Total Number of Carparks in the File Read in [3]')
        print('[5] Display Carparks Without Available Lots')
        print('[6] Display Carparks With At Least x% Available Lots')
        print('[7] Display Addresses of Carparks With At Least x% Available Lots')
        print('[8] Display All Carparks at Given Location')
        print('[0] Exit')
        try:
            option = int(input('Enter your option: '))
        except ValueError:
            print('Please enter a valid integer.')
            continue
        else:
            if option < 0 or option > 9:
                print('Please enter an integer within 0 and 9')
                continue
            if option == 1:
                total_no_carparks()
            elif option == 2:
                all_basement_carpark()
            elif option == 3:
                carpark_no, carpark_availability = read_carpark_availability()
                option_3_done = True
            elif option == 4:
                display_carpark_count()
            elif option == 5:
                display_carparks_without_available_lots()
            elif option == 6:
                min_available_lots()
            elif option == 7:
                add_of_carpark_with_min_lots()
            elif option == 8:
                display_carparks_at_location()
            elif option == 9:
                display_carpark_with_most_lots()
            elif option == 0:
                print('Exiting the program. Thank you!')
                break

# Call the main function to start the program.
display_menu()











