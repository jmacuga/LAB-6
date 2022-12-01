from light_board_text import LightBoardText
from datetime import date


class TextError(Exception):
    pass


class TextNotFoundError(Exception):
    pass


class LightBoard:
    def __init__(self, serial_num: int, width: int, height: int, letter_width: int, letter_height: int, texts=[]):
        self.validate_arguments(serial_num,
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
        try:
            text = self.get_text_at_start_point(point)
            self._texts.remove(text)
            return str(text)
        except(TextNotFoundError):
            return ''

    def get_text_at_start_point(self, point: tuple):
        for text in self._texts:
            if text.get_start_point() == point:
                return point
        raise TextNotFoundError

    def get_text(self, point: tuple):
        for text in self._texts:
            end_p = text.end_point(self._letter_width, self._letter_height)
            start_p = text.get_start_point()
            if start_p[0] <= point[0] and point[0] <= end_p[0] and start_p[1] <= point[1] and point[1] <= end_p[1]:
                return text
        raise TextNotFoundError

    def get_price_per_day(self, price_per_hour):
        return self.total_points_num() * price_per_hour * 24

    def total_points_num(self):
        return sum([txt.total_points(self._letter_width, self._letter_width)
                    for txt in self._texts])

    def print_texts(self):
        out_str = f'texts:\n'
        for i, text in enumerate(self._texts):
            out_str += f'{i}. {text}\n'
        return out_str

    def generate_raport(self, price_per_hour):
        # powierzchnia
        # cena na dzień
        today = date.today().isoformat()
        board_data_str = '\nserial number: {0._serial_num}, width: {0._width}, height: {0._height},' \
            ' letter width: {0._letter_width}, letter height: {0._letter_height}\nTEXTS:\n'.format(
                self)
        ppd = self.get_price_per_day(price_per_hour)
        ppd_str = f'Cena za dzień wyświetlania: {ppd}\n'
        texts = self.print_texts()
        return today + board_data_str + ppd_str + texts

    def validate_arguments(self, serial_num: int,  width: int, height: int, letter_width: int, letter_height: int):
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


if __name__ == '__main__':
    text1 = LightBoardText("texte", (1, 1))
    text2 = LightBoardText("cos", (1, 2))
    text3 = LightBoardText("inny", (6, 2))
    board = LightBoard(11, 10, 10, 1, 1, [text1, text2, text3])
    print(board.generate_raport(10))
