import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Calculadora(tk.Tk):
   def __init__(self):
      super().__init__()
      self.geometry('450x360')
      self.resizable(0,0)
      self.title('Calculadora')
      # Atributos clase
      self.expresion = ''
      # Caja de texto   (input)
      self.entrada = None
      # StringVar para actualizar el valor del input
      self.entrada_texto = tk.StringVar()
      # Seleccionamos el tema oscuro de tkinter

      # Creamos los componentes
      self._creacion_componentes()


   # Metodos de Clase
   # Metodo para crear componentes
   def _creacion_componentes(self):
      # Crear un frame para la caja de texto
      entrada_frame = tk.Frame(self, width=400, height=50, bg='grey')
      entrada_frame.pack(side=tk.TOP)
      # Caja de texto
      entrada = tk.Entry(entrada_frame,
                        font=('Jetbrains Mono Medium', 15, 'bold'),
                        textvariable=self.entrada_texto,
                        width=30, justify=tk.RIGHT)
      entrada.grid(row=0, column=0, ipady=7)

      # Creamos otro frame para la parte inferior
      botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
      botones_frame.pack()

      def crear_boton(valor, f, c):
         event = lambda: self._evento_click(valor)
         width, height = (10, 3)
         if isinstance(valor, int):
            bg = '#fff'
            if valor == 0:
               width = 24
         elif isinstance(valor, str):
            bg = '#eee'
            if valor == '=':
               event = lambda: self._evento_evaluar() # si no se usa lambda no lleva parentesis para command
         # Edicion: eliminado parametro bg=bg para una buena adaptacion al tema oscuro
         boton = tk.Button(botones_frame, text=valor, width=width, height=height, bd=0,
                                cursor='hand2', command=event)
         if valor == 0:
            return boton.grid(row=f, column=c, columnspan=2, padx=1, pady=1)

         return boton.grid(row=f, column=c, padx=1, pady=1)

      # Edicion: eliminado parametro bg='#eee' para una buena adaptacion al tema oscuro
      boton_limpiar = tk.Button(botones_frame, text='C', width=38, height=3, bd=0
                                 , cursor='hand2', command=self._evento_limpiar
                                ).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
      # Boton de division
      crear_boton('/', 0, 3)

      # Segundo Renglon, botones 7, 8, 9 y '*'
      crear_boton(7, 1, 0)
      crear_boton(8, 1, 1)
      crear_boton(9, 1, 2)
      crear_boton('*', 1, 3)

      # Tercer Renglon
      crear_boton(4, 2, 0)
      crear_boton(5, 2, 1)
      crear_boton(6, 2, 2)
      crear_boton('+', 2, 3)

      # Cuarto Renglon
      crear_boton(1, 3, 0)
      crear_boton(2, 3, 1)
      crear_boton(3, 3, 2)
      crear_boton('-', 3, 3)
      # Quinto Renglon
      crear_boton(0, 4, 0 )
      crear_boton('.', 4, 2)
      crear_boton('=', 4, 3)
   def _evento_limpiar(self):
      self.expresion = ''
      self.entrada_texto.set(self.expresion)

   def _evento_click(self, elemento):
      # Concatenamos el nuevo elemento a la expresion ya existente
      self.expresion = f'{self.expresion}{elemento}'
      self.entrada_texto.set(self.expresion)

   def _evento_evaluar(self):
      try:
         if self.expresion:
            resultado = str(eval(self.expresion))
            self.entrada_texto.set(resultado)
      except Exception as e:
         messagebox.showerror('Error', f'Ocurrio un error:{e}')
         self.entrada_texto.set('')
      self.expresion = ''


if __name__ == '__main__':
   calculadora = Calculadora()
   calculadora.mainloop()

