from aidial_client import Dial, AsyncDial

from task.clients.base import BaseClient
from task.constants import DIAL_ENDPOINT
from task.models.message import Message
from task.models.role import Role


class DialClient(BaseClient):

    def __init__(self, deployment_name: str):
        super().__init__(deployment_name)
        # Documentation: https://pypi.org/project/aidial-client/ (here you can find how to create and use these clients)
        # 1. Create Dial client
        self.sync_client = Dial(api_key=self._api_key, base_url=DIAL_ENDPOINT)
        # 2. Create AsyncDial client

    def get_completion(self, messages: list[Message]) -> Message:
        # 1. Create chat completions with client
        #    Hint: to unpack messages you can use the `to_dict()` method from Message object
        completion = self.sync_client.chat.completions.create(
            deployment_name=self._deployment_name,
            stream=False,
            messages=[m.to_dict() for m in messages],
            api_version="2024-12-01-preview",
        )
        # 2. Get content from response, print it and return message with assistant role and content
        # print("Assistant: ", completion)
        # 3. If choices are not present then raise Exception("No choices in response found")
        if not completion.choices:
            raise Exception("No choices in response found")
        llm_answer = completion.choices[0].message
        print("Assistant: ", llm_answer.content)
        print(" Date: ", completion.created)
        print(" Tokens: input=", completion.usage.prompt_tokens, ", output=", completion.usage.completion_tokens)
        assert llm_answer.role == "assistant"
        return llm_answer

    async def stream_completion(self, messages: list[Message]) -> Message:
        #TODO:
        # 1. Create chat completions with async client
        #    Hint: don't forget to add `stream=True` in call.
        # 2. Create array with `contents` name (here we will collect all content chunks)
        # 3. Make async loop from `chunks` (from 1st step)
        # 4. Print content chunk and collect it contents array
        # 5. Print empty row `print()` (it will represent the end of streaming and in console we will print input from a new line)
        # 6. Return Message with assistant role and message collected content
        raise NotImplementedError
