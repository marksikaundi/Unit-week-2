def function(x): #x is param
    print(x)
    print(x)
    print(x)


t1 = 1
function(9 - 1)
function('rufus')
function(1)


def fun_2():
    loc = 228


# fun_2() if you run this code,
#print(loc)  there will be an error, since the variable is local
def func_3(unical_param):
    print('really unical')


func_3(1000)
#print(unical_param) if you run this code,there will be NameError
t1 = 7
def fun_4(t1):
    print(t1)
#variable inside a function and a variable with the same name outside
# of it are two different variables
# and their values do not overlap or replace
fun_4(t1)
