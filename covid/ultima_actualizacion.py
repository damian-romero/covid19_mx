from datetime import datetime
from IPython.display import display, Markdown, Latex

csvs = ['05-11-2018', '25-03-2017', '01-11-2018', '07-03-2017']

# my_dates.sort(key=lambda date: datetime.strptime(date, 'd-%m-%y'))

def ordenar_fechas(my_dates):
  print(my_dates)
  my_dates.sort(key = lambda date: datetime.strptime(date, '%d-%m-%Y'))
  return my_dates[0]

fecha_actualizacion = ordenar_fechas(csvs)



display(Markdown(f"""Hoy es: {datetime.today().strftime('%d/%m/%y')}"""))
display(Markdown(f"""Última actualización de los datos de COVID-19: {fecha_actualizacion}"""))
display(Markdown(f"""Si quieres tener la fecha más reciente, lee la documentación de este proyecto:
https://github.com/damian-romero/covid19_mx/blob/master/README.md"""))



