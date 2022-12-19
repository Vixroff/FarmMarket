from ETL.transform import transform

from model.csv.request import write
from model.csv.db import create_db


def load():
    create_db()
    data = transform()
    path_to_db_folders = [
        ('addresses', 'db/Addresses.csv'), ('categories', 'db/Categories.csv'), ('cities','db/Cities.csv'), 
        ('counties', 'db/Counties.csv'), ('markets', 'db/Markets.csv'), ('markets_categories', 'db/MarketsCategories.csv'),
        ('markets_payments', 'db/MarketsPayments.csv'), ('payments', 'db/Payments.csv'), ('season1', 'db/Season1.csv'),
        ('season2', 'db/Season2.csv'), ('season3', 'db/Season3.csv'), ('season4', 'db/Season4.csv'),
        ('states', 'db/States.csv'), ('zips', 'db/Zips.csv')]
    for item in path_to_db_folders:
        write(data[item[0]], item[1])


if __name__ == "__main__":
    load()
