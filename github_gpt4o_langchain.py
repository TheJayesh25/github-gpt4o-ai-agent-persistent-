from langchain_core.language_models import BaseChatModel
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    FunctionMessage,
    ToolMessage,
    BaseMessage,
)
from langchain_core.outputs import ChatResult, ChatGeneration
from typing import List, Optional
from openai import OpenAI
from pydantic import PrivateAttr


class GitHubGPT4oChatModel(BaseChatModel):
    _client: OpenAI = PrivateAttr()

    def __init__(self, api_key: str, **kwargs):
        """
        Initialize the GitHub-hosted GPT-4o model.

        Args:
            api_key (str): GitHub-hosted GPT API key.
        """
        if not api_key:
            raise ValueError("GitHub API key must be provided.")
        
        super().__init__(**kwargs)
        self._client = OpenAI(
            base_url="https://models.github.ai/inference",
            api_key=api_key
        )

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
    ) -> ChatResult:
        openai_messages = []
        for msg in messages:
            role = {
                HumanMessage: "user",
                AIMessage: "assistant",
                SystemMessage: "system",
                FunctionMessage: "function",
                ToolMessage: "tool"
            }.get(type(msg), "user")

            message_dict = {"role": role, "content": msg.content}

            if isinstance(msg, FunctionMessage):
                message_dict["name"] = msg.name
            if isinstance(msg, ToolMessage):
                message_dict["tool_call_id"] = getattr(msg, "tool_call_id", "tool_1")

            openai_messages.append(message_dict)

        response = self._client.chat.completions.create(
            model="openai/gpt-4o",
            messages=openai_messages,
            temperature=1,
            max_tokens=1024,
        )

        ai_msg = AIMessage(content=response.choices[0].message.content)
        return ChatResult(generations=[ChatGeneration(message=ai_msg)])

    @property
    def _llm_type(self) -> str:
        return "github-gpt4o"

    def invoke(self, messages: List[BaseMessage]) -> AIMessage:
        return self._generate(messages).generations[0].message
