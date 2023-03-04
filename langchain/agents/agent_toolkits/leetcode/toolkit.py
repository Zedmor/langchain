from __future__ import annotations

from typing import Any, List

from langchain.agents.agent import AgentExecutor
from langchain.agents.agent_toolkits.json.base import create_json_agent
from langchain.agents.agent_toolkits.json.toolkit import JsonToolkit
from langchain.agents.agent_toolkits.openapi.prompt import DESCRIPTION
from langchain.agents.tools import Tool
from langchain.llms.base import BaseLLM
from langchain.requests import RequestsWrapper
from langchain.tools import BaseTool
from langchain.tools.json.tool import JsonSpec

from langchain.agents.agent_toolkits.base import BaseToolkit
from langchain.tools.python.tool import PythonREPLTool


class LeetCodeToolkit(BaseToolkit):
    """Toolkit for interacting with a OpenAPI api."""

    json_agent: AgentExecutor
    requests_wrapper: RequestsWrapper

    def get_tools(self) -> List[BaseTool]:
        """Get the tools in the toolkit."""
        return [PythonREPLTool(), LeetCodeTool()]

    @classmethod
    def from_llm(cls) -> LeetCodeToolkit:
        """Create json agent from llm, then initialize."""
        return cls()
