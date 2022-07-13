from recommender import recommend_members,get_challenges
import click
import json
from pathlib import Path
from surprise import  dump
import tqdm
import pandas as pd

data_folder = Path("data/")

 
@click.command()
@click.option('--member_dir_path', default=data_folder / "input_member_profiles.json", help="Member Profile JSON Path")
@click.option('--challenge_dir_path', default=data_folder / "input_challenge_profiles.json", help="Challenge Profile JSON Path")
def cli(member_dir_path,challenge_dir_path):
    try:
        if member_dir_path and challenge_dir_path:
            print("Recommending Members!")

            print("Loading Data!")
            with open(member_dir_path,'r') as f:
                member_profiles = json.load(f)
    
            with open(challenge_dir_path,'r') as f:
                challenge_profiles = json.load(f)

            challenges = get_challenges(challenge_profiles)
            
            print("Total No of challenges-", len(challenges))

            print("loading Model!")
            _, model = dump.load('recmdr')

            print("Creating Output!")

            output_data = []
            for key in tqdm.tqdm(member_profiles.keys()):
                for challenge in challenges:
                    top_members = recommend_members(model,challenge,member_profiles[key])
                    temp = [key,challenge['id'],challenge['skills']]
                    temp.extend(top_members)
                    output_data.append(temp)
            
            print("Total no of records processed-",len(output_data))

            columns = ['time block', 'challenge id', 'challenge skills profile']
            for i in range(1,61):
                columns.append(str(i))
            output = pd.DataFrame(output_data, columns = columns)
            output.to_csv(data_folder/"recommendations.csv",index=False)
            print("Done - data/recommendations.csv")
        else:
            print("Please enter a valid directory path")
    except Exception as e:
        print("Error - ", str(e))
        print()

if __name__ == '__main__':
    cli()