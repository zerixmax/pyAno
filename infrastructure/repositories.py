from core.models import Piano, PianoType
from utils.db_connector import get_db_connection

class PianoRepository:
    """
    Rukuje CRUD operacijama (Create, Read, Update, Delete) za klavire i tipove klavira
    direktno s SQLite bazom podataka.
    """

    def get_all_piano_types(self) -> list[PianoType]:
        """
        Dohvaća sve tipove klavira iz tablice 'piano_types'.
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT id, name, description FROM piano_types")
            
            piano_types = []
            for row in cursor.fetchall():
                # Pretvaranje retka iz baze u Python objekt
                piano_type = PianoType(
                    id=row['id'], 
                    name=row['name'], 
                    description=row['description']
                )
                piano_types.append(piano_type)
            return piano_types
            
        finally:
            conn.close()


    def get_all_pianos(self) -> list[Piano]:
        """
        Dohvaća sve klavire iz tablice 'pianos'.
        """
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            # Koristimo JOIN kako bismo jednim upitom dobili podatke iz obje tablice,
            # ali Repository vraća samo osnovni 'Piano' objekt
            cursor.execute("""
                SELECT 
                    p.id, p.name, p.manufacturer, p.price, p.piano_type_id 
                FROM pianos p
            """)
            
            pianos = []
            for row in cursor.fetchall():
                # Pretvaranje retka iz baze u Python objekt
                piano = Piano(
                    id=row['id'],
                    name=row['name'],
                    manufacturer=row['manufacturer'],
                    price=row['price'],
                    piano_type_id=row['piano_type_id']
                )
                pianos.append(piano)
            
            return pianos

        finally:
            conn.close()