import unittest
from tasks.generic import GenericTask

class TestGenericTask(unittest.TestCase):

    def setUp(self):
        self.task = GenericTask('prompts/generic_prompt.py')

    def test_generate_prompt_standard(self):
        input_data = "This is a test prompt."
        expected_output = "Standard prompt: This is a test prompt.\n"
        self.assertEqual(self.task.generate_prompt(input_data, 'standard'), expected_output)

    def test_generate_prompt_cot(self):
        input_data = "This is a test prompt."
        expected_output = "CoT prompt: This is a test prompt.\n"
        self.assertEqual(self.task.generate_prompt(input_data, 'cot'), expected_output)

    def test_evaluate_output(self):
        input_data = "This is a test prompt."
        output_data = "This is a test response."
        expected_output = {'r': 1}
        self.assertEqual(self.task.evaluate_output(input_data, output_data), expected_output)

    def test_generate_prompt_standard_multiple(self):
        input_data = "This is another test prompt."
        expected_output = "Standard prompt: This is another test prompt.\n"
        self.assertEqual(self.task.generate_prompt(input_data, 'standard'), expected_output)

    def test_generate_prompt_cot_multiple(self):
        input_data = "This is another test prompt."
        expected_output = "CoT prompt: This is another test prompt.\n"
        self.assertEqual(self.task.generate_prompt(input_data, 'cot'), expected_output)

    def test_evaluate_output_multiple(self):
        input_data = "This is another test prompt."
        output_data = "This is another test response."
        expected_output = {'r': 1}
        self.assertEqual(self.task.evaluate_output(input_data, output_data), expected_output)

    def test_generate_prompt_edge_case(self):
        input_data = ""
        expected_output = "Standard prompt: \n"
        self.assertEqual(self.task.generate_prompt(input_data, 'standard'), expected_output)

    def test_evaluate_output_edge_case(self):
        input_data = ""
        output_data = ""
        expected_output = {'r': 1}
        self.assertEqual(self.task.evaluate_output(input_data, output_data), expected_output)

if __name__ == '__main__':
    unittest.main()
