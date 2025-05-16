# Intermediate table for N:N relationship between TAG & POST
#
from sqlalchemy import Column, BigInteger, ForeignKey, Table
from src.db.base_class import Base

post_tag = Table(
  'post_tags', 
  Base.metadata, 
  Column('post_id', BigInteger, ForeignKey('posts.id')), 
  Column('tag_id', BigInteger, ForeignKey('tags.id'))
)