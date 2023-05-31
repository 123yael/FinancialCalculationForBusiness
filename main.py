import fixed_expense as fe, Profit_or_loss_summary as p, expense as e, revenue as r

from colorama import Fore

from datetime import date

import matplotlib.pyplot as plt


class FileMatchingAndYearErorr(Exception):

    def __init__(self, file_name):
        self._file_name = file_name

    def __str__(self):
        return "The %s file path does not match the year and/or request" % self._file_name


def creating_list_from_file(sign, update_year):
    """
    A function that checks that the file is opened
    :param sign: The file type
    :param update_year: A year that updates
    :type sign: str
    :type update_year: str
    :return: A list from a function that checks for matches
    :rtype: list
    """
    file_name = input(Fore.RESET + f"Enter the name of the {sign} file: ")
    try:
        f = open(file_name, "r")
    except:
        print(Fore.LIGHTRED_EX + "The input entered is incorrect")
        return creating_list_from_file(sign, update_year)
    else:
        lines_in_file = f.read().split("\n")
        f.close()
        return is_the_file_correct(sign, update_year, lines_in_file, file_name)


def is_the_file_correct(sign, year_update, lines_file, name_file):
    """
    A function that checks that everything matches in
    terms of name and year, and if so creates a list
    The parameters [sign, update_year] behave like creating_list_from_file
    :param lines_file: List of file contents by lines
    :param name_file: The received file path
    :type lines_file: list
    :type name_file: str
    :return: A list in which each member is a list of arguments
    to be passed to the appropriate class
    :rtype: list
    """
    try:
        if not (sign in lines_file[0] and year_update in lines_file[0]):
            raise FileMatchingAndYearErorr(name_file)
    except FileMatchingAndYearErorr as E:
        print(Fore.LIGHTRED_EX + type(E).__name__ + ":", E)
        return creating_list_from_file(sign, year_update)
    else:
        lines_of_data = lines_file[3:]
        return [[j.strip() for j in i.split("|")] for i in lines_of_data]


def a_monthly_dictionary(list_for_dic, firs_sum=0):
    """
    Creating a months dictionary with sum values
    :param list_for_dic: A list of class instances
    :param firs_sum: Optional, an initial sum for the values
    :type list_for_dic: list
    :type firs_sum: int
    :return: Dictionary: key - month name, value - amount
    :rtype: dictionary
    """
    dic = {date(2022, i, 1).strftime('%B'): firs_sum for i in range(1, 13)}
    for i in list_for_dic:
        dic[i.get_date().strftime('%B')] += i.get_sum()
    return dic


def main():
    update_year = input("Which year do you want to update? ")
    while not update_year.isdigit() or len(update_year) != 4:
        update_year = input("The input is incorrect, type a 4-digit year again: ")

    list_file = creating_list_from_file("fixedExpenses", update_year)
    fixed_expenses = [fe.Fixed_expense(i[0], int(i[1]), i[2]) for i in list_file]

    list_file = creating_list_from_file("expenses", update_year)
    expenses = [e.Expense(i[0], i[1], int(i[2]), i[3]) for i in list_file]

    list_file = creating_list_from_file("revenues", update_year)
    revenues = [r.Revenue(i[0], int(i[1]), i[2], i[3], int(i[4])) for i in list_file]

    revenues_by_months = a_monthly_dictionary(revenues)
    sum_of_fixed_expenses = sum(map(lambda x: x.get_sum(), fixed_expenses))
    expenses_by_months = a_monthly_dictionary(expenses, sum_of_fixed_expenses)

    summary_by_years = [p.Profit_or_loss_summary(revenues_by_months, expenses_by_months, update_year)]

    is_add_type = input("To add income or expense, type: R or E respectively, otherwise enter: ")
    while is_add_type == "E" or is_add_type == "R" or is_add_type == "e" or is_add_type == "r":
        if is_add_type.upper() == 'E':
            e_date = input("Enter the date of the expense in the format: dd/mm/yyyy: ")
            reason = input("Enter a expense reason: ")
            sum_e = int(input("Enter the amount of expense: "))
            payment_method = input("Enter payment method: ")
            expenses.append(e.Expense(e_date, reason, sum_e, payment_method))
            summary_by_years[0].set_expenses_by_months(e_date.split("/"), sum_e)
        else:
            r_date = input("Enter the date of income in the format: dd/mm/yyyy: ")
            client = input("Enter customer name: ")
            reason = input("Enter the reason for the income: ")
            sum_R = int(input("Enter an income amount: "))
            revenues.append(r.Revenue(r_date, revenues[-1].get_num_R() + 1, client, reason, sum_R))
            summary_by_years[0].set_revenues_by_months(r_date.split("/"), sum_R)
        is_add_type = input("To add income or expense, type: R or E respectively, otherwise enter: ")

    show_year = input("Data for which year you want to see? ")

    while show_year != "":
        year_summary = 0
        for i in summary_by_years:
            if i.get_year() == show_year:
                year_summary = i

        if year_summary:
            data1 = year_summary.get_revenues_by_months()
            data2 = year_summary.get_expenses_by_months()
            group_data1 = list(data1.values())
            group_names = list(data1.keys())
            group_data2 = list(data2.values())
            fig, ax = plt.subplots(figsize=(12, 5))
            ax.bar(group_names, group_data1, 0.35, label='Revenues', align='edge')
            ax.bar(group_names, group_data2, -0.35, label='Expenses', align='edge')
            ax.set_title('Total profit for the year {} is: ₪{}'.format(show_year, year_summary.get_sum()))
            ax.legend()
            fig.tight_layout()
            plt.show()
        else:
            print("The input entered is invalid, ", end="")
        show_year = input("to display another year, type year again: ")

    print("Thank you for using our system, best of luck in the future!")


if __name__ == "__main__":
    main()
