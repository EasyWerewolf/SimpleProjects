#open file
gcap = open('capitals.txt', 'rt')

#initializing states and capitals lists
states = []
capitals = []
count = 0

#for loop to create two lists
for line in gcap:
    if count % 2:
        capitals.append(line.strip())
    else:
        states.append(line.strip())
    count += 1

#create dictionary from two lists
chart = dict(zip(states, capitals))

#print result if state is found, loops back if invalid
def print_result():
    #gets user input for state
    input_state = input('Please enter a state:\n') 
    #initialize if statement
    if input_state.capitalize() in chart:
        print('The capitol of ' + input_state.capitalize() + ' is ' + chart[input_state.capitalize()])
    else:
        print('This state could not be found, Please try again')
        print_result()

print_result()
input()