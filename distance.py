import csv
import package
from package import packageHash
from datetime import datetime
from datetime import timedelta

# Create empty lists to hold corresponding information
distanceList = []
addressList = []

# Reads Distance data from csv
with open('data/WGUPS Distance Table.csv') as WGUPS_Distances:
    distanceData = csv.reader(WGUPS_Distances, delimiter=',')
    # Time Complexity: O(n)
    for row in distanceData:
        distanceList.append(row)

# Gets distance between hubs
# Time Complexity: O(1)
def getDistance(hub1ID, hub2ID):
    swapID = 0
    if hub1ID < hub2ID:
        swapID = hub1ID
        hub1ID = hub2ID
        hub2ID = swapID
    return float(distanceList[hub1ID-1][hub2ID+1])

# Creates list of all hub addresses
# Time Complexity: O(n)
def addAddresses():
    i = 0
    while i < len(distanceList):
        addressList.append(distanceList[i][1])
        i+=1

# Gets ID for address string
# Time Complexity: O(1)
def getAddressID(address):
    return addressList.index(address) + 1

# Time complexity O(n)
# Get ID of closest hub to given hub in given truck list
def getMinDistanceIDInList(hubID, truckList):
    truckDistances = []
    truckIDs = []
    i = 0
    for package in truckList:
        address = package[1]
        hubID2 = getAddressID(address)
        truckDistances.insert(i,getDistance(hubID, hubID2))
        truckIDs.insert(i, hubID2)
        i+=1
    return truckIDs[truckDistances.index(min(truckDistances))]

# Function for simulating truck delivery
# Time complexity: O(n)
def runTruck(truckNum, truckList, truckHub, truckDistance, truckDepartureTime, endTime):
    print('------------------------------------TRUCK ' + str(truckNum) + '------------------------------------')
    truckTime = datetime.strptime(truckDepartureTime, '%H:%M:%S')
    endTime = datetime.strptime(endTime, '%H:%M:%S')

    # First, set status of all packages in current truck to "in transit" upon delivery start
    if truckTime <= endTime:
        for p in truckList:
            packageID = truckList[truckList.index(p)][0]
            updatePackage = packageHash.search(int(packageID))
            updatePackage.setStatus("En route")
            packageHash.insert(packageID, updatePackage)

    # deliver each package in current truck, add time to starting time, and set package status to "delivered"
    for p in truckList:
        if truckTime <= endTime:
            packageID = truckList[truckList.index(p)][0]
            packageAddress = truckList[truckList.index(p)][1]
            addressID = addressList.index(packageAddress) + 1
            distanceToHub = getDistance(addressID, truckHub)
            truckHub = addressID
            updatePackage = packageHash.search(int(packageID))
            truckTime = truckTime + timedelta(hours=distanceToHub / 18)
            if truckTime <= endTime:
                truckDistance += distanceToHub
                updatePackage.setStatus("Delivered")
                packageHash.insert(packageID, updatePackage)
                print("Package " + str(packageID) + " has been delivered at: " + str(truckTime.strftime('%H:%M:%S')))
    package.allTrucksDistance += truckDistance
    print('------------------------------------TRUCK ' + str(truckNum) + '------------------------------------')

# Function for sorting truck packages for delivery
# Time complexity: O(n)
def sortPackageTrucks(truckList, truckHubID):

    # Empty list to contain final sorted truck list
    truckPackagesSorted = []

    # Lists with truck package attributes
    truckAddressIDs = []
    truckPackageAddresses = []
    truckPackageIDs = []
    truckPackageList = truckList.copy()

    # Get addresses and IDs for each package in the given list
    for p in truckList:
        address = p[1]
        ID = p[0]
        truckPackageAddresses.append(address)
        truckPackageIDs.append(ID)

    # Get the address IDs for each address in the truck packages
    for a in truckPackageAddresses:
        address = a
        truckAddressIDs.append(getAddressID(address))

    for p in truckList:
        closestHubID = getMinDistanceIDInList(truckHubID, truckPackageList)
        closestPackageID = truckPackageIDs[truckAddressIDs.index(closestHubID)]
        insertPackage = truckPackageList[truckPackageIDs.index(closestPackageID)]
        truckPackagesSorted.append(insertPackage)
        truckPackageList.pop(truckPackageIDs.index(closestPackageID))
        truckAddressIDs.pop(truckPackageIDs.index(closestPackageID))
        truckPackageIDs.pop(truckPackageIDs.index(closestPackageID))
        truckHubID = closestHubID

    return truckPackagesSorted

# Create list of all addresses
addAddresses()

# Optimize mileage by running sorting algorithm for each truck list
package.truck1Packages = sortPackageTrucks(package.truck1Packages, package.truck1Hub)
package.truck2Packages = sortPackageTrucks(package.truck2Packages, package.truck2Hub)
package.truck3Packages = sortPackageTrucks(package.truck3Packages, package.truck3Hub)