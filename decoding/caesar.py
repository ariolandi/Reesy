from dependencies.text_transformation_utils\
    import shift_letter_forward, find_possible_shift
from dependencies.text_recognition_utils import is_english_text
from string import ascii_letters as LETTERS
from dependencies.common import *


def text_statistic(text):
    all_letters = len(filter_list((lambda x: x.isalpha()), text))
    return {letter: text.count(letter) / all_letters for letter in LETTERS}


def filter_keys(text):
    frequency_table = text_statistic(text)
    keys_possibility = count_values(flatten(
        [find_possible_shift(letter, frequency_table[letter])
         for letter in LETTERS]))
    avrg_value = sum(keys_possibility.values()) / len(keys_possibility)
    return filter_dict_keys((lambda y: y > avrg_value), keys_possibility)


def transform(x, key):
    return shift_letter_forward(x, key) if x.isalpha() else x


def caesar_with_key(text, key):
    return "".join([transform(x, key) for x in text])


def caesar(text):
    possible_keys = filter_keys(text)
    all_texts = [caesar_with_key(text, key) for key in possible_keys]
    return [text for text in all_texts if is_english_text(text)]


if __name__ == '__main__':
    def test(message, key):
        crypted = caesar_with_key(message, key)
        print(crypted)
        print(filter_keys(crypted))

        decrypted = caesar(crypted)
        print(decrypted)
        print(message.upper() in decrypted)

    message = "We tell the word our secrets in language it doesn't understand."
    crypted = "Zh whoo wkh zrug rxu vhfuhwv lq odqjxdjh lw grhvq'w xqghuvwdqg."
    key = 3

    message2 = "The greater the uncertainty, the bigger the gap between \
what you can measure and what matters, the more you should watch \
out for overfitting - that is, the more you should prefer simplicity"
    crypted2 = "Wkh juhdwhu wkh xqfhuwdlqwb, wkh eljjhu wkh jds ehwzhhq \
zkdw brx fdq phdvxuh dqg zkdw pdwwhuv, wkh pruh brx vkrxog zdwfk \
rxw iru ryhuilwwlqj - wkdw lv, wkh pruh brx vkrxog suhihu vlpsolflwb"
    key2 = 3

    test(message, key)
    test(message2, key2)
