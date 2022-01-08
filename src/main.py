import json

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
locations = ['New York', 'India', 'China']

user_input = (str)(input("\n"))
data = [int(s) for s in user_input.split() if s.isdigit()]

hours = 0
units = 0

for d in data:
    if(data.index(d)==0):
        units = d
    else:
        hours = d

output = []

for reg in region:

    machine_combinations = [] #Lists different sets of machines that could work for the given input.
    machines = []
    for i in reg.keys(): #Creates a list of machines available for each region.
        machines.append(i)

    equipment_cost = []
    for i in reg.values():
        equipment_cost.append(i)
    
    capacity_levels = [] #Outer scope set for machine capacities
    machine_set = [] #Outer scope set to extract machine combination for each region.
    cost_table=[] #Outer scope set to extract costings of each combination for each region

    for machine in machines:

        capacity_levels.append(capacity[machine]) #Creates a capacity array in corespondence to the "machines" list.
 
    capacity_levels.sort(reverse=True)
    units_copy = units
    for level in capacity_levels: #Iterates over the capacity levels.
        combination = []
        for cap in capacity_levels[capacity_levels.index(level)::]: #Nested iteration to list out different combinations of machines
            if(units < cap): #Checks if current unit requirement is less than machine capacity. 
                combination.append(0)
            else:
                count = (int)(units_copy/cap) #Stores the floor quotient (or the number of machines required from the current capacity iteration.)

                units_copy = units_copy%cap #Stores the remainder units.

                combination.append(count) #Appends machine count to combination set.
        units_copy = units
        machine_combinations.append(combination) #Appends all combinations of a particular region.
        machine_set.append(combination) #Appends to global set.
    costing = []
    for combination in machine_combinations: #Iterates over different sets.
        equipment_cost2 = equipment_cost[machine_combinations.index(combination)::] #Slices the cost list so as to match with the combination length
        sum = 0 #sum variable
        x = 0 #iterator variable
        for count in combination: #Iterates over each machine count.
                cost = count*equipment_cost2[x] #Multiplies machine count with respective costs.
                sum += cost #Aggregate sum of all machine cost thus giving total cost of each combination.
                x += 1
        costing.append(sum)
        cost_table.append(sum) #Appends to global set.
    print(cost_table)
    print(machine_set)
    optimum_cost = min(costing) #Finds the least cost.
    machine_cost = []
    if optimum_cost in cost_table:
        optimum_set = machine_set[cost_table.index(optimum_cost)] #Finds the combination with the optimum_cost.
        for combinations in machine_set:
            x = 0
            machines2 = machines[machine_set.index(combinations)::] #Slices machines list with each iteration
            if (optimum_set == combinations): #Filters out unnecessary sets.
                for i in combinations: #This if-else block appends a tuple of (machine_type, count) format as well as removes any null count.
                    if(i != 0):
                        machine_cost.append((machines2[x], i))
                        x += 1
                    else:
                        x += 1
                        continue
    optimum_cost = hours*(int)(optimum_cost)
    output.append({
        "region" : locations[region.index(reg)],
        "total_cost" : "$"+(str)(optimum_cost),        #Preparing output
        "machines" : machine_cost
    })
final_output = {
    "Output" : output                                  #Final output
}            

print(json.dumps(final_output, indent=2))