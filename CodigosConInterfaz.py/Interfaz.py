from tkinter import *
ventana=Tk()
car=5
#Nombre del archivo
ventana.title(f"Esto es para crear nombre de mi titulo")
#Icono del programa
ventana.iconbitmap("Imagenpy.ico")
#Medidas de la ventana primero ancho luego alto
ventana.geometry("100x300")
#Cambiar el color de la ventana
ventana.config(bg="cyan")
miframe=Frame()
#miframe.pack(side="top")
miframe.pack(side="top",expand=False)
miframe.config(bg="red")
miframe.config(width="600",height="400")

ventana.mainloop()

