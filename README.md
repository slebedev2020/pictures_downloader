Формат конфигурационного файла:

Sections:
	Можно задавать в виде списка или в виде словаря(ключ - слово, значение - количество для скачивания)

	sections = {
     "Красная площадь" : 2,
     "Самара" : 3
     }
	 
	sections = [
     "Красная площадь",
     "Самара"
     ]
	
amount:
	в случае поля Sections в виде списка количество для скачивания

color:
	Необязательный
	Основной цвет фотографий
	
size:
	Необязательный
	large или medium
	
store_path:
	Путь для сохранения
	Например, C:\pictures (без кавычек и т.п.)
