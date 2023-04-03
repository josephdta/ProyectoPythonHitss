sql_select= "SELECT * FROM institution WHERE status = 'A'"


class IntitutionRepository:
    def __init__(self, mysql_client):
        self.session_factory = mysql_client.session_factory 
    

    def get_institution(self):
        """
        Resuelve la consulta a la base de datos
        """
        with self.session_factory() as session:
            rowss = session.execute(sql_select)
            return rowss 

    def get_institution_by_id(self, institution_id):
        self.institution_id = institution_id
        #Le pasamos la consulta a la base de datos con el id que llega por parámetro. 
        sql_id= (f"SELECT * FROM institution WHERE id={self.institution_id}")
        with self.session_factory() as session:
            rows12 = session.execute(sql_id)
        return rows12

    def adds_institution(self,name,description,address,created_user):
        self.name= name
        self.description= description
        self.address = address
        self.created_user = created_user
        #Sentencia que ingresa una nueva fila a la tabla con los parámetros que llegan.
        sql_add= (f"INSERT INTO institution(name, description, address, created_user) VALUES ('{self.name}','{self.description}','{self.address}','{self.created_user}')")
        
        #Sentencia para leer la tabla ingresada; usamos el nombre que llega como parámetro.
        sql_get= (f"SELECT * FROM institution WHERE name='{self.name}'")
        with self.session_factory() as session:
            session.execute(sql_add)
            session.commit() #Método para guardar los cambios en la database.
            rowsadd = session.execute(sql_get)
        return rowsadd
    
    def delete_institution(self,intitution_id):
        self.intitution_id= intitution_id
        #Le pasamos el id a la sentencia para consultar y borrar la fila
        sql_get= (f"SELECT * FROM institution WHERE id={self.intitution_id}")
        sql_borrar= (f"DELETE FROM institution WHERE id={self.intitution_id}")
        
        with self.session_factory() as session:
            rowsid = session.execute(sql_get)
            session.execute(sql_borrar)
            session.commit()
        return rowsid

        