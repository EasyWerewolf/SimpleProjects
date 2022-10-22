import math

place_one = input('Enter a city: ')
place_two = input('Enter a store: ')
number = int(input('Enter a number: '))
animal = input('Enter an animal: ')
emotion = input('Enter an emotion: ')
random = input('Now enter the first random thing that comes to mind: ')

print('It was a hot summer day in ' + place_one + ',')
print('and I was on my way home from the ' + place_two + '.')
print("Looking up from my phone, I saw " + str(number) + " " + animal + "'s")
print('and they were multiplying.')
print('After a few seconds it doubled to ' + str(number*2) + '.')
print('After a while, there were ' + str(math.pow(number,2)) + " " + animal + "'s and I started to feel " + emotion + '.')
print('I sprinted back to ' + place_two + ' running in and out of traffic')
print('before I realized that it was just a ' + random + ' that I was running from.')
print('Oh right, I forgot my glasses today.')