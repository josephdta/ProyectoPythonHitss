import connexion
import six
#import json


from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.request_institution_add import RequestInstitutionAdd  # noqa: E501
from swagger_server.models.request_institution_upd import RequestInstitutionUpd  # noqa: E501
from swagger_server import util
from swagger_server.frameworks.db.sqlalchemy import SQLAlchemyClient
from flask.views import MethodView
from swagger_server.models.response400 import Response400
from swagger_server.repository.institution_repository import IntitutionRepository
from swagger_server.use_case.institution_use_case import InstitutionUseCase

class InstitutionView(MethodView):

    def __init__(self):
        sqlalchemy_client= SQLAlchemyClient()
        intitution_repository = IntitutionRepository(sqlalchemy_client)
        institution_usecase= InstitutionUseCase(intitution_repository)
        self.institution_usecase = institution_usecase

    def add_institution(self,body):  # noqa: E501
        """Agrega una nueva instituciÃ³n

        Agrega una nueva instituciÃ³n # noqa: E501

        :param body: Crea una nueva instituciÃ³n
        :type body: dict | bytes

        :rtype: InlineResponse200
        """        
        try:

            if connexion.request.is_json:
                body = RequestInstitutionAdd.from_dict(connexion.request.get_json())  # noqa: E501

            #Con esto podemos acceder a las propiedades del objeto 'body'    
            nombre= body.name
            direccion=body.address
            descripcion=body.description
            creado_user=body.created_user
            respon = self.institution_usecase.addd_institution(nombre,descripcion,direccion,creado_user)
                
            
        except Exception as ex:
                message = str(ex)
                respon= Response400(
                    code=-1,
                    message=message
                )
                

        return respon

    def delete_institution(self,institution_id):  # noqa: E501
        """Elimina una instituciÃ³n

        Elimina una instituciÃ³n # noqa: E501

        :param institution_id: Institution id to delete
        :type institution_id: int

        :rtype: InlineResponse200
        """
        self.institution_id = institution_id
        
        try:
            
            response = self.institution_usecase.delete_institution(self.institution_id)


        except Exception as ex:
            message = str(ex)
            response= Response400(
                code=-1,
                message=message
            )

        return response


    def get_institution(self):  # noqa: E501
        """Lista instituciones

        Lista instituciones # noqa: E501


        :rtype: InlineResponse200
        """
        try:
            
            response = self.institution_usecase.get_institution()


        except Exception as ex:
            message = str(ex)
            response= Response400(
                code=-1,
                message=message
            )
        
        return response


    def get_institution_by_id(self,institution_id):  # noqa: E501
        """Busca una instituciÃ³n por ID

        Busca una instituciÃ³n por ID # noqa: E501

        :param institution_id: Busca una instituciÃ³n por ID
        :type institution_id: int

        :rtype: InlineResponse200
        """

        self.institution_id = institution_id
        
        try:
            
            respo = self.institution_usecase.get_institution_by_id(self.institution_id)


        except Exception as ex:
            message = str(ex)
            respo= Response400(
                code=-1,
                message=message
            )

        return respo 

        
    def update_institution(self,body):  # noqa: E501
        """Actualiza una instituciÃ³n existente

        Actualiza una instituciÃ³n existente # noqa: E501

        :param body: Actualiza una instituciÃ³n existente
        :type body: dict | bytes

        :rtype: InlineResponse200
        """
        try:

            if connexion.request.is_json:
                body = RequestInstitutionUpd.from_dict(connexion.request.get_json())  # noqa: E501

            #Con esto podemos acceder a las propiedades del objeto 'body' 
            id= body.id   
            nombre= body.name
            direccion=body.address
            descripcion=body.description
            updated_user=body.updated_user
            respon = self.institution_usecase.update_institution(id,nombre,descripcion,direccion,updated_user)
                
            
        except Exception as ex:
                message = str(ex)
                respon= Response400(
                    code=-1,
                    message=message
                )
                

        return respon        
        
            
        
