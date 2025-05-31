import tkinter as tk
from PIL import Image,ImageTk #PIL es la librería que nos permite usar imágenes con Tkinter.

class Application:
    def __init__(self):
        #Información básica para la ventana.
        self.window=tk.Tk()
        self.window.title("Ventana con Imágen")
        self.window.geometry("500x725")

        #Añadir un .jpg
        self.imagen=Image.open("IM001.jpg") #Búsqueda de imagen.
        self.imagen_tk=ImageTk.PhotoImage(self.imagen)
        self.Label_imagen=tk.Label(self.window,image=self.imagen_tk)
        self.Label_imagen.pack() #Centrar Imagen

        #Bloque de Color
        self.img=Image.new("RGB",(300,200),(255,0,0)) #(Tipo de color,(Ancho,Alto),(R,G,B))
        self.img_tk=ImageTk.PhotoImage(self.img)
        self.Label_img=tk.Label(self.window,image=self.img_tk)
        self.Label_img.pack()

        self.window.mainloop()
def main():
        app = Application()
if __name__ == "__main__":
    main()