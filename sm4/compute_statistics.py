"""
compute_statistics.py

This module offers the ComputeStatistics class that performs operations on a list of elements in a data archive.
"""

class ComputeStatistics:
    """
    Class to carry out state operations in a list of items.
    """

    def __init__(self):
        pass

    def __get_file_data(self, file_name):
        try:
            data = []
            file = open(file_name, 'r')
            line = file.readline()
            while line:
                data.append(int(line))
                line = file.readline()
            file.close()
            return data
        except FileNotFoundError:
            raise ValueError(f"File '{file_name}' not found.")
        except Exception as e:
            raise ValueError(e)

    def operation(self):
        """
        Realiza una operación en la lista de elementos.

        :param data: Lista de elementos (presumiblemente números).
        """
        try:
            file_name = input("File name: ")
            file_data = self.__get_file_data(file_name)
            print(file_data)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    compute_statistics = ComputeStatistics()
    compute_statistics.operation()
