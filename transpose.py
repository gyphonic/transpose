#gyphonic/transpose.py
#V1.2

import pandas as pd
import os

def main():
    try:
        #boilerplate
        print(" ")
        print("gyphonic/transpose V1.2")
        print("Script to transpose a .csv file")
        print("Transposition swaps the rows and columns of a file by reflecting over the diagonal.")
        print(" ")

        #get current directory
        cwd = os.getcwd()

        #Get file
        file = input("File: ")

        #verify
        print("> " + file)
        consent = input("Is this correct? (Y/N) ")

        if consent.upper() == "Y":
            
            #read csv to dataframe
            try:
                df = pd.read_csv(file)
            except:
                print("File error. Double check file type.")

            #transpose
            try:
                df = df.T
            except:
                print("Transposition error.")

            #save
            try:
                fileT = "output.csv"
                df.to_csv(fileT)

                print("Completed. Saved to " + cwd + "/" + fileT)
            except:
                print("Saving error.")


    except:
        print("Main error. Check file path and script validity.")

   




if __name__ == "__main__":
    main()