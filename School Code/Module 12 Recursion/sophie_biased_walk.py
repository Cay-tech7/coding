import random #helps with random choices for direction and weights

# define movement directions and how they change coordinates
up = (0, 1) 
down = (0, -1)
left = (-1, 0)
right = (1, 0)

def sophie_biased_walk(steps=200):
    location = (0, 0)  # starting at origin
    counts = {"up":0, "down":0, "left":0, "right":0} # initialize direction counts

    directions = [up, down, left, right]  # possible movement directions
    labels = ["up", "down", "left", "right"]  # string labels
    weights = [50, 16.67, 16.67, 16.67]  # corresponding weights

    for _ in range(steps):  # simulate each step
        move, label = random.choices(list(zip(directions, labels)), weights=weights)[0] # choose direction based on weights by zipping directions and labels together
        location = (location[0] + move[0], location[1] + move[1])  # update location
        counts[label] += 1 # increment the count for the chosen direction
    return location, counts

if __name__ == "__main__":
    final_location, counts = sophie_biased_walk()
    print(f"Final position: {final_location}")
    print("Direction counts:")
    for direction, count in counts.items(): # print each direction and its count
        print(f"{direction}: {count}") 
