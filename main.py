from helper.write_a_json import write_a_json
from db.database import Graph


class PersonCRUD(object):
    def __init__(self):
        self.db = Graph(uri='bolt://44.203.219.42:7687',
                        user='neo4j', password='masses-streets-debt')

    def create(self, person):
        return self.db.execute_query('CREATE (n:Person {name:$name, age:$age}) return n',
                                {'name': person['name'], 'age':person['age']})

    def read_by_name(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) RETURN n',
                                {'name': person['name']})

    def update_age(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) SET n.age = $age RETURN n',
                                {'name': person['name'], 'age':person['age']})

    def delete(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) DELETE n',
                                {'name': person['name']})

    def delete_all_nodes(self):
        return self.db.execute_query('MATCH (n) DETACH DELETE n')


    def create_relation(self, person1, person2, year):
        return self.db.execute_query('MATCH (n:Person {name:$name1}), (m:Person {name:$name2}) CREATE (n)-[r:KNOWS{year: $year}]->(m) RETURN n, r, m',
                                {'name1':person1['name'], 'name2': person2['name'], 'year': year})

    def read_relation(self, person1, person2):
        return self.db.execute_query('MATCH (n:Person {name:$name1})-[r]->(m:Person {name:$name2}) RETURN n, r, m',
                                {'name1':person1['name'], 'name2': person2['name']})


john = {
    'name': 'John',
    'age': 30
}

amanda = {
    'name': 'Amanda',
    'age': 27
}

db = PersonCRUD()

db.delete_all_nodes()
aux = db.create(amanda)
aux = db.create(john)
aux = db.create_relation(john, amanda, 2018)
write_a_json(aux, "zxasxs")
