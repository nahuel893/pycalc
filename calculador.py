import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ct

ct.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ct.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Calculadora(ct.CTk):
   def __init__(self):
      super().__init__()
      self.geometry('410x318')
      self.resizable(0,0)
      self.title('Calculadora')
      # Atributos clase
      self.expresion = ''
      # Caja de texto   (input)
      self.entrada = None
      # StringVar para actualizar el valor del input
      self.entrada_texto = tk.StringVar()
      # Seleccionamos el tema oscuro de tkinter
      self.grid_columnconfigure(1, weight=1)
      self.grid_columnconfigure((2, 3), weight=0)
      self.grid_rowconfigure((0, 1, 2), weight=1)
      # Creamos los componentes
      self._creacion_componentes()


   # Metodos de Clase
   # Metodo para crear componentes
   def _creacion_componentes(self):
      # Crear un frame para la caja de texto
      entrada_frame = ct.CTkFrame(self, height=200, width=200,corner_radius=10)#, bg='grey')
      entrada_frame.pack( fill='x')
      # Caja de texto
      entrada = ct.CTkEntry(entrada_frame,
                        font=('Jetbrains Mono Medium', 15, 'bold'),
                        textvariable=self.entrada_texto,height=55, justify=tk.RIGHT)

      entrada.pack(fill='x')

      # Creamos otro frame para la parte inferior
      botones_frame = ct.CTkFrame(self, width=400, height=450,corner_radius=10)#, bg='grey')
      botones_frame.pack(fill='x')

      def crear_boton(valor, f, c):
         event = lambda: self._evento_click(valor)
         width, height = (100, 50)
         if isinstance(valor, int):
            if valor == 0:
               width = 100
         elif isinstance(valor, str):
            if valor == '=':
               event = lambda: self._evento_evaluar() # si no se usa lambda no lleva parentesis para command
         boton = ct.CTkButton(botones_frame, text=valor, width=width, height=height,
                                cursor='hand2', command=event)
         if valor == 0:
            return boton.grid(row=f, column=c, columnspan=2, padx=1, pady=1, sticky='nsew')

         return boton.grid(row=f, column=c, padx=1, pady=1)

      boton_limpiar = ct.CTkButton(botones_frame, text='C', cursor='hand2', command=self._evento_limpiar
                                ).grid(row=0, column=0, columnspan=3, padx=1, pady=1, sticky='nsew')
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

