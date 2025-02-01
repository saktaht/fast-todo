import os
from functools import lru_cache
from pydantic_settings import BaseSettings #pydanticのは使えなくなってた

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Environment(BaseSettings):
    """ 環境変数を読み込む
    """
    database_url: str
    db_user: str
    db_pass: str
    db_name: str
    db_port: str

    model_config = {
        "env_file": ".env"
    }

@lru_cache
def get_env():
    """
    @lru_cacheで.envの結果をキャッシュする / パフォーマスが向上する
    """
    return Environment()
