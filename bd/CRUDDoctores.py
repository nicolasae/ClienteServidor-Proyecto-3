class Doctores:

    def __init__(self, id_doctor, id_hospital, doctor_name, speciality):
        self._id_doctor = id_doctor
        self.id_hospital = id_hospital
        self.doctor_name = doctor_name
        self.speciality = speciality

    @property
    def id_doctor(self):
        return self.id_doctor
    @id_doctor.setter
    def id_doctor(self, id):
        self.id_doctor = id
    @property
    def id_hospital(self):
        return self.id_hospital
    @id_hospital.setter
    def id_hospital(self, id):
        self.id_hospital = id

    @property
    def doctor_name(self):
        return self.doctor_name

    @doctor_name.setter
    def doctor_name(self, doctor_name):
        self.doctor_name = doctor_name

    @property
    def speciality(self):
        return self.speciality

    @speciality.setter
    def speciality(self, speciality):
        self.speciality = speciality