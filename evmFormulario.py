import tkinter as tk
from tkinter import ttk,Button,Entry
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import conexion 

class FormularioEVM:
    def __init__(self):
        self.articulo1=conexion.Conexion()
        self.ventana1=tk.Tk()
        self.ventana1.title("Mantenimiento de EVM")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        self.style = ttk.Style()       
        self.style.configure("TLabelframe", bordercolor="red")

        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10) 

        self.carga_articulos()
        self.consulta_proyecto() 
        self.evm()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        #
        self.ventana1.configure(background="#33FFA1")
        self.ventana1.mainloop()
       

    def evm(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Earned Value Analysis")
        
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Formulario de registro")        
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
 
         

        self.label4=ttk.Label(self.labelframe4, text="Codigo:")
        self.label4.grid(column=0, row=0, padx=4, pady=4)
        self.codigo4=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe4, textvariable=self.codigo4)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        #
        self.label2=ttk.Label(self.labelframe4, text="Nombre del Proyecto:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        self.nomproyecto4=tk.StringVar()
        self.entrynomproyecto=ttk.Entry(self.labelframe4, textvariable=self.nomproyecto4, state="readonly")
        self.entrynomproyecto.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe4, text="Hitos:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        
        self.hitos4=tk.StringVar()
        self.entryhitos=ttk.Entry(self.labelframe4, textvariable=self.hitos4, state="readonly")
        self.entryhitos.grid(column=1, row=2, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe4, text="BAC:")        
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        
        self.bac4=tk.StringVar()
        self.entryBAC4=ttk.Entry(self.labelframe4, textvariable=self.bac4, state="readonly")
        self.entryBAC4.grid(column=1, row=3, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe4, text="PV")        
        self.label3.grid(column=0, row=4, padx=2, pady=2) 
        self.label3=ttk.Label(self.labelframe4, text="PV ACUMULADO")        
        self.label3.grid(column=1, row=4, padx=2, pady=2) 

        self.label3=ttk.Label(self.labelframe4, text="EV")        
        self.label3.grid(column=2, row=4, padx=2, pady=2) 
        self.label3=ttk.Label(self.labelframe4, text="EV ACUMULADO")        
        self.label3.grid(column=3, row=4, padx=2, pady=2) 

        self.label3=ttk.Label(self.labelframe4, text="AC")        
        self.label3.grid(column=4, row=4, padx=4, pady=4) 
        self.label3=ttk.Label(self.labelframe4, text="AC ACUMULADO")        
        self.label3.grid(column=5, row=4, padx=4, pady=4) 

        self.label3=ttk.Label(self.labelframe4, text="CV")        
        self.label3.grid(column=6, row=4, padx=4, pady=4) 
        self.label3.configure(foreground="blue")
        self.label3=ttk.Label(self.labelframe4, text="SV")        
        self.label3.grid(column=7, row=4, padx=4, pady=4) 
        self.label3.configure(foreground="blue")
        self.label3=ttk.Label(self.labelframe4, text="CPI",width=10)        
        self.label3.grid(column=8, row=4, padx=4, pady=4) 
        self.label3.configure(foreground="blue")
        self.label3=ttk.Label(self.labelframe4, text="SPI",width=10)        
        self.label3.grid(column=9, row=4, padx=4, pady=4)
        self.label3.configure(foreground="blue") 
        self.label3=ttk.Label(self.labelframe4, text="TCPI",width=10)        
        self.label3.grid(column=10, row=4, padx=4, pady=4)
        self.label3.configure(foreground="blue") 
        self.label3=ttk.Label(self.labelframe4, text="EAC",width=10)        
        self.label3.grid(column=11, row=4, padx=4, pady=4)
        self.label3.configure(foreground="blue") 
        self.label3=ttk.Label(self.labelframe4, text="ETC",width=10)        
        self.label3.grid(column=12, row=4, padx=4, pady=4)
        self.label3.configure(foreground="blue")

        self.label3=ttk.Label(self.labelframe4, text="VAC",width=10)        
        self.label3.grid(column=13, row=4, padx=4, pady=4)
        self.label3.configure(foreground="blue") 
        #   leyenda
        self.label3=ttk.Label(self.labelframe4, text="LEYENDA:")        
        self.label3.grid(column=3, row=0, padx=2, pady=2) 
        self.label3.configure(foreground="red")

        self.label3=ttk.Label(self.labelframe4, text="CV:")        
        self.label3.grid(column=4, row=0, padx=2, pady=2) 
        self.label3.configure(foreground="red")
        self.label3=ttk.Label(self.labelframe4, text="Constance Variance")        
        self.label3.grid(column=5, row=0, padx=2, pady=2)
        
        self.label3=ttk.Label(self.labelframe4, text="SV:")        
        self.label3.grid(column=4, row=1, padx=2, pady=2) 
        self.label3.configure(foreground="red")
        self.label3=ttk.Label(self.labelframe4, text="Schedule Variance")        
        self.label3.grid(column=5, row=1, padx=2, pady=2)

        self.label3=ttk.Label(self.labelframe4, text="SPI:")        
        self.label3.grid(column=4, row=2, padx=2, pady=2) 
        self.label3.configure(foreground="red")
        self.label3=ttk.Label(self.labelframe4, text="Schedule Performance Index")        
        self.label3.grid(column=5, row=2, padx=2, pady=2)

        self.label3=ttk.Label(self.labelframe4, text="TCPI:")        
        self.label3.grid(column=4, row=3, padx=2, pady=2)
        self.label3.configure(foreground="red") 
        self.label3=ttk.Label(self.labelframe4, text="To Complete Performance Index")        
        self.label3.grid(column=5, row=3, padx=2, pady=2)

        self.label3=ttk.Label(self.labelframe4, text="EAC:")        
        self.label3.grid(column=8, row=0, padx=2, pady=2) 
        self.label3.configure(foreground="red")
        self.label3=ttk.Label(self.labelframe4, text="Estimate at Completion")        
        self.label3.grid(column=9, row=0, padx=2, pady=2)

        self.label3=ttk.Label(self.labelframe4, text="ETC:")        
        self.label3.grid(column=8, row=1, padx=2, pady=2) 
        self.label3.configure(foreground="red")
        self.label3=ttk.Label(self.labelframe4, text="Estimate to Complete")        
        self.label3.grid(column=9, row=1, padx=2, pady=2)

        self.label3=ttk.Label(self.labelframe4, text="VAC:")        
        self.label3.grid(column=8, row=2, padx=2, pady=2) 
        self.label3.configure(foreground="red")

        self.label3=ttk.Label(self.labelframe4, text="Variance at Completion")        
        self.label3.grid(column=9, row=2, padx=2, pady=2)
        #fin leyenda
       
        button=Button(self.labelframe4,text="Mostrar Datos",command=self.verAcumulados4, bg = "#298CF8",fg = "#FFFFFF").grid(column=2, row=0, padx=4, pady=4)

    def mostrarDatosEVM(self): 
        datos=(self.codigo4.get(), )
        respuesta=self.articulo1.consulta(datos)  
        if len(respuesta)>0:  
            self.nomproyecto4.set(respuesta[0][0])
            self.hitos4.set(respuesta[0][1]) 
            self.bac4.set(respuesta[0][2])


    def verAcumulados4(self):
        self.mostrarDatosEVM()
        datos=(self.codigo4.get(), )

        respuesta3=self.articulo1.consultaPV(datos)  
        for fila in respuesta3:  
            for i in range(fila[1]):
              self.entryCV=tk.IntVar() 
              enCV = Entry(self.labelframe4, textvariable=self.entryCV, state="readonly",width=10)
              enCV.grid(column=0, row=6+i, padx=4, pady=4) 
              self.entryCV.set(respuesta3[i][0])
             
              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelframe4, textvariable=self.entryCVV, state="readonly",width=10)
              enCVV.grid(column=1, row=6+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][1])

              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelframe4, textvariable=self.entryCVV, state="readonly",width=10)
              enCVV.grid(column=2, row=6+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][2]) 

              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelframe4, textvariable=self.entryCVV, state="readonly",width=10)
              enCVV.grid(column=3, row=6+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][3]) 

              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelframe4, textvariable=self.entryCVV, state="readonly",width=10)
              enCVV.grid(column=4, row=6+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][4])

              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelframe4, textvariable=self.entryCVV, state="readonly",width=10)
              enCVV.grid(column=5, row=6+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][5]) 
              #
               
              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelframe4, textvariable=self.entryCVV, state="readonly",width=10)
              enCVV.grid(column=6, row=6+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][6]) 

               
              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelframe4, textvariable=self.entryCVV, state="readonly",width=10)
              enCVV.grid(column=7, row=6+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][7]) 
               
              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelframe4, textvariable=self.entryCVV, state="readonly",width=10)
              enCVV.grid(column=8, row=6+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][8]) 

              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelframe4, textvariable=self.entryCVV, state="readonly",width=8)
              enCVV.grid(column=9, row=6+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][9])  
              #
              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelframe4, textvariable=self.entryCVV, state="readonly",width=8)
              enCVV.grid(column=10, row=6+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][10]) 
              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelframe4, textvariable=self.entryCVV, state="readonly",width=8)
              enCVV.grid(column=11, row=6+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][11]) 
              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelframe4, textvariable=self.entryCVV, state="readonly",width=8)
              enCVV.grid(column=12, row=6+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][12]) 
              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelframe4, textvariable=self.entryCVV, state="readonly",width=8)
              enCVV.grid(column=13, row=6+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][13]) 
        

    def carga_articulos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Registro de proyecto")
        self.labelRegistro=ttk.LabelFrame(self.pagina1, text="Formulario de registro")        
        self.labelRegistro.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelRegistro, text="Nombre del Proyecto:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelRegistro, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelRegistro, text="N° de Hitos:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.preciocarga=tk.IntVar()
        self.entryprecio=ttk.Entry(self.labelRegistro, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)
 
        button=Button(self.labelRegistro,text="Registrar Proyecto",command=self.agregar, bg = "#298CF8",fg = "#FFFFFF").grid(column=1, row=2, padx=4, pady=4)
 

    def agregar(self):
        datos=(self.descripcioncarga.get(), self.preciocarga.get())
        valida = self.descripcioncarga.get()
        valida2 = self.preciocarga.get()
        if len(valida)>0 and valida2 >0:
           # print('existe')
            self.articulo1.alta(datos)
            mb.showinfo("Información", "Se registro el proyecto!")
            self.descripcioncarga.set("")
            self.preciocarga.set("")
        else:
            mb.showinfo("Información", "Ingrese los datos correctamente")
 

    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])+"\ndescripción:"+fila[1]+"\nprecio:"+str(fila[2])+"\n\n")
 

    def consulta_proyecto(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Registro de hitos")
        self.labelConsulta=ttk.LabelFrame(self.pagina2, text="Proyecto")
        self.labelConsulta.grid(column=0, row=0, padx=5, pady=10)
        self.labelframeHijo=ttk.LabelFrame(self.pagina2, text="Hitos")
        self.labelframeHijo.grid(column=0, row=5, padx=5, pady=10)

        self.label1=ttk.Label(self.labelConsulta, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelConsulta, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelConsulta, text="Nombre del Proyecto:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        self.nomproyecto=tk.StringVar()
        self.entrynomproyecto=ttk.Entry(self.labelConsulta, textvariable=self.nomproyecto, state="readonly")
        self.entrynomproyecto.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelConsulta, text="Hitos:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        
        self.hitos=tk.StringVar()
        self.entryhitos=ttk.Entry(self.labelConsulta, textvariable=self.hitos, state="readonly")
        self.entryhitos.grid(column=1, row=2, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelConsulta, text="BAC:")        
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        
        self.bac=tk.StringVar()
        self.entryBAC=ttk.Entry(self.labelConsulta, textvariable=self.bac, state="readonly")
        self.entryBAC.grid(column=1, row=3, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelConsulta, text="Buscar", command=self.consultar)
        self.boton1.grid(column=2, row=0, padx=4, pady=4) 

 
    
    def verAcumulados(self):
        datos=(self.codigo.get(), )
        respuesta3=self.articulo1.consultaPV(datos)  
        for fila in respuesta3:
            for i in range(fila[1]):
              self.entryCV=tk.IntVar() 
              enCV = Entry(self.labelConsulta, textvariable=self.entryCV, state="readonly")
              enCV.grid(column=4, row=5+i, padx=4, pady=4) 
              self.entryCV.set(respuesta3[i][0])
            
              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelConsulta, textvariable=self.entryCVV, state="readonly")
              enCVV.grid(column=5, row=5+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][1])

              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelConsulta, textvariable=self.entryCVV, state="readonly")
              enCVV.grid(column=6, row=5+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][2]) 

              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelConsulta, textvariable=self.entryCVV, state="readonly")
              enCVV.grid(column=7, row=5+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][3]) 

              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelConsulta, textvariable=self.entryCVV, state="readonly")
              enCVV.grid(column=8, row=5+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][4]) 
              self.entryCVV=tk.IntVar() 
              enCVV = Entry(self.labelConsulta, textvariable=self.entryCVV, state="readonly")
              enCVV.grid(column=9, row=5+i, padx=4, pady=4) 
              self.entryCVV.set(respuesta3[i][5]) 
         
        

    def consultar(self): 
        self.labelframeHijo.grid_remove()
        datos=(self.codigo.get(), )
        respuesta=self.articulo1.consulta(datos) 
        respuesta2=self.articulo1.consulta2(datos)
        consultaBac=self.articulo1.consultaBac(datos)
        entries = []
        entriesEV = []
        entriesAC = [] 
        if len(respuesta)>0:
            self.labelframeHijo=ttk.LabelFrame(self.pagina2, text="Hitos")
            self.labelframeHijo.grid(column=0, row=5, padx=5, pady=10) 

            self.nomproyecto.set(respuesta[0][0])
            self.hitos.set(respuesta[0][1]) 
            self.bac.set(respuesta[0][2]) 
            entriesCV = [] 
            for fila in respuesta2:
                for i in range(fila[0]):
                    self.label3=ttk.Label(self.labelframeHijo, text="Hito N°:" + str(1+i))        
                    self.label3.grid(column=0, row=5+i, padx=4, pady=4)

                    #self.hitoss=tk.StringVar()
                    self.hitoss=tk.IntVar() 
                    en = Entry(self.labelframeHijo, textvariable=self.hitoss)
                    en.grid(column=1, row=5+i, padx=4, pady=4)

                    self.entryEV=tk.IntVar()  
                    enEV = Entry(self.labelframeHijo, textvariable=self.entryEV)
                    enEV.grid(column=2, row=5+i, padx=4, pady=4)

                    self.entryAC=tk.IntVar()  
                    enAC = Entry(self.labelframeHijo, textvariable=self.entryAC)
                    enAC.grid(column=3, row=5+i, padx=4, pady=4)
                    
                    self.entryCV=tk.IntVar()   
                   

                    entries.append(en)
                    entriesEV.append(enEV)
                    entriesAC.append(enAC)
                     
            self.labelPV=ttk.Label(self.labelframeHijo, text="PV",width=10)        
            self.labelPV.grid(column=1, row=4, padx=4, pady=4)   
            self.labelEV=ttk.Label(self.labelframeHijo, text="EV",width=10)        
            self.labelEV.grid(column=2, row=4, padx=4, pady=4)
            self.labelAC=ttk.Label(self.labelframeHijo, text="AC",width=10)        
            self.labelAC.grid(column=3, row=4, padx=4, pady=4)
        else :
             self.labelframeHijo.grid_remove()
             if len(consultaBac)>0:
                mb.showinfo("Información", "Ya se realizo el registro de PV - EV - AC")
             else:
                mb.showinfo("Información", "No existe un registro con este código")

            
        def registrarHitos():
            BAC = self.codigo.get()
            #print(BAC)
            suma =0
            i=0 
            j=self.articulo1.maxPV()
            if len(j)>0:
             jj  = j[0][0]
            for entry in entries: 
                jj = jj+1  
                suma =suma +int(entry.get())
                i = i+1 
                datos=(jj,entry.get(),self.codigo.get(),suma)
                self.articulo1.agregarPV(datos) 

                self.bac.set(suma)
            actualizaBAC(self)
            registrarEV()
            registrarAC()

        def registrarEV():
            BAC = self.codigo.get()
           # print(BAC)
            suma =0 
            i=0
            j=self.articulo1.maxEV()
            if len(j)>0:
             jj  = j[0][0]
            for entry in entriesEV:
                #print(entry.get())
                jj = jj+1  
                suma =suma +int(entry.get())
                #print(jj) 
                datos=(jj,entry.get(),suma,self.codigo.get())
                self.articulo1.actualizaEV(datos) 

                self.bac.set(suma)

        def registrarAC():
            BAC = self.codigo.get()
           # print(BAC)
            suma =0 
            i=0
            j=self.articulo1.maxAC()
            if len(j)>0:
             jj  = j[0][0]
            for entry in entriesAC: 
                i = i+1
                jj = jj+1 
                
                suma =suma +int(entry.get())  
                datos=(jj,entry.get(),suma,self.codigo.get())
                self.articulo1.actualizaAC(datos) 

                self.bac.set(suma)           

        def actualizaBAC(self):
           # print("aqui "+self.entryBAC.get())
            datos=(self.entryBAC.get(),self.codigo.get())
            self.articulo1.actualizarPV(datos)
            mb.showinfo("Información", "datos actualizados")

        #self.verAcumulados()   
        
        button=Button(self.labelframeHijo,text="Registrar Datos",command=registrarHitos, bg = "#298CF8",fg = "#FFFFFF").grid(column=0, row=4, padx=4, pady=4)
       

        

aplicacion1=FormularioEVM()