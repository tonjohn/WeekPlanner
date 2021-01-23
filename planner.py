import random

TASK_COUNT_MINIMUM = 7 # at least 1 task per day of week

def ask_user(tasks):

    print('')

    while len(tasks) < TASK_COUNT_MINIMUM:
        print('What do you need to do this week? Input tasks separated by a comma then a space. ')
        answers = input('Enter: ').split(', ')
        tasks += answers
        task_count = len(tasks)
        if task_count < TASK_COUNT_MINIMUM:
            answers_left = TASK_COUNT_MINIMUM - task_count
            print('You still have {answers_left} more tasks to put in.'.format(answers_left=answers_left))
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