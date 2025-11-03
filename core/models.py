# 1. Klasa za Tip Klavira (Digitalni, Akustični, Sintetizator)
class PianoType:
    def __init__(self, id: int, name: str, description: str = ""):
        # ID je važan jer će se koristiti kao Foreign Key u bazi
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        # Dobro za debugiranje i ispis
        return f"PianoType(id={self.id}, name='{self.name}')"

# 2. Klasa za Konkretni Klavir
class Piano:
    def __init__(self, id: int, name: str, manufacturer: str, price: float, piano_type_id: int):
        self.id = id
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        # Ovdje spremamo ID tipa, a ne cijeli objekt PianoType. 
        # Cijeli objekt ćemo "spojiti" kasnije u Service sloju.
        self.piano_type_id = piano_type_id 

    def __repr__(self):
        return f"Piano(id={self.id}, name='{self.name}', manufacturer='{self.manufacturer}')"


# --- Mjesto za ostale modele (ChordType, ScaleType, Lesson) koje ćemo dodati kasnije. ---

# class ChordType:
#     pass
# 
# class Lesson:
#     pass