# import json

# data = {
#     "new_york" : [
#         {"name" : "10XLarge", "cost" : 2820},
#         {"name" : "8XLarge", "cost" : 1400},
#         {"name" : "4XLarge", "cost" : 774},
#         {"name" : "2XLarge", "cost" : 450},
#         {"name" : "XLarge", "cost" : 230},
#         {"name" : "Large", "cost" : 120}
#     ],
#     "india" : [
#         {"name" : "10XLarge", "cost" : 2970},
#         {"name" : "8XLarge", "cost" : 1300},
#         {"name" : "4XLarge", "cost" : 890},
#         {"name" : "2XLarge", "cost" : 413},
#         {"name" : "Large", "cost" : 140}
#     ],
#     "china" : [
#         {"name" : "8XLarge", "cost" : 1180},
#         {"name" : "4XLarge", "cost" : 670},
#         {"name" : "XLarge", "cost" : 200},
#         {"name" : "Large", "cost" : 110}
#     ]

# }



new_york = {
    "10XLarge" : 2820,
    "8XLarge" : 1400,
    "4XLarge" : 774,
    "2XLarge" : 450,
    "XLarge" : 230,
    "Large" : 120
    }

india = {
    "10XLarge" : 2970,
    "8XLarge" : 1300,
    "4XLarge" : 890,
    "2XLarge" : 413,
    "Large" : 140
    }

china = {
    "8XLarge" : 1180,
    "4XLarge" : 670,
    "XLarge" : 200,
    "Large" : 110
    }

capacity = {
    "10XLarge" : 320,
    "8XLarge" : 160,
    "4XLarge" : 80,
    "2XLarge" : 40,
    "XLarge" : 20,
    "Large" : 10
    }

region = [new_york, india, china]

hours = input("Enter no. of hours\n")

units = (int)(input("Enter required units\n"))

for reg in region:

    print(region.index(reg))

    machine_combinations = [] #Lists different sets of machines that could work for the given input.

    machines = reg.keys() #Creates a list of machines available for each region.
    equipment_cost = []
    for i in reg.values():
        equipment_cost.append(i)
    capacity_levels = []

    for machine in machines:

        capacity_levels.append(capacity[machine]) #Creates a capacity array in corespondence to the "machines" list.
 
    capacity_levels.sort(reverse=True)
    units_copy = units
    for level in capacity_levels: #Iterates over the capacity levels.
        combination = []
        for cap in capacity_levels[capacity_levels.index(level)::]: #Nested iteration to list out different combinations of machines
            if(units < cap): #Checks if current unit requirement is less than machine capacity. 
                continue
            else:
                count = (int)(units_copy/cap) #Stores the floor quotient (or the number of machines required from the current capacity iteration.)

                units_copy = units_copy%cap #Stores the remainder units.

                combination.append(count) #Appends machine count to combination set.
        units_copy = units
        machine_combinations.append(combination) #Appends all combinations of a particular region.
    costing = []
    for combination in machine_combinations: #Iterates over different sets.
        equipment_cost2 = equipment_cost[machine_combinations.index(combination)::] #Slices the cost list so as to match with the combination length
        sum = 0 #sum variable
        x = 0 #iterator variable
        for count in combination: #Iterates over each machine count.
                cost = count*equipment_cost2[x] #Multiplies machine count with respective costs.
                sum += cost #Aggregate sum of all machine cost thus giving cost of each combination.
                x += 1
        costing.append(sum)
    optimum_cost = min(costing)
    print({region.index(reg) : optimum_cost})