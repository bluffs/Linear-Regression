def ft_reset():
    print ("start reset")
    file = open("parameters.txt", "w")
    file.write("0\n")
    file.write("0")
    exit()

def ft_train(data):
    print("start training")
    rate = 0.5
    tmp0 = 0.0
    tmp1 = 0.0
    m = len(data)
    #new tmp0 and tmp1
    sum0 = 0.0
    sum1 = 0.0
    for i in range(10):
        sum0 = 0.0
        sum1 = 0.0
        for line in data:
            mile = int(line[0])
            price = int(line[1])
            #print("mile = {}, price = {}".format(mile, price))
            sum0 = sum0 + (tmp0 + tmp1 * mile) - price
            sum1 = sum1 + tmp0 * mile
            #sum1 = sum1 + (((tmp0 + tmp1 * mile) - price) * mile)
            #print("diff = {}".format(diff0))
            #print("diff = {}".format(diff1))
        tmp0 = sum0 / (100 * m)
        tmp1 = sum1 / (100 * m)
        print("new tmp0 = {}".format(tmp0))
        print("new tmp1 = {}".format(tmp1))
        theta0 = tmp0
        theta1 = tmp1
    theta0 = tmp0
    theta1 = tmp1
    print("last value of theta0 = {}".format(theta0))
    print("last value of theta1 = {}".format(theta1))
