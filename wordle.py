import random

def choose_secret():
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """
    words = []
    with open(r'C:\Users\Usuario\Desktop\SEMESTRE 3B\PROYECTO\PYTHON\Examen\ExamenPython2022\palabras_reduced.txt', 'r') as f:
      for line in f:
        words.append(line)
    secret = random.choice(words).upper()
    return secret
    
def compare_words(word, secret):
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    same_position = []
    same_letter = []
    striped_word = []
    striped_secret = []

    for i in range(0, len(word)):
      striped_word.append(word[i])
      for j in range(0, len(secret) -1):
        striped_secret.append(secret[j])
        # Se comprueba si las letras de la palabra coinciden con la de secret (misma posicion)
        if striped_word[i].lower() == striped_secret[i].lower():
          same_position.append(i)

        # Se comprueba si las letras de la palabra coinciden con la de secret (distinta posicion)
        elif striped_word[i].lower() == striped_secret[j].lower():
          same_letter.append(i)
    
    return same_position, same_letter


def print_word(word, same_letter_position, same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    transformed = ["-", "-", "-", "-", "-"]

    # Comprueba si hay letras que coinciden en posicion
    if len(same_letter_position) > 0:
      for i in same_letter_position:
        # Sustituye en la lista transformed el guion por la letra en mayuscula
        transformed[i] = word[i].upper()

    # Comprueba si hay letras iguales
    if len(same_letter) > 0:
      for j in same_letter:
        # Susituye en la lista transformed el guion por la letra en minuscula
        transformed[j] = word[j].lower()

    return transformed 

def choose_secret_advanced():
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """

    words = []
    with open(r'C:\Users\Usuario\Desktop\SEMESTRE 3B\PROYECTO\PYTHON\Examen\ExamenPython2022\palabras_extended.txt', 'r', encoding='utf-8') as f:
      for line in f:
        # Se eligen solo si son palabras de 5 letras
        if len(line) == 5:
          words.append(line)
    # Se eligen 15 palabras aleatorias
    secrets = random.choices(words, weights=None, cum_weights=None, k=15)
    # Se elige solo una palabra aleatoria
    secret = random.choice(secrets).upper()
    return secrets, secret
 
def check_valid_word(selected):
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """
    while(True):
      word = input("Introduce una nueva palabra para compribar que esta en la listaa: ")
      if word in selected:
        return word

        
if __name__ == "__main__":
    secret=choose_secret()
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words(word, secret)
        resultado=print_word(word, same_position, same_letter)
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   
