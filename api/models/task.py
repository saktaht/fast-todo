from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
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
  id = Column(Integer, primary_key=True)
  title = Column(String(1024))
  
  # relationshipsはデーブル同士の関係性を定義
  done = relationship("Done", back_populates="task", cascade="delete")
  

class Done(Base):
  __tablename__ = "dones"
  
  id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)
  task = relationship("Task", back_populates="done")