def decor_func(function):
    def wapper(*args, **kwargs):
        #print('get code', args)
        function(*args, **kwargs)
        print("Function name:",function.__name__, 'with aruments', args)
    return wapper

@decor_func
def calc_sum(a,b,x):
    x = a*x+b
    print('Resul t=',x)

calc_sum(5,4,9)