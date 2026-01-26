import mysql.connector
from config import Config

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASS,
            port=Config.DB_PORT,
            database=Config.DB_NAME
        )
        return connection
    except Exception as e:
        print(e)


def save_record(data):
    conn = create_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO 
    weather_records (miasto,temperatura,odczuwalna_temperatura,wilgotnosc,cisnienie,wiatr_predkosc,wiatr_kierunek, data_pomiaru)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    variables = (
        data.get("miasto"), data.get("temperatura"), data.get("odczuwalna_temperatura"),
        data.get("wilgotnosc"), data.get("cisnienie"), data.get("wiatr").get("predkosc"), data.get("wiatr").get("kierunek"),
        data.get("data_pomiaru")
    )

    cursor.execute(query, variables)
    conn.commit()









