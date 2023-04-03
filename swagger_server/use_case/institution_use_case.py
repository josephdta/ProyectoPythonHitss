from swagger_server.models.response_institution import ResponseInstitution
from swagger_server.models.response_institution_data import ResponseInstitutionData
#from swagger_server.models.request_institution_add import RequestInstitutionAdd


class InstitutionUseCase:
    
    def __init__(self, intitution_repository):
        self.intitution_repository= intitution_repository

    def get_institution(self):
        """
        Resuelve los casos de uso del endpoint Get 
        """
        data_response= []
        institutions = self.intitution_repository.get_institution()

        for i in institutions:
            data_response.append(
                ResponseInstitutionData(
                    id =i.id,
                    name =i.name,
                    description =i.description,
                    address =i.address
                    )
                )

        response = ResponseInstitution(
            code=0, 
            message= "Proceso exitoso",
            data = data_response
        )

        return response
    

    def get_institution_by_id(self,intitution_id):     
        self.intitution_id = intitution_id
        data_responde= []
        institutions2 = self.intitution_repository.get_institution_by_id(self.intitution_id)

        for i in institutions2:
            data_responde.append(
                ResponseInstitutionData(
                    id =i.id,
                    name =i.name,
                    description =i.description,
                    address =i.address
                    )
                )
        responde = ResponseInstitution(
            code=0, 
            message= "Proceso exitoso",
            data = data_responde
            )

        return responde

    def addd_institution(self,nombre,descripcion,direccion,usuario_creado):  # noqa: E501
        """        Resuelve los casos de uso del endpoint Add institution

        """
        self.nombre= nombre
        self.descripcion= descripcion
        self.direccion= direccion
        self.usuario_creado=usuario_creado

        data_repo=[]
        institutions3 = self.intitution_repository.adds_institution(self.nombre,self.descripcion,self.direccion,self.usuario_creado)

        for i in institutions3:
            data_repo.append(
                ResponseInstitutionData(
                   
                    name =i.name,
                    description =i.description,
                    address =i.address,
                    created_user=i.created_user
                    )
                )
        responder = ResponseInstitution(
            code=0, 
            message= "Proceso exitoso",
            data = data_repo
            )

        return responder

    def delete_institution(self,intitution_id):     
        self.intitution_id = intitution_id
        data_responder= []
        institutions4 = self.intitution_repository.delete_institution(self.intitution_id)

        for i in institutions4:
            data_responder.append(
                ResponseInstitutionData(
                    id =i.id,
                    name =i.name,
                    description =i.description,
                    address =i.address
                    )
                )
        responde = ResponseInstitution(
            code=0, 
            message= "Proceso exitoso",
            data = data_responder
            )

        return responde