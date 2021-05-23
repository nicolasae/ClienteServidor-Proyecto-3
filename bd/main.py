import os
import time
# from classes.validations import Validations
from CRUDDoctores import Doctores
from CRUDHospitales import Hospital
from dbCRUDDoctores import DBDoctors
from dbCRUDHospitales import DBHospitals
from dbPostgres import DBPostgresql
# from prettytable import PrettyTable
# validator = Validations()
db = DBHospitals()


def print_options():
    print('AGENDA DE CONTACTOS')
    print('*' * 50)
    print('Selecciona una opción:')
    print('[C]rear contacto')
    print('[L]istado de contactos')
    print('[M]odificar contacto')
    print('[E]liminar contacto')
    print('[B]uscar contacto')
    print('[S]ALIR')


def check_data(message, data_name, force = True):
    print(message)
    input_data = input()
    if not force and not input_data:
        return input_data
    # try:
        # getattr(validator, f'validate{data_name.capitalize()}')(input_data)
        # return input_data
    # except ValueError as err:
    #     print(err)
    #     return check_data(message, data_name, force)


def create_Doctor():

    print('CREACIÓN')
    print('*' * 50)
    name = check_data('Inserta el nombre:', 'name')
    speciality = check_data('Inserta la especialidad:', 'speciality')

    contact = Doctores(None, name,speciality)
    if db.save(contact):
        print('Contacto insertado con éxito')
    else:
        print('Error al guardar el contacto')

def create_Hospital():

    print('CREACIÓN')
    print('*' * 50)
    name = check_data('Inserta el nombre:', 'name')
    id = 'a260f55a-bb54-11eb-8529-0242ac130003'

    contact = Hospital(None,id,name)
    if db.save(contact):
        print('Contacto insertado con éxito')
    else:
        print('Error al guardar el contacto')

def lists():
    lists = db.lists()

    if not lists:
        return print('Todavía no hay contactos guardados')

    _print_tables(lists)


def search():

    filters = {}
    print('Introduce un nombre (vacío para usar otro filtro):')
    nombre = input()
    if nombre:
        filters['name'] = nombre
    print('Introduce un apellido (vacío para usar otro filtro):')
    apellidos = input()
    if apellidos:
        filters['surname'] = apellidos
    print('Introduce un email (vacío para usar otro filtro):')
    email = input()
    if email:
        filters['email'] = email

    try:
        lists = db.searchs(filters)
        if not lists:
            return print('No hay ningún contacto con esos criterios de búsqueda')

        _print_tables(lists)
    except ValueError as err:
        print(err)
        time.sleep(1)
        search()


def update():

    lists()

    print('Introduce el id del contacto que quieres actualizar:')
    id_object = input()

    data = {}
    nombre = check_data('Introduce un nombre (vacío para mantener el nombre actual):', 'name', False)
    if nombre:
        data['name'] = nombre
    apellidos = check_data('Introduce un apellido (vacío para mantener los apellidos actuales):', 'surname', False)
    if apellidos:
        data['surname'] = apellidos
    email = check_data('Introduce un email (vacío para mantener el email actual):', 'email', False)
    if email:
        data['email'] = email
    phone = check_data('Introduce un teléfono (vacío para mantener el teléfono actual):', 'phone', False)
    if phone:
        data['phone'] = phone
    birthday = check_data('Introduce una fecha de nacimiento YYYY-MM-DD (vacío para mantener la fecha actual):', 'birthday', False)
    if birthday:
        data['birthday'] = birthday
    
    try:
        res = db.update(id_object, data)
        if res:
            print('Contacto actualizado con éxito')
    except Exception as err:
        print(err)
        time.sleep(1)
        update()

def delete():
    lists()

    print('Introduce el id del contacto que quieres eliminar:')
    id_object = input()
    try:
        res = db.delete(id_object)
        if res:
            print('Contacto eliminado con éxito')
    except Exception as err:
        print(err)
        time.sleep(1)
        delete()
    

def _print_tables(lists):
    table = PrettyTable(db.get_schema().keys())
    for contact in lists:
        table.add_row([
            contact.id,
            contact.name,
            contact.surname,
            contact.email,
            contact.phone,
            contact.birthday
        ])

    print(table)
    print('Pulsa cualquier letra para continuar')
    command = input()

def run():

    print_options()

    command = input()
    command = command.upper()

    if command == 'C':
        create_Hospital()
    elif command == 'L':
        lists()
    elif command == 'M':
        update()
    elif command == 'E':
        delete()
    elif command == 'B':
        search()
    elif command == 'S':
        os._exit(1)
    else:
        print('Comando inválido')

    time.sleep(1)
    run()

if __name__ == "__main__":
    run()