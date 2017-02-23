import csv


with open('me_at_the_zoo.in') as csvfile:
        file = csv.DictReader(csvfile)

        for row in file:
          print row['100 10 100 10 100']