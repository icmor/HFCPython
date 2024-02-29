#!/usr/bin/env python3
"""Módulo para jugar adivina el número, el juego consiste en adivinar un
número entre 1 y 100, por cada intento el programa responde si el número
adivinado es más alto o más bajo."""


def randint():
    """Function to generate a random number in [0-100] reading directly from
    /dev/urandom."""
    with open("/dev/urandom", 'rb') as f:
        return int.from_bytes(f.read(8)) % 101


def play(number):
    """Guessing game, guess a number between 1-100, the program tells you
    if the answer is lower or higher than your guess."""
    while True:
        guess = input("Adivina un número del 1 al 100 (s para salir): ")
        if guess == "s":
            break
        if not guess.isdigit() or int(guess) < 0 or int(guess) > 100:
            print("Tienes que ingresar un número entre el 1 y el 100!")
            continue
        guess = int(guess)
        if guess == number:
            print("Ganaste! El número era", number)
            break
        elif guess < number:
            print("El número es mayor que", guess)
        else:
            print("El número es menor que", guess)


if __name__ == "__main__":
    play(randint())
