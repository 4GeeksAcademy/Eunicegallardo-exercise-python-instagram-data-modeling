import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), index=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    Comment_text = Column(String(50))
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship(Post)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum('videos', 'image'))
    url = Column(String(150), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    post = relationship(Post)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
