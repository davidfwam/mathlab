import random
from random import randint

### this is for addition section-easy
numberone = randint(0, 10)
numbertwo = randint(0, 10)

n1 = str(numberone)
n2 = str(numbertwo)

print n1 + "+" + n2 + "="
user_sum = raw_input("Enter sum here:")
sumofrandint = numberone + numbertwo
usersum = int(user_sum)
if sumofrandint == usersum:
    print 'Congrats! Your answer is correct.'

else:
    finalsum = str(sumofrandint)
    print 'Sorry. The correct answer is ' + finalsum

### This is for addition-medium

import random
from random import randint

numberthree = randint(10, 50)
numberfour = randint(10, 50)

n3 = str(numberthree)
n4 = str(numberfour)

print n3 + "+" + n4 + "="
user_summed = raw_input("Enter sum here:")
sumofrandintmed = numberthree + numberfour
usersummed = int(user_summed)
if sumofrandintmed == usersummed:
    print 'Congrats! Your answer is correct.'

else:
    finalsummed = str(sumofrandintmed)
    print 'Sorry. The correct answer is ' + finalsummed

### This is for addition-hard

import random
from random import randint

numberfive = randint(50, 1000)
numbersix = randint(50, 1000)

n5 = str(numberfive)
n6 = str(numbersix)

print n5 + "+" + n6 + "="
user_sumhard = raw_input("Enter sum here:")
sumofrandinthard = numberfive + numbersix
usersumhard = int(user_sumhard)
if sumofrandinthard == usersumhard:
    print 'Congrats! Your answer is correct.'

else:
    finalsumhard = str(sumofrandinthard)
    print 'Sorry. The correct answer is ' + finalsumhard
### This is for multiplication-easy

import random
from random import randint

numberseven = randint(0, 10)
numbereight = randint(0, 10)

n7 = str(numberseven)
n8 = str(numbereight)

print n7 + "*" + n8 + "="
user_product = raw_input("Enter product here:")
product = numberseven * numbereight
userproduct = int(user_product)
if product == userproduct:
    print 'Congrats! Your answer is correct.'

else:
    finalproduct = str(product)
    print 'Sorry. The correct answer is ' + finalproduct

### This is for multiplication-medium

import random
from random import randint

numbernine = randint(10, 50)
numberten = randint(10, 50)

n9 = str(numbernine)
n10 = str(numberten)

print n9 + "*" + n10 + "="
user_productmed = raw_input("Enter product here:")
productmed = numbernine * numberten
userproductmed = int(user_productmed)
if productmed == userproductmed:
    print 'Congrats! Your answer is correct.'

else:
    finalproductmed = str(productmed)
    print 'Sorry. The correct answer is ' + finalproductmed

### This is for multiplication-hard

import random
from random import randint

numbera = randint(50, 1000)
numberb = randint(50, 1000)

na = str(numbera)
nb = str(numberb)

print na + "*" + nb + "="
user_producthard = raw_input("Enter product here:")
producthard = numbera * numberb
userproducthard = int(user_producthard)
if producthard == userproducthard:
    print 'Congrats! Your answer is correct.'

else:
    finalproducthard = str(producthard)
    print 'Sorry. The correct answer is ' + finalproducthard
