from helper.write_a_json import write_a_json
from db.database import Graph


db = Graph("bolt://3.89.131.153:7687", "neo4j", "curls-magnetos-developments")

data = db.execute_query("match (n) return n")
write_a_json(data, "all_data")


data = db.execute_query("create (n:Person {name: 'John'}) return n")
write_a_json(data, "all_data")




