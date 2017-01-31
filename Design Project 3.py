#determine the state of alert (green, yellow, orange, red) and trigger the appropriate safety measures.
#Green: Normal conditions
#Yellow: Earthquake [4, 6], Electrical Grid Offline, Temperature (301-500 C), Low radiation leak
#Orange: Earthquake (6, 8.5], High Water, High Radiation Leak, Temperature (501-1000 C), Tsunami (0-5)m
#Red: Earthquake >8.5, Explosion, Low Water, Temperature >1000 C, Tsunami >=5m

#For solutions and appropriate responses, follow the task tree.

status = "Green Conditions."

#conditions:
#Earthquake, Electrical Grid, Temperature, Radiation Leak, Tsunami, Explosion, Water level

def getStatus(earthquake, temperature, tsunami, radiation, water, grid, explosion):
    global status
    if earthquake > 8.5 or explosion or water == 1 or temperature > 1000 or tsunami >= 5.0:
        status = "Red Alert!"
    elif earthquake > 6 or water == 2 or radiation == 2 or temperature > 500 or tsunami > 0.0:
        status = "Orange Alert!"
    elif earthquake >= 4 or grid == False or radiation == 1 or temperature > 300:
        status = "Yellow Alert!"
    else:
        status = "Green Conditions."
    return status


earthquake = 0.0 #richter scale
temp = 100 #degrees celsuis
tsunami = 0.0 #height in meters
radiation = 0 #none, low, high(0/1/2)
water = 2 #none, low, high(0/1/2)
isGridOn = True #is the electrical grid on
isExplosion = False

print(getStatus(earthquake, temp, tsunami, radiation, water, isGridOn, isExplosion))

#Part 2: the correct response
#multiple responses are available: 
#Insert Neurton absorbing rods, Inject boron neturon absorber, Turn on condensors (only if grid is on or back up is on. Backup can only be on if there is NOT high water), Evacuate non-critical personnel, Dump seawater into reactor, Evacuate region surrounding plant

def correctResponse():
    status = input("What is the power plant status? (g/y/o/r) ").lower()
    if status == "g":
        print("Maintain normal operation.")
    if status == "o" or status == "r":
        status = "y"        
    if status == "y":
        print("Insert the neutron absorbing rods!")
        resp = input("Is the temperature below 300 degrees and decreasing? (y/n) ").lower()
        if resp == "y":
            print("Wait for Green status.")
        elif resp == "n":
            print("Orange Alert!")
            status = "o2"
    if status == "o2":
        print("Inject Boron!")
        resp = input("Is the temperature below 300 degrees and decreasing? (y/n) ").lower()
        if resp == "y":
            print("Wait for Green status.")
        if resp == "n":
            isGrid = input("Is the electrical grid on? (y/n) ")
            if isGrid == "y":
                print("Turn on condensors!")
                resp = input("Is the temperature below 300 degrees and decreasing? (y/n) ").lower()
                if resp == "y":
                    print("Wait for Green status.")
                if resp == "n":
                    status = "r2"
            if isGrid == "n":
                isBackup = input("Is the backup power working? (y/n) ")
                if isBackup == "y":
                    print("Turn on condensors!")
                    resp = input("Is the temperature below 300 degrees and decreasing? (y/n) ").lower()
                    if resp == "y":
                        print("Wait for Green status.")
                    if resp == "n":
                        status = "r2"
                if isBackup == "n":
                    status = "r2"
    if status == "r2":
        print("Evacuate non-critical personnel!\nAirlift emergency response personnel robots and backup power generators!\nDump Seawater into the reactor!")
        resp = input("Is the temperature below 300 degrees and decreasing? (y/n) ").lower()
        if resp == "y":
            print("Maintain temperature and Containment until the reactor can be decommissioned.")
        if resp == "n":
            print("Evacuate the region immediately!")
        