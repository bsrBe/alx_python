import sys

if __name__ == "__main__":
    # Get the number of arguments
    num_args = len(sys.argv) - 1

    # Print the number of arguments and the appropriate label
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_args))

    # Print the position and value of each argument
    for i in range(1, num_args + 1):
        print("{}: {}".format(i, sys.argv[i]))
