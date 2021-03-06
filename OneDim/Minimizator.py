import math


def test_func(x):
    return x * x - x + 1


class FuncWrapper:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def get_value(self, x):
        self.count += 1
        return self.func(x)

    def reset_count(self):
        self.count = 0


class Minimizator:
    def __init__(self, f, a, b, eps):
        self.f = f
        self.a = a
        self.b = b
        self.eps = eps

    def dichotomy_min(self):
        ak = self.a
        bk = self.b
        delta = (bk - ak) / 1000
        while delta + delta >= self.eps:
            delta /= 2
        print("Right = ", (self.b-self.a) / (self.eps - 2 * delta))
        while (bk - ak) >= self.eps:
            ck = (ak + bk) / 2
            xl = ck - delta
            xr = ck + delta
            fl = self.f.get_value(xl)
            fr = self.f.get_value(xr)
            if fl < fr:
                # ak = ak
                bk = xr
            else:
                ak = xl
                # bk = bk

        return ak, bk

    def fibonacci_min(self):
        ak = self.a
        bk = self.b

        criteria = (self.b - self.a) / self.eps
        fib = []
        fib.append(1)
        fib.append(1)
        n = 1
        while (fib[n] <= criteria):
            fib.append(fib[n] + fib[n - 1])
            n += 1
        print("Fib_method, n =", n)
        k = 1
        lambdak = ak + fib[n - k - 1] / fib[n - k + 1] * (bk - ak)
        muk = ak + fib[n - k] / fib[n - k + 1] * (bk - ak)
        fl = self.f.get_value(lambdak)
        fr = self.f.get_value(muk)
        mul = 1
        while (k != (n - 1)):
            mul *= fib[n - k] / fib[n - k + 1]
            k += 1
            if (fl < fr):
                #ak = ak
                bk = muk

                muk = lambdak
                fr = fl

                if k != (n - 1):
                    lambdak = ak + fib[n - k - 1] / fib[n - k + 1] * (bk - ak)
                    fl = self.f.get_value(lambdak)
                else:
                    delta = (bk - ak) / 1000
                    while delta + muk - ak >= self.eps:
                        delta /= 2

                    lambdak = muk - delta
                    fl = self.f.get_value(lambdak)
                    if fl < fr:
                        bk = muk
                    else:
                        ak = lambdak
            else:
                ak = lambdak
                #bk = bk

                lambdak = muk
                fl = fr

                if k != (n - 1):
                    muk = ak + fib[n - k] / fib[n - k + 1] * (bk - ak)
                    fr = self.f.get_value(muk)
                else:
                    delta = (bk - ak) / 1000
                    while delta + lambdak - ak >= self.eps:
                        delta /= 2

                    muk = lambdak + delta
                    fr = self.f.get_value(muk)
                    if fl < fr:
                        bk = muk
                    else:
                        ak = lambdak

        return ak, bk


a, b = -1, 3
eps = [0.1, 0.01, 0.001]
wrp = FuncWrapper(test_func)
min = []
for e in eps:
    min.append(Minimizator(wrp, a, b, e))

print("Real answer:", 0.5)
for m in min:
    ak, bk = m.dichotomy_min()
    print("Answer: (%.5f, %.5f)" % (ak, bk))
    print("Interval abs: %.5f" % (bk - ak))
    print("Number of func calls: ", wrp.count)
    print()

    wrp.reset_count()

    ak, bk = m.fibonacci_min()
    print("Answer: (%.5f, %.5f)" % (ak, bk))
    print("Interval abs: %.5f" % (bk - ak))
    print("Number of func calls:", wrp.count)
    print()

    wrp.reset_count()