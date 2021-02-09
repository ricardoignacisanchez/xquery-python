from BaseXClient import BaseXClient

def crud():
    # create session
    # los siguientes son los valores por defecto de host, puerto, usuario y password
    session = BaseXClient.Session('localhost', 1984, 'admin', 'admin')

    try:
        # create empty database
        session.execute("create db prueba")
        print(session.info())

        # add document
        session.add("world/World.xml", "<x>Hello World!</x>")
        print(session.info())

        # add document
        session.add("Universe.xml", "<x>Hello Universe!</x>")
        print(session.info())

        # run query on database
        print("\n" + session.execute("xquery collection('prueba')"))



        # Vamos a ver, aunque sea de pasada, algunos ejemplos de
        # "insert, update y delete", tomados de https://docs.basex.org/wiki/XQuery_Update
        # documento de mayor complejidad
        session.add("documento.xml", """
        <html>
        <body>
        </body>
        </html>
        """)
        print("Documento xml (html) sin contenido en el body:\n" + session.execute("xquery serialize(html)"))

        # insert
        insert = session.query("""
        insert node (
          element article {
            attribute { "class" } { "principal" },
            <div>Ejemplo de elemento insertado (article con atributo, el article contiene un div)</div>
          }
        ) 
        into //body
        """)
        insert.execute()
        print(session.info())
        print("Documento tras insertar article con div:\n"+ session.execute("xquery serialize(html)"))

        # update - contenido
        update_contenido = session.query("""
            replace value of node //div
            with 'Ejemplo de elemento insertado (article con atributo, el article contiene un div) --modificado'
        """)
        update_contenido.execute()
        print(session.info())
        print("Documento tras actualizar el contenido del div:\n" + session.execute("xquery serialize(html)"))

        # update - renombrar etiqueta
        renombrar_etiqueta = session.query("""
            rename node //div as 'section'
        """)
        renombrar_etiqueta.execute()
        print(session.info())
        print("Documento tras cambiar el div por un section:\n" + session.execute("xquery serialize(html)"))

        # delete
        delete = session.query("""
            delete node //article
        """)
        print(delete.execute())
        print(session.info())
        print("Documento tras eliminar el article:\n" + session.execute("xquery serialize(html)"))

        # drop database
        print("\nFinalmente se borra la bd. Si se comenta el drop de abajo, la bd se mantiene accesible en la GUI (interesante)")
        session.execute("drop db prueba")

    finally:
        # close session
        if session:
            session.close()
