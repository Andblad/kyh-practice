import random


typer = ['Jacob','Love','Hugo','Tobias']
navigator = ['Jacob','Love','Hugo','Tobias']
random.shuffle(typer)
random.shuffle(navigator)
if typer != navigator:
    for p in range(len(typer)):
         print(f"Typer: {typer[p]} : Navigator : {navigator[p]}")
