import sqlite3
import os

# Definicija staze do SQLite datoteke
DATABASE_PATH = 'pyano.db'

def get_db_connection() -> sqlite3.Connection:
    """
    Vraća konekciju (vezu) na SQLite bazu podataka.
    """
    try:
        # Povezivanje na bazu podataka. Ako datoteka ne postoji, SQLite će je kreirati.
        conn = sqlite3.connect(DATABASE_PATH)
        # Postavljamo row_factory na sqlite3.Row kako bismo mogli pristupiti 
        # stupcima po imenu umjesto po indeksu (npr. row['name'] umjesto row[1]).
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Greška pri spajanju na bazu podataka: {e}")
        # U stvarnoj aplikaciji, ovdje bi se moglo logirati ili baciti iznimku
        raise e

def initialize_db():
    """
    Kreira tablice ako već ne postoje i unosi početne podatke.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # --- 1. Kreiranje tablice piano_types ---
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS piano_types (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                description TEXT
            )
        """)

        # --- 2. Kreiranje tablice pianos ---
        # Vanjski ključ (FOREIGN KEY) povezuje s tablicom piano_types
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pianos (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                manufacturer TEXT NOT NULL,
                price REAL,
                piano_type_id INTEGER NOT NULL,
                FOREIGN KEY (piano_type_id) REFERENCES piano_types(id)
            )
        """)
        
        # --- 3. Unos početnih podataka (SEEDING) ---
        
        # Unos tipova klavira
        initial_types = [
            (1, 'Digitalni', 'Klaviri s elektroničkom simulacijom zvuka.'),
            (2, 'Akustični', 'Tradicionalni klaviri sa žicama i čekićima.'),
            (3, 'Sintetizator', 'Instrumenti za stvaranje i modulaciju zvuka.')
        ]
        # Koristimo INSERT OR IGNORE da spriječimo duple unose ako se funkcija pozove više puta
        cursor.executemany("""
            INSERT OR IGNORE INTO piano_types (id, name, description) VALUES (?, ?, ?)
        """, initial_types)
        
        # Unos primjera klavira (Koristimo ID-jeve tipova 1, 2, 3)
        initial_pianos = [
            ('Yamaha P-45', 'Yamaha', 499.00, 1), # Digitalni (ID 1)
            ('Kawai K-300', 'Kawai', 8500.00, 2), # Akustični (ID 2)
            ('Nord Stage 4', 'Nord', 3800.00, 3), # Sintetizator (ID 3)
            ('Bechstein B', 'Bechstein', 12000.00, 2) # Akustični (ID 2)
        ]
        cursor.executemany("""
            INSERT OR IGNORE INTO pianos (name, manufacturer, price, piano_type_id) 
            VALUES (?, ?, ?, ?)
        """, initial_pianos)

        conn.commit()
        
    except sqlite3.Error as e:
        print(f"Greška pri inicijalizaciji baze: {e}")
        raise e
        
    finally:
        # Osiguravamo zatvaranje veze
        conn.close()

# Inicijaliziraj bazu čim se modul uveze (za prvi put)
if not os.path.exists(DATABASE_PATH):
    print("Kreiranje i inicijalizacija baze podataka...")
    initialize_db()