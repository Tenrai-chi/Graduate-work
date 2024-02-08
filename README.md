# Graduate-work
Тренажер по цифровой логике для студентов 1 курса. Он позволяет сформировать у студентов умение читать логические схемы.

* **Генератор заданий** В своей основе тренажер содержит генератор логических схем. Каждое задание создает новую логическую схему на основе шаблонов, в которых все элементы, а именно входящие сигналы и логические элементы выбираются случайным образом. Всего доступно 3 типа заданий:
    - Первый тип представляет из себя логическую схему с неизвестным для пользователя сигналом на выходе. Пользователь должен указать значение неизвестного сигнала;
      ![image](https://github.com/Tenrai-chi/Graduate-work/assets/79309888/f57d7680-847a-4467-8303-0aa53bba44ca)
    - Во втором типе заданий неизвестно одно из входящих значений, а сигнал на выходе известен. Пользователь так же должен указать значение неизвестного сигнала;
      ![image](https://github.com/Tenrai-chi/Graduate-work/assets/79309888/36695a4e-0be6-4682-a8ec-7ee3f623c7aa)
    - Третий тип заданий – это усложненная версия первого типа. Помимо сигнала на выходе пользователю необходимо указать значение промежуточных элементов схемы. Если хотя бы один элемент будет указан неверно – всё задание будет считаться невыполненным.
      ![image](https://github.com/Tenrai-chi/Graduate-work/assets/79309888/e3ed96c6-0085-4862-b84c-87fb5e22e916)
* **Нотации** Для обозначения логических вентилей тренажер использует нескольно видов нотаций: IEC, ANSI и булевы функции.

* **Три режима** Всего тренажер поддерживает 3 режима работы:
    - Обучение. Пользователь свободно выбирает интересующий типа задания, используемую нотацию. Также ему доступны подсказки и справочная информация. Этот режим предназначен для знакомтсва пользователями с тренажером и доступными заданиями.
    - Тренировка. Каждое новое задание как и используемая нотация выбирается случайно. пользователю доступная смена нотации при необходимости и просмотр справочных материалов. В этом режиме ведется учет правильных ответов и он предназначен для подготовки к тестированию.
    - Тестирование. Пользователю предлагается пройти определенное количество заданий разного типа. В каждом задании меняется использованная нотация и ее невозможно поменять. В этом режиме не доступны подсказки и смена режима. Каждый ответ учитывается и влияет на конечную оценку. Этот режим необходим для проверки знаний обучающихся и отслеживания их успеваемости.

* **Интерфейс**
  На экран выводится логическая схема. В зависимости от типа задания скрывается одно из сигналов, значение которого нужно вычислить согласно заданию. Ниже расположена панель с текстом задания и доступными вариантами ответа: True и False. После ответа пользователя на схеме открывается правильный ответ, а на панели задания появляется оценка и кнопка с предложением перейти к следующему заданию. Во время выполнения задания пользователь может просматривать справочные материалы по логическим элементам. Для этого ему необходимо кликнуть на интересующий его элемент и на экране появится справка, содержащая в себе название логического элемента, его обозначения в различных нотациях и его таблицу истинности. Помимо справки пользователь может помечать цветом связи между элементами как для упрощения прохождения задания, так и в качестве обязательного действия для ответа на задания третьего типа.
  ![image](https://github.com/Tenrai-chi/Graduate-work/assets/79309888/5de22598-141f-4c85-84f7-2fe30c3d3410)

  * **Настройка тестирования**

Библиотеки: Tkinter, Pillow

