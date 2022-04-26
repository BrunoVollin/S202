from helper.write_a_json import write_a_json
from db.database import Graph

db = Graph(uri='bolt://35.172.240.205:7687', user='neo4j', password='humps-child-needle')

# Create Entity's
db.execute_query('CREATE (n:Person {name:"John", age:30})')
db.execute_query('CREATE (n:Person {name:"Mary", age:25})')
db.execute_query('CREATE (n:Person {name:"Peter", age:35})')

# Create Relation's
db.execute_query('MATCH (n:Person) WHERE n.name = "John" CREATE (n)-[:KNOWS]->(m:Person {name:"Mary", age:25})')
db.execute_query('MATCH (n:Person) WHERE n.name = "John" CREATE (n)-[:KNOWS]->(m:Person {name:"Peter", age:35})')

# Read Entity's
aux = db.execute_query('MATCH (n) RETURN n')
write_a_json(aux, 'read')

# Read Relation's
aux = db.execute_query('MATCH (n)-[r]->(m) RETURN n, r, m')
write_a_json(aux, 'read')

# Update Entity's
db.execute_query('MATCH (n:Person {name:"John"}) SET n.age = 31')

# Update Relation's
db.execute_query('MATCH (n:Person {name:"John"})-[r]->(m:Person {name:"Mary"}) SET r.since = "2018-01-01"')

# Delete Entity's
db.execute_query('MATCH (n:Person {name:"Peter"}) DELETE n')

# Delete Relation's
db.execute_query('MATCH (n:Person {name:"John"})-[r]->(m:Person {name:"Peter"}) DELETE r')


