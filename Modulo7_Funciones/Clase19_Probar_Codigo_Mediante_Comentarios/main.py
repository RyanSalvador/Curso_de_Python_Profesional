# docstring
# se prueba asi en consola "python3 -m doctest main.py"
# sino se tienen errores no manda nada si si te mandara donde esta mal
# usar pocos casos de prueba 

def palindromo(sentence):
    """Permite conocer si un string si es, o no, un palindromo.
    
    Args:
        - sentence (String)
    
    Return:
        - Bool
    
    Examples:
    >>> palindromo('oso')
    True

    >>> palindromo('Anita lava la tina')
    True

    >>> palindromo('CodigoFacilito')
    False
    """
    sentence = sentence.lower().replace(' ','')
    return sentence == sentence[::-1]

def average(*args):
    """Permite conocer el promedio de N argumentos.

    Example:
    >>> average(5, 5, 5, 5, 5)
    5.0

    >>> average(10, 9, 8, 7)
    8.5
    """

    return sum(args) / len(args)