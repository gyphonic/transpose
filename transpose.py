import pandas as pd
import os

def main():
    try:
        #boilerplate
        print("Script to transpose a .csv file")
        print("Transposition swaps the rows and columns of a file.")

        #get current directory
        cwd = os.getcwd()

        #Get file
        file = input("Path of file: >")

        #verify
        print(">" + file)
        consent = input("Is this correct? Y/N")

        if consent.upper() == "Y":
            
            #read csv to dataframe
            try:
                df = pd.read_csv(file)
            except:
                print("File error. Double check file type.")
                break

            #transpose
            df = df.T

            #save
            try:
                fileT = "output.csv"
                df.to_csv(fileT, index = False)

                print("Completed. Saved to " + cwd + "/" + fileT)
            except:
                print("Saving error.")
                break


    except:
        print("Main error. Check file path and script validity.")

   




if __name__ == "__main__":
    main()