import tkinter as tk
from PIL import Image,ImageTk #PIL es la librería que nos permite usar imágenes con Tkinter. // "-pip install Pillow" en la terminal de VSCode.

class Application:
    def __init__(self):
        #Información básica para la ventana.
        self.window=tk.Tk()
        self.window.title("Ventana con Imágen")
        self.window.geometry("400x950")
        self.window.config(bg="black")


        #- - - Añadir un .jpg - - -
        self.im001=Image.open("IM001.jpg") #Búsqueda de imagen.

        #Reestablecer su tamaño (crear una variable para ancho y alto), "resize" permite redimensionarla, "resample=Image.LANCZOS" Para mantener buena calidad.
        width = int(self.im001.width / 3) #Ancho
        height = int(self.im001.height / 3) #Alto
        self.im001 = self.im001.resize((width, height),resample=Image.LANCZOS)

        self.im001_tk=ImageTk.PhotoImage(self.im001)
        self.Label_im001=tk.Label(self.window,image=self.im001_tk)
        self.Label_im001.pack(pady=5) #Centrar Imagen


        #- - - Bloque de Color - - -
        self.img=Image.new("RGB",(150,175),(255,0,0)) #(Tipo de color,(Ancho,Alto),(R,G,B))
        self.img_tk=ImageTk.PhotoImage(self.img)
        self.Label_img=tk.Label(self.window,image=self.img_tk)
        self.Label_img.pack(pady=5)


        #- - - Rotar Imágen - - -
        self.im002=Image.open("IM002.jpg") #Búsqueda de imagen.

        #Se gira indicando el ángulo "angle", "expand" es para que las dimensiones se mantengan tal cual, "fillcolor" cambia el color del fondo en caso de no quedar en ángulos como 90,180 grados, "resample" para mantener la calidad de la imagen, "center" permite cambiar la posición dentro del recuadro.
        self.im002=self.im002.rotate(angle=45,expand=True,fillcolor="green",resample=Image.BICUBIC) #center=(100,100)

        width = int(self.im002.width / 3)
        height = int(self.im002.height / 3)
        self.im002 = self.im002.resize((width, height))

        #PhotoImage DESPUÉS de la rotación.
        '''¿Porqué? "ImageTk.PhotoImage()" toma como una captura precisa de la imágen que no se puede modificar.'''
        self.im002_tk=ImageTk.PhotoImage(self.im002)
        self.Label_im002=tk.Label(self.window,image=self.im002_tk)
        self.Label_im002.pack(pady=5) #Centrar Imagen

        #- - - Unificar 2 Imágenes - - -

        #Deben ser del mismo tamaño.
        width03 = height03 = width04 = height04 = 250

        self.im003=Image.open("IM003.jpg")
        self.im004=Image.open("IM004.jpg")

        self.im003 = self.im003.resize((width03, height03))
        self.im004 = self.im004.resize((width04, height04))

        #Se unifican con el "blend","alpha" solo toma valores de 0 a 1 para modificar la opacidad.
        self.blend=Image.blend(self.im003,self.im004,alpha=0.5)
        self.im003_im004_tk=ImageTk.PhotoImage(self.blend)
        #self.blend.show() // Abre la imagen por separado.
        self.Label_im003_im004=tk.Label(self.window,image=self.im003_im004_tk)
        self.Label_im003_im004.pack(pady=5)

        self.window.mainloop()

def main():
        app = Application()
if __name__ == "__main__":
    main()