from typing import Callable, List
from api.src.llm.basellm import BaseLLM


class LocalChat(BaseLLM):
    def __init__(self, model):
        self.model = model
    

    def generate(self, messages: List[str]) -> str:
        pass

    def generateStreaming(self, messages: List[str], onTokenCallback=Callable[[str], None]):
        pass

    def num_tokens_from_string(self, string: str) -> int:
        pass

    def max_allowed_token_length(self) -> int:
        return 2048