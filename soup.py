from collections import Counter

from bs4 import BeautifulSoup
from urllib.request import urlopen

from favorite_authors import poem

class TextParser:

    def get_file(self):

        my_books = ['/home/posseydon/Desktop/git_tutorial/work/favorite_authors/source_code/0600841.txt',
                    '/home/posseydon/Desktop/git_tutorial/work/favorite_authors/source_code/0600851.txt',
                    '/home/posseydon/Desktop/git_tutorial/work/favorite_authors/source_code/0600861.txt',
                    '/home/posseydon/Desktop/git_tutorial/work/favorite_authors/source_code/0600871.txt']
        self.soup = []
        for book in my_books:
            html_doc = open(book).read()
            parse_book = BeautifulSoup(html_doc)
            self.soup.append(str(parse_book.html.pre))

        return self.soup

    def get_list_of_words(self):

        print(len(self.soup))
        main_text = str(self.soup)
        print(len(main_text))
        list_bad_symbols = [".", ",", "<", ">", '\"', "!", "?", "\\"]
        for symbol in list_bad_symbols:
            if symbol in main_text:
                main_text = main_text.replace(symbol, "")
        text_replaces = main_text.replace("\r", " ").replace("\n", " ").replace("\\r", " ").replace("\\n", " ")
        self.list_of_words = text_replaces.split(" ")
        #print(self.list_of_words)
        return self.list_of_words

    def get_long_words(self):

        self.long_words = []
        for word in self.list_of_words:
            if len(word) >= 5:
                self.long_words.append(word)
        #print(self.long_words)
        return self.long_words

    def count_all_words(self):

        self.most_common_words = {}
        counts = Counter(self.long_words)
        for item, number in counts.items():
            if number > 4:
                self.most_common_words[item] = number
        print(self.most_common_words)
        return self.most_common_words

    def write_result_in_new_file(self):

        with open("/home/posseydon/Desktop/git_tutorial/work/favorite_authors/source_code/results.txt", "w") as _file:

                _file.write(str(self.most_common_words))










def main():
    poem()
    x = TextParser()
    x.get_file()
    x.get_list_of_words()
    x.get_long_words()
    x.count_all_words()
    x.write_result_in_new_file()
if __name__ == '__main__':
    main()
