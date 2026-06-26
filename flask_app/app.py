from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_connection():
    conn = sqlite3.connect("database/bluestock_mf.db")
    return conn

@app.route("/")
def home():
    return "Mutual_Fund_Analytics API Running"

@app.route("/top_funds")
def top_funds():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""select f.scheme_name, a.aum
                    from fact_aum a
                    join dim_fund f
                    on a.scheme_code = f.scheme_code
                    order by a.aum desc
                    limit 5;""")

    result = cursor.fetchall()
    conn.close()

    return jsonify(result)


@app.route("/performance")
def performance():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""select scheme_code, return_5y, sharpe
                    from fact_performance
                    limit 10""")


    result=cursor.fetchall()
    conn.close()

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)