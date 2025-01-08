# This file defines generic prompts for the GenericTask class

standard_prompt = '''
Please provide a response to the following prompt:
{input}
'''

cot_prompt = '''
Please provide a response to the following prompt:
{input}

First, make a plan, then write your response. Your output should be of the following format:

Plan:
Your plan here.

Response:
Your response here.
'''
