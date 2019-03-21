def write_data(filename, data):
    f = open(filename, "w")
    for i in range(len(data)):
        f.write(str(data[i]) + " ")

def read_data(filename):
    f = open(filename, "r")
    fl = f.read()
    data = fl.split(" ")[:-1]
    array = []
    for i in range(len(data)):
        num = float(data[i])
        array.append(num)
    return array