import os
import time
import pandas as pd

def load_row_data():
    start = time.time()

    FOLDER_PATH = r"D:\matplotlib_project\Data"

    for file in os.listdir(FOLDER_PATH):
        if not file.lower().endswith(".csv"):
            continue

        file_path = os.path.join(FOLDER_PATH, file)
        df = pd.read_csv(file_path)

        end = time.time()
        total_time = end - start

        print(f"Data Loaded: {file}")
        print(f"Total Time Taken: {total_time:.2f} seconds")

        return df

    
if __name__ == "__main__":
    load_row_data()
    
    # Schedule for function to run after every 30 minutes.........
    schedule.every(30).minutes.do(load_row_data)
    
    print("Scheduler started...")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
