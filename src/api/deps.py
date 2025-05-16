# dependencies
#

from typing import Generator
from src.db.session import SessionLocal

# Start and close a DB Session 
def get_db() -> Generator:
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

