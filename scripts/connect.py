import psycopg2 as pg
from config import load_config
  
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