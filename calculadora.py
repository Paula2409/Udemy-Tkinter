from tkinter import messagebox, ttk
import tkinter as tk
import tkmacosx

class Calculadora(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.geometry('500x350+900+300')
        self.resizable(0,0) # Para que no se pueda modificar el tamaño
        self.title('Calculadora')
        self.iconbitmap(r"Tkinter/icono.gif")

        # Atributos de clase, expresion: variable que va a ir almacenando lo que se va escribiendo en la caja de texto
        self.expresion = ''
        
        # Caja de texto (elemento input)
        self.entrada = None
        
        # Variable asociada a la caja de entrada (StringVar para obtener o actualizar el valor del input). A traves de esta variable modificamos el contenido de la caja de texto
        self.entrada_texto = tk.StringVar()
        
        # Creamos los componentes
        self._creacion_componentes()
        
# Creacion de metodos

    def _creacion_componentes(self):
        # Creamos un Frame para la caja de entrada
        # Utilizamos para publicar dentro del objeto creado con esta clase, por eso el self
        entrada_frame = tk.Frame(self, width=400,height=50, bg='grey')
        entrada_frame.pack(side=tk.TOP)

        # Caja de texto
        entrada = tk.Entry(entrada_frame, font=('arial',18,'bold'),
                           textvariable=self.entrada_texto, width=44, justify=tk.RIGHT)
        entrada.grid(row=0, column=0, ipady=10, sticky=tk.NSEW, padx=1, pady=1)
        
        # Agregamos otro Frame para la parte inferior
        botones_frame = tk.Frame(self,width=400,height=450, bg='grey')
        botones_frame.pack()
        
        # Primer renglo
        # Boton limpiar
        boton_limpiar = tkmacosx.Button(botones_frame, text='C', width=30,height=3,
                                  bd=0, bg='#eee', cursor='hand', command=self._limpiar)
        boton_limpiar.grid(row=0,column=0, columnspan=3, padx=1, pady=1, sticky=tk.NSEW)
        
        # Boton dividir
        # Utilizamos lambda ya que generamos un funcion generalizada para todas las operaciones y le debemos pasar por parametro el simbolo de la operacion
        # Al pasarle el simbolo la funcion se invocara cuando ejecutemos el programa, para evitar esto y que el command asocie a un objeto utilizamos lambda que ejecutara la funcion cada vez que clickeamos en el boton correspondiente
        boton_dividir = tk.Button(botones_frame,text='/', width=10, height=3, bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click('/'))
        boton_dividir.grid(row=0, column=3, padx=1, pady=1)
        
        # Segundo renglon
        # Boton 7. Utilizamos el grid aqui para simplificar codigo
        boton_7 = tk.Button(botones_frame, text='7', width=10, height=3, 
                             bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click(7)).grid(row=1, column=0, padx=1, pady=1)
        # boton_7.grid(row=0, column=3, padx=1, pady=1) # Lo indicamos arriba
        
        # Boton 8
        boton_8 = tk.Button(botones_frame, text='8', width=10, height=3, 
                             bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click(8)).grid(row=1, column=1, padx=1, pady=1)
        
        # Boton 9
        boton_9 = tk.Button(botones_frame, text='9', width=10, height=3, 
                             bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click(9)).grid(row=1, column=2, padx=1, pady=1)

        # Boton Multiplicar
        boton_multiplicar = tk.Button(botones_frame,text='*', width=10, height=3, bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click('*'))
        boton_multiplicar.grid(row=1, column=3, padx=1, pady=1)
        
        # Tercer renglon
        # Boton 4. 
        boton_4 = tk.Button(botones_frame, text='4', width=10, height=3, 
                             bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click(4)).grid(row=2, column=0, padx=1, pady=1)
        
        # Boton 5
        boton_5 = tk.Button(botones_frame, text='5', width=10, height=3, 
                             bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click(5)).grid(row=2, column=1, padx=1, pady=1)
        
        # Boton 6
        boton_6 = tk.Button(botones_frame, text='6', width=10, height=3, 
                             bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click(6)).grid(row=2, column=2, padx=1, pady=1)

        # Boton Resta
        boton_resta = tk.Button(botones_frame,text='-', width=10, height=3, bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click('-'))
        boton_resta.grid(row=2, column=3, padx=1, pady=1)

        # Cuarto renglon
        # Boton 1 
        boton_1 = tk.Button(botones_frame, text='1', width=10, height=3, 
                             bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click(1)).grid(row=3, column=0, padx=1, pady=1)
        
        # Boton 2
        boton_2 = tk.Button(botones_frame, text='2', width=10, height=3, 
                             bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click(2)).grid(row=3, column=1, padx=1, pady=1)
        
        # Boton 3
        boton_3 = tk.Button(botones_frame, text='3', width=10, height=3, 
                             bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click(3)).grid(row=3, column=2, padx=1, pady=1)

        # Boton Suma
        boton_suma = tk.Button(botones_frame,text='+', width=10, height=3, bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click('+'))
        boton_suma.grid(row=3, column=3, padx=1, pady=1)
        
        # Quinto renglon
        # Boton 0 
        boton_0 = tk.Button(botones_frame, text='0', width=10, height=3, 
                             bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click(0)).grid(row=4, column=0, padx=1, pady=1, columnspan=2, sticky=tk.NSEW)
        
        # Boton punto
        boton_punto = tk.Button(botones_frame, text='.', width=10, height=3, 
                             bd=0, bg='#eee', cursor='hand', command=lambda: self._evento_click('.')).grid(row=4, column=2, padx=1, pady=1)

        # Boton igual
        boton_igual = tk.Button(botones_frame, text='=', width=10, height=3, 
                             bd=0, bg='#eee', cursor='hand', command=self._evento_evaluar).grid(row=4, column=3, padx=1, pady=1)
    
    def _limpiar(self):
        self.expresion = ''
        self.entrada_texto.set(self.expresion)
    
    def _evento_click(self, elemento):
        # Concatenamos el nuevo elemento que se presiono a la expresion existente
        self.expresion = f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)
    
    def _evento_evaluar(self):
        # eval evalua la expresion str como una expresion aritmetica
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error','Ocurrio un error: {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion = ''

if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()