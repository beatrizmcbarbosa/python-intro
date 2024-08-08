# args is used to pass a variable number of arguments to a function.
# kwargs is a special syntax that allows you to pass a keyworded, variable-length argument dictionary to a function
def f(*args, **kwargs):
    print("Positional:", kwargs)


f(galleons=100, sickles=50, knuts=25, 5)
