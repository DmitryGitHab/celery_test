import time
import datetime
from tasks import hard_work_func


def main():
    result1 = (hard_work_func.delay(1, 2))
    result2 = (hard_work_func.delay(2, 2))
    result3 = (hard_work_func.delay(3, 2))
    result4 = (hard_work_func.delay(4, 2))

    print(result1.get())
    print(result2.get())
    print(result3.get())
    print(result4.get())


if __name__ == '__main__':
    start = datetime.datetime.now()
    main()
    print(datetime.datetime.now()-start)