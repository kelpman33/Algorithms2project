# Author: James Badke
# Student ID: 001280972
import package
from distance import runTruck

class Main:

    # This message displays upon program startup
    print('-------------------------------------------------------------------------------')
    print('                            WGUPS Delivery Program                             ')
    print('-------------------------------------------------------------------------------')

    # Prompts user for input
    userInput = input("""
Please select an option below to begin or type 'quit' to quit:
    1. Get info for all packages at a given time.
    2. Get info for a single package at a given time.
""")

    # Quits program
    if userInput == 'quit':
        print('Quitting program.')
        exit()

    while userInput != 'quit':

        # Selects option 1
        if userInput == '1':

            # Get user inputted time
            inputTime = input('Enter a time (HH:MM:SS): ')

            if inputTime == '' or inputTime == 'EOD':
                print('Using default EOD: 17:00:00')
                inputTime = '17:00:00'

            # Simulate deliveries for each truck
            try:
                runTruck(1, package.truck1Packages, package.truck1Hub, package.truck1Distance, package.truck1Departure, inputTime)
                print()
                runTruck(2, package.truck2Packages, package.truck2Hub, package.truck2Distance, package.truck2Departure, inputTime)
                print()
                runTruck(3, package.truck3Packages, package.truck3Hub, package.truck3Distance, package.truck3Departure, inputTime)
            except:
                print('Invalid entry. Quitting program.')
                exit()

            print()
            print('All packages at ' + str(inputTime))
            for i in range(len(package.packageHash.table)):
                print("Package: {}".format(package.packageHash.search(i + 1)))
            print()
            print('Total distance traveled by all trucks: ' + str(round(package.allTrucksDistance, 1)) + " miles.")

            exit()

        # Selects option 2
        elif userInput == '2':

            # Get user inputted ID and time
            packageID = input('Enter a valid package ID: ')
            inputTime = input('Enter a time (HH:MM:SS): ')

            if inputTime == '' or inputTime == 'EOD':
                print('Using default EOD: 17:00:00')
                inputTime = '17:00:00'

            # Simulate deliveries for each truck
            try:
                runTruck(1, package.truck1Packages, package.truck1Hub, package.truck1Distance, package.truck1Departure, inputTime)
                print()
                runTruck(2, package.truck2Packages, package.truck2Hub, package.truck2Distance, package.truck2Departure, inputTime)
                print()
                runTruck(3, package.truck3Packages, package.truck3Hub, package.truck3Distance, package.truck3Departure, inputTime)
            except:
                print('Invalid entry. Quitting program.')
                exit()

            print()
            print('Package ' + str(package.packageHash.search(int(packageID))) + ', at ' + str(inputTime))
            print()
            print('Total distance traveled by all trucks: ' + str(round(package.allTrucksDistance, 1)) + " miles.")
            exit()

        # If invalid input, display this message and end program
        else:
            print('Invalid entry. Quitting program.')
            exit()