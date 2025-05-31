import tkinter as tk
from PIL import Image,ImageTk #PIL es la librería que nos permite usar imágenes con Tkinter. // "-pip install Pillow" en la terminal de VSCode.

class Application:
    def __init__(self):
        #Información básica para la ventana.
        self.window=tk.Tk()
        self.window.title("Ventana con Imágen")
        self.window.geometry("500x900")


        #- - - Añadir un .jpg - - -
        self.im001=Image.open("IM001.jpg") #Búsqueda de imagen.
        #self.im001=self.im001.resize(int(self.im001.width/2),int(self.im001.height/2)) // Se supone cambia el tamaño pero todavía debe arreglarse.
        self.im001_tk=ImageTk.PhotoImage(self.im001)
        self.Label_imagen=tk.Label(self.window,image=self.im001_tk)
        self.Label_imagen.pack() #Centrar Imagen


        #- - - Bloque de Color - - -
        self.img=Image.new("RGB",(150,175),(255,0,0)) #(Tipo de color,(Ancho,Alto),(R,G,B))
        self.img_tk=ImageTk.PhotoImage(self.img)
        self.Label_img=tk.Label(self.window,image=self.img_tk)
        self.Label_img.pack()


        #- - - Rotar Imágen - - -
        self.im002=Image.open("IM002.jpg") #Búsqueda de imagen.
        #Se gira indicando el ángulo "angle", "expand" es para que las dimensiones se mantengan tal cual, "fillcolor" cambia el color del fondo en caso de no quedar en ángulos como 90,180 grados, "resample" para mantener la calidad de la imagen, "center" permite cambiar la posición dentro del recuadro.
        self.im002=self.im002.rotate(angle=45,expand=True,fillcolor="green",resample=Image.BICUBIC) #center=(100,100)

        #PhotoImage DESPUÉS de la rotación.
        '''¿Porqué? Según AI Studio: Cuando haces self.Label_im002=tk.Label(self.window,image=self.im002_tk) el Label toma una "instantánea" de la imagen que le pasaste en ese momento. Modificar el objeto original de Pillow (self.im002) después no actualizará automáticamente la imagen en el Label'''
        self.im002_tk=ImageTk.PhotoImage(self.im002)
        self.Label_im002=tk.Label(self.window,image=self.im002_tk)
        self.Label_im002.pack() #Centrar Imagen

        self.window.mainloop()

def main():
        app = Application()
if __name__ == "__main__":
    main()