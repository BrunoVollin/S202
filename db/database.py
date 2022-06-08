from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.protocol import ProtocolException

class Database(object):
    def __init__(self, client_id,client_secret,keyspace):
        cloud_config = {
            'secure_connect_bundle': './secure-connect-socielmedia.zip'
        }
        auth_provider = PlainTextAuthProvider(client_id, client_secret)
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        self.session = cluster.connect()
        self.session.set_keyspace(keyspace)
    
    def create_table(self, query):
        try:
            self.session.execute(query)
        except ProtocolException as ex:
            print(f'Erro ao criar tabela: {ex}')

    def drop_table(self, table_name):
        try:
            query = f"DROP TABLE IF EXISTS {table_name}"
            self.session.execute(query)
        except ProtocolException as ex:
            print(f'Erro ao excluir tabela: {ex}')
    
    def execute_query(self, query):
        try:
            results = self.session.execute(query)
            return results
        except ProtocolException as ex:
            print(f'Erro ao executar query: {ex}')

    def insert_stories(self, id, deployed_by, created_at, remaining_hours, content_file, time_to_display, viewed_by):
        try:
            query= "INSERT INTO stories (id, deployed_by, created_at, remaining_hours, content_file, time_to_display, viewed_by)"\
            f"VALUES({id},'{deployed_by}','{created_at}',{remaining_hours},'{content_file}',{time_to_display},{viewed_by})"
            self.session.execute(query)
        except ProtocolException as ex:
            print(f'Erro ao inserir stories: {ex}')

    def select_stories(self):
        try:
            query= "SELECT * FROM stories"
            results = self.session.execute(query)
            if results:
                for row in results:
                    num_columns = len(row)
                    for column in range(num_columns):
                        print(row[column])
                    print('------------------')
                return results
            else:
                print("Não existem stories ativos no momento")
        except ProtocolException as ex:
            print(f'Erro ao buscar todos os stories: {ex}')

    def update_stories_viewed_by(self, id, deployed_by, created_at, remaining_hours, viewed_by):
        try:
            query= "UPDATE stories "\
            f"SET viewed_by = {viewed_by}"\
            f"WHERE id = {id} AND deployed_by = '{deployed_by}' AND created_at = '{created_at}'"\
            f"AND remaining_hours = {remaining_hours}"
            self.session.execute(query)
        except ProtocolException as ex:
            print(f'Erro ao atualizar stories: {ex}')

    def delete_stories(self, id, deployed_by, created_at, remaining_hours):
        try:
            query= "DELETE FROM stories "\
            f"WHERE id = {id} AND deployed_by = '{deployed_by}' AND created_at = '{created_at}'"\
            f"AND remaining_hours = {remaining_hours}"
            self.session.execute(query)
        except ProtocolException as ex:
            print(f'Erro ao excluir stories: {ex}')