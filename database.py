# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql://postgres:062831@localhost/TodoApplicationDatabase"

## Render database url
DATABASE_URL = "postgresql://todosapplicationdatabase_lwxu_user:TyXkaa0v8fGnJRCbivoCk0GvvYzpuxXF@dpg-cp3k9gvsc6pc73fqli30-a.singapore-postgres.render.com/todosapplicationdatabase_lwxu"

# Create the synchronous engine
engine = create_engine(DATABASE_URL, echo=True)

# Create the session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
