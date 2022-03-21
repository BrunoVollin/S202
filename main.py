from unicodedata import name
from db.database import Database
from helper.WriteAJson import writeAJson
from dataset.produto_database import dataset

db = Database(database="crud", collection="pessoas", dataset=dataset)







