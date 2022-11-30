class LightBoardText:
    def __init__(self, text: str, start_point: tuple):
        if type(start_point) != tuple:
            raise TypeError
        if not text:
            raise ValueError

        self._text = text
        self._start_point = start_point

    def get_text(self):
        return self._text

    def get_start_point(self):
        return self._start_point

    def end_point(self, letter_width, letter_height):
        # returns coordinates of lower right point of the text rectangle
        first_coordinate = self._start_point[0] + \
            len(self._text)*letter_width - 1
        second_coordinate = self._start_point[1] + letter_height - 1
        return (first_coordinate, second_coordinate)

    def __str__(self):
        return f'text: {self._text}, start point: {self._start_point}'
