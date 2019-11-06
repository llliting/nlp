
import pandas as pd
import nltk
from pandas import DataFrame
import numpy as np
import os
import xlwt
import math
from nltk import word_tokenize

df = pd.read_csv("/Users/liting/Desktop/ProQuestDocuments-2019-11-01.csv")

titles = df["Title"]


abstract = df["Abstract"]

