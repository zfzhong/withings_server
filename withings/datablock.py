import pandas as pd
import numpy as np

import datetime as dt


class DataBlock:
    def __init__(self, block):
        self.sensor_name = block['sensor_name']
        self.startdate = block['startdate']
        self.enddate = block['enddate']
        self.df = pd.DataFrame(block['data'])

    def interpolate_timestamps(self):
        # Group by 'ts' and calculate the count for each group                                                                                    
        self.df['count'] = self.df.groupby('timestamp')['timestamp'].transform('count')

        # Calculate the interval for each group dynamically                                                                                       
        self.df['interval'] = 1000 / self.df['count']

        # Create an index within each group                                                                                                       
        self.df['index'] = self.df.groupby('timestamp').cumcount()

        # Calculate the new timestamp with dynamic milliseconds                                                                                   
        self.df['timestamp'] = self.df['timestamp'] * 1000 + self.df['index'] * self.df['interval']

    def dump(self):
        t1 = dt.datetime.fromtimestamp(self.startdate)
        t2 = dt.datetime.fromtimestamp(self.enddate)

        sec = self.enddate - self.startdate

        print("%s - %s: %s - %s: %s seconds" % (t1, t2, self.startdate, self.enddate, sec))
        #print("columns:", self.df.columns)                                                                                                       

        #for index, row in self.df.iterrows():                                                                                                    
        #    print("%s,%s,%s,%s" % (row["timestamp"],row["acc_x"], row["acc_y"], row["acc_z"]))                                                   

    def plot(self, plt):
        df = self.df
        df["Norm"] = np.sqrt(df["acc_x"]**2 + df["acc_y"]**2 + df["acc_z"]**2)
        df["Time"] = df['timestamp'].apply(lambda x: dt.datetime.fromtimestamp(x/1000))

        plt.plot(df["Time"], df["Norm"], color='red', label="Accel")