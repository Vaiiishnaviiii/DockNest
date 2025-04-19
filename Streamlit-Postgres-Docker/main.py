import streamlit as st
import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="my_postgres_container",  # PostgreSQL container name
    port="5432",
    database="testdb",
    user="vaishnavi",  # PostgreSQL username
    password="secret"  # Password for the 'vaishnavi' user
)

# Fetch data from the database
cur = conn.cursor()
cur.execute("SELECT * FROM passengers;")
rows = cur.fetchall()

# Display the data in Streamlit
st.title("Passenger Data")
st.write("This is the passenger data fetched from the PostgreSQL database.")
for row in rows:
    st.write(f"Name: {row[1]}, Location: {row[2]}")

# Close the connection
cur.close()
conn.close()
