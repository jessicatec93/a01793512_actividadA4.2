"""
compute_statistics.py

Basic statistics are calculated from the data of the given file.
"""

class ComputeStatistics:
    """
    Class to carry out state operations in a list of items.
    """

    def __init__(self):
        pass

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
        print("staticsss", data)

    def set_print_statics(self, data):
        """
            Print result data to a file
        """
        print("print staticsss", data)

    def set_save_statics(self, data):
        """
            Save result data to a file
        """
        print("set staticsss", data)

    def operation(self):
        """
        :param file_name: File name to read.
        """
        try:
            file_name = input("File name: ")
            file_data = self.get_file_data(file_name)
            self.get_statics(file_data)
            self.set_print_statics(file_data)
            self.set_save_statics(file_data)
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    compute_statistics = ComputeStatistics()
    compute_statistics.operation()
