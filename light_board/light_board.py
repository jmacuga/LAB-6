from light_board_text import LightBoardText
from datetime import date


class TextError(Exception):
    pass


class TextNotFoundError(Exception):
    pass


class LightBoard:
    def __init__(self, serial_num: int, width: int, height: int, letter_width: int, letter_height: int, texts=[]):
        self.__validate_arguments(serial_num,
                                  width, height, letter_width, letter_height)
        self._serial_num = serial_num
        self._width = width
        self._height = height
        self._letter_width = letter_width
        self._letter_height = letter_height
        self.check_texts(texts)
        self._texts = texts

    def get_serial_num(self):
        return self._serial_num

    def get_width(self):
        return self._width

    def get_hight(self):
        return self._height

    def get_letter_width(self):
        return self._letter_width

    def get_letter_hight(self):
        return self._letter_height

    def get_texts(self):
        return self._texts

    def add_text(self, new_text):
        self.check_fit(new_text)
        if not new_text:
            raise ValueError
        for text in self._texts:
            if self.check_overlap(text, new_text):
                raise TextError(
                    "New text must not overlap the rest of the texts")
        self._texts.append(new_text)

    def remove_text(self, point: tuple):
        if point[0] > self._width or point[1] > self._height:
            raise ValueError(
                f'Point ({point[0]},{point[1]}) is not on the board')
        self._texts.remove(self.get_text(point))

    def get_text(self, point: tuple):
        for text in self._texts:
            end_p = text.end_point(self._letter_width, self._letter_height)
            start_p = text.get_start_point()
            if start_p[0] <= point[0] <= end_p[0] and start_p[1] <= point[1] <= end_p[1]:
                return text
        raise TextNotFoundError

    def generate_raport(self, prize_per_hour):
        # której parametrem jest cena wyświetlenia jednego punktu przez jedną godzinę; raport ma zawierać:
        # datę wygenerowania, numer seryjny tablicy i jej parametry, listę wyświetlanych napisów
        # gdzie dla każdego napisu podane sa jego parametry (położenie i tekst)
        # oraz zajmowana powierzchnia (w punktach kwadratowych) oraz cena wyświetlenia przez jeden dzień.
        today = date.today().isoformat()
        output_str = '{0}\nserial number: {1._serial_num}, width: {1._width}, height: {1._height},' \
            ' letter width: {1._letter_width}, letter height: {1._letter_height}\nTEXTS:\n'.format(
                today, self)
        f'{self._letter_height}\n texts:\n'
        i = 0
        for text in self._texts:
            i += 1
            output_str += f'{i}. {text}\n'
        print(output_str)

    def __validate_arguments(self, serial_num: int,  width: int, height: int, letter_width: int, letter_height: int):
        if type(width) != int or type(height) != int or type(letter_height) != int or type(letter_width) != int or type(serial_num) != int:
            raise TypeError
        if serial_num < 0:
            raise ValueError("Incorrect serial number")
        if width <= 0 or height <= 0:
            raise ValueError("Incorrect board size")
        if letter_height <= 0 or letter_width <= 0:
            raise ValueError("Wrong Letter Size")

    def check_texts(self, texts):
        # check if texts dont overlap
        # check if texts fit on the board
        for text in texts:
            self.check_fit(text)
            if not text:
                raise ValueError
            for other_text in texts:
                if text == other_text:
                    continue
                if self.check_overlap(text, other_text):
                    raise TextError("Texts must not overlap")

    def check_overlap(self, text1: LightBoardText, text2: LightBoardText):
        # returns True if texts overlap
        text1_end_point = text1.end_point(
            self._letter_width, self._letter_height)
        text2_end_point = text2.end_point(
            self._letter_width, self._letter_height)
        return not (text1_end_point[0] < text2.get_start_point()[0] or
                    text1.get_start_point()[0] > text2_end_point[0] or
                    text1_end_point[1] < text2.get_start_point()[1] or
                    text1.get_start_point()[1] > text2_end_point[1])

    def check_fit(self, text):
        end_p = text.end_point(self._letter_width, self._letter_width)
        if end_p[0] > self._width or end_p[1] > self._height:
            raise TextError("Text does not fit in the board")


text1 = LightBoardText("texte", (1, 1))
text2 = LightBoardText("cos", (1, 2))
text3 = LightBoardText("inny", (6, 2))
board = LightBoard(11, 10, 10, 1, 1, [text1, text2, text3])
board.generate_raport(10)
