from app.DTO import DipartimentoDTO
from app.Model import Dipartimento


class DipartimentoMapper:
    @staticmethod
    def to_dto(dipartimento: Dipartimento) -> DipartimentoDTO:
        if not dipartimento:
            return None
        return DipartimentoDTO(
            dipartimentoId= dipartimento.id,
            codice= dipartimento.codice,
            nome= dipartimento.nome
        )
