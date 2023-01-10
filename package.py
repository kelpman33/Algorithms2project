import csv
import hashMap

# Hash table instance
packageHash = hashMap.ChainingHashTable()

# Package list for each truck
truck1Packages = []
truck2Packages = []
truck3Packages = []

# Hub ID of location of each truck
truck1Hub = 1
truck2Hub = 1
truck3Hub = 1

# Total distance traveled for each truck
truck1Distance = 0.0
truck2Distance = 0.0
truck3Distance = 0.0

# Total combined truck distance traveled
allTrucksDistance = 0.0

# Times the trucks leave the main hub
truck1Departure = '8:00:00'
truck2Departure = '9:05:00'
truck3Departure = '10:20:00'

# Class for package object containing all package variable types
class Package:
    def __init__(self, ID, address, deadline, city, zip, weight, status, truck):
        self.ID = ID
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip = zip
        self.weight = weight
        self.status = status
        self.truck = truck

    def __str__(self):  # overwite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.deadline, self.city, self.zip, self.weight, self.status, self.truck)

    # Getters
    def getID(self):
        return self.ID
    def getAddress(self):
        return self.address
    def getDeadline(self):
        return self.deadline
    def getCity(self):
        return self.city
    def getZip(self):
        return self.zip
    def getWeight(self):
        return self.weight
    def getStatus(self):
        return self.status
    def getTruck(self):
        return self.truck

    # Setters
    def setStatus(self, newStatus):
        self.status = newStatus
    def setZip(self, newZip):
        self.zip = newZip
    def setAddress(self, newAddress):
        self.address = newAddress
    def setID(self, newID):
        self.ID = newID
    def setTruck(self, newTruck):
        self.truck = newTruck
    def setWeight(self, newWeight):
        self.weight = newWeight
    def setCity(self, newCity):
        self.city = newCity
    def setDeadline(self, newDeadline):
        self.deadline = newDeadline

# Reads Package data from csv
with open('data/WGUPS Package File.csv') as WGUPS_Packages:
    packageData = csv.reader(WGUPS_Packages, delimiter=',')

    # Time Complexity: O(n^2)
    for package in packageData:
        pID = int(package[0])
        pAddress = package[1]
        pDeadline = package[5]
        pCity = package[2]
        pZip = package[4]
        pWeight = package[6]
        pStatus = "At the Hub"
        pTruck = package[7]

        # Corrects mislabeled package #9
        if 'Wrong address listed' in package[8]:
            pAddress = '410 S State St'
            pZip = '84111'

        # Inserts each package into hash list
        p = Package(pID, pAddress, pDeadline, pCity, pZip, pWeight, pStatus, pTruck)
        packageHash.insert(pID, p)

        # Creates truck lists and inserts corresponding packages
        if '1' in pTruck:
            truck1Packages.append(package)
        if '2' in pTruck:
            truck2Packages.append(package)
        if '3' in pTruck:
            truck3Packages.append(package)