import sys

# Get the number of arguments
num_args = len(sys.argv) - 1

# Print the number of arguments
if num_args == 0:
    print("Number of argument(s): 0.")
else:
    print("Number of argument(s): {}.".format(num_args))

    # Print the list of arguments
    for i in range(1, num_args + 1):
        print("Argument {}: {}".format(i, sys.argv[i]))
