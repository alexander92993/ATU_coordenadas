import requests
import pandas as pd

writer = pd.ExcelWriter('BD_final.xlsx', engine='openpyxl')

url = "https://sistemas.atu.gob.pe/paraderosCOVID/Home/traer_datos"
headers2 = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

for xx in range(1,4):
    payload = {'PARTIPCOD': xx}
    res = requests.post(url, data=payload, headers = headers2)

    r_dict = res.json()
    tamaño_dict = len(r_dict)

    Parnom = []
    Disnom = []
    Nivel = []
    Latitud = []
    Longitud = []
    Tipo = []

    for elem in range(tamaño_dict):
        Parnom.append(r_dict[elem]['PARNOM'])
        Disnom.append(r_dict[elem]['DISNOM'])
        Nivel.append(r_dict[elem]['NIVEL'])
        Latitud.append(r_dict[elem]['LATITUD'])
        Longitud.append(r_dict[elem]['LONGITUD'])
        Tipo.append(r_dict[elem]['TIPODET'])

    df = pd.DataFrame(list(zip(Parnom,Disnom,Nivel,Latitud,Longitud,Tipo)), columns = ['Nombre de paradero','Distrito','Nivel','Latitud','Longitud','Tipo'])
    df.to_excel(writer, index=False, sheet_name=str(xx))
    writer.save()


