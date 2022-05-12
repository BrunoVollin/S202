from pprintpp import pprint as pp
from db.database import Graph


class PersonDAO(object):
    def __init__(self):
        self.db = Graph(uri='bolt://52.91.64.64:7687',
                        user='neo4j', password='board-apparatuses-smashes')

    def create(self, person):
        return self.db.execute_query('CREATE (n:Person {name:$name, age:$age}) return n',
                                     {'name': person['name'], 'age': person['age']})

    def read_by_name(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) RETURN n',
                                     {'name': person['name']})
    
    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def update_age(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) SET n.age = $age RETURN n',
                                     {'name': person['name'], 'age': person['age']})

    def delete(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) DELETE n',
                                     {'name': person['name']})

    def delete_all_nodes(self):
        return self.db.execute_query('MATCH (n) DETACH DELETE n')

    def create_relation(self, person1, person2, year):
        return self.db.execute_query('MATCH (n:Person {name:$name1}), (m:Person {name:$name2}) CREATE (n)-[r:KNOWS{year: $year}]->(m) RETURN n, r, m',
                                     {'name1': person1['name'], 'name2': person2['name'], 'year': year})

    def read_relation(self, person1, person2):
        return self.db.execute_query('MATCH (n:Person {name:$name1})-[r]->(m:Person {name:$name2}) RETURN n, r, m',
                                     {'name1': person1['name'], 'name2': person2['name']})

def divider():
    print('\n' + '-' * 80 + '\n')

dao = PersonDAO()

while 1:    
    option = input('1. Create\n2. Read\n3. Update\n4. Delete\n')

    if option == '1':
        name = input('  Name: ')
        age = input('   Age: ')
        person = {
            'name': name,
            'age': age
        }
        aux = dao.create(person)
        divider()

    elif option == '2':
        aux = dao.read_all_nodes()
        pp(aux)
        divider()

    elif option == '3':
        name = input('  Name: ')
        age = input('   Age: ')
        person = {
            'name': name,
            'age': age
        }
        
        aux = dao.update_age(person)
        divider()

    elif option == '4':
        name = input('  Name: ')
        person = {
            'name': name
        }
        
        aux = dao.delete(person)
        divider()

    else:
        break

dao.db.close()