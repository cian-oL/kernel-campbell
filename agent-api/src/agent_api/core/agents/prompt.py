"""
System prompt for the agent
"""

from agent_api.core.agents.system_prompt import SYSTEM_PROMPT


class Prompt:
    """
    System prompt for the agent
    """

    def __init__(self, *, name, prompt) -> None:
        self.name = name
        self.prompt = prompt

    def __str__(self) -> str:
        return self.prompt

    def __repr__(self) -> str:
        return self.__str__()


system_prompt = Prompt(name="system_prompt", prompt=SYSTEM_PROMPT)
