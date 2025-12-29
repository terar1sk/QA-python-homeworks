class Diamond:
    def __setattr__(self, name, value):
        if name == "side":
            if not isinstance(value, (int, float)):
                raise TypeError("Сторона должна быть числом")
            if value <= 0:
                raise ValueError("Сторона должна быть больше 0")
            object.__setattr__(self, name, value)

        elif name == "alpha":
            if not isinstance(value, (int, float)):
                raise TypeError("Угол alpha должен быть числом")
            if not (0 < value < 180):
                raise ValueError("Угол alpha должен быть в диапазоне от 0 до 180")

            object.__setattr__(self, "beta", 180 - value)
            object.__setattr__(self, name, value)

        elif name == "beta":
            raise AttributeError("Угол beta вычисляется автоматически, не может быть задан вручную")

        else:
            object.__setattr__(self, name, value)

    def __init__(self, side, alpha):
        self.side = side
        self.alpha = alpha

    def __repr__(self):
        return f"Ромб(side={self.side}, alpha={self.alpha}, beta={self.beta})"

    def __str__(self):
        return f"Ромб со стороной {self.side} и углами {self.alpha} и {self.beta}"

    def __eq__(self, other):
        return isinstance(other, Diamond) and self.side == other.side and self.alpha == other.alpha

    def __len__(self):
        return int(self.side)

    def __mul__(self, scale):
        if scale <= 0:
            raise ValueError("Масштаб должен быть положительным числом")
        return Diamond(self.side * scale, self.alpha)

    def __rmul__(self, scale):
        return self.__mul__(scale)


d = Diamond(10, 60)
print(d)

print(repr(d))

d2 = Diamond(10, 60)
print(d == d2)

print(len(d))

d3 = d * 2
print(d3)