import sys

def main():
    #read theta0 and theta1
    file = open("../training/parameters.txt", "r")
    theta0 = file.readline()
    theta0 = int(theta0)
    theta1 = file.readline()
    theta1 = int(theta1)
    print("theta0 = {}".format(theta0))
    print("theta1 = {}".format(theta1))
    if len(sys.argv) == 2:
        print(sys.argv[1])
    #ask the user for a mileage
    try:
        mileage = int(raw_input("What mileage ?\n"))
    except ValueError:
        print("Bad input")
        exit()
    #estimate the price for that mileage
    price = theta0 + theta1 * mileage
    print("Estimated price for the mileage :\n{}".format(price))

if __name__ == "__main__":
    main()
