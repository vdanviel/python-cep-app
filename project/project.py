import sys;
import info_cep_app as cep;
import tkinter as tk;

gui = tk.Tk()

gui.title('Address Information App')#nome para a guia
gui.geometry("800x500")#o tamanho (px "WxH") da janela

#pack() - (https://docs.python.org/3/library/tkinter.html?highlight=tkinter#the-packer)

#pack(anchor="direction") - (https://chat.openai.com/share/42b2a221-897f-41b4-9ea4-5a149c4a72a3)
#pack(padx=int, pady=int) - A distance - designating external padding on each side of the slave widget.

#chamando p app de leitura de endereço
cep.App(gui,"Vitão");

gui.mainloop()#chama a tela principal
