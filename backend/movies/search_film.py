import pandas as pd


# ------ install follow packages first
# pip install pandas
# pip install openpyxl

def search_title(title: str):
    title = title.lower()
    df = pd.read_excel('film.xlsx', usecols=['Title'])
    title_list = df['Title'].values
    return list(filter(lambda _t: title in _t.lower(), title_list))


if __name__ == '__main__':
    print(search_title('Star'))
