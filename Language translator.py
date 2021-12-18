from translate import Translator

# https://en.wikipedia.org/wiki/ISO_639-1 for the languages
translator = Translator(to_lang="ja")

try:
    with open('text.txt', mode='r') as my_file:
        # print(my_file.read())
        text1 = my_file.read()
        print(text1)

        translation = translator.translate(text1)
        print(translation)
    with open('hii.txt', 'w') as my_file2:
        my_file2.write(translation)


except FileNotFoundError as e:
    print('check your file path ,dude', e)



