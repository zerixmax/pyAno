

# SADA možemo sigurno uvoziti ostale module
from utils.db_connector import initialize_db # Povući će konektor
from infrastructure.repositories import PianoRepository
from services.services import PianoService


def display_pianos(service: PianoService):
    """
    Prikazuje listu klavira u konzoli.
    """
    print("\n--- Popis Klavira ---")
    
    # 1. Dohvaćanje podataka iz Service sloja
    pianos_data = service.get_pianos_with_details()
    
    if not pianos_data:
        print("Nema unesenih klavira.")
        return

    # 2. Formatirani ispis
    # Ispis zaglavlja
    headers = list(pianos_data[0].keys())
    # Ograničavamo širinu kolona radi čitljivosti u konzoli
    col_widths = [15, 20, 15, 10, 15] 

    header_line = "".join(f"{h:<{w}}" for h, w in zip(headers, col_widths))
    print(header_line)
    print("-" * len(header_line))

    # Ispis podataka
    for item in pianos_data:
        row_line = "".join(f"{str(item[h]):<{w}}" for h, w in zip(headers, col_widths))
        print(row_line)
    print("-" * len(header_line))


def main():
    """
    Glavna funkcija aplikacije koja pokreće izbornik.
    """
    # Inicijalizacija baze (ako već nije)
    initialize_db()
    
    # Inicijalizacija slojeva
    piano_repo = PianoRepository()
    piano_service = PianoService(repository=piano_repo)
    
    while True:
        print("\n=== PYANO - GLAVNI IZBORNIK ===")
        print("1. Prikaz svih klavira")
        print("2. Izađi")
        
        choice = input("Odabir: ")
        
        if choice == '1':
            display_pianos(piano_service)
        elif choice == '2':
            print("Izlaz iz aplikacije. Hvala!")
            break
        else:
            print("Nevažeći odabir, pokušajte ponovo.")

if __name__ == "__main__":
    main()