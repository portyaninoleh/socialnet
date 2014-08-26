Что бы заинсталить данную апликуху нужно (предполагается, что репозиторий уже склонирован):
1. Создать базу данных. Для этого нужно поставить postgres и выполнить из консоли следующие операции:
psql -Upostgres
Вы попадаете в консоль сервера postgres. Далее:

create database socialnet;
create USER socialnet with password 'socialnet';
GRANT ALL PRIVILEGES ON DATABASE socialnet TO socialnet;

Что бы выйти из этой консоли, наберите \q

2. Далее нужно создать виртуальное окружение. Для этого нужно набрать в консоле:
virtualenv --no-site-packages <virtualenv_name>
Что бы активизировать его нужно набрать следующее:
source <virtualenv_name>/bin/activate

3. Заинсталить зависимости (Только из-под активизированного virtualenv):
pip install -r requirements.pip

4. Мигрировать базу:
python manage.py migrate

5. И залитьизначальные данные:
python manage.py loaddata common/basedata.json

6. Запустить проэкт
python manage.py runserver 0.0.0.0:8000

7. Открыть в браузере http://localhost:8000
