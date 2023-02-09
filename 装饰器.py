from functools import update_wrapper, wraps


def logger(wrapped):  # fn = add
    @wraps(wrapped)    # 有参装饰器 等价  wrapper = wraps(wrapped)(wrapper)   # partial function偏函数
    def wrapper(*args, **kwargs):
        print('执行前增强')
        ret = wrapped(*args, **kwargs)  # fn(4, y=8)  add(4, y=8), fn是闭包
        print('执行后增强')
        return ret

    update_wrapper(wrapper, wrapped)    # 用被包装的函数，替换包装函数，这个update_wrapper函数有个装饰器，叫warps
    return wrapper


@logger  # 等价  add = logger(add)
def add(x, y):
    return x + y




t = logger(add)   # t = inner
print(t(4, y=8))  # inner(4, y=8)

add = logger(add)  # add = inner
print(add(4, 5))
