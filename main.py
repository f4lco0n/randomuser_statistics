import argparse
from data_calculation import DataCalculation

parser = argparse.ArgumentParser()

parser.add_argument("--percentage","-p",help="Show percentage for female and male", action="store_true")
parser.add_argument("--average","-a",help="Show average age",type=str)
parser.add_argument("--city","-c",help="Show average age",type=int)
parser.add_argument("--best","-b",help="Show all passwords with the highest points", action="store_true")
parser.add_argument("--password","-pass",help="Show the most popular passwords",type=int)
parser.add_argument(
    "--date",
    "-d",
    nargs=2,
    metavar=('start_date', 'end_date'),
    help="Show users between start and end dates",
    )

args = parser.parse_args()

dl = DataCalculation()

if args.percentage:
    dl.show_percentage()
elif args.average:
    dl.show_average(args.average)
elif args.city:
    dl.most_popular_city(args.city)
elif args.best:
    dl.check_password_security()
elif args.password:
    dl.most_popular_passwords(args.password)
elif args.date:
    dl.show_users_between_date(args.date)