import os
import openai

openai.api_key = os.environ['OPENAI_API_KEY']


class GPT:
    """Instantiate GPT model for a multi-step conversation."""

    def __init__(self,
                 system_prompt='You are a helpful assistant.',
                 model='gpt-3.5-turbo',
                 temperature=.7,
                 **kwargs):
        """Setup model parameters and system prompt."""
        self.params = {'model': model, 'temperature': temperature, **kwargs}
        self.messages = [{'role': 'system', 'content': f'{system_prompt}'}]

    def chat(self, user_prompt):
        """Add user prompt to the buffer and generate a response."""
        self.messages.append({'role': 'user', 'content': f'{user_prompt}'})
        response = self.get_response()
        self.messages.append({'role': 'assistant', 'content': response})

    def get_response(self):
        """Generate a response from the model."""
        self.response = openai.ChatCompletion.create(messages=self.messages, **self.params)
        return self.response.choices[0].message.content

    def display(self):
        """Display the conversation history."""
        for message in self.messages:
            print(f'[{message["role"].upper():>9s}]: {message["content"]}')


if __name__ == '__main__':

    # instantiate the model and generate a conversation
    gpt = GPT(system_prompt='You are Arthur, king of the Britons. '\
              + 'You are on the quest to find the Holy Grail and have '\
              + 'to cross the mysterious and feared Bridge of Death. '\
              + 'In order to cross, you have to answer three questions.''')
    gpt.chat('What is your name?')
    gpt.chat('What is your quest?')
    gpt.chat('What is the airspeed velocity of an unladen swallow?')
    gpt.display()

