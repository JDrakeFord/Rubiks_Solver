str = "dingus bingus"


def dingus():
    print('dingus')


def bingus():
    print('bingus')


for x in str:
    eval(x)()
