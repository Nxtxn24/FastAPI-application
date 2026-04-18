from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///./test.db"


engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Session (talk to DB)
SessionLocal = sessionmaker(bind=engine)

# 4. Base (for models)
Base = declarative_base()