from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
#1
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


#2. Проверка, что установление жанра книги работает корректно. positive
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

#2.1. Проверка соответствия некорректного жанра с фильмом. negative
    def test_set_book_genre_not_true(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') != 'Ужасы'

#3. Проверка, что получение жанра книги по её названию работает правильно. positive
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        genre = collector.get_book_genre('Оно')
        assert genre == 'Ужасы'
#3.1. Проверка жанра несуществующей книги. negative
    def test_get_book_genre_is_none(self):
        collector = BooksCollector()
        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")

        assert collector.get_book_genre("Оно 2") is None

#4. Проверка, что метод возвращает список книг с заданным жанром.
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Ужасающий')
        collector.set_book_genre('Ужасающий', 'Ужасы')

        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == ['Гарри Поттер']

#5. Проверка, что метод возвращает словарь с книгами и их жанрами.
    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        books_genre = collector.get_books_genre()
        assert 'Гарри Поттер' in books_genre
        assert books_genre['Гарри Поттер'] == 'Фантастика'


#6. Проверка, что книга добавляется в избранные.
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')

        assert 'Оно' in collector.get_list_of_favorites_books()


#7. Проверка, что книга удаляется из избранных.
    def test_delete_book_from_favorites_not_in(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')

        collector.delete_book_from_favorites('Оно')
        assert 'Оно' not in collector.get_list_of_favorites_books()


#8. Проверка, что метод возвращает правильный список избранных книг.
    def test_get_list_of_favorites_books_(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')

        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Оно']

#9. Параметризованный тест
    @pytest.mark.parametrize("name, genre, expected",
            [
                ["Гарри Поттер", "Фантастика", {"Гарри Поттер": "Фантастика"}],
                ["Оно", "Ужасы", {"Оно": "Ужасы"}],
                ["Убийство в Восточном экспрессе", "Детективы", {"Убийство в Восточном экспрессе": "Детективы"}],
                ["Ревизор", "Комедии", {"Ревизор": "Комедии"}],
            ])
    def test_get_books_genre_parametrized(self, name, genre, expected):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_genre() == expected

    #6.1. Проверка, что метод возвращает книги, которые подходят для детей.
    @pytest.mark.parametrize('books_and_genres, books_for_children_expected', [
        (
            {
                'Гарри Поттер': 'Фантастика',
                'Оно': 'Ужасы',
                'Убийство в Восточном экспрессе': 'Детективы',
                'Волшебник Изумрудного города': 'Фантастика',

            },
            ['Гарри Поттер']
        )
    ])
    def test_get_books_for_children(self, books_and_genres, books_for_children_expected):
        collector = BooksCollector()

        # Добавление книг и их жанров
        for title, genre in books_and_genres.items():
            collector.add_new_book(title)
            collector.set_book_genre(title, genre)

        books_for_children = collector.get_books_for_children()

        for expected_book in books_for_children_expected:
            assert expected_book in books_for_children

        assert len(books_for_children) == len(books_for_children_expected)