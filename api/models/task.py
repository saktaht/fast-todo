from sqlalchemy import create_engine,Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from api.settings.config import get_env

Engine = create_engine( # SQLAlchemyがデータベースと通信するための「エンジン」を作成
    get_env().database_url,
    echo=False
)
Base = declarative_base()

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