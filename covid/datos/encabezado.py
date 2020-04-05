import os
from datetime import datetime
from IPython.display import display, Markdown, Latex


def ordenar_fechas(directorio):
  files = os.listdir(directorio)
  prefix = 'covid19_'
  sufix = '_.csv'
  my_dates = []
  for file in files:
    if file.startswith(prefix) and file.endswith(sufix):
      my_dates.append(file.split('_')[1])
  my_dates.sort(key = lambda date: datetime.strptime(date, '%d-%m-%Y'))
  print(my_dates)
  return my_dates[-1], prefix+my_dates[0]+sufix

def printmd(fecha_actualizacion):
  display(Markdown(f"""# Exploración de datos de COVID19
  ## Actualizado el: {fecha_actualizacion}
  """))

  display(Markdown(f"""### Fecha de hoy: {datetime.today().strftime('%d/%m/%y')}
  """))

  display(Markdown(f"""_Si quieres tener la fecha más reciente,
  lee la documentación de este proyecto:
  [https://github.com/damian-romero/covid19_mx/blob/master/README.md]_"""))

  display(Markdown(f"""#### Este archivo te permitirá explorar los datos del contagio de COVID19 [https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide]"""))

def printhdr(fecha_actualizacion):
  print(f"""# Exploración de datos de COVID19 :octocat:
  ## Actualizado el: {fecha_actualizacion}
  """)

  print(f"""### Fecha de hoy: {datetime.today().strftime('%d/%m/%y')}
  """)

  print(f"""_Si quieres tener la fecha más reciente,
  lee la documentación de este proyecto:
  [https://github.com/damian-romero/covid19_mx/blob/master/README.md]_""")

  print(f"""#### Este archivo te permitirá explorar los datos del contagio de COVID19 [https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide]""")

if __name__ == '__main__':
  directorio = '.'
  fecha_actualizacion, tabla_de_datos = ordenar_fechas(directorio)
  printhdr(fecha_actualizacion)
else:
  directorio = './datos'
  fecha_actualizacion, tabla_de_datos = ordenar_fechas(directorio)
  printmd(fecha_actualizacion)
