
# A list of houses as, for example, provided by MLS
MLS_list = [
['436','perth','semi-detatched',900,1,3,2,1200,0,'east',100,2100,479900],
['115','perth','semi-detatched',1100,2,3,2,1800,1,'west',100,3500,699900],
['516','perth','detatched',800,1,1,1,2600,2,'east',100,2000,498900,],
['194','manning','semi-detatched',900,1,2,2,1400,0,'west',50,4000,649880],
['288','perth','detatched',1300,3,5,3,2000,1,'west',100,3200,699000],
['753','shaw','semi-detatched',1200,2,3,4,2200,1,'east',100,4500,899000],
['152','palmerston','semi-detatched',1100,2,4,3,1800,1,'west',100,4300,799000],
['179','perth','detatched',1100,2,3,2,2200,1,'west',50,2800,699000],
['295','clinton','semi-detatched',1300,3,5,3,2000,1,'east',100,4600,899000],
['189','clinton','semi-detatched',1250,2,3,2,2100,0,'west',80,4200,849900],
['277','clinton','detatched',1100,1,2,2,2200,2,'east',50,4800,949800],
['264','clinton','detatched',1300,2,3,2,1800,0,'east',100,4400,799900],
['265','clinton','detatched',1100,1,2,1,1800,0,'west',100,4300,790000],
['517','delaware','semi-detatched',1200,2,3,1,2100,2,'east',80,3200,699900],
['713','euclid','semi-detatched',1100,3,3,2,1500,0,'west',70,4100,749000],
['808','shaw','detatched',1300,3,3,2,1700,1,'east',100,3500,929000],
['488','delaware','detatched',1100,1,2,2,1900,1,'west',80,3400,849000],
['308','delaware','semi-detatched',1100,2,3,3,1200,1,'east',100,2600,599000],
['332','delaware','semi-detatched',1000,3,5,2,1400,1,'west',80,3300,799000],
['17','mansfield','semi-detatched',900,2,3,2,1300,0,'north',50,3500,699000],
['13','mansfield','semi-detatched',1300,2,3,2,1300,0,'north',50,3800,899000]]

#write a program to allow the user to input a list of streets and see all the houses for sale on those streets

#ask for inputs like "Enter a street name (type exit when done): "
#outputs a list of all the houses on each street with the format:
# Address: XXX XXXX Size: XXX Price: $ XXX

def searchHouses():
    streets = []
    #takes the user input for all the streets to look for
    while True:
        resp = input("Enter a street name (type exit when done): ").lower()
        if resp == 'exit':
            break
        elif resp not in streets:
            streets.append(resp)
    #prints out the houses on each streets specified
    #if the street exists:
    for street in streets:
        print("Houses on {}:".format(street.title()))        
        if any(MLS_list[x][1] == street for x in range(len(MLS_list))):
            for x in range(len(MLS_list)):
                if MLS_list[x][1] == street:
                    print("Address: {0} {1}, Size: {3} Price: ${11}.".format(*MLS_list[x])) #have to use the '*' operator to unpack the list                   
                        
        else:
            print("No houses on {}.".format(street))
                
if __name__ == "__main__":
    searchHouses()
        
        
        
        
        