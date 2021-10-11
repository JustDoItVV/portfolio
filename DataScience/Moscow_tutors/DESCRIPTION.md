# Moscow tutor's price prediction
[English version](#English-version)

[Русская версия](#Русская-версия)

## English version
The aim is to build a model for estimation of a price of tutor's services in Moscow. For model creation a dataset collected based on the open information from the site [Ассоциация репетиторов](https://repetit.ru/) (in Russian). The dataset collected using a web scraper.

Used environment - Google Colab

Dataset obtaining date is 2021-10-06

**Files:**
* [Web_Scraper_for_tutors_dataset.ipynb](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Moscow_tutors/Web_Scraper_for_tutors_dataset.ipynb/) – Web Scraper
* [tutors_eng_2021_10_06.csv](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Moscow_tutors/tutors_eng_2021_10_06.csv) – Dataset in English, translated and transliterated from Russian
* [tutors_rus_2021_10_06.csv](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Moscow_tutors/tutors_rus_2021_10_06.csv) – Dataset in Russian
* [data_for_predictions.xlsx](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Moscow_tutors/data_for_predictions.xlsx) – User conditions for price estimation
* [Moscow_tutor's_price_prediction.ipynb](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Moscow_tutors/Moscow_tutor's_price_prediction.ipynb) – Dataset analysis, model creation, price estimation

**Features description:**

- **Categories** - Lists of taught subjects out of 27 subjects
- **Price** - Price in rubles per hour
- **Score** - Average score based on the reviews, 0.0-5.0
- **Format** - Lists of working formats. Options: remotely, at the tutor's place, at the student's place
- **Reviews_number** - Amount of student's reviews in the tutor's profile
- **Experience** - Experience in years
- **Status** - Current tutor's status. Options: Private tutor, School teacher, Postgraduate student, Native speaker, University professor, Student, not stated (missing)
- **Location** - Metro stations or cities in Moscow region
- **Tags** - Tutor's services. They are stated by tutors and can differs. They are remained in Russian in the dataset
- **Audience** - Tutor's target audience. For example: students, pupils of 10 grades etc. They are stated by tutors and can differs
- **Video_presentation** - Video presentation availability
- **Photo** - Profile photo availability


____


## Русская версия
Цель - сделать модель для оценки цены услуг репетитора в Москве. Для создания модели на основе открытой информации с сайта [Ассоциация репетиторов](https://repetit.ru/) с помощью веб парсера собран набор данных.

Среда - Google Colab

Дата сбора данных - 2021-10-06

**Файлы:**
* [Web_Scraper_for_tutors_dataset.ipynb](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Moscow_tutors/Web_Scraper_for_tutors_dataset.ipynb/) – Веб парсер
* [tutors_eng_2021_10_06.csv](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Moscow_tutors/tutors_eng_2021_10_06.csv) – Набор данных на английском, переведенный и транлитерированный
* [tutors_rus_2021_10_06.csv](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Moscow_tutors/tutors_rus_2021_10_06.csv) – Набор данных на русском
* [data_for_predictions.xlsx](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Moscow_tutors/data_for_predictions.xlsx) – Пользовательские условия для оценки цены
* [Moscow_tutor's_price_prediction.ipynb](https://github.com/JustDoItVV/portfolio/blob/main/DataScience/Moscow_tutors/Moscow_tutor's_price_prediction.ipynb) – Анализ набора данных, построение модели и оценка

**описание характеристик набора данных:**

- **Categories** - Списки преподаваемых предметов из 27 предметов
- **Price** - Цена в руб/ч
- **Score** - Средняя оценка по отзывам, 0.0-5.0
- **Format** - Списки форматов работы. Варианты: удаленно, у репетитора, у ученика
- **Reviews_number** - Количество отзывов в профиле репетитора
- **Experience** - Опыт в годах
- **Status** - Текущий статус репетитора. Варинанты: Независимый репетитор, Школьный учитель, Аспирант, Носитель языка, Преподаватель университета, Студент, не указано (пропущенное значение)
- **Location** - Станции метро или города за МКАДом
- **Tags** - Услуги репетитора. Вводятся репетитором и могут различаться. В наборе данных оставлены на русском языке
- **Audience** - Целевая аудитория репетитора. Например: студенты, школьники 10 класса и т.д. Указываются репетитором и могут быть различны
- **Video_presentation** - Наличие видео презентации
- **Photo** - Наличие фото профиля
