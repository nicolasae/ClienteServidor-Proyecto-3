from .CRUDHospitales import *
from .dbPostgres import *

SCHEMA = {
    '_id': {
        'type': 'uuid',
    }, 
    'hospital_name': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    }, 
}

class DBHospitals(DBPostgresql):

    def __init__(self):
        super().__init__(SCHEMA, 'Hospitales')

    
    def save_hospital(self, Hospital):
        data = {
            '_id':Hospital._id, 
            'hospital_name':Hospital.hospital_name, 
        }
        return self.insert(data)
    

    def update_hospital(self, id_object, data):
        if not id_object:
            raise ValueError('Debes envíar el id del Hospitalo')
        if not data:
            raise ValueError('Debes envíar al menos un parámetro a actualizar')
        self.update(id_object, data)


    def delete_hospital(self, id_object):
        if not id_object:
            raise ValueError('Debes envíar el id del Hospitalo')
        self.delete(id_object)


    def list_hospitals(self):
        list_hospitals = self.get_all()
        return self._create_object_hospitals(list_hospitals)

    
    def get_schema(self):
        return SCHEMA


    def search_hospitals(self, filters):
        if not filters:
            raise ValueError('Debes envíar al menos un filtro')

        list_hospitals = self.get_by_filters(filters)
        return self._create_object_hospitals(list_hospitals)


    def _create_object_hospitals(self, list_hospitals):

        if not list_hospitals:
            return None

        object_hospitals = []
        # Convertimos los datos a objectos de tipo Hospital
        for Hospital in list_hospitals:
            c = Hospital(Hospital['_id'], Hospital['hospital_name'])
            object_hospitals.append(c)

        return object_hospitals