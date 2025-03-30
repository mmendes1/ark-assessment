import psycopg2 as pg
from config import load_config

# Not sure if I should be using the load_config() call as a default arg
def connect(config=load_config()):
  try:
      # Attempt connection to PostreSQL server
      print(config)
      with pg.connect(**config) as conn:
          print('Connected to the PostgreSQL server')
          return conn
  except (pg.DatabaseError, Exception) as error:
      print(error)

if __name__ == '__main__':
    config = load_config()
    connect(config)