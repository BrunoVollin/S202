from db.database import Database
from helper.write_a_json import write_a_json as wj

db = Database(client_id='EXAYiSGKJoEeBofizyGshiuI',
    client_secret='-f8rZGv,gZ8pWUSp98wO+Du,FzB7E,ndfewDO+M3M48YbCBFvCFnsNzy8EzBQtU2.aArA55LdXi11Ua9XvhSdYbjobdUcyBpZZTAGs2X68yKwCgFysDj0wtbez0yC_qM',
    keyspace='instagram')

db.select_stories()


