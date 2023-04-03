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
        sql_id= (f"SELECT * FROM institution WHERE id={self.institution_id}")
        with self.session_factory() as session:
            rows12 = session.execute(sql_id)
        return rows12

    def adds_institution(self,name,description,address,created_user):
        self.name= name
        self.description= description
        self.address = address
        self.created_user = created_user
        sql_add= (f"INSERT INTO institution(name, description, address, created_user) VALUES ({self.name},{self.description},{self.address},{self.created_user})")
        sql_get= (f"SELECT * FROM institution WHERE name='{self.name}'")
        with self.session_factory() as session:
            session.execute(sql_add)
            session.commit()
            rowsadd = session.execute(sql_get)

        return rowsadd