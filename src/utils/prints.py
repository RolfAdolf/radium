from typing import Optional, Callable


def bounds_printer(
        start_title: str,
        end_title: Optional[str] = 'END',
        size: int = 10,
        pattern: str = '=',
) -> Callable:

    def bounds_decorator(func: Callable) -> Callable:

        half_bound = pattern * size
        start_bound = ' '.join(('\n', half_bound, start_title.upper(), half_bound, '\n'))
        end_bound = ' '.join(('\n', half_bound, end_title.upper(), half_bound, '\n'))

        def wrapped(*args, **kwargs):
            print(start_bound)
            result = func(*args, **kwargs)
            print(end_bound)
            return result

        return wrapped

    return bounds_decorator


def async_bounds_printer(
        start_title: str,
        end_title: Optional[str] = 'END',
        size: int = 10,
        pattern: str = '=',
) -> Callable:

    def bounds_decorator(func: Callable) -> Callable:

        half_bound = pattern * size
        start_bound = ' '.join(('\n', half_bound, start_title.upper(), half_bound, '\n'))
        end_bound = ' '.join(('\n', half_bound, end_title.upper(), half_bound, '\n'))

        async def wrapped(*args, **kwargs):
            print(start_bound)
            result = await func(*args, **kwargs)
            print(end_bound)
            return result

        return wrapped

    return bounds_decorator
