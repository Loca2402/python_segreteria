from app.DTO.CorsoDTO import CorsoDTO
from app.Model.Corso import Corso


class CorsoMapper:
    @staticmethod
    def to_dto(corso: Corso) -> CorsoDTO:
        if not corso:
            return None
        return CorsoDTO(
            corsoId= corso.id,
            codice= corso.codice,
            nome= corso.nome,
            anno_accademico= corso.anno_accademico,
            tipo_titolo= corso.tipo_titolo
        )
