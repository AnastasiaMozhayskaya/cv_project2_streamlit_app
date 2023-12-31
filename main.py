import streamlit as st

st.write("""
 # Очищение документов от шума📝 и Детекция объектов🔎
""")

st.write("""
  ### Команда: :rainbow[Mask R-CNN Team]
""")

st.write("""
  ### Состав команды: 
  \n1. ##### Анастасия 🤿
  \n2. ##### Роман 🤿
  \n3. ##### Руслан 🤿
""")

st.write("""
  ### Проекты:
""")

st.write("""
  ### 1. Автоэнкодер для очищения фотографий от шума.
  \n ##### Задачи:
        \n- Создать архитектуру модели для кодирования и декодирования входного объекта.
        \n- Провести обучение, учитывая следующие нюансы: делать предсказание модели на объекте с шумом, уменьшать Loss-func на аналогичном объекте без шума.
        \n- Отобрать веса, которые показали наилучший результат на тестовой выборке.
  
  \n ### 2. Детекция судов и кораблей на фотоснимках.
  \n #####  Задачи:
        \n- Загрузить размеченный датасет для детекции.
        \n- Протестировать результаты детекции на нескольких моделях (в приоритете были модели YOLOv5 и YOLOv8).
        \n- Выбрать наиболее оптимальную модель (веса) по объему памяти, количеству слоев и скорости предсказания.
""")

st.info('Обученные модели под наши задачи находятся в разделах: 🚢Ship и 📃Clearing_documents. '
        '\nКаждый сможет опробовать модели на своих примерах. Особенно полезной будет модель для очищения картинок от шума.'
        '\nМы старались!😇')

st.write("""
 ##### А теперь мы двинемся к тестированию наших крутых моделей, а также расскажем более подробно об этапах их создания... Вперед🚀
""")