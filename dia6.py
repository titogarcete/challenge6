import random

# Opciones disponibles
opciones = ["piedra", "papel", "tijeras"]

# Función para determinar el ganador
def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijeras") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijeras" and computadora == "papel"):
        return "Ganas tú"
    else:
        return "Gana la computadora"

# Solicitar al usuario que ingrese su elección
usuario = input("Elige piedra, papel o tijeras: ").lower()

# Asegurarse de que la elección del usuario es válida
if usuario not in opciones:
    print("Elección inválida. Por favor elige piedra, papel o tijeras.")
else:
    # Elección de la computadora
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    # Determinar y mostrar el ganador
    resultado = determinar_ganador(usuario, computadora)
    print(resultado)
