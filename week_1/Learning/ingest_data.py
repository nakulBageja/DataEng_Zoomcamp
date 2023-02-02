# Script for uploading the data to postgres db

## Steps

# 1. Downloading data and putting in data folder
# 2. Importing data using pandas
# 3. Creating connection to postgres using SQLAlchemy library
# 4. Creating Schema for data
#     1. Throws error of module not found psycopg2 -- Resolution - python -m pip install psycopg2-binary 
# 5. Uploading data in postgres db in batches since the data is too big for one time upload.
#     1. Creating the table.
#     2. Uploading the table data in batches (100000)

# Import for Data Manipulation
import pandas as pd

# Import for connecting to database
from sqlalchemy import create_engine

# Import for monitoring
from time import time

import argparse
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = params.csv_name
    download_dir_path = params.dir
    
    # Downloading the csv file
    os.system(f'wget {url} -O {download_dir_path}/{csv_name}')
    
    
    # Connection string for local-machine
    # engine = create_engine('postgresql://postgres:root@localhost:5432/ny_taxi')

    # Connection string for GCP
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    engine.connect()

    # Create schema for DF
    print(pd.io.sql.get_schema(df,name=table_name,con=engine))

    # Creating an iterator

    df_iter = pd.read_csv(csv_name,iterator=True,chunksize=100000)

    # Getting first batch
    df = next(df_iter)

    # Converting the datatypes
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # Creating the table in PostgresSQL
    df.head(n=0).to_sql(name=table_name,con=engine,if_exists='replace')

    # Uploading first batch of data
    df.to_sql(name=table_name,con=engine,if_exists='append')

    # Uploading batches of data in db
    while True:
        t_start = time()
        df = next(df_iter) 

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name=table_name,con=engine,if_exists='append')

        t_end = time()

        print('Inserted another chunk, took %.3f second' % (t_end - t_start))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = "Ingest CSV Data to Postgres")
    parser.add_argument('--user', help='User name for postgres')
    parser.add_argument('--password', help='Password for postgres')
    parser.add_argument('--host', help='Host name for postgres')
    parser.add_argument('--port', help='Port for postgres')
    parser.add_argument('--db', help='Database name for postgres')
    parser.add_argument('--table_name', help='name of the table for postgres')
    parser.add_argument('--url', help='Url of the csv file')
    parser.add_argument('--dir',help='Specify download directory for input files')
    parser.add_argument('--csv_name',help='Specify name of csv for input files')
    args = parser.parse_args()
    
    main(args)