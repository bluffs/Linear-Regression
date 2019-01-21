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
    #new tmp0 and tmp1
    for line in data:
        mile = int(line[0])
        price = int(line[1])
        #print("mile = {}, price = {}".format(mile, price))
        diff = (tmp0 + tmp1 * mile) - price
        print("diff = {}".format(diff))
    theta0 = tmp0
    theta1 = tmp1
