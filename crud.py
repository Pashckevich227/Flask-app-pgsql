from datetime import datetime
from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI
from models import Base, Book
from contextlib import contextmanager


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


# -----Внесение данных-----
# book = Book(
#     title='One way path.',
#     author='D. Bergman',
#     pages=124,
#     published=datetime(1991, 1, 15)
# )
#
# s.add(book)
# s.commit()

# print(s.query(Book)[-1])


# -----Фильтрация-----
# r = s.query(Book).filter(Book.title.ilike == 'Deep Learning').first()      # Для сложных SELECT
# print("filter:", r)

# r = s.query(Book).filter_by(title='Deep Learning').first()      # Для простых SELECT
# print("filter_by:", r)


# -----Фильтрация по дате через datatime-----
# start_date = datetime(2010, 1, 1)
# end_date = datetime(2020, 1, 1)
#
# print(*s.query(Book).filter(Book.published.between(start_date, end_date)).all(), sep='\n')


# -----Фильтрация по and_ и or_ -----
# print(s.query(Book).filter(
#     and_(
#         Book.pages > 200,
#         Book.published > datetime(2015, 1, 1)
#     )
# ).all())
#
# print(s.query(Book).filter(
#     or_(
#         Book.published < datetime(2010, 1, 1),
#         Book.published > datetime(2016, 1, 1)
#     )
# ).all())

# -----ORDER BY -----
# print(*s.query(Book).order_by(Book.id.desc()).all(), sep='\n')


# -----LIMIT-----
# print(s.query(Book).limit(2).all(), sep='\n')


# -----Multi querying-----
# print(*s.query(Book).filter(
#     and_(
#         or_(
#             Book.pages < 500,
#             Book.pages > 750
#         ),
#         Book.published.between(start_date, end_date)
#     )
# ) \
#       .order_by(Book.pages.desc())\
#       .limit(2)\
#       .all(), sep='\n')


# -----Add new values in column 'price'-----
# books = s.query(Book).all()
# for book in books:
#     price = input(f"Price for '{book.title}': $")
#     book.price = price
#     s.add(book)
#
# s.commit()
# s.close()


# with session_scope() as s:
#     book = s.query(Book).filter(Book.title.ilike('%Deep Learning%')).first()
#     book.price = '6,00'
#     s.add(book)

# with session_scope() as s:
#     print(*s.query(Book).order_by(Book.id.asc()).all(), sep='\n')

# s.close_all()
