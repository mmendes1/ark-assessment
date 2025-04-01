import psycopg2 as pg
import os
import pandas as pd
from connect import connect

# Is it bad practice to have this variable floating around?
path = 'C:/git/ark-assessment/data/'

# Get list of file names in data directory (exclude schema files)
def get_data_file_names():
    try:
        files = []
        dir_data = os.scandir(path)
        for entry in dir_data:
            # Ensure we are only checking non-schema csv files
            if entry.is_file() and not entry.name.__contains__('SCHEMA') and entry.name.__contains__('.csv'):
                files.append(entry.name)
        return files
    except Exception as err:
        print(f'Error reading data directory: {err}')

# Read and return columns from file at given path
def get_columns_from_file(path):
    try:
        df = pd.read_csv(path)
        columns_list = list(df.columns)
        if(len(columns_list) > 0):
            lowercase_list = [col.lower() for col in columns_list]
            return lowercase_list 
        else:
            print(f'No columns found at path: {path}')
    #TODO: Better error message here
    except Exception as err:
        print('Here is some error: {err}')

def copy_data(files):
    try:
        conn = connect()
        # Why does this need to be set to true for changes to take effect?
        conn.autocommit = True
        cur = conn.cursor()
        # Fetch column names
        for file in files:
            file_path = path + file
            table_name = file.replace('.csv', '')
            columns = get_columns_from_file(file_path)
            # Connect to db and copy data
            #TODO: Find a way to fetch schema dynamically if possible
            copy_query = f'COPY dbo.{table_name.lower()} ({",".join(columns)}) FROM \'{file_path}\' DELIMITER \',\' CSV HEADER;'
            print(f'{copy_query}')
            try:
                cur.execute(copy_query)
            except(pg.DatabaseError) as err:
                print(f'Error executing copy data query: {err}')
        pass
    except (Exception, pg.DatabaseError) as err:
        print(f'Error: {err}') # Need to made this better

# I feel like I am not using this correctly as I just call copy_data() from main.py
if __name__ == '__main__':
  files = get_data_file_names()
  # Make sure we have files to process
  if files is not None and len(files) > 0:
      copy_data(files)
  else:
      print('No non-schema csv files found in data directory.')