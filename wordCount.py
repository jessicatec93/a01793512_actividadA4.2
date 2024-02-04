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
        self.file_name_save = "WordCountResults.txt"
        self.title = ["Row Labels",	"Count Word"]


    def get_file_data(self, file_name):
        """
            Extracts the data from the given file and returns it in an array
        """
        data = []
        with open(file_name, 'r', encoding="utf-8") as file:
            data = [line.strip() for line in file]
        return data


    def get_count_words(self, data):
        """
            Calculate all statistical data
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


    def set_save_count_words(self, data):
        """
            Save result data to a file
        """
        with open(self.file_name_save, 'w', encoding="utf-8") as file:
            file.write(" ".join(self.title) + "\n")
            for word, frequency in data.items():
                concatenation = f'{word} {frequency}'
                file.write(concatenation + "\n")


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
            count_words = self.get_count_words(file_data)
            self.set_print_count_words(count_words)
            self.set_save_count_words(count_words)
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
