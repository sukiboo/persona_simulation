# Persona Simulation

Simulate people with GPT models and generate response statistics.
Not sure how to do any of these things yet but we're working on it.

## Collecting Responses
A simulated survey is generated from a prompt file in `./prompts/` directory.
Prompt file should consist by a series of prompts separated by `---`.
For example, a prompt file:
```
prompt1
---
prompt2
---
prompt3
```
will result in the following conversation:
```
user: prompt1
assistant: response1
user: prompt2
assistant: response2
user: prompt3
assistant: response3
```

Use a prompt file `prompt_name.txt` to simulate a survey with `num` participants via the command
```
python -m collect_responses -p prompt_name -n num
```
The default values for the arguments are `prompt_name=baseline` and `num=10`.

A survey will be saved in `./data/prompt_name/` as a series of `.json` files numbered after each simulated participant.
