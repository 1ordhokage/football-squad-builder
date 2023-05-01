from fastapi import Depends, HTTPException, status

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.database import get_async_session
from src.players.models import Player


class PlayersService:
    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session

    async def get_by_id(self, id: int) -> Player:
        player = await self.session.scalar(
            select(Player)
            .where(Player.id == id)
        )
        if player is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Player not found."
            )
        return player

    async def get_by_name(self, name: str) -> list[Player]:
        pass
