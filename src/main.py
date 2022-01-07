new_york = {
    "Large" : 120, 
    "XLarge" : 230, 
    "2XLarge" : 450, 
    "4XLarge" : 774, 
    "8XLarge" : 1400, 
    "10XLarge" : 2820
    }

india = {
    "Large" : 140, 
    "2XLarge" : 413, 
    "4XLarge" : 890, 
    "8XLarge" : 1300, 
    "10XLarge" : 2970
    }

china = {
    "Large" : 110,
    "XLarge" : 200, 
    "4XLarge" : 670, 
    "8XLarge" : 1180
    }

capacity = {
    "Large" : 10, 
    "XLarge" : 20, 
    "2XLarge" : 40, 
    "4XLarge" : 80, 
    "8XLarge" : 160, 
    "10XLarge" : 320
    }

region = [new_york, india, china]

hours = input("Enter no. of hours\n")

units = (int)(input("Enter required units\n"))

for reg in region:

    print(region.index(reg))

    machines = reg.keys() #Creates a list of machines available for each region.

    capacity_levels = []

    for machine in machines:

        capacity_levels.append(capacity[machine]) #Creates a capacity array in corespondence to the "machines" list.
 
    capacity_levels.sort(reverse=True)
    list3 = capacity_levels
    units_copy = units
    for level in capacity_levels: #Iterates over the capacity levels.
        list2 = []
        for cap in capacity_levels[capacity_levels.index(level)::]: #Nested iteration to list out different combinations of machines
            if(units < cap): #Checks if current unit requirement is less than machine capacity. 
                continue
            else:
                val = (int)(units_copy/cap) #Stores the floor quotient (or the number of machines required from the current capacity iteration.)

                units_copy = units_copy%cap #Stores the remainder units.

                list2.append({val : cap}) #Appends 
        units_copy = units
        print(list2)