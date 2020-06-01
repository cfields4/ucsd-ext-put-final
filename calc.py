class calc:
    def sum(self, a, b):
        return a + b

    def prod(self, a, b):
        return a * b


if __name__ == "__main__":
    print("calc")
    c = calc()
    print(c.sum(10, 20))
    print(c.prod(10, 20))
