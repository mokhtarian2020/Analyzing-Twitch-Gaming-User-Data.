import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('chat_data.db')
cursor = conn.cursor()

# SQL query to extract data
query = """
SELECT 
    user_id,
    message,
    timestamp
FROM 
    chat_messages
WHERE 
    timestamp >= '2023-01-01' AND timestamp <= '2023-12-31'
"""
# Execute the query and load data into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the database connection
conn.close()

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract hour from timestamp for analysis
df['hour'] = df['timestamp'].dt.hour

# Group by hour and count messages
hourly_activity = df.groupby('hour').size()

# Plot the hourly chat activity
plt.figure(figsize=(10, 6))
plt.plot(hourly_activity.index, hourly_activity.values, marker='o')
plt.title('Hourly Chat Activity')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Messages')
plt.grid(True)
plt.xticks(range(0, 24))
plt.show()
