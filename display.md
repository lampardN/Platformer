# [pygame.display](https://www.pygame.org/docs/ref/display.html)

Данный модуль предоставляет контроль над дисплеем pygame. У pygame есть объект Surface экрана, который может быть запущен в окне или на полный экран.
Как только вы создали экран, вы можете использовать его как обычный объект типа Surface. Изменения не появляются на экране немедленно;
вы должны использовать одну из функций для обновления состояния экрана.

Начало экрана, то есть координаты `x = 0`, `y = 0`, находится в левом верхнем углу экрана. Обе оси имеют положительное направление и направлены вправо и внизу экрана соответственно.

Экран pygame может быть инициализирован в одном из нескольких режимов. По умолчанию экран - это буфер кадров, управляемый безовым программным обеспечением. Вы можете запрашивать специальные модули такие как модули аппаратного ускорения или поддержки OpenGL. Они контролируются с помощью флагов, передаваемых в `pygame.display.set_mode()`. 

В pygame может быть только один экран в отдельный момент времени. Создание нового с помощью `pygame.display.setmode()` будет закрывать предыдущий экран.
Если требуется точный контроль над форматом пикселей или разрешениями экрана, используйте функции `pygame.display.mode_ok()`, `pygame.display.list_modes()` и `pygame.display.Info()`, чтобы запросить информацию об экране.

Как только создан объект Surface экрана, функции из этого модуля влияют на существующий в данный момент экран. Объект Surface становится невалидным, если модуль не инициализирован. Если установлен новый режим экрана, то существующий объект Surface будет автоматически переключен для работы на новом экране.

Когда устанавливается режим экрана несколько событий помещаются в очередь событий pygame. `pygame.QUIT` отправляется, когда пользователь запрашивает выключение программы. Окно будет получать события `pygame.ACTIVEEVENT`, когда экран получает и теряет фокус. Если для
экрана установлен флаг `pygame.RESIZABLE`, то события `pygame.VIDEORESIZE` будут происходить, когда пользователь меняет размеры окна. 
Аппаратные экраны, которые выводят изображения напрямую на экран, будут получать события `pygame.VIDEOEXPOSE`, когда части экрана должны быть перерисованы. 

Некоторые окружения экрана имеют параметры для автоматического растягивания всех окон. Когда эта опция включена, это автоматическое растягивание может искажать содержимое окна pygame. В папке с примерами к pygame есть пример кода (prevent_display_stretching.py), который показывает как отключить автоматическое растягивание экрана на Microsoft Windows (для версий Vista или новее).
