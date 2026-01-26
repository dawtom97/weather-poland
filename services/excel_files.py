import pandas as pd
import os

pd.set_option("display.max_columns",None)
pd.set_option("display.width",None)

def save_to_excel(data,path):
    try:
        new_df = pd.json_normalize([data])
        if os.path.exists(path):
            old_df = pd.read_excel(path)
            concat_data = pd.concat([old_df, new_df], ignore_index=True)
            concat_data.to_excel(path, index=False)
            print("Aktualizacja pliku XLSX")
        else:
            print("Tworzę nowy plik XLSX")
            new_df.to_excel(path, index=False)
    except Exception as e:
        print(e)

def read_excel_file(path):
    try:
        file = pd.read_excel(path)
        return file
    except Exception as e:
        print(e)