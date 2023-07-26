import os
import json
import argparse

from gpt import GPT


def simulate_person(prompts, exp_dir, display=True):
    """Generate a synthetic person via GPT and collect their responses."""
    gpt = GPT()
    for prompt in prompts:
        gpt.chat(prompt)
    if display:
        gpt.display()
    return gpt.messages


if __name__ == '__main__':

    # parse the configs
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prompt',
                        default='baseline',
                        help='name of the prompt file in "./prompts/"')
    parser.add_argument('-n', '--num',
                        default=10,
                        help='number of simulated people to take responses from')

    # read the inputs
    args = parser.parse_args()
    prompt_file = args.prompt
    num_people = int(args.num)

    # read the prompt
    with open(f'./prompts/{prompt_file}.txt') as f:
        prompts = f.read().split('\n---\n')
    print(f'Loaded prompt {prompt_file}:', *prompts, sep='\n\n')

    # simulate people and save responses
    exp_dir = f'./data/{prompt_file}/'
    os.makedirs(exp_dir, exist_ok=True)
    for n in range(num_people):
        num_person = str(n+1).rjust(len(str(num_people)))
        print(f'\nSimulating person {num_person}/{num_people}...')
        response = simulate_person(prompts, exp_dir, display=True)
        with open(exp_dir + f'{num_person}.json', 'w') as f:
            json.dump(response, f)

