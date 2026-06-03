class Letter:
    def __init__(self, char):
        self.char = char


class Word:
    def __init__(self, text):
        self.text = text


class Sentence:
    def __init__(self, words):
        self.words = words


class Text:
    def __init__(self, sentences):
        self.sentences = sentences


try:
    text_input = input("Введіть текст: ")

    if not text_input.strip():
        raise ValueError("Текст не може бути порожнім")

    words = []

    for word in text_input.split():
        words.append(Word(word))

    sentence = Sentence(words)
    text = Text([sentence])

    result = []

    for word in text.sentences[0].words:
        first_letter = word.text[0]
        new_word = first_letter

        for char in word.text[1:]:
            if char.lower() != first_letter.lower():
                new_word += char

        result.append(new_word)

    print("\nРезультат:")
    print(" ".join(result))

except ValueError as e:
    print("Помилка:", e)

except Exception as e:
    print("Непередбачена помилка:", e)
