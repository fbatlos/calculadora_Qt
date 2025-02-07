import math
import sys
import os
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import Qt

class Calculadora(QMainWindow):
    def __init__(self):
        super(Calculadora, self).__init__()

        rutaUi = os.path.join(os.path.dirname(__file__), 'calculadora.ui')

        uic.loadUi(rutaUi, self)

        #Botones de numeros y operadores 
        
        botones = {
            "Bt_0": "0", "Bt_1": "1", "Bt_2": "2", "Bt_3": "3", "Bt_4": "4", 
            "Bt_5": "5", "Bt_6": "6", "Bt_7": "7", "Bt_8": "8", "Bt_9": "9",
            "Bt_coma": ".", "Bt_dividir": "/", "Bt_multi": "*",
            "Bt_menos": "-", "Bt_sumar": "+", "Bt_parenIzq": "(", "Bt_parenDer": ")"
        }
        
        for boton, valor in botones.items():
            getattr(self, boton).clicked.connect(lambda _, v=valor: self.agregar_numero(v))

        #Botones de control
        self.Bt_clean.clicked.connect(self.borrar)
        self.Bt_cleanAll.clicked.connect(self.borrar_todo)
        self.Bt_igual.clicked.connect(self.evaluar_expresion)

        #Botones de funciones y constantes
        
        self.Bt_seno.clicked.connect(lambda: self.agregar_funcion("sin"))
        self.Bt_coseno.clicked.connect(lambda: self.agregar_funcion("cos"))
        self.Bt_tangente.clicked.connect(lambda: self.agregar_funcion("tan"))
        self.Bt_logaritmo.clicked.connect(lambda: self.agregar_funcion("log"))
        self.Bt_tau.clicked.connect(lambda: self.agregar_constante("tau"))
        self.Bt_e.clicked.connect(lambda: self.agregar_constante("e"))
        self.Bt_pi.clicked.connect(lambda: self.agregar_constante("pi"))
        self.Bt_raiz.clicked.connect(lambda: self.agregar_funcion("sqrt"))
        self.Bt_factorial.clicked.connect(lambda: self.agregar_funcion("factorial"))
        self.Bt_expo.clicked.connect(lambda: self.agregar_numero("**"))

        #Aspectos de la tabla
        self.TW_table.setColumnCount(2)
        self.TW_table.setHorizontalHeaderLabels(["Operación", "Resultado"])
        self.TW_table.setRowCount(0)
        
        self.expresion = ""
        self.interno = ""

        self.isFirst = True

    #Funcion encargada de agregar un numero a la expresion, se muestra de forma diferente en el TE_resultado y en la variable interna
    def agregar_numero(self, numero):
        if self.isFirst and numero.isdigit():
            self.expresion = ""
            self.interno = ""
            self.isFirst = False
        else:
            self.isFirst = False

        if numero == "**":
            self.expresion += "^"
            self.interno += numero
        elif numero == "(":
            self.expresion += numero
            self.interno += "*"+numero
        else:
            self.expresion += numero
            self.interno += numero

        self.TE_resultado.setText(self.expresion)

    #Funcion encargada de agregar una constante a la expresion, se muestra de forma diferente en el TE_resultado y en la variable interna
    def agregar_constante(self, constante):
        showConstant = {
            "tau": "τ",
            "e": "e",
            "pi": "π",
        }

        if self.interno[len(self.interno)-1].isdigit():
            self.expresion += f"{showConstant[constante]}"
            self.interno += f"*math.{constante}"
        else:
            self.expresion += f"{showConstant[constante]}"
            self.interno += f"math.{constante}"

        self.TE_resultado.setText(self.expresion)

    #Funcion encargada de agregar una funcion a la expresion, se muestra de forma diferente en el TE_resultado y en la variable interna
    def agregar_funcion(self, funcion):
        showFunction = {
            "sin": "sin",
            "cos": "cos",
            "tan": "tan",
            "log": "log",
            "sqrt": "√",
            "factorial": "!"
        }

        if self.interno[len(self.interno)-1].isdigit():
            self.expresion += f"{showFunction[funcion]}("
            self.interno += f"*math.{funcion}("
        else:
            self.expresion += f"{showFunction[funcion]}("
            self.interno += f"math.{funcion}("

        self.TE_resultado.setText(self.expresion)

    #Funcion encargada de borrar el ultimo caracter de la expresion, se comprueba si es una constante, funcion o numero para eliminar de forma diferente la variable interna
    def borrar(self):
        if self.expresion.endswith("τ"):
            self.expresion = self.expresion[:-1]
            self.interno = self.interno[:-3]

        elif self.expresion.endswith("π") or self.expresion.endswith("*"):
            self.expresion = self.expresion[:-1]
            self.interno = self.interno[:-2]

        elif self.expresion.endswith("√"):
            self.expresion = self.expresion[:-1]
            self.interno = self.interno[:-4]
        else:
            self.expresion = self.expresion[:-1]
            self.interno = self.interno[:-1]
        
        if self.interno.endswith("math."):
            self.interno = self.interno[:-5]

        self.TE_resultado.setText(self.expresion)
    
    def borrar_todo(self):
        self.expresion = ""
        self.interno = ""
        self.TE_resultado.setText(self.expresion)

    #Aquí se evalua la expresión y se muestra el resultado en el TE_resultado y se guarda en el historial
    def evaluar_expresion(self):
        try:
            if self.interno == "":
                self.TE_resultado.setText("")
            else:
                resultado = eval(self.interno, {"math": math})
                self.TE_resultado.setText(str(resultado))
                self.guardar_historial(self.expresion, str(resultado))
                self.expresion = str(resultado)
                self.interno = str(resultado)
                self.isFirst = True


        except Exception as error:
            #Lugar donde se manejan los errores de sintaxis
            print(self.interno)
            QMessageBox.critical(self,"Error", "Sintaxis incorrecta") 
            self.TE_resultado.setText("")
            self.expresion = ""
            self.interno = ""


    #Funcion encargada de guardar el historial de operaciones en surespectivo lugar
    def guardar_historial(self, operacion, resultado):
        row_position = self.TW_table.rowCount()
        self.TW_table.insertRow(row_position)
        self.TW_table.setItem(row_position, 0, QTableWidgetItem(operacion))
        self.TW_table.setItem(row_position, 1, QTableWidgetItem(resultado))
        



def main():
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    app.exec() 

if __name__ == "__main__":
    main()
