PREFIX = """Solve following algorithmic question from leetcode using Python interpreter, running your solution in the intepreter and using interpreter results to improve your code and validate solution, then submit result back to leetcode, validating the solution, get output from leetcode if solution is not correct and correct it. You have access to the following tools:"""


FORMAT_INSTRUCTIONS = """Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Action: I will use leetcode and submit my answer"""

SUFFIX = """Begin!

Question: {input} 
Thought:{agent_scratchpad}"""