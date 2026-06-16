from app.DTO.AteneoDTO import AteneoDTO
from app.Model.Ateneo import Ateneo


class AteneoMapper:
    @staticmethod
    def to_dto(ateneo: Ateneo) -> AteneoDTO:
        if not ateneo:
            return None
        return AteneoDTO(
            ateneoId=ateneo.id,
            nome=ateneo.nome,
            codice=ateneo.codice,
            citta=ateneo.citta
        )
