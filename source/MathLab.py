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
### This is for subtraction-easy

numberz = randint(0, 10)
numbery = randint(0, 10)

nz = str(numberz)
ny = str(numbery)

if numberz >= numbery:
    print nz + "-" + ny + "="
    user_difference = raw_input("Enter answer here:")
    difference = numberz - numbery
    userdifference = int(user_difference)
    if userdifference == difference:
        print 'Congrats! Your answer is correct.'
    else:
        finaldifference = str(difference)
        print 'Sorry. The correct answer is ' + finaldifference
else:
    print ny + "-" + nz + "="
    user_difference = raw_input("Enter answer here:")
    difference = numbery - numberz
    userdifference = int(user_difference)
    if userdifference == difference:
        print 'Congrats! Your answer is correct.'
    else:
        finaldifference = str(difference)
        print 'Sorry. The correct answer is ' + finaldifference

### This is for subtraction-med

numbero = randint(10, 50)
numberp = randint(10, 50)

no = str(numbero)
np = str(numberp)

if numbero >= numberp:
    print no + "-" + np + "="
    user_differencemed = raw_input("Enter answer here:")
    differencemed = numbero - numberp
    userdifferencemed = int(user_differencemed)
    if userdifferencemed == differencemed:
        print 'Congrats! Your answer is correct.'
    else:
        finaldifferencemed = str(differencemed)
        print 'Sorry. The correct answer is ' + finaldifferencemed
else:
    print np + "-" + no + "="
    user_differencemed = raw_input("Enter answer here:")
    differencemed = numberp - numbero
    userdifferencemed = int(user_differencemed)
    if userdifferencemed == differencemed:
        print 'Congrats! Your answer is correct.'
    else:
        finaldifferencemed = str(differencemed)
        print 'Sorry. The correct answer is ' + finaldifferencemed
### This is for subtraction-hard

numberj = randint(50, 1000)
numberk = randint(50, 1000)

nj = str(numberj)
nk = str(numberk)

if numberj >= numberk:
    print nj + "-" + nk + "="
    user_differencehard = raw_input("Enter answer here:")
    differencehard = numberj - numberk
    userdifferencehard = int(user_differencehard)
    if userdifferencehard == differencehard:
        print 'Congrats! Your answer is correct.'
    else:
        finaldifferencehard = str(differencehard)
        print 'Sorry. The correct answer is ' + finaldifferencehard
else:
    print nk + "-" + nj + "="
    user_differencehard = raw_input("Enter answer here:")
    differencehard = numberk - numberj
    userdifferencehard = int(user_differencehard)
    if userdifferencehard == differencehard:
        print 'Congrats! Your answer is correct.'
    else:
        finaldifferencehard = str(differencehard)
        print 'Sorry. The correct answer is ' + finaldifferencehard
