from dataclasses import dataclass


@dataclass
class Complex:
    real: float
    imag: float

    def __str__(self):
        if self.imag >= 0:
            sing = '+'
        else:
            sing = '-'
        return f'{self.real} {sing} {abs(self.imag)}i'


if __name__ == '__main__':
    c = Complex(5,-5.6)
    print(c)