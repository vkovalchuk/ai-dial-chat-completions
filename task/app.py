import asyncio

import readline

from task.clients.client import DialClient
from task.constants import DEFAULT_SYSTEM_PROMPT, DEFAULT_LLM_NAME
from task.models.conversation import Conversation
from task.models.message import Message
from task.models.role import Role


async def start(stream: bool) -> None:
    # 1.1. Create DialClient
    # (you can get available deployment_name via https://ai-proxy.lab.epam.com/openai/models
    #  you can import Postman collection to make a request, file in the project root `dial-basics.postman_collection.json`
    #  don't forget to add your API_KEY)
    print("LLM to use: ", DEFAULT_LLM_NAME)
    dial_cli = DialClient(DEFAULT_LLM_NAME)
    # 1.2. Create CustomDialClient
    print("Not using CustomDialClient")
    # 2. Create Conversation object
    conv1 = Conversation()
    # 3. Get System prompt from console or use default -> constants.DEFAULT_SYSTEM_PROMPT and add to conversation
    #    messages.
    # 4. Use infinite cycle (while True) and get yser message from console
    while True:
        user_input = input("User: ")
        # 5. If user message is `exit` then stop the loop
        if user_input == "exit":
            break
        # 6. Add user message to conversation history (role 'user')
        conv1.add_message(Message(role=Role.USER, content=user_input))
        # 7. If `stream` param is true -> call DialClient#stream_completion()
        assistant_message = dial_cli.get_completion(messages=conv1.get_messages())
        #    else -> call DialClient#get_completion()
        # 8. Add generated message to history
        conv1.add_message(assistant_message)
        print("-" * 60)
    print("Exiting")
    # 9. Test it with DialClient and CustomDialClient
    # 10. In CustomDialClient add print of whole request and response to see what you send and what you get in response


asyncio.run(
    start(True)
)
