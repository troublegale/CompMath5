from math import sin, sqrt
from interpolation import solve


def read_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            xs = []
            ys = []
            x_read = False
            for line in file:
                if not x_read:
                    x_read = True
                    x = float(line.strip())
                else:
                    point = line.strip().replace(',', '.').split()
                    if len(point) == 2:
                        xs.append(float(point[0]))
                        ys.append(float(point[1]))

        return x, xs, ys, None
    except IOError as err:
        return None, None, None, f"Unable to read file '{filename}': {err}"


def read_data_from_input():
    print("Enter the interpolation point:")
    x = 0
    while not x:
        try:
            x = float(input("$ ").replace(',', '.'))
            break
        except ValueError:
            print("Please, enter a correct number.")
    s = ''
    xs = []
    ys = []
    print("Enter 'quit' to stop.")
    print("Enter the interpolation nodes (pairs of x and y values):")
    while s.strip().lower() != 'quit':
        s = input()
        point = s.strip().replace(',', '.').split()
        if len(point) == 2:
            xs.append(float(point[0]))
            ys.append(float(point[1]))
        else:
            if s.strip().lower() != 'quit':
                print("Incorrect input. This won't be used.")
    return x, xs, ys


def read_data_from_example():
    x = 0.502
    xs = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]
    ys = [1.5320, 2.5356, 3.5406, 4.5462, 5.5504, 6.5559, 7.5594]
    return x, xs, ys


def read_data_from_function():
    print('Functions:')
    print('1. 2*x^2 - 5*x')
    print('2. x^5')
    print('3. sin(x)')
    print('4. sqrt(x)')

    print("Choose a function (1, 2, 3 or 4):")
    while True:
        input_func = input("$ ").strip()
        if input_func == "1":
            f = lambda x: 2 * x ** 2 - 5 * x
            break
        elif input_func == "2":
            f = lambda x: x ** 5
            break
        elif input_func == "3":
            f = lambda x: sin(x)
            break
        elif input_func == "4":
            f = lambda x: sqrt(x)
            break
        else:
            print("Please, choose one of the available options.")

    print("Enter the number of nodes:")
    while True:
        try:
            n = int(input("$ "))
            if n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please, enter a correct number")
    print("Enter x0:")
    while True:
        try:
            x0 = float(input("$ "))
            break
        except ValueError:
            print("Please, enter a correct number")
    print("Enter xn:")
    while True:
        try:
            xn = float(input("$ "))
            if xn < x0:
                raise ValueError
            break
        except ValueError:
            print("Please, enter a correct number")

    h = (xn - x0) / (n - 1)
    xs = [x0 + h * i for i in range(n)]
    ys = list(map(f, xs))

    print('Enter the interpolation point: ')
    while True:
        try:
            x = float(input("$ "))
            if x < x0 or x > xn:
                raise ValueError
            break
        except ValueError:
            print("Please, enter a correct number")

    return x, xs, ys


def main():
    while True:
        while True:
            print(
                "Enter:\n  - 'fi' to read from file;\n  - 'e' to use default example data;\n  - 't' to read data from "
                "terminal;\n  - 'fu' to use a prepared function.")
            option = input("$ ")
            if option == 'fi':
                while True:
                    print("Enter the file name:")
                    filename = input("$ ")
                    x, xs, ys, error = read_data_from_file(filename)
                    if error != None:
                        print(error)
                        print("Try another file name? [y/n]:")
                        one_more_time = input("$ ")
                        if one_more_time == 'y':
                            continue
                        else:
                            print('Reading from terminal:')
                            x, xs, ys = read_data_from_input()
                            break
                    else:
                        break
                n = len(xs)
                break
            elif option == 't':
                x, xs, ys = read_data_from_input()
                n = len(xs)
                break
            elif option == 'fu':
                x, xs, ys = read_data_from_function()
                n = len(xs)
                break
            elif option == 'e':
                x, xs, ys = read_data_from_example()
                n = len(xs)
                break
            else:
                print("Please, choose a correct option.\n")

        if len(set(xs)) != len(xs):
            print('All interpolation nodes have to be different. Please, retry your input.')
        elif xs != sorted(xs):
            print('Interpolation nodes have to be sorted. Please, retry your input.')
        else:
            break

    solve(xs, ys, x, n)


if __name__ == "__main__":
    main()
    print("Closing application...")
