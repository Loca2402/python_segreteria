from app.DTO.StudenteDTO import StudenteDTO
from app.Model.Studente import Studente


class StudenteMapper:
    @staticmethod
    def to_dto(studente: Studente) -> StudenteDTO:
        if not studente:
            return None
        return StudenteDTO(
            studenteId= studente.id,
            matricola= studente.matricola,
            nome= studente.nome,
            cognome= studente.cognome,
            data_nascita= studente.data_nascita
        )
