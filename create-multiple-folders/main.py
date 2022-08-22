import calendar
from pathlib import Path

# Crear funcion main
def main():
    # Crear lista con los meses del año
    list_months = list(calendar.month_name[1:])

    # Crear lista con días aleatorios del mes manualmente
    list_days = ['Dia 1', 'Dia 3', 'Dia 6', 'Dia 9', 'Dia 12', 'Dia 15', 'Dia 18', 'Dia 21', 'Dia 24', 'Dia 27',
                 'Dia 30']

    # Crear carpetas para el año 2022
    for i, month in enumerate(list_months):
        for day in list_days:
            Path(f'2022/{i + 1}.{month}/{day}').mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    main()