# config 
from pydantic_settings import BaseSettings

class Settings (BaseSettings):
    PROJECT_NAME: str = 'FastAPI-Blog'
    PROJECT_VERSION: str = '0.0.1'
    PROJECT_DESCRIPTION: str = 'This is my very first time setting a real backend !!! 🐘💻🛢️🚀⚙️'  
    DATABASE_URL: str 

class Config:
  env_file = '.env'

settings = Settings()