
from variable_load_2 import a

if __name__ == "__main__":
    print("a =", a if "a" in globals() else "a missing")
