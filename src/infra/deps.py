from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from database import Session

from sqlalchemy.exc import SQLAlchemyError
import logging


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session: AsyncSession = Session()
    try:
        yield session
    except SQLAlchemyError as e:
        logging.error(f'Database error: {e}')
        raise
    finally:
        await session.close()
