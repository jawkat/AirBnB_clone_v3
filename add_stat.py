from os import chmod
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import State  # Import your State model

# Create engine and session
engine = create_engine('mysql://username:password@localhost/database_name')
Session = sessionmaker(bind=engine)
session = Session()

# Create a new State object
new_state = State(name='New York')

# Add the State object to the session
session.add(new_state)

# Commit the session to persist the changes
session.commit()

# Close the session
session.close()
