DATA_PATH = './data'

class Task:
    def __init__(self):
        pass

    def __len__(self) -> int:
        pass

    def get_input(self, idx: int) -> str:
        pass

    def test_output(self, idx: int, output: str):
        pass

    def generate_prompt(self, input_data: str, method: str) -> str:
        if method == 'standard':
            return self.standard_prompt_wrap(input_data)
        elif method == 'cot':
            return self.cot_prompt_wrap(input_data)
        else:
            raise ValueError(f'Unknown method: {method}')

    def evaluate_output(self, input_data: str, output_data: str) -> dict:
        return self.test_output(input_data, output_data)
