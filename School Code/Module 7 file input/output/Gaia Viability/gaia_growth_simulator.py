#This program determines if Gaia-4 is capable of supporting human life. 
#This is the Gaia Viability Estimator - a simulation tool based on logistic growth model.
#I kept getting messed up  with the argv in the if __name__ == "__main__": block so I got a suggestion from AI to move it to a main function so that it could take arguments properly.
"""
Take input from the command line
Simulate population growth over a number of steps
Write the results to a file in a readable format
"""
import sys

# Compute the next population value using the logistic equation: Pn = r * P_{n-1} * (1 - P_{n-1})
def next_population(prev_population, growth_rate):
    return growth_rate * prev_population * (1 - prev_population)

# Run the simulation and return the list of populations (one value per time step)
def gaia_viability_estimator(initial_population, growth_rate, simulation_steps):
    populations = [initial_population]
    for step in range(1, simulation_steps):
        next_pop = next_population(populations[-1], growth_rate)
        populations.append(next_pop)
    return populations

def main(argv=None):
    """Parse command-line args, validate, run simulation, and write results."""
    if argv is None:
        argv = sys.argv
    if len(argv) != 5:
        print("Usage: python gaia_growth_simulator.py <initial_population> <growth_rate> <steps> <output_filename>")
        print("Example: python gaia_growth_simulator.py 0.01 2.5 100 results.txt")
        sys.exit(1)

    try:
        initial_population = float(argv[1])
        growth_rate = float(argv[2])
        simulation_steps = int(argv[3])
        output_filename = argv[4]
    except ValueError:
        print("Error: initial_population and growth_rate must be numbers; steps must be an integer.")
        sys.exit(1)

    # Validate ranges
    if not (0 < initial_population < 1):
        print("Error: initial_population must be > 0 and < 1.")
        sys.exit(1)
    if not (0 < growth_rate < 4):
        print("Error: growth_rate must be > 0 and < 4.")
        sys.exit(1)
    if simulation_steps <= 0:
        print("Error: steps must be a positive integer.")
        sys.exit(1)
    if not output_filename:
        print("Error: output filename must be provided.")
        sys.exit(1)

    populations = gaia_viability_estimator(initial_population, growth_rate, simulation_steps)

    # Write results to specified output file
    with open(output_filename, "w") as f:
        f.write("Step\tPopulation\n")
        for step, pop in enumerate(populations):
            f.write(f"{step}\t\t{pop:.3f}\n")

    print(f"Simulation complete. Results saved to {output_filename}")


if __name__ == "__main__":
    main()
