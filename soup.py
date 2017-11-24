from collections import Counter

from bs4 import BeautifulSoup
from urllib.request import urlopen
#we take a function from another file favorite_authors.py, downloading your favorite books

from favorite_authors import poem

#we take new class for our script
class TextParser:

    #parser from html in text our favorite books
    def get_file(self):
        html_doc = open('/home/posseydon/Desktop/git_tutorial/work/favorite_authors/source_code/0600851.txt').read()
        self.soup = BeautifulSoup(html_doc)
        return self.soup

    #we clean up our text from some bad symbols
    def get_list_of_words(self):

        main_text = str(self.soup.html.pre)
        list_bad_symbols = [".", ",", "<", ">", '\"', "!", "?", "\\"]
        for symbol in list_bad_symbols:
            if symbol in main_text:
                main_text = main_text.replace(symbol, "")
        text_replaces = main_text.replace("\r", " ").replace("\n", " ").replace("\\r", " ").replace("\\n", " ")
        self.list_of_words = text_replaces.split(" ")
        #print(self.list_of_words)
        return self.list_of_words

    #Find all words that have 5 letters or more
    def get_long_words(self):

        self.long_words = []
        for word in self.list_of_words:
            if len(word) >= 5:
                self.long_words.append(word)
        #print(self.long_words)
        return self.long_words

    #count how often these words are found in the texts
    def count_all_words(self):

        self.most_common_words = {}
        counts = Counter(self.long_words)
        for item, number in counts.items():
            if number > 4:
                self.most_common_words[item] = number
        #print(self.most_common_words)
        return self.most_common_words

    #write the results in new file 
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
