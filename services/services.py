from core.models import Piano, PianoType
from infrastructure.repositories import PianoRepository

class PianoService:
    """
    Rukuje poslovnom logikom vezanom za klavire. 
    Koristi PianoRepository za pristup podacima.
    """
    
    def __init__(self, repository: PianoRepository):
        # Service prima instancu Repositoryja - ovo je ključno za dobru arhitekturu
        self.repository = repository
        # Možemo unaprijed učitati sve tipove klavira jer se rijetko mijenjaju
        self._piano_types_cache = self._load_piano_types_cache()

    def _load_piano_types_cache(self) -> dict[int, PianoType]:
        """
        Pomoćna metoda koja dohvaća tipove klavira i sprema ih kao rječnik (cache).
        Ključ rječnika je ID tipa.
        """
        types = self.repository.get_all_piano_types()
        # Vraća rječnik u formatu: {1: PianoType(id=1, name='Digitalni'), 2: ...}
        return {p_type.id: p_type for p_type in types}


    def get_pianos_with_details(self) -> list[dict]:
        """
        Dohvaća sve klavire i "spaja" Piano objekt s detaljima o njegovom tipu.
        Ovo je primjer kompleksnije poslovne logike.
        """
        pianos = self.repository.get_all_pianos()
        
        # Lista za rezultat koja sadrži i detalje
        result_list = []
        
        for piano in pianos:
            # Dohvaćamo cijeli PianoType objekt iz cachea koristeći piano_type_id
            piano_type = self._piano_types_cache.get(piano.piano_type_id)
            
            # Pripremamo rječnik za prikazivanje u glavnom izborniku
            piano_details = {
                'ID': piano.id,
                'Naziv': piano.name,
                'Proizvođač': piano.manufacturer,
                'Cijena (€)': f"{piano.price:.2f}",
                # Ovdje dodajemo puno ime tipa iz spojenog objekta
                'Tip': piano_type.name if piano_type else 'Nepoznato',
                'Opis Tipa': piano_type.description if piano_type else ''
            }
            result_list.append(piano_details)
            
        return result_list