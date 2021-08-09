def calc_bmi(weight, height):
    #print("weight = {:f}".format(weight))
    #print("height = {:f}".format(height))
    bmi = weight / height**2
    #print("bmi = {:f}".format(bmi))

    if bmi < 18.5:
        return "under"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "over"
    return "obese"

def take_input():
    n = input("Enter data:\n")
    ret = []
    for i in range (0, int(n)):
        n2 = input()
        l1 = n2.split()
        l2 = float(l1[0]), float(l1[1])
        ret.append(l2)
    return ret

inputs = take_input()
output = ""
for l in inputs:
    #print (l)
    output+=calc_bmi(l[0], l[1]) + " "
print(output)

