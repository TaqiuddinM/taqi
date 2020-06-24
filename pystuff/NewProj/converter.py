def announce(f):
    def wrapper():
        print("about to run function..")
        f()
        print("function ran")

    return wrapper


@announce
def hello():
    print("hello worlds")


hello()



