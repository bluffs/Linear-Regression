import sys
import tools

def main():
    data = []
    if len(sys.argv) == 2:
        print(sys.argv[1])
        if sys.argv[1] == "reset":
            print("calling reset")
            tools.ft_reset()
    #read dataset
    file = open("data.csv", "r")
    lines = file.readlines()
    lines = lines[1:]
    for line in lines:
        data.append(line[:-1].split(','))
    print(data)
    #train
    tools.ft_train(data)
    
if __name__ == "__main__":
    main()
