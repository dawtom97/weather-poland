from flask import Flask, render_template, jsonify
from services.mysql_db import all_weather_records
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = Flask(__name__)

COMMON_LAYOUT = dict(
    template="plotly_white",
    hovermode="x unified",
    margin=dict(l=40, r=40, t=60, b=40),
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    xaxis=dict(
        showgrid=False,
        title="Czas"
    )
)

@app.route("/")
def home_page():

    try:
        weather = all_weather_records()
    except Exception as e:
        weather = []
        print(e)

    df = pd.DataFrame(weather)

    temp_fig = px.line(
        df,
        x="data_pomiaru",
        y="temperatura",
        title="Temperatura"
    )

    humidity_fig = px.scatter(
        df,
        x="data_pomiaru",
        y="wilgotnosc",
        labels=["A","B"]
    )

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df["data_pomiaru"],
        y=df["temperatura"],
        name="Temperatura rzeczywista"
    ))
    fig.add_trace(go.Bar(
        x=df["data_pomiaru"],
        y=df["odczuwalna_temperatura"],
        name="Temperatura odczuwalna"
    ))
    fig.update_layout(
        **COMMON_LAYOUT,
        title="Porównanie temp. odczuwalnej i rzeczywistej",
        xaxis_title="Czas",
        yaxis_title="Temperatura"
    )


    return render_template(
        "index.html",
        weather=weather,
        temp_plot=temp_fig.to_html(full_html=False),
        humidity_plot=humidity_fig.to_html(full_html=False),
        temp_compare_plot= fig.to_html(full_html=False)
    )










# @app.route("/")
# def hello_world():
#     year = datetime.now().year
#     cities = ["Warszawa","Kraków","Poznań"]
#     admin = True
#     return render_template(
#         "index.html",
#         rok=year,
#         miasta=cities,
#         admin=admin
#     )
#
# @app.route("/kontakt")
# def contact_page():
#     phone = "463829201"
#     email = "firma@firma.pl"
#     return render_template(
#         "contact.html",
#         adres_email=email,
#         nr_telefonu=phone
#     )
#
# @app.route("/wiadomosci/<title>")
# def news_page(title: str):
#     return f"Strona wiadomości {title.capitalize()}"
#
# @app.route("/panstwa")
# def all_countries_page():
#     response = requests.get("https://restcountries.com/v3.1/all?fields=name,flags,cca3")
#     data = response.json()
#     return render_template(
#         "countries.html",
#         countries=data
#     )
#
# @app.route("/panstwa/kraj/<cca3>")
# def single_country(cca3):
#
#     response = requests.get(f"https://restcountries.com/v3.1/alpha/{cca3}")
#     data = response.json()
#
#     return render_template(
#         "details.html",
#         country=data[0]
#     )