# Cайт для Telegram WebApp 
### [Техническая задача "DiamondGaming"](https://teletype.in/@sxm/r7AsIau4JYHsqqE)

## Оглавление:
- [Технологии](#технологии)
- [Установка и запуск](#установка-и-запуск)
- [Описание работы](#описание-работы)
- [Удаление](#удаление)

## Технологии
<details>
  <summary>Подробнее</summary>
    <p><strong>Языки программирования:</strong> python, javascript</p>
    <p><strong>Фреймворк и модули:</strong> Django, djangorestframework, django-channels</p>
    <p><strong>Базы данных и инструменты работы с ними:</strong> PostgreSQL, SQLite, Redis</p>
    <p><strong>Отложенные задачи:</strong>celery</p>  
    <p><strong>CI/CD:</strong> Docker Hub, Docker Compose, uWSGI, daphne, Nginx</p>  
</details>

## Установка и запуск

<details>
  <summary>Предварительные условия</summary>
  <p>Предполагается, что пользователь:</p>
  
  - Создал аккаунт [DockerHub](https://hub.docker.com/).
  - Установил [Docker](https://docs.docker.com/engine/install/) и [Docker Compose](https://docs.docker.com/compose/install/) на локальной машине или удаленном сервере, где проект будет запускаться в контейнерах. Проверить наличие можно выполнив команды:
    
  `docker --version && docker-compose --version`
  
</details>
<details>
  <summary>Запуск</summary>
  
  <p><strong>!!! Для пользователей Windows обязательно выполнить команду:</strong></p>
  
    `git config --global core.autocrlf false`
    
  <p>иначе файл start.sh при клонировании будет бракован</p>
  
  1. Клонируйте репозиторий с GitHub и введите данные для переменных окружения (значения даны для примера, некоторые можно оставить по типу DB*):
    
    git clone https://github.com/s0ull877/DIAMOND.git && \
    cd DIAMOND/app && \
    cp .env_example .env && \
    nano .env

  2. Из корневой директории проекта выполните команду:

    docker compose -f casino_infra/docker-compose.yml up -d --build

  Проект будет развернут в шести docker-контейнерах (db, asgi, wsgi, redis, celery, nginx) по адресу `http:/host_ip/`
  
  3. Остановить docker и удалить контейнеры можно командой из корневой директории проекта:

    docker compose -f infra/docker-compose.yml down
  
  Если также необходимо удалить тома базы данных, статики и медиа:

    docker compose -f infra/docker-compose.yml down -v

</details>

---

При первом запуске будут автоматически произведены следующие действия:

  - выполнены миграции

  - собрана статика

  - создан суперюзер с учетными данными:


## Описание работы

Проект представляет из себя сайт/webapp, переход в который осущетсвляется через inline button в телеграм боте.<br>
Требования к сайту:

  - Реализация API для коннекта бота к вебапп и вывода актуальных действий пользователя в обоих сервисах

  - Реализация онлайн игр из ТЗ: Аукцион, Крестики-Нолики, Джекпот

  - Сайт должен иметь 3 языка: Английский, Украинский, Русский.

В ходе реализации проекта, т.к. регистрация пользователей происходит в телеграм боте, было принято решение создавать [кастомного юзера](https://github.com/s0ull877/DIAMOND/blob/master/app/users/models.py).<br>


## Удаление
Для удаления проекта выполните следующие действия:

  `cd .. && rm -fr DIAMOND && deactivate`

[Оглавление](#оглавление)

## <a id="#автор">Автор</a>
[Radmir Galiullin](https://github.com/s0ull877)
