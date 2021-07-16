id_proyecto = input('Id de proyecto: ')
nombre_proyecto = input('Nombre de proyecto: ')
hitos = int(input('Número de hitos: '))

matriz = []
bac = 0
for i in range(hitos):
    row = []
    print(f'Hito {i + 1}')
    row.append(float(input('PV (Valor planteado): ')))
    row.append(float(input('EV (Valor Ganado): ')))
    row.append(float(input('AC (Costo Real): ')))
    bac += row[0] + row[1] + row[2]
    matriz.append(row)

pv = 0
ev = 0
ac = 0

print('\nIdProyecto: %s\nNombreProyecto: %s\nHitos: %s\nBAC: %.2f\n' % (id_proyecto, nombre_proyecto, hitos, bac))

print("%-15s%-15s%-20s%-20s%-20s%-15s%-15s%-15s%-10s%-10s%-10s%-10s" % 
      ('IdProyecto','NumeroHito','PV (Valor Planeado)','EV (Valor Ganado)',
       'AC (Costo Real)','PV_ACUMULADO','EV_ACUMULADO','AC_ACUMULADO','CV','SV','CPI','SPI'))

for i in range(hitos):
    pv += matriz[i][0]
    ev += matriz[i][1]
    ac += matriz[i][2]
    cv = ev - ac
    sv = ev - pv
    cpi = round(ev / ac, 4)
    spi = round(ev / pv, 4)
    
    print("%-15s%-15i%-20.2f%-20.2f%-20.2f%-15.2f%-15.2f%-15.2f%-10.2f%-10.2f%-10.3f%-10.3f" % 
          (id_proyecto, (i + 1), matriz[i][0], matriz[i][1], matriz[i][2], 
           pv, ev, ac, cv, sv, cpi, spi))
    
    