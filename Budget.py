"""
Author tony.gold
Date 21/06/2019

"""

import csv
import os


def add_transaction(transaction):
    duplicate_tran = False
    if os.path.exists("Y2D2019.csv"):
        with open("Y2D2019.csv", 'r', newline='') as y2dfile:
            y2d_reader = csv.reader(y2dfile, delimiter=',')
            for tran in y2d_reader:
                if tran[0] == transaction[0] and tran[1] == transaction[1] and tran[5] == transaction[5]:
                    print("You've already loaded this transaction \t" + tran[0], tran[1], tran[5] +
                          "\nYou're trying to load this transaction \t" + transaction[0], transaction[1], transaction[5] +
                          "\nDo you want to keep it?")
                    duplicate_tran = not input()

    if not duplicate_tran:
        with open("Y2D2019.csv", 'a+', newline='') as y2dfile:
            y2d_writer = csv.writer(y2dfile)
            y2d_writer.writerow(transaction)


def add_category(transaction_description):
    if os.path.exists("categories.csv"):
        with open("categories.csv", 'r', newline='') as categories_file:
            categories = csv.DictReader(categories_file)
            print(categories[transaction_description])
            return categories[transaction_description]

    print("could not find a category for " + transaction_description)

    with open("categories.csv", 'a+', newline='') as categories_file:
        fieldnames = ['description', 'category']
        category = input(transaction_description)
        cat_writer = csv.DictWriter(categories_file, fieldnames=fieldnames)
        cat_writer.writerow()




def read_new_transactions():
    with open("TransactionHistory.csv", 'r') as transactions:
        for transaction in reversed(list(csv.reader(transactions))):
            transaction[3] = add_category(transaction[5])
            add_transaction(transaction)



if __name__ == "__main__":
    read_new_transactions()