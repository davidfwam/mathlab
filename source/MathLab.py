import jinja2
import webapp2
import random
from random import randint

### this is for addition section-easy
class AdditionEasy(webapp2.RequestHandler):
    def get(self):
        numberone = randint(0, 10)
        numbertwo = randint(0, 10)

        n1 = str(numberone)
        n2 = str(numbertwo)

        print n1 + "+" + n2 + "="
        user_sum = raw_input("Enter sum here:")
        sumofrandint = numberone + numbertwo
        usersum = int(user_sum)
        if sumofrandint == usersum:
            self.response.write('Congrats! Your answer is correct.')

        else:
            finalsum = str(sumofrandint)
            self.response.write('Sorry. The correct answer is ' + finalsum)

### This is for addition-medium
class AdditionMedium(webapp2.RequestHandler):
    def get(self):
        numberthree = randint(10, 50)
        numberfour = randint(10, 50)

        n3 = str(numberthree)
        n4 = str(numberfour)

        print n3 + "+" + n4 + "="
        user_summed = raw_input("Enter sum here:")
        sumofrandintmed = numberthree + numberfour
        usersummed = int(user_summed)
        if sumofrandintmed == usersummed:
            self.response.write('Congrats! Your answer is correct.')

        else:
            finalsummed = str(sumofrandintmed)
            self.response.write('Sorry. The correct answer is ' + finalsummed)

### This is for addition-hard
class AdditionHard(webapp2.RequestHandler):
    def get(self):
        numberfive = randint(50, 1000)
        numbersix = randint(50, 1000)

        n5 = str(numberfive)
        n6 = str(numbersix)

        print n5 + "+" + n6 + "="
        user_sumhard = raw_input("Enter sum here:")
        sumofrandinthard = numberfive + numbersix
        usersumhard = int(user_sumhard)
        if sumofrandinthard == usersumhard:
            self.response.write('Congrats! Your answer is correct.')

        else:
            finalsumhard = str(sumofrandinthard)
            self.response.write('Sorry. The correct answer is ' + finalsumhard)
### This is for multiplication-easy
class MultiplicationEasy(webapp2.RequestHandler):
    def get(self):
        numberseven = randint(0, 10)
        numbereight = randint(0, 10)

        n7 = str(numberseven)
        n8 = str(numbereight)

        print n7 + "*" + n8 + "="
        user_product = raw_input("Enter product here:")
        product = numberseven * numbereight
        userproduct = int(user_product)
        if product == userproduct:
                self.response.write('Congrats! Your answer is correct.')

        else:
                finalproduct = str(product)
                self.response.write('Sorry. The correct answer is ' + finalproduct)

### This is for multiplication-medium
class MultiplicationMedium(webapp2.RequestHandler):
    def get(self):
        numbernine = randint(10, 50)
        numberten = randint(10, 50)

        n9 = str(numbernine)
        n10 = str(numberten)

        print n9 + "*" + n10 + "="
        user_productmed = raw_input("Enter product here:")
        productmed = numbernine * numberten
        userproductmed = int(user_productmed)
        if productmed == userproductmed:
            self.response.write('Congrats! Your answer is correct.')

        else:
            finalproductmed = str(productmed)
            self.response.write('Sorry. The correct answer is ' + finalproductmed)

### This is for multiplication-hard
class MultiplactionHard(webapp2.RequestHandler):
    def get(self):
        numbera = randint(50, 1000)
        numberb = randint(50, 1000)

        na = str(numbera)
        nb = str(numberb)

        print na + "*" + nb + "="
        user_producthard = raw_input("Enter product here:")
        producthard = numbera * numberb
        userproducthard = int(user_producthard)
        if producthard == userproducthard:
            self.response.write('Congrats! Your answer is correct.')

        else:
            finalproducthard = str(producthard)
            self.response.write('Sorry. The correct answer is ' + finalproducthard)

### This is for subtraction-easy
class SubtractionEasy(webapp2.RequestHandler):
    def get(self):
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
                self.response.write('Congrats! Your answer is correct.')
            else:
                finaldifference = str(difference)
                self.response.write('Sorry. The correct answer is ' + finaldifference)
        else:
            print ny + "-" + nz + "="
            user_difference = raw_input("Enter answer here:")
            difference = numbery - numberz
            userdifference = int(user_difference)
            if userdifference == difference:
                self.response.write('Congrats! Your answer is correct.')
            else:
                finaldifference = str(difference)
                self.response.write('Sorry. The correct answer is ' + finaldifference)

