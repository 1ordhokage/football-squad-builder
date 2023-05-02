from fastapi import APIRouter, Depends

from src.players.schemas import PlayerRead
from src.players.service import PlayersService


router = APIRouter(
    prefix='/players',
    tags=['players']
)


@router.get('/{id}', response_model=PlayerRead)
async def get_player(id: int, players_service: PlayersService = Depends()):
    return await players_service.get_by_id(id)
