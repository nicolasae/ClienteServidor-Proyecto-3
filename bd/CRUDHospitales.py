class Hospital:

    def __init__(self, id_hospital, hospital_name):
        self.id_hospital = id_hospital
        self.hospital_name = hospital_name

    @property
    def id_doctor(self):
        return self.id_doctor
    @id_doctor.setter
    def id_doctor(self, id):
        self.id_doctor = id

    @property
    def hospital_name(self):
        return self.hospital_name

    @hospital_name.setter
    def hospital_name(self, hospital_name):
        self.hospital_name = hospital_name