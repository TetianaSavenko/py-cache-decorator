from typing import Callable


def cache(func: Callable) -> Callable:
    stored_results = {}

    def wrapper(*args):
        if args not in stored_results:
            print("Calculating new result")
            stored_results[args] = func(*args)
        else:
            print("Getting from cache")
        return stored_results[args]

    return wrapper
