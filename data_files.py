def write_data(filename, data):
    f = open(filename, "w") # "w" indicates the file will open to be overwritten
    for i in range(len(data)):
        f.write(str(data[i]) + " ")

def read_data(filename):
    f = open(filename, "r")
    fl = f.read()
    data = fl.split(" ")[:-1] # the last value is a space which need to be removed
    array = []
    for i in range(len(data)):
        num = float(data[i])
        array.append(num)
    return array

def extend_scale(scale_array):
        for i in range(len(scale_array)):
                if i == 0:
                        continue
                newFreq = scale_array[i] * 2
                scale_array.append(newFreq)
        return scale_array
        


a = read_data("OtherScale.txt")
b = extend_scale(a)
print(b)