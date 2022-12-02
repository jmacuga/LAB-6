from light_board_text import LightBoardText
from light_board import LightBoard, TextNotFoundError, TextError
import pytest


def test_light_text_type_error():
    text = "jakis tekst"
    start_point = [2, 3]
    with pytest.raises(TypeError):
        LightBoardText(text, start_point)


def test_light_text_empty_string():
    with pytest.raises(ValueError):
        LightBoardText("", (0, 0))


def test_light_board_incorrect_width1():
    with pytest.raises(ValueError):
        LightBoard(11, -1, 2, 1, 1)


def test_light_board_incorrect_width2():
    with pytest.raises(TypeError):
        LightBoard(11, 1.3, 2, 1, 1)


def test_light_board_incorrect_height():
    with pytest.raises(ValueError):
        LightBoard(11, 1, 0, 1, 1)


def test_light_board_incorrect_letter_width():
    with pytest.raises(ValueError):
        LightBoard(11, 1, 1, -7, 1)


def test_light_board_incorrect_letter_width():
    with pytest.raises(TypeError):
        LightBoard(11, 1, 1, 7.4, 1)


def test_light_board_incorrect_letter_height():
    with pytest.raises(ValueError):
        LightBoard(11, 1, 1, 7, -5)


def test_get_end_point():
    letter_width = 3
    letter_height = 4
    text = LightBoardText("text", (1, 1))
    assert text.end_point(letter_width, letter_height) == (12, 4)


def test_check_overlap1():
    text1 = LightBoardText("Test", (1, 1))
    text2 = LightBoardText("Inny", (1, 1))
    with pytest.raises(TextError):
        LightBoard(11, 10, 10, 2, 2, [text1, text2])


def test_check_overlap2():
    text1 = LightBoardText("ab", (2, 1))
    text2 = LightBoardText("cd", (5, 2))
    with pytest.raises(TextError):
        LightBoard(11, 10, 10, 3, 2, [text1, text2])


def test_check_overlap3():
    text1 = LightBoardText("text", (1, 2))
    text2 = LightBoardText("co tam", (5, 4))
    LightBoard(11, 10, 10, 1, 4, [text1, text2])


def test_check_overlap4():
    text1 = LightBoardText("texte", (1, 1))
    text2 = LightBoardText("cos", (1, 2))
    text3 = LightBoardText("inny", (6, 2))
    LightBoard(11, 10, 10, 1, 1, [text1, text2, text3])


def test_check_overlap5():
    text1 = LightBoardText("texte", (1, 1))
    text2 = LightBoardText("cos", (1, 2))
    text3 = LightBoardText("inny", (5, 1))
    with pytest.raises(TextError):
        LightBoard(11, 10, 10, 1, 1, [text1, text2, text3])


def test_check_check_fit():
    text1 = LightBoardText("texte ale dlugi text chyba nie pasuje", (1, 1))
    with pytest.raises(TextError):
        LightBoard(11, 10, 10, 1, 1, [text1])


def test_add_text():
    text1 = LightBoardText("texte", (1, 1))
    text2 = LightBoardText("cos", (1, 2))
    text3 = LightBoardText("inny", (6, 2))
    new_text = LightBoardText("nowy", (1, 1))
    board = LightBoard(11, 10, 10, 1, 1, [text1, text2, text3])
    with pytest.raises(TextError):
        board.add_text(new_text)


def test_add_text2():
    text1 = LightBoardText("texte", (1, 1))
    text2 = LightBoardText("cos", (1, 2))
    text3 = LightBoardText("inny", (6, 2))
    new_text = LightBoardText("nowy", (5, 6))
    board = LightBoard(11, 10, 10, 1, 1, [text1, text2, text3])
    board.add_text(new_text)


def test_remove_text():
    text1 = LightBoardText("texte", (1, 1))
    text2 = LightBoardText("cos", (1, 2))
    text3 = LightBoardText("inny", (6, 2))
    board = LightBoard(11, 10, 10, 1, 1, [text1, text2, text3])
    board.remove_text((2, 1))
    assert len(board.get_texts()) == 3
    assert board.get_texts()[0].get_text() == "texte"
    assert board.get_texts()[1].get_text() == "cos"


def test_get_text_at_start_point():
    pass


def test_remove_text_outpt_text():
    pass


def test_remove_text_point_outside_the_board():
    pass


def test_remove_text_text_not_found():
    pass
