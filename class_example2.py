import requests

class Publication:
    __udc = '0.0.0' #приватный атрибут, видимый только классу
    default_format = 'hardcover'
    default_edition = 'basic edition'

    # Конструктор
    def __init__(self, title, author, year, publisher):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher

    #Метод класса, зависит от экземпляра
    def get_short_info(self):
        return f'{self.title} by {self.author}'


    #Метод класса, общий для всех
    @classmethod
    def get_default_edition(self):
        return self.default_format, self.default_edition

    #Публичный метод , работающий с приватным атрибутом
    def get_udc(self):
        return self.__udc

    #Приватный метод класса
    def __set_udc(self,udc):
        self.__udc = udc


class Book(Publication):
    def get_book_udc(self):
        return self.__udc

    #Статический метод
    @staticmethod
    def get_phrase_of_a_day():
        r = requests.get('https://citbase.ru/random', timeout=20)
        txt = r.text
        tag_beg = '<pre>'
        tag_end = '</pre>'
        ben = txt.find(tag_beg) + len(tag_beg)
        end = txt.find(tag_end)
        txt = txt[ben:end]
        return txt



if __name__  == '__main__':
    # pub = Publication('статья', 'Иванова И.И.', 2024, 'Зеленоград24')
    # book = Book('Мастер и Маргарита', "Булгаков М.А.", 2024, "АСТ")
    # print(pub.get_short_info())
    # print(Publication.get_default_edition())
    # print(pub.get_udc())
    # print(book.get_udc())
    # print(book.get_book_udc()) #не имеет доступ к классу
    print(Book.get_phrase_of_a_day())

