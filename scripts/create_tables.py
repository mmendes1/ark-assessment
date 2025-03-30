import pandas as pd
import psycopg2 as pg
from connect import connect

def create_sql_query(schema_name, table_name, group):
    columns = ''
    for index, row in group.iterrows():
        column_name = row['COLUMN_NAME']
        data_type = row['DATA_TYPE']
        if(index == len(group) - 1):
            columns += (f'{column_name} {data_type}')
        else:
            columns += (f'{column_name} {data_type}, ')

    # Append createdAt and updatedAt columns here. Only append created if table name not accounts
    columns += ', created TIMESTAMP WITH TIME ZONE DEFAULT now(), modified TIMESTAMP WITH TIME ZONE'
    
    # Not a huge fan of this, as its kind of hacky to just try and create the schema each time I create a table. Maybe move schema creation to its own function?
    create_query = f'CREATE SCHEMA IF NOT EXISTS {schema_name}; CREATE TABLE {table_name} ({columns});'
    return create_query

def create_tables():
  # Loading in schema data to spin up tables
  tables_df = pd.read_csv('./data/INFORMATION_SCHEMA.csv', sep=',', quotechar='"', skipinitialspace=True)
  grouped_df = tables_df.groupby(['TABLE_SCHEMA', 'TABLE_NAME'])
  create_queries = []

  for table, group in grouped_df:
      schema_name = table[0]
      table_name = ".".join(name for name in table)
      group = group.sort_values(by='ORDINAL_POSITION')
      group = group.reset_index(drop=True)
      create_queries.append(create_sql_query(schema_name, table_name, group))
  
  conn = connect()
  cur = conn.cursor()
  for query in create_queries:
      print(f'Executing query: {query}')
      try:
          cur.execute(query)
          print(f'Query finished executing.')
      except(Exception, pg.Error) as error:
          print(error)
  cur.close()
  conn.commit()
  if conn is not None:
     conn.close()

if __name__ == '__main__':
   create_tables()