import os
import requests

# Define the API endpoints and folder names
endpoints = {
    "despesas_ceaps": "/api/v1/senadores/despesas_ceaps/{year}/csv",
    "quantitativos_senadores": "/api/v1/senadores/quantitativos/senadores/csv",
    "escritorios": "/api/v1/senadores/escritorios/csv",
    "auxilio_moradia": "/api/v1/senadores/auxilio-moradia/csv",
    "aposentados": "/api/v1/senadores/aposentados/csv"
}

folders = {
    "despesas_ceaps": "despesas_ceaps",
    "quantitativos_senadores": "quantitativos_senadores",
    "escritorios": "escritorios",
    "auxilio_moradia": "auxilio_moradia",
    "aposentados": "aposentados"
}

# Create the folders if they don't exist
for folder_name in folders.values():
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

# Loop over the endpoints and years, and download the CSV files
for endpoint_name, endpoint_url in endpoints.items():
    if "{year}" in endpoint_url:
        print(f"Downloading CSV files for {endpoint_name}...")
        for year in range(1990, 2024):
            try:
                url = f"https://adm.senado.gov.br/adm-dadosabertos{endpoint_url.format(year=year)}"
                response = requests.get(url)
                file_path = os.path.join(folders[endpoint_name], f"{endpoint_name}_{year}.csv")
                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded CSV for {endpoint_name} and year {year}")
            except:
                print(f"Error downloading CSV for {endpoint_name} and year {year}")
    else:
        print(f"Downloading CSV files for {endpoint_name}...")
        try:
            url = f"https://adm.senado.gov.br/adm-dadosabertos{endpoint_url}"
            response = requests.get(url)
            file_path = os.path.join(folders[endpoint_name], f"{endpoint_name}.csv")
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded CSV for {endpoint_name}")
        except:
            print(f"Error downloading CSV for {endpoint_name}")
