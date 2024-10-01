import pandas as pd
import matplotlib.pyplot as plt

# Пример данных
data = {
    'Год': [2020, 2020, 2020, 2020, 2020, 2020, 
            2021, 2021, 2021, 2021, 2021, 2021],
    'Месяц': ['January', 'February', 'March', 'April', 'May', 'June', 
              'January', 'February', 'March', 'April', 'May', 'June'],
    'Значение': [10, 15, 20, 25, 30, 35, 
                 12, 18, 22, 28, 32, 38]
}

df = pd.DataFrame(data)

# Создание столбца с датами
# Сначала создаем числовые значения для месяцев
df['Месяц'] = pd.to_datetime(df['Месяц'], format='%B').dt.month

# Создаем столбец с датами
df['Дата'] = pd.to_datetime(df[['Год', 'Месяц']].assign(День=1), dayfirst=True)

# Группировка данных по годам и месяцам
df_grouped = df.groupby(['Год', 'Месяц'])['Значение'].sum().reset_index()

# Построение графика
plt.figure(figsize=(10, 5))

# Для каждого года строим линию
for year in df_grouped['Год'].unique():
    subset = df_grouped[df_grouped['Год'] == year]
    plt.plot(subset['Месяц'], subset['Значение'], marker='o', label=year)

# Настройка графика
plt.title('Значения по месяцам для каждого года')
plt.xlabel('Месяц')
plt.ylabel('Значение')
plt.xticks(ticks=range(1, 13), labels=['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 
                                         'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'], rotation=45)
plt.legend(title='Год')
plt.grid()
plt.tight_layout()

# Показать график
plt.show()
