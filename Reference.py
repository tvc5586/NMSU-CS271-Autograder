
# ===========================================
# Edit this file according to the assignments
# ===========================================

import pandas as pd

def reference_code(programParameters):
    Answers = []
 
    df = pd.read_csv(programParameters)
    df = df.dropna(axis = "index", how = "any", subset = ['TMAX', 'TMIN'])
    
    rows, _ = df.shape
    Answers.append(f"Number of data records: {rows}")

    Answers.append(f"Beginning date: {df.iloc[0, 5]}")
    Answers.append(f"Ending date: {df.iloc[-1, 5]}")

    Answers.append(f"Maximum temperature: {int(df.iloc[-1, 18])} degrees on {df.iloc[-1, 5]}")
    Answers.append(f"Minimum temperature: {int(df.iloc[-1, 19])} degrees on {df.iloc[-1, 5]}")

    Answers.append(f"Number of days 100 and over: {len(df[df["TMAX"] >= 100.0])}")
    Answers.append(f"Number of days below freezing: {len(df[df["TMIN"] < 32.0])}")

    return Answers
	
if __name__ == "__main__":
    answers = reference_code("weather-small.csv")
    
    for i in answers:
        print(i)
