from helper.WriteAJson import writeAJson
from db.database import Graph

db = Graph("bolt://54.236.32.197:7687", "neo4j", "egg-diseases-war")

data = db.execute_query("match (n) return n")
writeAJson(data, "all_data")

