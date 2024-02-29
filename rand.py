#!/usr/bin/env python3
"""Módulo para generar contraseñas aleatorias"""

import random
import argparse
import string


def gen_password(lower, upper, digits):
    """Generates a password with lower number of lowercase letters,
    upper number of uppercase letters and digits number of digits."""
    chars = random.choices(string.ascii_lowercase, k=lower)
    chars += random.choices(string.ascii_uppercase, k=upper)
    chars += random.choices("0123456789", k=digits)
    random.shuffle(chars)
    return "".join(chars)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("lower", help="number of lowercase letters", type=int)
    parser.add_argument("upper", help="number of uppercase letters", type=int)
    parser.add_argument("digits", help="number of digits", type=int)
    args = parser.parse_args()

    print(gen_password(args.lower, args.upper, args.digits))
