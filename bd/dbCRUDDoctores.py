from CRUDDoctores import Doctores
from dbPostgres import DBPostgresql

SCHEMA = {
    '_id': {
        'type': 'uuid',
    }, 
    'doctor_name': {
        'type': 'string',
        'min_length': 3,
        'max_length': 50
    }, 
    'speciality': {
        'type': 'string',
        'min_length': 5,
        'max_length': 100
    }, 
    'id_Hospital': {
        'type': 'uuid',
    }, 
}

class DBDoctors(DBPostgresql):

    def __init__(self):
        super().__init__(SCHEMA, 'Doctores')

    
    def save_doctor(self, Doctor):
        data = {
            'id_doctor':Doctor.id_doctor, 
            'doctor_name':Doctor.doctor_name, 
            'speciality':Doctor.speciality, 
            'id_Hospital':Doctor.id_Hospital, 
        }
        return self.insert(data)
    

    def update_doctor(self, id_object, data):
        if not id_object:
            raise ValueError('Debes envíar el id del Doctoro')
        if not data:
            raise ValueError('Debes envíar al menos un parámetro a actualizar')
        self.update(id_object, data)


    def delete_doctor(self, id_object):
        if not id_object:
            raise ValueError('Debes envíar el id del Doctoro')
        self.delete(id_object)


    def list_doctors(self):
        list_doctors = self.get_all()
        return self._create_object_doctors(list_doctors)

    
    def get_schema(self):
        return SCHEMA


    def search_doctors(self, filters):
        if not filters:
            raise ValueError('Debes envíar al menos un filtro')

        list_doctors = self.get_by_filters(filters)
        return self._create_object_doctors(list_doctors)


    def _create_object_doctors(self, list_doctors):

        if not list_doctors:
            return None

        object_doctors = []
        # Convertimos los datos a objectos de tipo Doctor
        for Doctor in list_doctors:
            c = Doctor(Doctor['_id'], Doctor['doctor_name'], Doctor['speciality'], Doctor['id_Hospital'])
            object_doctors.append(c)

        return object_doctors