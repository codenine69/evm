import mysql.connector

class Conexion:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="root", 
                                              database="evm")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into proyecto(nom_proyecto, hitos) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
    
    def agregarPV(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()  
        print(datos)
        sql="insert into detallepv (orden,pv,id_proyecto,pv_acumulado) values (%s,%s,%s,%s)"
        cursor.execute(sql,datos) 
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select nom_proyecto, hitos,bac from proyecto where idproyecto=%s and bac is null"
        cursor.execute(sql, datos)
        #cone.close()
        return cursor.fetchall()
    def consultaBac(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select nom_proyecto, hitos,bac from proyecto where idproyecto=%s and bac >=0"
        cursor.execute(sql, datos)
        #cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select idproyecto, nom_proyecto, hitos from proyecto"
        cursor.execute(sql)
        #cone.close() 
        return cursor.fetchall()

        
    def consulta2(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select hitos from proyecto where idproyecto=%s"
        cursor.execute(sql, datos)
        #cone.close()
        return cursor.fetchall()  

   

    def actualizarPV(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()  

        sql="update proyecto set bac = %s where idproyecto = %s"
        cursor.execute(sql,datos) 
        cone.commit()
        cone.close()

    def actualizaEV(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()  
        print(datos)
        sql="insert into detalleev (orden,ev,ev_acumulado,id_proyecto) values (%s,%s,%s,%s)"
        #sql="update detalle_proyecto set ev = %s, ev_acumulado=%s where id_proyecto=%s"
        cursor.execute(sql,datos) 
        cone.commit()
        cone.close()
    
    def actualizaAC(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()  
        print(datos)
        sql="insert into detalleac (orden,ac,ac_acumulado,id_proyecto) values (%s,%s,%s,%s)"
        #sql="update detalle_proyecto set ev = %s, ev_acumulado=%s where id_proyecto=%s"
        cursor.execute(sql,datos) 
        cone.commit()
        cone.close()

    def consultaPV(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select pv,pv_acumulado, ev,ev_acumulado,ac,ac_acumulado,(ev_acumulado - ac_acumulado)as cv, (ev_acumulado - pv_acumulado)as sv, (ev_acumulado/ac_acumulado) as cpi, (ev_acumulado/pv_acumulado) as spi,((bac- ev_acumulado)/(bac-ac_acumulado))as tcpi, (bac/(ev_acumulado/ac_acumulado)) as eac, ((bac/(ev_acumulado/ac_acumulado))-ac_acumulado) as etc,(bac-(bac/(ev_acumulado/ac_acumulado)))as vac,bac from detallepv  inner join detalleev on detallepv.orden = detalleev.orden inner join detalleac on detalleac.orden = detalleev.orden  inner join proyecto on detalleev.id_proyecto = proyecto.idproyecto where detallepv.id_proyecto =%s"
        cursor.execute(sql, datos)
        #cone.close()
        return cursor.fetchall()

    def consultaEV(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select ev,ev_acumulado from detalleev where id_proyecto =%s"
        cursor.execute(sql, datos)
        #cone.close()
        return cursor.fetchall()

    def consultaAC(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select ac,ac_acumulado from detalleac where id_proyecto =%s"
        cursor.execute(sql, datos)
        #cone.close()
        return cursor.fetchall()

    def maxEV(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql=" select max(orden) + 1 as orden from detalleev"
        cursor.execute(sql)
        #cone.close()
        return cursor.fetchall()

    def maxPV(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql=" select max(orden) + 1 as orden from detallepv"
        cursor.execute(sql)
        #cone.close()
        return cursor.fetchall()

    def maxAC(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql=" select max(orden) + 1 as orden from detalleac"
        cursor.execute(sql)
        #cone.close()
        return cursor.fetchall()