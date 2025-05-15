# 
# Archivo para la lógica principal de la API 
# 
from fastapi import FastAPI
from src.core.config import settings
from src.db import base

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION, description=settings.PROJECT_DESCRIPTION)


