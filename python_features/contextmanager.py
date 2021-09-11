from contextlib import contextmanager

@contextmanager
def myconman():
    a = "hello" 
    yield a
    a = "bye"
    print(f"{a} from conman")


with myconman() as cm:
    print(f"{cm} from func")

