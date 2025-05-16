# posts data table model 
#
from sqlalchemy import Boolean, Column, BigInteger, ForeignKey, String, DateTime, Table, Text
from sqlalchemy.orm import relationship
from src.db.base_class import Base
from datetime import datetime
from src.models.associations import post_tag

# Intermediate table for N:N relationship between TAG & POST
#   Move it to associations.py

class Post(Base):
  __tablename__ = "posts"
  id = Column(BigInteger, primary_key=True, index=True)
  title = Column(String, index=True)
  content = Column(Text)
  created_at = Column(DateTime, default=datetime.now)
  published_at = Column(DateTime, nullable=True)
  published = Column(Boolean, default=False)
  author_id = Column(BigInteger, ForeignKey('authors.id'))

  author = relationship('Author', back_populates='posts')
  tags = relationship('Tag', secondary=post_tag, back_populates='posts')
