import requests
from bs4 import BeautifulSoup

wiki = "https://pt.wikipedia.org/wiki/Lista_de_capitais_do_Brasil_por_%C3%A1rea"
page = requests.get(wiki)
soup = BeautifulSoup(page.text, features="html.parser")
all_table = soup.find_all("table")
table = soup.find("table", class_="wikitable sortable")

# print(table)

A = []
B = []
C = []
D = []
E = []

for row in table.findAll("tr"):  # para tudo que estiver em <tr>
    cells = row.findAll("td")  # variável para encontrar <td>
    if len(cells) == 5:  # número de colunas
        A.append(cells[0].find(text=True))  # iterando sobre cada linha
        B.append(cells[1].find(text=True))
        C.append(cells[2].find(text=True))
        D.append(cells[3].find("a").text)
        E.append(cells[4].find(text=True))

import pandas as pd
import numpy as np

structure_table = np.array([A, B, C, D, E]).transpose()
df = pd.DataFrame(
    index=A,
    data=structure_table,
    columns=["Posição", "Estado", "Código/IBGE", "Capital", "Área"],
)
print(df.head())
print(df.shape)
