from ast import List

from sqlalchemy.orm import Session

from app.DTO.AteneoDTO import AteneoDTO
from app.DTO.AteneoMapper import AteneoMapper
from app.model.Ateneo import Ateneo
from app.repository.AteneoRepository import AteneoRepository


class AteneoService:
    @staticmethod
    def trova_tutti_atenei(db:Session)-> List[AteneoDTO]:
        atenei_db = AteneoRepository.get_all(db)
        return [AteneoMapper.to_dto(ateneo) for ateneo in atenei_db]

    @staticmethod
    def cerca_ateneo(db:Session, ateneoId:str)-> AteneoDTO:
        ateneo_db = AteneoRepository.get_by_id(db, ateneoId)
        if not ateneo_db:
            raise ValueError(f"ateneo con ID {ateneoId} non trovato")
        return AteneoMapper.to_dto(ateneo_db)

    @staticmethod
    def crea_ateneo(db:Session, ateneoDTO:AteneoDTO)-> AteneoDTO:
        gia_esiste=db.query(Ateneo).filter(Ateneo.nome==ateneoDTO.nome).first()
        if gia_esiste:
            raise ValueError("L'ateneo già esiste")
        nuovoAteneo= Ateneo(
            nome=ateneoDTO.nome,
            codice=ateneoDTO.codice,
            citta=ateneoDTO.citta,
        )
        ateneoSalvato=AteneoRepository.save(nuovoAteneo)
        return AteneoMapper.to_dto(ateneoSalvato)