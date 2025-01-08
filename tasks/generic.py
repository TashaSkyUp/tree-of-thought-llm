from tasks.base import Task

class GenericTask(Task):
    def __init__(self, file):
        super().__init__()
        self.data = open(file).readlines()
        self.steps = 1
        self.stops = [None]

    def __len__(self) -> int:
        return len(self.data)
    
    def get_input(self, idx: int) -> str:
        return self.data[idx]
    
    def test_output(self, idx: int, output: str):
        return {'r': 1}  # Placeholder for actual evaluation logic
    
    @staticmethod
    def standard_prompt_wrap(x: str, y:str='') -> str:
        return f"Standard prompt: {x}\n{y}"

    @staticmethod
    def cot_prompt_wrap(x: str, y:str='') -> str:
        return f"CoT prompt: {x}\n{y}"
    
    def generate_prompt(self, input_data: str, method: str) -> str:
        if method == 'standard':
            return self.standard_prompt_wrap(input_data)
        elif method == 'cot':
            return self.cot_prompt_wrap(input_data)
        else:
            raise ValueError(f'Unknown method: {method}')

    def evaluate_output(self, input_data: str, output_data: str) -> dict:
        return self.test_output(input_data, output_data)
