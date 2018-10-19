#!/usr/bin/python3

from typing import Tuple

import math


def tr(a: float, b: float, c: float) -> float:
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def read() -> Tuple[float, float, float]:
    return (float(input("A: "))), (float(input("B: "))), (float(input("C: ")))


def output(s: float):
    print("S: ", str(s))


a, b, c = read()
output(tr(a, b, c))
