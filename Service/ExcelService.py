import os
import pandas as pd

class ExcelService:
    def readCourseCSV(self):
        # Get the absolute path to the project's root directory
        project_root = os.path.dirname(__file__)

        # Assuming your Excel file is in a subdirectory named 'data'
        excel_file_path = os.path.join(project_root, 'anonymisedData', 'courses.csv')

        # Read the Excel file into a pandas DataFrame
        df = pd.read_csv(excel_file_path)

        # Display the DataFrame
        print(df)

    def readRegistrationInfoToGraph(self):
        # Get the absolute path to the project's root directory
        project_root = os.path.dirname(__file__)

        # Assuming your Excel file is in a subdirectory named 'data'
        excel_file_path = os.path.join(project_root, 'anonymisedData', 'studentRegistration.csv')

        # Read the Excel file into a pandas DataFrame
        df = pd.read_csv(excel_file_path)

        # Display the DataFrame
        print(df)


