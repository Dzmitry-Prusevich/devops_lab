import getpass
import requests
import datetime


# user = input('Enter user for login to github: ')
def pas_git():
    password = getpass.getpass('Insert your password to github: ')
    return password


def user_git():
    user = input('Enter user for login to github: ')
    return user


# number = input('Enter number of pull request to github: ')
# author = input('Enter name of github rep holder: ')
# rep = input('Enter name of github rep: ')
# user = input('Enter user for login to github: ')
# insert number of pull request, author rep, rep name
# use this 5 fields if you want to correct program use without interactive passing user,name,..
user = ""
author = ''
rep = ''
# Enter user for github
# password = 'enter pass'


def pul_info():
    author = input('Enter name of github rep holder: ')
    rep = input('Enter name of github rep: ')
    return author, rep


def make_req(user, password, author, rep):
    r = requests.get('https://api.github.com/repos/' + author + '/' + rep + '/pulls', auth=(user, password))
    num = r.json()[0]['number']
    number = num + 1
    while number > num:
        try:
            number = int(input("Input number of pull request you are interested in, less then {0}: ".format(num)))
        except ValueError:
            print("It's not valid format. Input integer value!")
    # get info about pull request we are interested in
    b = requests.get('https://api.github.com/repos/' + author + '/' + rep + '/pulls/' + str(number),
                     auth=(user, password))
    # print number of comments
    num_comments = b.json()['comments'] + b.json()['review_comments']
    # print day of the week opened
    dt = b.json()['created_at']
    year, month, day = (x for x in dt.split('-'))
    day, time = day.split('T')
    day, month, year = map(int, (day, month, year))
    ans = datetime.date(year, month, day)
    time = time.split(':', 1)[0]
    num_label = len(b.json()['labels'])
    return b, num_comments, day, month, year, ans, time, num_label


def num_com(num_comments):
    print("Number of comments created = {0}".format(num_comments))


def weekday(day, month, year, ans):
    print('Opened in {0} {1} {2}, it was - {3}'.format(day, month, year, ans.strftime("%A")))


def hour(day, month, year, time):
    print('Opened in {0} {1} {2}, at {3} hour'.format(day, month, year, time))


def user_create(b):
    print("This request was opened by {0}".format(b.json()['user']['login']))


def label(b):
    num_label = len(b.json()['labels'])
    if not num_label:
        print("There is no labels in this pull request")
    else:
        print("This pull request has next labels:")
    for i in range(num_label):
        print(b.json()['labels'][i]['name'], "\n")


if __name__ == "__main__":
    user = user_git()
    password = pas_git()
    author, rep = pul_info()
    b, num_comments, day, month, year, ans, time, num_label = make_req(user, password, author, rep)
    num_com(num_comments)
    weekday(day, month, year, ans)
    hour(day, month, year, time)
    user_create(b)
    label(b)
