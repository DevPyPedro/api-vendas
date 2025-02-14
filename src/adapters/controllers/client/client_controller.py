from fastapi import APIRouter, Depends, HTTPException

from src.app.use_case.client.client_use_case import ClientUseCase
from .client_depends import get_client_depends
from .client_models import GetClientResponseDTO

router = APIRouter()

@router.get("/all_clients", response_model=GetClientResponseDTO, tags=['Client'])  
async def filials(data: ClientUseCase =  Depends(get_client_depends)) -> dict:
    try:
        response = data.execute()
        return GetClientResponseDTO(**response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

