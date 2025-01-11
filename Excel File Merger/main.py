import pandas, os


dataframes_2024 = [pandas.read_excel(f'./excel_files/{file}') for file in os.listdir('excel_files') if '2024' in file]
dataframes_2025 = [pandas.read_excel(f'./excel_files/{file}') for file in os.listdir('excel_files') if '2025' in file]

new_2024 = pandas.concat(dataframes_2024)
new_2024.to_excel("./excel_files/2024.xlsx")

new_2025 = pandas.concat(dataframes_2025)
new_2025.to_excel("./excel_files/2025.xlsx")