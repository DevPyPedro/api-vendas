from pydantic import BaseModel

class GetClientResponseDTO(BaseModel):
    status  : bool
    data   : list = None


class GetClientDTO(BaseModel):
    idcliente: int