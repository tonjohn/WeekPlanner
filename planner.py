import random

TASK_COUNT_MINIMUM = 7 # at least 1 task per day of week

def ask_user(tasks):
    """
    Prompt the user and collect list of tasks from user input

    NOTE: the list of tasks is modified in-place as lists are passed by reference, not value.
    """

    print('')

    # Loop until the user has provided at least the minimum number of tasks
    while len(tasks) < TASK_COUNT_MINIMUM:
        print('What do you need to do this week? Input tasks separated by a comma then a space. ')
        
        # get user's input and convert to list of strings
        answers = input('Enter: ').split(', ')

        # merge user's answers into task list
        tasks += answers

        # create intermediate variables to make code more semantic
        # this also can help in debugging as it allows you inspect changes step-by-step
        task_count = len(tasks)
        answers_left = TASK_COUNT_MINIMUM - task_count

        # if user hasn't provided enough tasks, let them know how many they have remaining
        if answers_left > 0:
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