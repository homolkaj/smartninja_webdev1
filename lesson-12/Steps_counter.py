# Homework 12.3 - Steps counter
#
# Create a function that will calculate the number of steps that you make for a certain distance.
#
#     Inputs:
#         The distance walked
#         The length of your step
#     Output:
#         The number of steps made

def calc(dist_walk, length_of_steps):
    x = int(dist_walk/length_of_steps)
    return x

print(calc(100, 0.5))