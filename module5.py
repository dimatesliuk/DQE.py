from datetime import datetime, timedelta
import random

class Newsfeed:
    def __init__(self):
        print(f'[Session started] - {datetime.now().strftime("%d/%m/%Y, %H:%M")}')
        self.delimiter = '--------------------'

    def run_feed(self):
        while True:
            self.publication_type = input('Enter publication type (News, Private Ad, Weather) or Exit to close the program: ').lower()
            print(f'Selected type: {self.publication_type.capitalize()}')

            if self.publication_type == 'news':
                post = News()
                self.post_to_feed(post.lines)
            elif self.publication_type == 'private ad':
                post = PrivateAd()
                self.post_to_feed(post.lines)
            elif self.publication_type == 'weather':
                post = Weather()
                self.post_to_feed(post.lines)
            elif self.publication_type == 'exit':
                print(f'[Session ended] - {datetime.now().strftime("%d/%m/%Y, %H:%M")}')
                break
            else:
                print('Wrong input. Repeat.')
                print(self.delimiter)

    def post_to_feed(self, lines):
        self.lines = lines
        print('\n'.join(self.lines))
        print(self.delimiter)
        with open('feed.txt', 'a') as f:
            f.write('\n'.join(self.lines))
            f.write('\n\n')


class News:
    def __init__(self):
        self.header = 'News ---------------'
        self.text = input('Enter the text of the news: \n')
        self.metadata = input('Enter the city: ') + ', ' + datetime.now().strftime("%d/%m/%Y, %H:%M")
        self.lines = [self.header, self.text, self.metadata]

class PrivateAd:
    def __init__(self):
        self.header = 'Private Ad ---------'
        self.text = input('Enter the text of the Ad: \n')
        self.expiry_date = input('Actual until (dd-mm-yyyy): ')
        self.days_left = str((datetime.strptime(self.expiry_date, '%d-%m-%Y') - datetime.now()).days)
        self.metadata = 'Actual until: ' + self.expiry_date + ', ' + self.days_left + ' days left.'
        self.lines = [self.header, self.text, self.metadata]

class Weather:
    def __init__(self):
        self.header = 'Weather ------------'
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




