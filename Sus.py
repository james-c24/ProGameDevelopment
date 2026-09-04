import random

crewmates = []


for i in range(10):
    crewmates.append("crewmate" + str(i))

impostor = random.choice(crewmates)

print("Crewmates:", crewmates)
print("The Impostor is:", impostor)


# Recursive function to find the Impostor
def find_impostor(crewmates, impostor, index):

    # Base case: we've checked everyone
    if index >= len(crewmates):
        return -1

    
    if crewmates[index] == impostor:
        return index

 
    return find_impostor(crewmates, impostor, index + 1)


# Start searching from index 0
result = find_impostor(crewmates, impostor, 0)

print(" Impostor found at index:", result)
