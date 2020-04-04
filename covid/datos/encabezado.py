import os
from datetime import datetime
from IPython.display import display, Markdown, Latex


def ordenar_fechas():
  files = os.listdir('./datos')
  prefix = 'covid19_'
  sufix = '_.csv'
  my_dates = []
  for file in files:
    if file.startswith(prefix) and file.endswith(sufix):
      my_dates.append(file.split('_')[1])
  my_dates.sort(key = lambda date: datetime.strptime(date, '%d-%m-%Y'))
  return my_dates[0], prefix+my_dates[0]+sufix

fecha_actualizacion, tabla_de_datos = ordenar_fechas()


display(Markdown(f"""# Exploración de datos de COVID19 :octocat:
## Actualizado el: {fecha_actualizacion}
"""))

display(Markdown(f"""### Fecha de hoy: {datetime.today().strftime('%d/%m/%y')}
"""))

display(Markdown(f"""_Si quieres tener la fecha más reciente,
lee la documentación de este proyecto:
[https://github.com/damian-romero/covid19_mx/blob/master/README.md]_"""))


display(Markdown(f"""#### Este archivo te permitirá explorar los datos del contagio de COVID19 [https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide]"""))

