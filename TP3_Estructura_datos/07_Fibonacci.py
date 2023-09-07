
import time


def fib1(n):  # O(2^n)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n-1) + fib1(n-2)


def fib2(n):  # O(n)
    def do_fib(a, b, i):
        if i == n:
            return a
        return do_fib(b, a+b, i+1)

    return do_fib(0, 1, 0)


contador = 1

for i in range(37):

    t0 = time.time()
    finob_1 = fib1(contador)

    t1 = time.time()
    finob_2 = fib2(contador)

    t2 = time.time()

    print("Prueba: " + str(i))
    print('{} - {:.8f}'.format(finob_1, t1 - t0))
    print('{} - {:.8f}'.format(finob_2, t2 - t1)+'\n')

    contador += 1
