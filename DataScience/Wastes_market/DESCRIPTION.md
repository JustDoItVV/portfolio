# Industrial waste products market in Russia (TAM-SAM-SOM)
[English version](#English-version)

[Русская версия](#Русская-версия)

## English version
The estimation was carried out within the framework of the project "Экологически-рациональная альтернатива" (Environmentally sustainable alternative). 
The project is a web marketplace for the sale of industrial waste products with integration of state personal account of a natural resource user. 
The project aims to simplify the sale of waste products from manufacturers, the resources search for waste disposers and the interaction of both sides with government authorities. 
It is assumed that the project will increase the number of recycled waste and reduce the number of landfills as part of the implementation of the national project Ecology.
The market estimation is carried out both from the top and bottom-up ways.
The data was collected using my own web scraper from the site of the competitor of the project.

Used environment - Google Colab, Tableau Public

Dataset obtaining date is 2021-10-24

**Files:**
* [Industrial_waste_products_market_in_Russia_(TAM_SAM_SOM).ipynb](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Wastes_market/Industrial_waste_products_market_in_Russia_(TAM_SAM_SOM).ipynb) – Web Scraper and the data analysis
* [wastes_reactor_2021_10_24.csv](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Wastes_market/wastes_reactor_2021_10_24.csv) – Dataset with wastes advertisements from the competitotrs site in csv
* [wastes_reactor_2021_10_24.xlsx](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Wastes_market/wastes_reactor_2021_10_24.xlsx) – The same in excel


**Features description:**

- **Status** - Status of the advertisement: open for sale, sold
- **Date** - Publish date of the advertisement
- **Title** - The advertisement title
- **Price** - Price in rubles for a waste unit
- **Price_units** - Price units
- **Amount** - Waste amount for sale
- **Amount_units** - Units of waste amount
- **Waste_type** - Waste type


____


## Русская версия
Оценка проводилась в рамках проекта «Экологически-рациональная альтернатива».
Проект представляет собой интернет-площадку по продаже промышленных отходов с интеграцией государственного личного кабинета приодопользователя.
Проект направлен на упрощение продажи отходов производства от предприятий-производителей, поиск ресурсов для переработчиков отходов и взаимодействие обеих сторон с государственными органами.
Предполагается, что в рамках реализации нацпроекта «Экология» проект увеличит количество переработанных отходов и сократит количество полигонов/свалок.
Оценка рынка выполнена как "сверху", так и "снизу".
Данные собраны с помощью собсвенного парсера с сайта конкурента проекта.

Среда - Google Colab, Tableau Public

Дата сбора данных - 2021-10-24

**Файлы:**
* [Industrial_waste_products_market_in_Russia_(TAM_SAM_SOM).ipynb](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Wastes_market/Industrial_waste_products_market_in_Russia_(TAM_SAM_SOM).ipynb) – Веб парсер и анализ данных
* [wastes_reactor_2021_10_24.csv](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Wastes_market/wastes_reactor_2021_10_24.csv) – Набор данных с объявлениями о продаже отходов с сайта конкурента в csv
* [wastes_reactor_2021_10_24.xlsx](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Wastes_market/wastes_reactor_2021_10_24.xlsx) – То же в excel

**Описание характеристик набора данных:**

- **Status** - Статус объявления: открыто, продано.
- **Date** - Дата публикации объявления
- **Title** - Заголовок объявления
- **Price** - Цена за единицу отходов
- **Price_units** - Размерность цены
- **Amount** - Количество отходов на продажу
- **Amount_units** - Единицы измерения количества отходов
- **Waste_type** - тип отходов
