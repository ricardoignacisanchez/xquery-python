from BaseXClient import BaseXClient
import os

def consulta():
    # create session
    # los siguientes son los valores por defecto de host, puerto, usuario y pasword
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')
    directorio_actual = os.path.abspath(os.getcwd())

    try:
        consulta_xquery = """ 
            for $libro in doc("{ruta}/books.xml")//book
            order by $libro/title
            return $libro/title/text()
            """.format(ruta=directorio_actual)

        query = session.query(consulta_xquery)

        # imprimir resultado
        print(query.execute())

        # close query object
        query.close()

    finally:
        # close session
        if session:
            session.close()
