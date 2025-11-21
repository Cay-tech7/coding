#helper functions
def name(name):
    print(f"Hello, {name}!")
    age(25) #calling a global function

def age(age): # this function is global
    print(f"You are {age} years old.")

#inner function
def favorite_color(color):
    def color_message(): # Inner function which is only accessible within favorite_color
        return f"Your favorite color is {color}."
    return color_message()

if __name__ == "__main__":
    names = "Cayden"
    name(names)

    color = "Green"
    print(favorite_color(color))