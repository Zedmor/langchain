from unittest.mock import patch

import pytest

from langchain.tools.leetcode.tool import LeetcodeSubmitter


@pytest.fixture
def patch_leetcode_directory():
    with patch("langchain.tools.leetcode.tool.LEETCODE_DIRECTORY",
               "tests/integration_tests/leetcode/fixtures"):
        yield


def test_submitter_incorrect(patch_leetcode_directory):
    filename = "1147.longest-chunked-palindrome-decomposition.py"
    code = "        return 0"
    tool = LeetcodeSubmitter()
    result = tool.run(filename, code)
    print(result)

