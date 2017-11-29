#If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
#get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
multiples5 = []
multiples3 = []
all_multiples = []

mult5 = 5
mult3 = 3


while mult5 <= 1000:
    multiples5.append(mult5)
    mult5 += 5
print(multiples5)


while mult3 <= 1000:
    if mult3 in multiples5:
        pass
    else:
        multiples3.append(mult3)
    mult3 += 3
print(multiples3)


all_multiples = multiples5 + multiples3
print('The total sum is: ' + str(sum(all_multiples)))
