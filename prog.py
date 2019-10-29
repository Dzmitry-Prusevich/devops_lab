import argparse
import task4

parser = argparse.ArgumentParser(description="This program give you info about "
                                             "github pull request to 'name'/'repo'. "
                                             "Without additional arguments show full stat:\n"
                                             "Number of comments created,\n"
                                             "Day of the week opened,\n"
                                             "Hour of the day opened,\n"
                                             "User who opened,\n"
                                             "Attached labels.")
parser.add_argument("-v", "--version", action="store_true", help="print version of program")
parser.add_argument("-nc", "--numcom", action="store_true", help="print number of comments created")
parser.add_argument("-d", "--day", action="store_true", help="day of the week opened")
parser.add_argument("-t", "--time", action="store_true", help="hour of the day opened")
parser.add_argument("-u", "--user", action="store_true", help="user who opened")
parser.add_argument("-l", "--labels", action="store_true", help="attached labels")
parser.add_argument("name", help="name of user - rep author")
parser.add_argument("repo", help="name of repo on github")
args = parser.parse_args()

if args.version:
    print("Current version of program is 1.0")
else:
    user = task4.user_git()
    password = task4.pas_git()
    author, rep = args.name, args.repo
    b, num_comments, day, month, year, ans, time, num_label = task4.make_req(user, password, author, rep)

    if args.numcom:
        task4.num_com(num_comments)
    if args.day:
        task4.weekday(day, month, year, ans)
    if args.time:
        task4.hour(day, month, year, time)
    if args.user:
        task4.user_create(b)
    if args.labels:
        task4.label(b)
    if True not in (args.numcom, args.day, args.time, args.user, args.labels, args.version):
        task4.num_com(num_comments)
        task4.weekday(day, month, year, ans)
        task4.hour(day, month, year, time)
        task4.user_create(b)
        task4.label(b)