### This is for subtraction-med
class SubtractionMedium(webapp2.RequestHandler):
    def get(self):
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
                self.response.write('Congrats! Your answer is correct.')
            else:
                finaldifferencemed = str(differencemed)
                self.response.write('Sorry. The correct answer is ' + finaldifferencemed)
        else:
            print np + "-" + no + "="
            user_differencemed = raw_input("Enter answer here:")
            differencemed = numberp - numbero
            userdifferencemed = int(user_differencemed)
            if userdifferencemed == differencemed:
                self.response.write('Congrats! Your answer is correct.')
            else:
                finaldifferencemed = str(differencemed)
                self.response.write('Sorry. The correct answer is ' + finaldifferencemed)
### This is for subtraction-hard
class SubtractionHard(webapp2.RequestHandler):
    def get(self):
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
                self.response.write('Congrats! Your answer is correct.')
            else:
                finaldifferencehard = str(differencehard)
                self.response.write('Sorry. The correct answer is ' + finaldifferencehard)
        else:
            print nk + "-" + nj + "="
            user_differencehard = raw_input("Enter answer here:")
            differencehard = numberk - numberj
            userdifferencehard = int(user_differencehard)
            if userdifferencehard == differencehard:
                self.response.write('Congrats! Your answer is correct.')
            else:
                finaldifferencehard = str(differencehard)
                self.response.write('Sorry. The correct answer is ' + finaldifferencehard)
### This is for division-easy
class DivisionEasy(webapp2.RequestHandler):
    def get(self):
        number01 = randint(1, 10)
        number02 = randint(1, 10)

        n01 = str(number01)
        n02 = str(number02)

        if number01 >= number02:
            print n01 + "/" + n02 + "="
            user_q = raw_input("**Please only enter whole numbers!(round down)** Enter answer here:")
            q = number01 / number02
            userq = int(user_q)
            if userq == q:
                self.response.write('Congrats! Your answer is correct.')
            else:
                finalq = str(q)
                self.response.write('Sorry. The correct answer is ' + finalq)
        else:
            print n02 + "/" + n01 + "="
            user_q = raw_input("**Please only enter whole numbers(round down)!** Enter answer here:")
            q = number02 / number01
            userq = int(user_q)
            if userq == q:
                self.response.write('Congrats! Your answer is correct.')
            else:
                finalq = str(q)
                self.response.write('Sorry. The correct answer is ' + finalq)

### This is for division-medium
class DivisionMedium(webapp2.RequestHandler):
    def get(self):
        number03 = randint(1, 100)
        number04 = randint(1, 100)

        n03 = str(number03)
        n04 = str(number04)

        if number03 >= number04:
            print n03 + "/" + n04 + "="
            user_qmed = raw_input("**Please only enter whole numbers!(round down)** Enter answer here:")
            qmed = number03 / number04
            userqmed = int(user_qmed)
            if userqmed == qmed:
                self.response.write('Congrats! Your answer is correct.')
            else:
                finalqmed = str(qmed)
                self.response.write('Sorry. The correct answer is ' + finalqmed)
        else:
            print n04 + "/" + n03 + "="
            user_qmed = raw_input("**Please only enter whole numbers(round down)!** Enter answer here:")
            qmed = number04 / number03
            userqmed = int(user_qmed)
            if userqmed == qmed:
                self.response.write('Congrats! Your answer is correct.')
            else:
                finalqmed = str(qmed)
                self.response.write('Sorry. The correct answer is ' + finalqmed)

### This is for division-hard
class DivisionHard(webapp2.RequestHandler):
    def get(self):
        number05 = randint(1, 1000)
        number06 = randint(1, 1000)

        n05 = str(number05)
        n06 = str(number06)

        if number05 >= number06:
            print n05 + "/" + n06 + "="
            user_qhard = raw_input("**Please only enter whole numbers!(round down)** Enter answer here:")
            qhard = number05 / number06
            userqhard = int(user_qhard)
            if userqhard == qhard:
                self.response.write('Congrats! Your answer is correct.')
            else:
                finalqhard = str(qhard)
                self.response.write('Sorry. The correct answer is ' + finalqhard)
        else:
            print n06 + "/" + n05 + "="
            user_qhard = raw_input("**Please only enter whole numbers(round down)!** Enter answer here:")
            qhard = number06 / number05
            userqhard = int(user_qhard)
            if userqhard == qhard:
                self.response.write('Congrats! Your answer is correct.')
            else:
                finalqhard = str(qhard)
                self.response.write('Sorry. The correct answer is ' + finalqhard)
