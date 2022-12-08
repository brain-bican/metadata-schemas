from example_pkg import ExampleClass, example_function


def main():
    _ = [1, 2, 3]
    cls = ExampleClass()
    print(f"This should print 'True': {cls.example_method() and example_function()}")


if __name__ == "__main__":
    main()
