from create_tables import create_tables
from copy_data import copy_data, get_data_file_names
from answers import overdrawn_checking, overpaid_loans

def main():
    overdrawn_checking()
    overpaid_loans()

    # This is all to make the db tables and load data
    # create_tables()
    #files = get_data_file_names()
    #if(files is None or len(files) == 0):
    #    print('No non-schema csv files found in data directory.')
    #    pass # What about this? Is this right?
    #else:  
    #    copy_data(files)
     

if __name__ == '__main__':
    main()