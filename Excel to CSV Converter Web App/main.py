import streamlit, pandas

streamlit.title("Excel to CSV File Converter")
excel_file = streamlit.file_uploader("Upload your .xlsx file", type='xlsx')

if excel_file is not None:
    df = pandas.read_excel(excel_file)
    csv = df.to_csv()
    streamlit.download_button(label='Download CSV', data=csv, file_name='data.csv')