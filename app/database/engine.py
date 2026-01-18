from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.config import appConfig

engine = create_async_engine(
    url=appConfig.postgres_dsn,
    echo=True,
    pool_size=5,
    max_overflow=10,
)

session_factory = async_sessionmaker(bind=engine)
