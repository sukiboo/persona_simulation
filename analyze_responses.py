import os
import re
import json
import tqdm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

sns.set_theme(style='darkgrid', palette='muted', font='monospace', font_scale=1.)


def visualize_experiment(exp_dir):
    """Parse and visualize a given experiment."""
    print(f'Analyzing experiment {exp_dir}...\n')
    os.makedirs(f'./images/{exp_dir}', exist_ok=True)

    # parse responses and collect demographics/statistics
    demos = defaultdict(list)
    stats = defaultdict(list)
    for response_log in sorted(os.listdir(f'./data/{exp_dir}/')):
        try:
            with open(f'./data/{exp_dir}/{response_log}') as response_file:
                response_num = int(response_log[:-5])
                response = json.load(response_file)[-1]['content']

                # parse demographics
                demos['id'].append(response_num)
                for line in response.split('\n')[:-5]:
                    demo, val = line.split(': ')
                    demos[re.sub('[^a-zA-Z]', '', demo).lower()].append(val.lower())

                # parse statistics
                stats['id'].append(response_num)
                response_stats = re.findall(r'\d+', response)
                stats['Binge drank'].append(int(response_stats[-3]))
                stats['Frozen food for dinner'].append(int(response_stats[-2]))
                stats['Sugary soda consumption'].append(int(response_stats[-1]))

        except:
            print(f'Could not parse response {response_log}...')

    # visualize stats
    for label, stat in stats.items():
        plt.hist(stat, density=True, bins=max(stat)+1, range=(0,max(stat)+1), align='left')
        plt.title(f'{label} in the last 30 days')
        plt.tight_layout()
        plt.savefig(f'./images/{exp_dir}/{label}.png')
        plt.show()

    return demos, stats


if __name__ == '__main__':

    exp_dir = 'susanne_230725'
    demos, stats = visualize_experiment(exp_dir)

