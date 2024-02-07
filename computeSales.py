"""
Alumno: Jessica Lechuga Ramos
Matrícula: A01793512

Calculation of profits.
"""
import json
import sys
import time

class ComputeSales:
    """
    Class to perform operations from two files that have sales.
    """

    def __init__(self):
        self.start_time = time.time()
        self.elapsed_time = None
        self.file_name_save = "SalesResults.txt"
        self.title = ["Row Labels",	"Count Word"]


    def get_file_data(self, file_name):
        """
            Extracts the data from the given file and returns it in an array
        """
        data = []
        with open(file_name, 'r', encoding="utf-8") as file:
            data = json.load(file)
        return data


    def get_total_sales(self, products_file_data, sales_file_data):
        """
            Bring sales totals
        """
        results = {}
        for word in data:
            word = word.lower()
            results[word] = results.get(word, 0) + 1
        results["Grant Total"] = len(data)
        return results


    def set_print_count_words(self, data):
        """
            Print result data to a file
        """
        print("\nRESULTS")
        print(" ".join(self.title) + "\n")
        for word, frequency in data.items():
            concatenation = f'{word} {frequency}'
            print(concatenation)
        end_time = time.time()
        self.elapsed_time = end_time - self.start_time
        print(f"\nTime elapsed: {round(self.elapsed_time, 4)} seconds\n")


    def set_save_count_words(self, data):
        """
            Save result data to a file
        """
        with open(self.file_name_save, 'w', encoding="utf-8") as file:
            file.write(" ".join(self.title) + "\n")
            for word, frequency in data.items():
                concatenation = f'{word} {frequency}'
                file.write(concatenation + "\n")
            file.write(f"\nTime elapsed: {round(self.elapsed_time, 4)} seconds\n")


    def operation(self):
        """
        :param file_name: File name to read.
        """
        try:
            if len(sys.argv) != 3:
                products_file_name = input("Products file name: ")
            else:
                products_file_name = sys.argv[1]
            if len(sys.argv) != 3:
                sales_file_name = input("Sales file name: ")
            else:
                sales_file_name = sys.argv[2]
            products_file_data = self.get_file_data(products_file_name)
            print(products_file_data)
            sales_file_data = self.get_file_data(sales_file_name)
            #total_sales = self.get_total_sales(products_file_data, sales_file_data)
            #self.set_print_total_sales(count_words)
            #self.set_save_total_sales(count_words)
        except FileNotFoundError:
            print(f"Error: File '{products_file_name}' or '{sales_file_name}' not found.")
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    compute_sales = ComputeSales()
    compute_sales.operation()
