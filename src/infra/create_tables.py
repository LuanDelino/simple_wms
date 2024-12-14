from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel import SQLModel


async def create_tables(engine: AsyncEngine) -> None:
    """Cria todas as tabelas do banco de dados."""
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
