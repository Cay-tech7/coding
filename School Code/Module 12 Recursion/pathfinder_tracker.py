# this code simulates the movements of three seperate astronauts (Lance, sophie, adn finn)
#It visualizes each of their paths on a grid based on a series of movement commands.
#It will then output their paths as a png file. 

import matplotlib.pyplot as plt
import random

# Lance: random in all directions
def lance_path(steps=500): # simulate Lance's random path
    x, y = 0, 0 # starting at origin
    path_x, path_y = [x], [y] # lists to store path coordinates
    moves = ['U', 'D', 'L', 'R'] # possible moves
    for _ in range(steps): # simulate each step
        step = random.choice(moves) # choose a random move
        if step == 'U': y += 1 
        elif step == 'D': y -= 1
        elif step == 'L': x -= 1
        elif step == 'R': x += 1
        path_x.append(x) # append new x coordinate
        path_y.append(y) # append new y coordinate
    return path_x, path_y 

# Sophie: prefers Up (50%), others 16.67%
def sophie_path(steps=500):
    x, y = 0, 0
    path_x, path_y = [x], [y]
    moves = ['U', 'D', 'L', 'R']
    weights = [0.5, 0.1667, 0.1667, 0.1667] # weights for each direction
    for _ in range(steps):
        step = random.choices(moves, weights)[0] # choose move based on weights
        if step == 'U': y += 1
        elif step == 'D': y -= 1
        elif step == 'L': x -= 1
        elif step == 'R': x += 1
        path_x.append(x)
        path_y.append(y)
    return path_x, path_y

# Finn: only Left or Right
def finn_path(steps=500):
    x, y = 0, 0
    path_x, path_y = [x], [y] 
    moves = ['L', 'R'] # possible moves
    for _ in range(steps):
        step = random.choice(moves)
        if step == 'L': x -= 1
        elif step == 'R': x += 1
        path_x.append(x)
        path_y.append(y)
    return path_x, path_y

def main():
    steps = 500 # number of steps for each astronaut
    # Lance 
    lance_x, lance_y = lance_path(steps) # simulate Lance's path
    plt.figure(figsize=(8, 8)) # create a new figure
    plt.plot(lance_x, lance_y, 'bo-', markersize=3, label='Lance (Blue Circle)') # plot Lance's path
    plt.title("Lance's Spacewalk") # title of the plot
    plt.xlabel('X Coordinate') # x label
    plt.ylabel('Y Coordinate') # y label
    plt.legend() # show legend
    plt.grid(True) # show grid
    plt.savefig('Lance_spacewalk.png') # save the plot as a png file
    plt.close()

    # Sophie
    sophie_x, sophie_y = sophie_path(steps)
    plt.figure(figsize=(8, 8))
    plt.plot(sophie_x, sophie_y, 'rs-', markersize=3, label='Sophie (Red Square)')
    plt.title("Sophie's Spacewalk")
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid(True)
    plt.savefig('Sophie_spacewalk.png')
    plt.close()

    # Finn
    finn_x, finn_y = finn_path(steps)
    plt.figure(figsize=(8, 8))
    plt.plot(finn_x, finn_y, 'g^-', markersize=3, label='Finn (Green Triangle)')
    plt.title("Finn's Spacewalk")
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.legend()
    plt.grid(True)
    plt.savefig('Finn_spacewalk.png')
    plt.close()

if __name__ == "__main__":
    main() # run the main function