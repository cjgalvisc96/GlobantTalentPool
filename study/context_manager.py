from contextlib import contextmanager


# Using classes
class HelloContextManager:
    def __enter__(self):
        print("Entering the context...")
        return "Hello, World!"

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Leaving the context...")
        if isinstance(exc_value, IndexError):
            # Handle IndexError here...
            print(f"An exception occurred in your with block: {exc_type}")
            print(f"Exception message: {exc_value}")
            return True


# Using functions
@contextmanager
def hello_context_manager_function():
    print("Entering the context...")
    yield "Hello, World!"
    print("Leaving the context...")


if __name__ == '__main__':
    # Using functions
    with hello_context_manager_function() as hello:
        print(hello)

    print("#"*45)

    # Using functions
    with HelloContextManager() as hello:
        print(hello)
        hello[100]

