import pandas as pd
import psycopg2 as pg
from config import load_config

def connect(config):
  try:
    # Attempt connection to PostreSQL server
    print(config)
    with pg.connect(**config) as conn:
      print('Connected to the PostgreSQL server')
      return conn
  except (pg.DatabaseError, Exception) as error:
    print(error)

# Define a function that will take in relevant data from SCHEMA.csv files and create tables
def create_table():
    config = load_config()
    # Just testing db connections for now
    with connect(config) as conn:
        print(conn.status)
        pass

def main():
   # Loading in schema data to spin up tables
  tables_df = pd.read_csv('./data/INFORMATION_SCHEMA.csv', sep=',', quotechar='"', skipinitialspace=True)

  for index, row in tables_df.iterrows():
      #print(row['TABLE_NAME'] + ' ' + row['TABLE_SCHEMA'] + ' ' + str(row['ORDINAL_POSITION']) + ' ' + row['COLUMN_NAME'] + ' ' + row['DATA_TYPE'])
      pass

  create_table()

if __name__ == '__main__':
   main()