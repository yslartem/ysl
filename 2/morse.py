morse = dict((
('A', '.-'),
('B', '-...'),
('C', '-.-.'),
('D', '-..'),
('E', '.'),
('F', '..-.'),
('G', '--.'),
('H', '....'),
('I', '..'),
('J', '.---'),
('K', '-.-'),
('L', '.-..'),
('M', '--'),
('N', '-.'),
('O', '---'),
('P', '.--.'),
('Q', '--.-'),
('R', '.-.'),
('S', '...'),
('T', '-'),
('U', '..-'),
('V', '...-'),
('W', '.--'),
('X', '-..-'),
('Y', '-.--'),
('Z', '--..'),
('1', '.----'),
('2', '..---'),
('3', '...--'),
('4', '....-'),
('5', '.....'),
('6', '-....'),
('7', '--...'),
('8', '---..'),
('9', '----.'),
('0', '-----')))

decodemorse = {v: k for k, v in morse.items()}

def text_to_morse(text):
    text = text.upper()
    morse_words = []
    for word in text.split():
        morse_chars = [morse[char] for char in word if char in morse]
        morse_words.append(' '.join(morse_chars))
    return ' / '.join(morse_words)

def morse_to_text(morse_code):
    text_words = []
    for word in morse_code.split(' / '):
        chars = [decodemorse[code] for code in word.split()]
        text_words.append(''.join(chars))
    return ' '.join(text_words)

# Пример использования
message = "PYTHON 3"
morse_code = text_to_morse(message)
print("Шифрование:", morse_code)

decoded_text = morse_to_text(morse_code)
print("Дешифрование:", decoded_text)
