from random import choices

import pandas as pd
import numpy as np
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option("Display.max_columns" ,None)
pd.set_option("Display.width" ,500)
df = pd.read_csv( "C:/Users/selin/Downloads/miuul_gezinomi.csv", sep=";")
print(df.head())
print(df.info())
print(df.shape)
print(df["SaleCityName"].unique())
print(df["SaleCityName"].value_counts())
print(df["ConceptName"].unique())
print(df["ConceptName"].value_counts())
df["Price"] = df["Price"].str.replace(",",".")
df["Price"] = pd.to_numeric(df["Price"]).astype(float)
print(df.info())
city_price = df.groupby("SaleCityName").agg({"Price" : "sum"})
print(city_price)
concept_price = df.groupby("ConceptName")["Price"].sum()
print(concept_price)
city_ave = df.groupby("SaleCityName")["Price"].mean()
print(city_ave)
concept_ave = df.groupby("ConceptName")["Price"].mean()
print(concept_ave)
city_concept = df.groupby(["SaleCityName", "ConceptName"])["Price"].mean()
print(city_concept)
conditions = [df["SaleCheckInDayDiff"].between(0,7),
              df["SaleCheckInDayDiff"].between(7,30),
              df["SaleCheckInDayDiff"].between(30,90),
              df["SaleCheckInDayDiff"].between(90,1000)]
choice = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]
df["EB_Score"] = np.select(conditions, choice, default="UnKnown")
print(df.head())
eb_score = df.groupby(["SaleCityName", "ConceptName", "EB_Score"]).agg({"Price" : ["mean", "count"]})
print(eb_score)
seasons = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price" : ["mean", "count"]})
print(seasons)
cınday = df.groupby(["SaleCityName", "ConceptName", "CInDay"]).agg({"Price" : ["mean", "count"]})
print(cınday)
agg_df = df.groupby(["SaleCityName", "ConceptName", "Seasons"]).agg({"Price" : "mean"}).sort_values("Price",ascending = False)
print(agg_df.head())
print(agg_df.reset_index(inplace = True))
print(agg_df.head())
agg_df["sales_level_based"] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x : "_".join(x).upper(), axis=1)
print(agg_df.head())
agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4 , labels=["D" ,"C" ,"B", "A"])
print(agg_df.head())
seg = agg_df.groupby("SEGMENT").agg({"Price" : ["mean", "max" ,"sum"]})
print(seg.head())
agg_df.sort_values(by="Price")
new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
print(agg_df[agg_df["sales_level_based"] == new_user])