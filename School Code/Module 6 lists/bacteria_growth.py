#This code is a model of how bacteria mulitpy over time with a fixed growth rate.

current_population = int(input("Enter a starting population: "))  # Initial number of bacteria
hourly_growth_rate = float(input("Enter the hourly growth rate (as a decimal): "))  # Growth rate per hour
hours = int(input("Enter the number of hours to simulate: "))  # Total hours to simulate

population_history = []  # List to store population at each hour
population_history.append(current_population)  # Record initial population

for hour in range(hours):  # Loop through each hour
    current_population = current_population * (hourly_growth_rate)  # Update population based on growth rate
    population_history.append(current_population)  # Record population for the current hour

print("Hour\tPopulation")  # Print header
for hour, population in enumerate(population_history):  # Loop through recorded populations
    print(f"{hour}\t{population:.2f}")  # Print hour and population formatted to 2 decimal places
