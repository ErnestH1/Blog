from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# SQLAlchemy configurations
# Replace 'BLOG' with your actual database name and 'Blog363' with your password
SQLALCHEMY_DATABASE_URL = "postgresql://BLOG:Blog363@localhost/BLOG"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Import models
from app.models.user import User
from app.models.post import Post
from app.models.comment import Comment

# Create tables
Base.metadata.create_all(bind=engine)

# Your FastAPI routes and other configurations can be added below
# For example:
@app.get("/")
async def read_root():
    return {"message": "Hello, this is your FastAPI application!"}
