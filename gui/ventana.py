# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(958, 676)
        MainWindow.setMinimumSize(QtCore.QSize(0, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Consulta = QtWidgets.QFrame(self.centralwidget)
        self.Consulta.setGeometry(QtCore.QRect(280, 10, 421, 211))
        self.Consulta.setStyleSheet("background-color: #AAA;  color:blue")
        self.Consulta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Consulta.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Consulta.setObjectName("Consulta")
        self.botonConsultarIdDoc = QtWidgets.QPushButton(self.Consulta)
        self.botonConsultarIdDoc.setGeometry(QtCore.QRect(280, 70, 89, 25))
        self.botonConsultarIdDoc.setObjectName("botonConsultarIdDoc")
        self.labelHospital = QtWidgets.QLabel(self.Consulta)
        self.labelHospital.setGeometry(QtCore.QRect(60, 140, 67, 17))
        self.labelHospital.setObjectName("labelHospital")
        self.labelDoctor = QtWidgets.QLabel(self.Consulta)
        self.labelDoctor.setGeometry(QtCore.QRect(60, 80, 67, 17))
        self.labelDoctor.setObjectName("labelDoctor")
        self.butonConsultaNombreHospital = QtWidgets.QPushButton(self.Consulta)
        self.butonConsultaNombreHospital.setGeometry(QtCore.QRect(290, 140, 89, 25))
        self.butonConsultaNombreHospital.setObjectName("butonConsultaNombreHospital")
        self.tituloConsulta = QtWidgets.QLabel(self.Consulta)
        self.tituloConsulta.setGeometry(QtCore.QRect(180, 20, 67, 17))
        self.tituloConsulta.setObjectName("tituloConsulta")
        self.inputIdDoctorConsulta = QtWidgets.QLineEdit(self.Consulta)
        self.inputIdDoctorConsulta.setGeometry(QtCore.QRect(140, 70, 113, 25))
        self.inputIdDoctorConsulta.setObjectName("inputIdDoctorConsulta")
        self.inputNombreHospital = QtWidgets.QLineEdit(self.Consulta)
        self.inputNombreHospital.setGeometry(QtCore.QRect(140, 140, 131, 25))
        self.inputNombreHospital.setObjectName("inputNombreHospital")
        self.CRUD = QtWidgets.QFrame(self.centralwidget)
        self.CRUD.setGeometry(QtCore.QRect(10, 240, 431, 391))
        self.CRUD.setStyleSheet("background-color: #AAA;  color:blue")
        self.CRUD.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.CRUD.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CRUD.setObjectName("CRUD")
        self.botonAgregarDoc = QtWidgets.QPushButton(self.CRUD)
        self.botonAgregarDoc.setGeometry(QtCore.QRect(170, 120, 91, 25))
        self.botonAgregarDoc.setObjectName("botonAgregarDoc")
        self.tituloCRUDDoc = QtWidgets.QLabel(self.CRUD)
        self.tituloCRUDDoc.setGeometry(QtCore.QRect(170, 20, 111, 17))
        self.tituloCRUDDoc.setObjectName("tituloCRUDDoc")
        self.botonEliminarDoc = QtWidgets.QPushButton(self.CRUD)
        self.botonEliminarDoc.setGeometry(QtCore.QRect(230, 180, 89, 25))
        self.botonEliminarDoc.setObjectName("botonEliminarDoc")
        self.botonActualizarDoc = QtWidgets.QPushButton(self.CRUD)
        self.botonActualizarDoc.setGeometry(QtCore.QRect(160, 290, 91, 25))
        self.botonActualizarDoc.setObjectName("botonActualizarDoc")
        self.inputHospitalDoc = QtWidgets.QLineEdit(self.CRUD)
        self.inputHospitalDoc.setGeometry(QtCore.QRect(290, 70, 113, 25))
        self.inputHospitalDoc.setObjectName("inputHospitalDoc")
        self.inputEspecialidadDoc = QtWidgets.QLineEdit(self.CRUD)
        self.inputEspecialidadDoc.setGeometry(QtCore.QRect(160, 70, 113, 25))
        self.inputEspecialidadDoc.setObjectName("inputEspecialidadDoc")
        self.inputNombreDoc = QtWidgets.QLineEdit(self.CRUD)
        self.inputNombreDoc.setGeometry(QtCore.QRect(20, 70, 113, 25))
        self.inputNombreDoc.setObjectName("inputNombreDoc")
        self.inputDelDoc = QtWidgets.QLineEdit(self.CRUD)
        self.inputDelDoc.setGeometry(QtCore.QRect(100, 180, 113, 25))
        self.inputDelDoc.setObjectName("inputDelDoc")
        self.inputActualizarEspecialiadadDoctor = QtWidgets.QLineEdit(self.CRUD)
        self.inputActualizarEspecialiadadDoctor.setGeometry(QtCore.QRect(220, 240, 91, 25))
        self.inputActualizarEspecialiadadDoctor.setObjectName("inputActualizarEspecialiadadDoctor")
        self.inputActualizarNombreDoctor = QtWidgets.QLineEdit(self.CRUD)
        self.inputActualizarNombreDoctor.setGeometry(QtCore.QRect(130, 240, 71, 25))
        self.inputActualizarNombreDoctor.setObjectName("inputActualizarNombreDoctor")
        self.inputActualizarDoc = QtWidgets.QLineEdit(self.CRUD)
        self.inputActualizarDoc.setGeometry(QtCore.QRect(10, 240, 101, 25))
        self.inputActualizarDoc.setObjectName("inputActualizarDoc")
        self.inputActualizarHospitalDoc = QtWidgets.QLineEdit(self.CRUD)
        self.inputActualizarHospitalDoc.setGeometry(QtCore.QRect(320, 240, 81, 25))
        self.inputActualizarHospitalDoc.setObjectName("inputActualizarHospitalDoc")
        self.tituloCRUDHospital_2 = QtWidgets.QFrame(self.centralwidget)
        self.tituloCRUDHospital_2.setGeometry(QtCore.QRect(490, 240, 431, 391))
        self.tituloCRUDHospital_2.setStyleSheet("background-color: #AAA;  color:blue")
        self.tituloCRUDHospital_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tituloCRUDHospital_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tituloCRUDHospital_2.setObjectName("tituloCRUDHospital_2")
        self.botonAgregarHospital = QtWidgets.QPushButton(self.tituloCRUDHospital_2)
        self.botonAgregarHospital.setGeometry(QtCore.QRect(230, 60, 91, 25))
        self.botonAgregarHospital.setObjectName("botonAgregarHospital")
        self.tituloCRUDHospital = QtWidgets.QLabel(self.tituloCRUDHospital_2)
        self.tituloCRUDHospital.setGeometry(QtCore.QRect(160, 10, 111, 17))
        self.tituloCRUDHospital.setObjectName("tituloCRUDHospital")
        self.botonEliminarHospital = QtWidgets.QPushButton(self.tituloCRUDHospital_2)
        self.botonEliminarHospital.setGeometry(QtCore.QRect(230, 130, 89, 25))
        self.botonEliminarHospital.setObjectName("botonEliminarHospital")
        self.botonActualizarHospital = QtWidgets.QPushButton(self.tituloCRUDHospital_2)
        self.botonActualizarHospital.setGeometry(QtCore.QRect(170, 280, 91, 25))
        self.botonActualizarHospital.setObjectName("botonActualizarHospital")
        self.inputNombreHos = QtWidgets.QLineEdit(self.tituloCRUDHospital_2)
        self.inputNombreHos.setGeometry(QtCore.QRect(70, 60, 113, 25))
        self.inputNombreHos.setObjectName("inputNombreHos")
        self.inputDelHospital = QtWidgets.QLineEdit(self.tituloCRUDHospital_2)
        self.inputDelHospital.setGeometry(QtCore.QRect(70, 130, 111, 25))
        self.inputDelHospital.setObjectName("inputDelHospital")
        self.inputActualizarIdHospital = QtWidgets.QLineEdit(self.tituloCRUDHospital_2)
        self.inputActualizarIdHospital.setGeometry(QtCore.QRect(70, 210, 111, 25))
        self.inputActualizarIdHospital.setObjectName("inputActualizarIdHospital")
        self.inputActualizarNombreHospital = QtWidgets.QLineEdit(self.tituloCRUDHospital_2)
        self.inputActualizarNombreHospital.setGeometry(QtCore.QRect(210, 210, 111, 25))
        self.inputActualizarNombreHospital.setObjectName("inputActualizarNombreHospital")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botonConsultarIdDoc.setText(_translate("MainWindow", "Consultar"))
        self.labelHospital.setText(_translate("MainWindow", "Hospital"))
        self.labelDoctor.setText(_translate("MainWindow", "Doctor"))
        self.butonConsultaNombreHospital.setText(_translate("MainWindow", "Consultar"))
        self.tituloConsulta.setText(_translate("MainWindow", "Consulta"))
        self.inputIdDoctorConsulta.setPlaceholderText(_translate("MainWindow", "Id del Doctor"))
        self.inputNombreHospital.setPlaceholderText(_translate("MainWindow", "Nombre Hospital"))
        self.botonAgregarDoc.setText(_translate("MainWindow", "Agregar"))
        self.tituloCRUDDoc.setText(_translate("MainWindow", "CRUD Doctor"))
        self.botonEliminarDoc.setText(_translate("MainWindow", "Eliminar"))
        self.botonActualizarDoc.setText(_translate("MainWindow", "Actualizar"))
        self.inputHospitalDoc.setPlaceholderText(_translate("MainWindow", "Hospital"))
        self.inputEspecialidadDoc.setPlaceholderText(_translate("MainWindow", "Especialidad"))
        self.inputNombreDoc.setPlaceholderText(_translate("MainWindow", "Nombre"))
        self.inputDelDoc.setPlaceholderText(_translate("MainWindow", "Id del Doctor"))
        self.inputActualizarEspecialiadadDoctor.setPlaceholderText(_translate("MainWindow", "Especialidad"))
        self.inputActualizarNombreDoctor.setPlaceholderText(_translate("MainWindow", "Nombre"))
        self.inputActualizarDoc.setPlaceholderText(_translate("MainWindow", "Id del Doctor"))
        self.inputActualizarHospitalDoc.setPlaceholderText(_translate("MainWindow", "Hospital"))
        self.botonAgregarHospital.setText(_translate("MainWindow", "Agregar"))
        self.tituloCRUDHospital.setText(_translate("MainWindow", "CRUD Hospital"))
        self.botonEliminarHospital.setText(_translate("MainWindow", "Eliminar"))
        self.botonActualizarHospital.setText(_translate("MainWindow", "Actualizar"))
        self.inputNombreHos.setPlaceholderText(_translate("MainWindow", "Nombre"))
        self.inputDelHospital.setPlaceholderText(_translate("MainWindow", "Id.Hospital"))
        self.inputActualizarIdHospital.setPlaceholderText(_translate("MainWindow", "Id.Hospital"))
        self.inputActualizarNombreHospital.setPlaceholderText(_translate("MainWindow", "Nombre"))

        # boton de consultar por idDoctor
        self.botonConsultarIdDoc.clicked.connect(self.showPopUpConsultaDoctor)
        # boton de consultar por Nombre del Hospital
        self.butonConsultaNombreHospital.clicked.connect(self.showPopUpConsultaHospital)

        # CRUD DOCTOR
        # boton de agregar Doctor
        self.botonAgregarDoc.clicked.connect(self.showPopUpAddDoctor)
        # boton de agregar Doctor
        self.botonEliminarDoc.clicked.connect(self.showPopUpDelDoctor)
        # boton de actualizar Doctor
        self.botonActualizarDoc.clicked.connect(self.showPopUpUpdDoctor)

        # CRUD HOSPITAL
        # boton de agregar Hospital
        self.botonAgregarHospital.clicked.connect(self.showPopUpAddHospital)
        # boton de agregar Hospital
        self.botonEliminarHospital.clicked.connect(self.showPopUpDelHospital)
        # boton de actualizar Hospital
        self.botonActualizarHospital.clicked.connect(self.showPopUpUpdHospital)
        
    
    # Validaciones formularios

    # Validación consulta por IdDoctor 
    def validacionConsultaDoctor(self):
        if self.inputIdDoctorConsulta.text():
            booleano = True
        else:
            booleano = False
        return booleano
    # Validación consulta por Nombre Hospital 
    def validacionNombreHospital(self):
        if self.inputNombreHospital.text():
            booleano = True
        else:
            booleano = False
        return booleano

    # Validación Agregar Doctor 
    def validacionAddDoctor(self):
        if self.inputNombreDoc.text() and self.inputEspecialidadDoc.text() and self.inputHospitalDoc.text():
            booleano = True
        else:
            booleano = False
        return booleano
    # Validación Eliminar Doctor 
    def validacionDelDoctor(self):
        if self.inputDelDoc.text():
            booleano = True
        else:
            booleano = False
        return booleano
    # Validación Actualizar Doctor 
    def validacionUpdDoctor(self):
        if self.inputActualizarDoc.text() and self.inputActualizarNombreDoctor.text() and self.inputActualizarEspecialiadadDoctor.text() and self.inputActualizarHospitalDoc:
            booleano = True
        else:
            booleano = False
        return booleano

    # Validación Agregar Hospital
    def validacionAddHospital(self):
        if self.inputNombreHos.text():
            booleano = True
        else:
            booleano = False
        return booleano
    # Validación Eliminar Hospital 
    def validacionDelHospital(self):
        if self.inputDelHospital.text():
            booleano = True
        else:
            booleano = False
        return booleano
    # Validación Actualizar Hospital
    def validacionUpdHospital(self):
        if self.inputActualizarIdHospital.text() and self.inputActualizarNombreHospital.text():
            booleano = True
        else:
            booleano = False
        return booleano

    # Funciones para mostrar dialogos 

    # Dialogo consulta por ID Doctor
    def showPopUpConsultaDoctor(self):
        if self.validacionConsultaDoctor():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Consulta Doctor")
            msg.setText("Consulta doctor exitosa!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Consulta Doctor")
            msg.setText("Ingrese los datos!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox

    # Dialogo consulta por nombre Hospital
    def showPopUpConsultaHospital(self):
        if self.validacionNombreHospital():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Consulta Hospital")
            msg.setText("Consulta hospital exitosa!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Consulta Hospital")
            msg.setText("Ingrese los datos!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox

    # Dialogo Agregar Doctor
    def showPopUpAddDoctor(self):
        if self.validacionAddDoctor():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Agregar Doctor")
            msg.setText("Doctor agregado con exito!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Agregar Doctor")
            msg.setText("Ingrese los datos!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox
    
    # Dialogo Eliminar Doctor
    def showPopUpDelDoctor(self):
        if self.validacionDelDoctor():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Eliminar Doctor")
            msg.setText("Doctor eliminado con exito!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Eliminar Doctor")
            msg.setText("Ingrese los datos!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox
    
    # Dialogo Actualizar Doctor
    def showPopUpUpdDoctor(self):
        if self.validacionUpdDoctor():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Actualizar Doctor")
            msg.setText("Doctor actualizado con exito!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Actualizar Doctor")
            msg.setText("Ingrese los datos!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox


    # Dialogo Agregar Hospital
    def showPopUpAddHospital(self):
        if self.validacionAddHospital():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Agregar Hospital")
            msg.setText("Hospital agregado con exito!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Agregar Hospital")
            msg.setText("Ingrese los datos!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox
    
    # Dialogo Eliminar Hospital
    def showPopUpDelHospital(self):
        if self.validacionDelHospital():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Eliminar Hospital")
            msg.setText("Hospital eliminado con exito!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Eliminar Hospital")
            msg.setText("Ingrese los datos!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox
    
    # Dialogo Actualizar Hospital
    def showPopUpUpdHospital(self):
        if self.validacionUpdHospital():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Actualizar Hospital")
            msg.setText("Hospital actualizado con exito!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Actualizar Hospital")
            msg.setText("Ingrese los datos!")
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            x = msg.exec_()  # this will show our messagebox

            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
