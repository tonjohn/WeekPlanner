import random

def ask_user(tasks):

    print('')
    answers_left = 7
    while len(tasks) < 7:
        print('What do you need to do this week? Input tasks separated by a comma then a space. ')
        answers = input('Enter: ').split(', ')
        tasks += answers
        answer_count = len(answers)
        if len(tasks) < 7:
            answers_left -= answer_count
            print('You still have ' + str(answers_left) + ' more tasks to put in.')
            print('')

    return tasks

def combine_lists(weekdays, tasks):

    def task_list():
        for i in range(7):
            print(weekdays[i] + ': ' + task_copy[i])

    task_copy = tasks.copy()
    random.shuffle(task_copy)
    reroll = True

    print('')
    print('Here\'s your task assignment for the week:')
    print('')

    task_list()

    while reroll == True:
        print('')
        print('Do you want to re-roll the results?')
        reroll_ask = input('Enter (Y) or (N): ').upper()
        if reroll_ask == ('Y'):
            print('')
            random.shuffle(task_copy)
            task_list()
        elif reroll_ask == ('N'):
            break
        else:
            print('Input invalid. Please try again.')