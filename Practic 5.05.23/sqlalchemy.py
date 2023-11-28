


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# создаем подключение к базе данных SQLite
engine = create_engine('sqlite:///example.db')

# создаем объект-сессию, через который будем общаться с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# создаем базовый класс, от которого будут наследоваться все остальные классы-модели
Base = declarative_base()

# создаем класс-модель для таблицы users
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# создаем таблицу в базе данных
Base.metadata.create_all(engine)

# добавляем запись в таблицу
user = User(name='John', age=30)
session.add(user)
session.commit()

# получаем записи из таблицы
users = session.query(User).all()
for user in users:
    print(user.id, user.name, user.age)
