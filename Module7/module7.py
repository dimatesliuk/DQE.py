from datetime import datetime, timedelta
import random
import sentence_normalizer
import statistics

delimiter = '--------------------'

class Newsfeed:
    def __init__(self):
        print(f'[Session started] - {datetime.now().strftime("%d/%m/%Y, %H:%M")}')
        global delimiter
        delimiter = '--------------------'

    def run_feed(self):
        self.source_selector = input('Enter "K" to use keyboard as a input method or "F" to load data from file: ')
        if self.source_selector.lower() == 'f':
            file = FileReader()
        elif self.source_selector.lower() =='k':
            while True:
                self.publication_type = input('Enter publication type (News, Private Ad, Weather) or Exit to close the program: ').title()
                print(f'Selected type: {self.publication_type}')
                
                if self.publication_type == 'News':
                    post = News(self.publication_type)
                    self.post_to_feed(post.lines)
                elif self.publication_type == 'Private Ad':
                    post = PrivateAd(self.publication_type)
                    self.post_to_feed(post.lines)
                elif self.publication_type == 'Weather':
                    post = Weather(self.publication_type)
                    self.post_to_feed(post.lines)
                elif self.publication_type == 'Exit':
                    print(f'[Session ended] - {datetime.now().strftime("%d/%m/%Y, %H:%M")}')
                    statistics.exectute_stat()
                    break
                else:
                    print('Wrong input. Repeat.')
                    print(delimiter)

    def post_to_feed(self, lines):
        self.lines = lines
        print('\n'.join(self.lines))
        print(delimiter)
        with open('feed.txt', 'a') as f:
            f.write('\n'.join(self.lines))
            f.write('\n\n')

class FileReader(Newsfeed):
    def __init__(self):
        print('Warning!\nUsed file type is CSV.\nPlease follow the same sequence of data entry as for keyboard input.\nEach publication type should be separate record in file')
        self.filepath = input('Please enter filepath: ')

        with open(self.filepath) as file:
            for row in file:
                row = row.split(',')
                self.publication_type = row[0]
                self.lines = row

                self.lines[1] = sentence_normalizer.string_cleaner(self.lines[1])

                if self.publication_type == 'News':
                    self.lines[0] = self.lines[0] + ' ' + delimiter
                    self.lines[2] = self.lines[2].replace('\n','')
                    self.lines[-1] = self.lines[2] + ', ' + datetime.now().strftime("%d/%m/%Y, %H:%M")
                    self.post_to_feed(self.lines)
                elif self.publication_type == 'Private Ad':
                    self.lines[0] = self.lines[0] + ' ' + delimiter
                    self.expiry_date = self.lines[-1].replace('\n', '')
                    self.days_left = str((datetime.strptime(self.expiry_date, '%d-%m-%Y') - datetime.now()).days)
                    self.lines[-1] = 'Actual until: ' + self.expiry_date + ', ' + self.days_left + ' days left.'
                    self.post_to_feed(self.lines)
                elif self.publication_type == 'Weather':
                    self.lines = self.lines[0:2]
                    self.lines[0] = self.lines[0] + ' ' + delimiter
                    self.n_days = int(self.lines[1])
                    self.lines[1] = f'The weather for next {self.lines[1]}  days for forecast:'
                    self.current_date = datetime.now()
                    self.metadata = []
                    for i in range(0, self.n_days):
                        self.current_date += timedelta(days=i)
                        temp = random.randint(0, 40)
                        self.metadata.append(f'{self.current_date.strftime("%A %d/%m/%Y")} - {temp}C')
                    self.lines = self.lines + self.metadata
                    self.post_to_feed(self.lines)

        statistics.exectute_stat()

class Publication:
    def __init__(self, header):
        self.header = header + ' ' + delimiter
        self.text = input(f'Enter the text of the {header}: ')

class News(Publication):
    def __init__(self, header):
        super().__init__(header)
        self.metadata = input('Enter the city: ') + ', ' + datetime.now().strftime("%d/%m/%Y, %H:%M")
        self.lines = [self.header, self.text, self.metadata]


class PrivateAd(Publication):
    def __init__(self, header):
        super().__init__(header)
        self.expiry_date = input('Actual until (dd-mm-yyyy): ')
        self.days_left = str((datetime.strptime(self.expiry_date, '%d-%m-%Y') - datetime.now()).days)
        self.metadata = 'Actual until: ' + self.expiry_date + ', ' + self.days_left + ' days left.'
        self.lines = [self.header, self.text, self.metadata]


class Weather(Publication):
    def __init__(self, header):
        self.header = header + ' ' + delimiter
        self.text = 'The weather for next ' + input('Enter number of days 1 - 7: ') + ' days for forecast:'
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