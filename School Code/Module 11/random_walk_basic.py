# This program is a simple simmulation of a random walk in 2D space.
# It starts at the origin (0,0) and takes a series of steps in random
# directions (up, down, left, right). The final position after all steps
# is printed to the console.

import random
import matplotlib.pyplot as plt

def random_walk(steps):
    x,y = 0,0 #starting position
    path = [(x, y)] # list to stroe each position
    directions = ["up", "down", "left", "right"]

    for _ in range(steps):
        move = random.choice(directions)
        if move == "up":
            y += 1
        elif move == "down":
            y -= 1
        elif move == "left":
            x -= 1
        elif move == "right":
            x += 1
        path.append((x,y))

    # Plot the path
    xs, ys = zip(*path)
    plt.plot(xs, ys, marker='o', linestyle='-')
    plt.title("Random Walk Path")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.axis('equal')  # Keep aspect ratio square
    plt.show()
    
    print(f"Final destination: ({x},{y})")
    return x,y
        
if __name__ == "__main__":
    steps = 100
    random_walk(steps)
