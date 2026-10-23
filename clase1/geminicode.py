import random

def main():
    print("--- Generador Aleatorio Sencillo ---")
    
    # 1. Número entero aleatorio entre 1 y 100
    entero_aleatorio = random.randint(1, 100)
    print(f"Número entero (1 al 100): {entero_aleatorio}")
    
    # 2. Número decimal aleatorio entre 0.0 y 1.0
    decimal_aleatorio = random.random()
    print(f"Número decimal (0.0 a 1.0): {decimal_aleatorio:.2f}")
    
    # 3. Elección aleatoria de una lista de elementos
    frutas = ["Manzana", "Banana", "Naranja", "Pera", "Frutilla"]
    fruta_elegida = random.choice(frutas)
    print(f"Fruta elegida al azar: {fruta_elegida}")
    
    # 4. Mezclar una lista (barajar)
    cartas = ["As", "Rey", "Reina", "Jota"]
    random.shuffle(cartas)
    print(f"Cartas barajadas: {cartas}")

if __name__ == "__main__":
    main()