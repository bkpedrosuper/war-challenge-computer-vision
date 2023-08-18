import time

from war_challenge_computer_vision.utils.enviroment import is_dev


# https://www.tutorialspoint.com/concurrency_in_python/concurrency_in_python_benchmarking_and_profiling.htm
def timer_func(func):
    if not is_dev:
        return func

    def function_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "{func} took {time} seconds to complete its execution."
        print(msg.format(func=func.__name__, time=runtime))
        return value

    return function_timer
