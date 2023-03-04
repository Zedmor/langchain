"""
This tool is able to submit buffer to the leetcode and get the result to the agent
"""
import sys
from io import StringIO
from pydantic import BaseModel, Field
from typing import Dict, Optional

from langchain.tools import BaseTool

LEETCODE_DIRECTORY = "~/tmp/leetcode"


class LeetcodeSubmitter(BaseModel):

    globals: Optional[Dict] = Field(default_factory=dict, alias="_globals")
    locals: Optional[Dict] = Field(default_factory=dict, alias="_locals")

    def combine_code_and_template(self, problem, code):
        """
        Combine the code and template
        :return: the combined code
        """
        with open(f"{LEETCODE_DIRECTORY}/{problem}", "r") as f:
            template = f.read()
        output_filename = f"{LEETCODE_DIRECTORY}/{problem}_submit.py"
        with open(output_filename, "w") as f:
            f.write(f"{template}\n{code}")
        return output_filename

    def run(self, problem: str, code: str) -> str:
        """
        Submit the code to leetcode and return the result
        :param code: the code to submit
        :param problem: the problem id
        :return: the result of the code
        """
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        try:
            filename = self.combine_code_and_template(problem, code)
            command = f"lcc submit {filename}"
            exec(command, self.globals, self.locals)
            sys.stdout = old_stdout
            output = mystdout.getvalue()
        except Exception as e:
            sys.stdout = old_stdout
            output = str(e)
        return output


def _get_default_leetcode_submitter() -> LeetcodeSubmitter:
    return LeetcodeSubmitter(_globals=globals(), _locals=None)


class LeetcodeSubmitTool(BaseTool):
    """A tool for running python code in a REPL."""

    name = "Leetcode Submitter"
    description = (
        "This tool submits the code to leetcode and "
        "returns the result to the agent"
    )
    submitter: LeetcodeSubmitter = Field(default_factory=_get_default_leetcode_submitter)

    def __init__(self, problem_file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.problem_file = problem_file
        self.submitter = LeetcodeSubmitter()

    def _run(self, code: str) -> str:
        """Use the tool."""
        return self.submitter.run(self.problem_file, code)

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("LeetcodeSubmitTool does not support async")
