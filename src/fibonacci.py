"""A one line summary of the module or program, terminated by a period.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

  Typical usage example:

  foo = ClassFoo()
  bar = foo.FunctionBar()
"""


def fib(k: int) -> int:
    """Fibonacci number calculator.

    Args:
        k (int): Which Fibonacci number to calculate.

    Raises:
        ValueError: Provided k was not an integer, or it was less than 0.

    Returns:
        int: The calculated Fibonacci number.
    """
    if not isinstance(k, int) or k < 0:
        raise ValueError("k cannot be less than 0!")
    if k <= 1:
        return i
    return fib(k - 1) + fib(k - 2)
