
import csv

l = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic",
                                                        "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open("movies.csv", "w") as f:
    write = csv.writer(f, delimiter=",")
    for a in l:
        write.writerow(a)
