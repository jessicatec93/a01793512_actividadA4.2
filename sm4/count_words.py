"""
compute_statistics.py

Basic statistics are calculated from the data of the given file.
"""
import sys
import time

class ComputeStatistics:
    """
    Class to carry out state operations in a list of items.
    """

    def __init__(self):
        self.file_name_save = "StatisticsResults.txt"

    def get_file_data(self, file_name):
        """
            Extracts the data from the given file and returns it in an array
        """
        data = []
        with open(file_name, 'r', encoding="utf-8") as file:
            data = [float(line.strip()) for line in file]
        return data

    def get_statics(self, data):
        """
            Calculate all statistical data
        """
        statics = {
            "count":  data[0],
            "mean": 0,
            "median": 0,
            "mod": 0,
            "sd": 0,
            "variance": 0
        }
        return statics

    def set_print_statics(self, data):
        """
            Print result data to a file
        """
        print("\nRESULTS")
        for clave, valor in data.items():
            print(f"{clave.upper()}: {valor}")

    def set_save_statics(self, data):
        """
            Save result data to a file
        """
        with open(self.file_name_save, 'w', encoding="utf-8") as file:
            for clave, valor in data.items():
                file.write(f"{clave.upper()}: {valor}" + "\n")

    def operation(self):
        """
        :param file_name: File name to read.
        """
        try:
            if len(sys.argv) != 2:
                file_name = input("File name: ")
            else:
                file_name = sys.argv[1]
            file_data = self.get_file_data(file_name)
            statics = self.get_statics(file_data)
            self.set_print_statics(statics)
            self.set_save_statics(statics)
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    start_time = time.time()
    compute_statistics = ComputeStatistics()
    compute_statistics.operation()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTime elapsed: {round(elapsed_time, 4)} seconds\n")
