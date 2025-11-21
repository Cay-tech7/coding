# This program is a simple simulation of a random walk in 2D space.
# It starts at the origin (0,0) and takes a series of steps in random
# directions (up, down, left, right). The final position after all steps
# I don't recall learning, but I researched and implemented a way to visualize the path taken using matplotlib.
# is printed to the console.

import random
import matplotlib.pyplot as plt 

def random_walk(steps):
    x,y = 0,0 #starting position
    path = [(x, y)] # list to store each position
    directions = ["up", "down", "left", "right"]

    for _ in range(steps): #take 'steps' number of steps
        move = random.choice(directions) #randomly choose a direction
        if move == "up":
            y += 1
        elif move == "down":
            y -= 1
        elif move == "left":
            x -= 1
        elif move == "right":
            x += 1
        path.append((x,y)) #append new position to path

    # Plot the path (I couldn't find anything on modules explaiing this concept so I looked it up myself, and had some help from AI to teach me how to do it)
    xs, ys = zip(*path) #unzip path into x and y coordinates
    plt.plot(xs, ys, marker='o', linestyle='-') #plot the path with markers
    plt.title("Random Walk Path") #set title
    plt.xlabel("X") #label x-axis
    plt.ylabel("Y") #label y-axis
    plt.grid(True) #enable grid
    plt.axis('equal')  # Keep aspect ratio square
    plt.show() #display the plot
    
    print(f"Final destination: ({x},{y})") #print final position
    return x,y 
        
if __name__ == "__main__":
    steps = 100 #number of steps in the random walk
    random_walk(steps) #call the random_walk function
