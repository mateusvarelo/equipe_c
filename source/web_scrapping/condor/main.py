from scrapping import CondorWebsite
import uuid
import json
from datetime import datetime
from pathlib import Path


def main():

    searches = ['arroz', 'feijão', 'tomate', 'refrigerante', 'suco'][0]

    for search in searches:
        condor_api = CondorWebsite()
        website_data = condor_api.get_website_data(search)

        id = uuid.uuid4()
        date = datetime.now().strftime('%Y-%m-%d')

        # Pushing HTML raw data to brass datalake

        directory_path = Path(f'equipe_c/brass/condor_html/search={search}/date={date}/')
        directory_path.mkdir(parents=True, exist_ok=True)
        path = directory_path / f'{id}.html'
        with open(path, 'w+') as f:
            f.write(website_data)


        parsed_website_data = condor_api.parse_website_data(website_data)

        # Pushing JSON data to bronze datalake

        directory_path = Path(f'equipe_c/bronze/condor_html/search={search}/date={date}/')
        directory_path.mkdir(parents=True, exist_ok=True)
        path = directory_path / f'{id}.json'
        with open(path, 'w+') as f:
            print(parsed_website_data)
            
            json.dump(parsed_website_data, f)

    
if __name__ == "__main__":
    main()