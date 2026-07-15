from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )

        if connection.is_connected():
            connection.close()
            return """
            <h2>Backend Service - Flask</h2>
            <p style="color:green;">✅ Connected to MySQL Successfully!</p>
            """

    except Exception as e:
        return f"""
        <h2>Backend Service - Flask</h2>
        <p style="color:red;">❌ Database Connection Failed</p>
        <pre>{e}</pre>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)