from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from api.settings.config import get_env

# 非同期エンジンを作成
Engine = create_async_engine(
    get_env().database_url,
    echo=False
)
# セッションを作成
SessionLocal = sessionmaker(bind=Engine, class_=AsyncSession, expire_on_commit=False)
                            
Base = declarative_base()

# Sessionを取得する依存関数
async def get_db():
  async with SessionLocal() as session:
    yield session

class Task(Base):
  __tablename__ = "tasks"
  
  # Columnは1つ1つのカラムを定義
  id: Mapped[int] = mapped_column(primary_key=True)
  title: Mapped[str] = mapped_column(String(1024))
  
  # relationshipsはデーブル同士の関係性を定義
  done: Mapped["Done"] = relationship(back_populates="task", cascade="delete")
  

class Done(Base):
  __tablename__ = "dones"
  
  id: Mapped[int] = mapped_column(ForeignKey("tasks.id"), primary_key=True)
  task: Mapped["Task"] = relationship(back_populates="done")