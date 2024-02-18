from mw import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.contenido = ''

        self.ui.pushButton_abrir.clicked.connect(self.AbrirArchivo)
        self.ui.pushButton_analizar.clicked.connect(self.Analizar)

        # Lista de palabras reservadas y operadores
        self.palabras_reservadas = ['int', 'float', 'string', 'if', 'else', 'while', 'for','void','return','true','false']
        self.operadores = ['+', '-', '*', '/', '<', '>', '<=', '>=', '&&', '||', '!', '!=','==' , '=']
    def AbrirArchivo(self):
        archivo, _ = QFileDialog.getOpenFileName(None, "Seleccionar archivo", "", "Archivos de texto (*.txt)")
        print("Archivo seleccionado:", archivo)
        try:
            with open(archivo, 'r') as f:
                self.contenido = f.read()
                print("Contenido del archivo:")
                print(self.contenido)
        except Exception as e:
            print("Error al leer el archivo:", str(e))
        
        self.ui.plainTextEdit_entrada.setPlainText(self.contenido)

    #funcion que se usara para imprimir datos en la interfaz
    def Analizar(self):
        texto = self.ui.plainTextEdit_entrada.toPlainText()
        tokens = self.analizador_lexico(texto)
        self.ui.plainTextEdit_salida.setPlainText('\n'.join(tokens))

    def analizador_lexico(self, texto):
        #tokens a devolver
        tokens = []

        #cadena a evaluar y concatena si son numeros o letras si es guion lo concatena por que se trataria de un id
        palabra_actual = ''
        for caracter in texto:
            if caracter.isalnum() or caracter == '_' or caracter == '.' or caracter == '=':
                print(caracter)
                palabra_actual += caracter
            else:
                if palabra_actual:
                    tokens.append(self.clasificar_token(palabra_actual))
                    palabra_actual = ''
                if caracter.strip():
                    tokens.append(self.clasificar_token(caracter))
        if palabra_actual:
            tokens.append(self.clasificar_token(palabra_actual))
        return tokens

    # evalua y retorna la funcion 
    def clasificar_token(self, token):
        if self.es_numero(token):
            return f'{token}: Numero entero'
        elif self.es_decimal(token):
            return f'{token}: numero Desimal'
        elif token in self.operadores:
            return f'{token}: Operador'
        elif token in ['(', '{', '[']:
            return f'{token}: apertura de llave'
        elif token in [')', '}', ']']:
            return f'{token}: cierre de llave'
        elif token in self.palabras_reservadas:
            return f'{token}: Palabra Reservada'
        elif token == ';':
            return f'{token}: delimitador'
        else:
            return f'{token}: Identificador'


    def es_numero(self, palabra):
        try:
            int(palabra)
            return True
        except ValueError:
            return False
        
    def es_decimal(self, palabra):
        try:
            float(palabra)
            return True
        except ValueError:
            return False

app = QApplication(sys.argv)
ventana = Window()
ventana.show()
sys.exit(app.exec_())
