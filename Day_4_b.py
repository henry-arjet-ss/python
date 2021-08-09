list1 = [
    [34587, "Learning Python, Mark Lutz", 4, 40.95],
    [98762,	"Programming Python, Mark Lutz",	5,	56.80],
    [77226,	"Head First Python, Paul Barry",	3,	32.95],
    [88112,	"Einführung in Python3, Bernd Klein",	3,	24.99]
]



def calc_price1(l):
    
    p = l[2]*l[3]
    if p < 100:
       p += 10
    return (l[0], p)
#I really can't see how to fit this into a lambda

list1_calc = list(map(calc_price1, list1))

print(list1_calc)


def calc_price2(l):
    p = 0 #accumulator
    for t in l:
        if type(t) is not tuple:
            continue
        p += t[1]*t[2]
        
    if p < 100:
       p += 10
    return (l[0], p)
