import pandas as pd
from sqlalchemy import create_engine

# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:@localhost/{db}".format(user="root",db="fueleconomy2"))

#EXTRACT

data15 = pd.read_excel('2015 - Dataset.xls')

#TRANSFORM

# replacing spaces with _ for the column names
data15.rename(columns=lambda x: x.strip().lower().replace(" ","_"), inplace=True)

#LOAD
data15.to_sql('data15', con = engine, if_exists = 'append', chunksize = 1000)

print("fueleconomy2 database, data15 table is ready.")