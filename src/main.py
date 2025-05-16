# 
# Archivo para la lógica principal de la API  
# 
from fastapi import FastAPI
from src.core.config import settings
from src.api.routes import tags, authors, posts

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION, description=settings.PROJECT_DESCRIPTION)

app.include_router(tags.router, prefix='/tags', tags=['TAGS by rh'])
