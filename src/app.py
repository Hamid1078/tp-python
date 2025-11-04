def add(a: float, b: float) -> float:
    """Retourne la somme de deux nombres."""
    return a + b


def is_palindrome(s: str) -> bool:
    """
    Vérifie si une chaîne est un palindrome (insensible à la casse et aux espaces).
    Exemple : 'Kayak' -> True
    """
    clean = ''.join(c.lower() for c in s if c.isalnum())
    return clean == clean[::-1]


