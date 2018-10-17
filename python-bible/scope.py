a = [1,2,3]

def f1():
    a[0] = 5

    print(a)

def f2():
    print(a)

f1()
f2()
print(a)


def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    # modified the global not the spam local to the function which was set by do_nonlocal()
    print("After global assignment:", spam)

# -----------------------------------------------------------------
spam="test"
scope_test()
print("In global scope:", spam)
