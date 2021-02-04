# Proyecto de ejemplo de consulta xquery

Basex proporciona clientes para distintos lenguajes.  Vienen aquí: https://docs.basex.org/wiki/Clients

En java por ejemplo estamos bastante bien, hay un cliente totalmente autónomo (standalone), y por tanto no se necesita ninguna instancia de basex.

En python sin embargo, el cliente básicamente envía las peticiones a una instancia de basex que haya sido arrancada previamente. Además no utiliza un socket seguro, con lo que no es recomendable para un sistema en producción, en mi opinión. Este código utiliza los valores por defecto: host, puerto, usuario y contraseña. 

El cliente está en la carpeta BaseXClient, es bastante sencillo y viene, junto con algunos ejemplos, de aquí: https://github.com/BaseXdb/basex/tree/master/basex-api/src/main/python

Algunos ejemplos dan error si se ejecutan con python3, así que estoy ejecutando python a secas

Finalmente he incluido dos ejemplos: consulta y crud

## Consulta
Se trata sencilamente de un ejemplo de realización de consulta xquery a partir de un fichero xml. Requiere que basex esté instalado en la misma máquina en la que se ejecute la consulta (por el path del documento)

## CRUD
Xquery permite no solo consultas, sino inserts, updates, deletes, índices, etc. Vamos a ver un crud (create, read, update, delete), aunque sea solo a modo de ejemplo.

# Ejecución
- Arrancar el servidor (basexserver o basexhttp, recomiendo este último)
- El código utiliza los parámetros de host (localhost), puerto (1984), usuario y contraseña (admin en ambos casos) para conectarse. Están hardcodeados, y dos veces
- Una cosa interesante es comentar la línea del drop y ver cómo:
    - La base de datos sigue accesible en la gui
    - Su contenido se puede visualizar en la interfaz web
