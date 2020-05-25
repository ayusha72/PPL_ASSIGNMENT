def factors(num):
    mylist = []
    for i in range(1, num + 1):
        if num % i == 0:
            mylist.append(i)
    return mylist


def harmonic_mean(factors_list):
    sum = 0.0
    count = 0
    for i in factors_list:
        # print (i)
        #print(1 / i)
        sum += 1 / i
        # print (sum)
        count += 1
    mean = count / sum
    return mean


i = 1
count = 0
while 1:
    factors_list = factors(i)
    #print(factors_list)
    mean = harmonic_mean(factors_list)
    #print('---{}'.format(mean))
    if count == 10:
        break
    if (mean - int(mean)) < 0.00000001:
        print(i)
        count += 1
    i += 1
