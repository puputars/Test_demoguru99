from types import CoroutineType
import numpy as np
import csv, os, io
from pandas import pandas as pd


class manage_data():
  def read_file(self, files):
    data = pd.read_csv(files)
    data = data.replace(np.nan, '', regex=True)

    new_data = {}
    new_data["first_name"] = data["first_name"].to_list()
    new_data["last_name"] = data["last_name"].to_list()
    new_data["phone"] = data["phone"].to_list()
    new_data["email"] = data["email"].to_list()
    new_data["address"] = data["address"].to_list()
    new_data["city"] = data["city"].to_list()
    new_data["state"] = data["state"].to_list()
    new_data["postal_code"] = data["postal_code"].to_list()
    new_data["country"] = data["country"].to_list()
    new_data["user_name"] = data["user_name"].to_list()
    new_data["password"] = data["password"].to_list()
    new_data["confirm_password"] = data["confirm_password"].to_list()
    
    #print(len(data))
    return new_data
    #print(new_data["first_name"][0])
    #print(data["first_name"].to_list())
    ##print(data2["last_name1"])
    #print(data["last_name"].to_list())

  def total_file(self, files):
    data = pd.read_csv(files)
    return len(data)

#if __name__ == "__main__":
#  file="file_csv/data.csv"
#  manage_data().read_file(file)