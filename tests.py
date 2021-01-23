import io
import unittest
from unittest.mock import patch, call

from planner import ask_user

PROMPT_USER_FOR_TASKS = 'What do you need to do this week? Input tasks separated by a comma then a space. '
SPACER = ''
FORMATED_TASKS_REMAINING = 'You still have {count} more tasks to put in.'

class TestAskUser(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input')
    def test_happy_path(self, mock_input, mock_print):
        """
        Test that single input of 7 items seperated by comma and a space require no additional input from user
        """
        tasks = []
        
        mock_input.side_effect = ['task1, task2, task3, task4, task5, task6, task7']
        response = ask_user(tasks)
        self.assertEqual(len(tasks), 7)
        self.assertIs(tasks, response)
        calls = [call(SPACER), call(PROMPT_USER_FOR_TASKS)]
        mock_print.assert_has_calls(calls)

    @patch('builtins.print')
    @patch('builtins.input')
    def test_single_entry_loops(self, mock_input, mock_print):
        """
        Test that function loops until 7 tasks have been provided
        """
        tasks = []
        example_tasks = ['task1', 'task2', 'task3', 'task4', 'task5', 'task6', 'task7']
        mock_input.side_effect = example_tasks.copy()
        response = ask_user(tasks)
        self.assertEqual(len(tasks), len(example_tasks))
        self.assertIs(tasks, response)
        calls = [call(SPACER)]
        count = 6
        while count > 0:
            calls.append(call(PROMPT_USER_FOR_TASKS))
            calls.append(call(FORMATED_TASKS_REMAINING.format(count=count)))
            calls.append(call(SPACER))
            count = count-1
            
        calls.append(call(PROMPT_USER_FOR_TASKS))
        mock_print.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()