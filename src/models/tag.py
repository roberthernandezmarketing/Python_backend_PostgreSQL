# tags data table model 
#
from sqlalchemy import Boolean, Column, BigInteger, ForeignKey, String, DateTime, Table, Text
from sqlalchemy.orm import relationship
from src.db.base_class import Base
from src.models.post import post_tag

class Tag(Base):
  __tablename__ = "tags"
  id = Column(BigInteger, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)

  posts = relationship('Post', secondary=post_tag, back_populates='tags')

