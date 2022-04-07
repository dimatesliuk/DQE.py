from datetime import datetime, timedelta
import random
import sentence_normalizer
import statistics
import json

class Newsfeed:
    def __init__(self):
        global delimiter
        delimiter = '--------------------'

    def run_feed(self):
        while True:
            self.source_selector = input('Enter "K" to use keyboard as a input method or "F" to load data from file. \nEnter "Exit" to close the program. ')

            if self.source_selector.lower() == 'f':
                print("Warning! \nSupported formats: CSV, JSON, XML. \nPlease follow the same sequence as for manual input.")
                filepath = input("Please enter the filepath or Exit to close the app: ")
                if filepath.lower() == 'exit':
                    statistics.exectute_stat()
                    break
                else: 
                    reader = FileReader(filepath)
                    parser = reader.parser_definer()
                    total_lines = parser.parser()
                    for lines in total_lines:
                        self.post_to_feed(lines)
            elif self.source_selector.lower() =='k':
                while True:
                    self.publication_type = input('Enter publication type (News, Private Ad, Weather) or Exit to close the program: ').title()
                    print(len(self.publication_type))
                    if self.publication_type.lower() == 'exit':
                        break
                    else:
                        reader = InputReader(self.publication_type)
                        lines = reader.type_definer()
                        self.post_to_feed(lines)
            elif self.source_selector.lower() == 'exit':
                statistics.exectute_stat()
                break
            else:
                statistics.exectute_stat()
                break

    def post_to_feed(self, lines):
        self.lines = lines
        print('\n'.join(self.lines))
        print(delimiter)
        with open('feed.txt', 'a') as f:
            f.write('\n'.join(self.lines))
            f.write('\n\n')


#-------------------------------------------------------------------------READING CLASESS----------------------------------------------------------------------#

class FileReader():
    def __init__(self, filepath):
        self.filepath = filepath
        self.format = self.filepath.split(".")[-1]
        # statistics.exectute_stat()

    def parser_definer(self):
        if self.format.lower() == 'csv':
            print("Reading CSV file")
            return CsvParser(self.filepath)         
        elif self.format.lower() == 'json':
            print("Reading JSON file")
            return JsonParser(self.filepath)
        elif self.format.lower() == 'xml':
            print("Reading XML file")
            return XmlParser(self.filepath)
        elif self.format.lower() == 'exit':
            print('Closing app')
        else:
            print("Uknown file format")

class CsvParser(FileReader):
    def __init__(self, filepath):
        super().__init__(filepath)

    def parser(self):
        self.lines_total = []
        with open(self.filepath) as file:
            for row in file:
                row = row.split(',')
                publication_type = row[0]
                pre_lines = row
                pre_lines[-1] = pre_lines[-1].replace("\n","")
                if publication_type == 'News':
                    post = News(pre_lines)
                    self.lines_total.append(post.lines)
                elif publication_type == 'Private Ad':
                    post = PrivateAd(pre_lines)
                    self.lines_total.append(post.lines)
                elif publication_type == 'Weather':
                    post = Weather(pre_lines)
                    self.lines_total.append(post.lines)
        return self.lines_total

class JsonParser(FileReader):
    def __init__(self, filepath):
        super().__init__(filepath)
        print('JSON ********************')

    def parser(self):
        self.total_lines = []
        with open(self.filepath, "r") as file:
            json_object = json.load(file)

        for publication_type in json_object:
            if publication_type == 'news':
                header = publication_type.title()
                text = json_object[publication_type]['text']
                city = json_object[publication_type]['city']
                pre_lines = [header, text, city]
                post = News(pre_lines)
                self.total_lines.append(post.lines)
            elif publication_type == 'private ad':
                header = publication_type.title()
                text = json_object[publication_type]['text']
                expiry_date = json_object[publication_type]['expiry_date']
                pre_lines = [header, text, expiry_date]
                post = PrivateAd(pre_lines)
                self.total_lines.append(post.lines)
            elif publication_type == 'weather':
                header = publication_type.title()
                text = json_object[publication_type]['text']
                pre_lines = [header, text]
                post = Weather(pre_lines)
                self.total_lines.append(post.lines) 
            else:
                print(f"Unknown type - {publication_type}")
        return self.total_lines

class XmlParser(FileReader):
    def __init__(self):
        print('XML ********************')

class InputReader():
    def __init__(self, publication_type):
        self.publication_type = publication_type
        print(f'Selected type: {self.publication_type}')

    def type_definer(self):
        if self.publication_type == 'News':
            pre_lines = self.news_reader()
            post = News(pre_lines)
            return (post.lines)
        elif self.publication_type == 'Private Ad':
            pre_lines = self.ad_reader()
            post = PrivateAd(pre_lines)
            return (post.lines)
        elif self.publication_type == 'Weather':
            pre_lines = self.weather_reader()
            post = Weather(pre_lines)
            return (post.lines)

    def news_reader(self):
        text = input("Enter the text of a news: ")
        city = input("Enter the city: ")
        pre_lines = [self.publication_type, text, city]
        return pre_lines

    def ad_reader(self):
        text = input("Please enter the text of your ad: ")
        expity_date = input('Actual until (dd-mm-yyyy): ')
        pre_lines = [self.publication_type, text, expity_date]
        return pre_lines
    
    def weather_reader(self):
        text = input('Enter number of days 1 - 7: ')
        pre_lines = [self.publication_type, text]
        return pre_lines


#---------------------------------------------------------------PUBLICATION CLASESS-----------------------------------------------------------------------#
class Publication:
    def __init__(self, pre_lines):
        self.pre_lines = pre_lines

class News(Publication):
    def __init__(self, pre_lines):
        super().__init__(pre_lines)
        self.header = pre_lines[0] + ' ' + delimiter
        self.text = sentence_normalizer.string_cleaner(pre_lines[1])
        self.metadata = pre_lines[2] + ', ' + datetime.now().strftime("%d/%m/%Y, %H:%M")
        self.lines = [self.header, self.text, self.metadata]

class PrivateAd(Publication):
    def __init__(self, pre_lines):
        super().__init__(pre_lines)
        self.header = pre_lines[0] + ' ' + delimiter
        self.text = sentence_normalizer.string_cleaner(pre_lines[1])
        self.expiry_date = pre_lines[2]
        self.days_left = str((datetime.strptime(self.expiry_date, '%d-%m-%Y') - datetime.now()).days)
        self.metadata = 'Actual until: ' + self.expiry_date + ', ' + self.days_left + ' days left.'
        self.lines = [self.header, self.text, self.metadata]

class Weather(Publication):
    def __init__(self, pre_lines):
        super().__init__(pre_lines)
        self.header = pre_lines[0] + ' ' + delimiter
        self.text = 'The weather for next ' + pre_lines[1] + ' days for forecast:'
        self.n_days = int(self.text[-20])
        self.current_date = datetime.now()
        self.metadata = []
        for i in range(0, self.n_days):
            self.current_date += timedelta(days=i)
            temp = random.randint(0, 40)
            self.metadata.append(f'{self.current_date.strftime("%A %d/%m/%Y")} - {temp}C')
        self.lines = [self.header, self.text] + self.metadata


if __name__ == '__main__':
    p = Newsfeed()
    f = p.run_feed()