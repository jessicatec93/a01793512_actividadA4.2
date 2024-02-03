"""
computeStatistics.py

Basic statistics are calculated from the data of the given file.
"""
import sys
import time

class ComputeStatistics:
    """
    Class to carry out state operations in a list of items.
    """


    def __init__(self):
        self.decimals = 6
        self.file_name_save = "StatisticsResults.txt"


    def get_file_data(self, file_name):
        """
            Extracts the data from the given file and returns it in an array
        """
        data = []
        with open(file_name, 'r', encoding="utf-8") as file:
            for line in file:
                try:
                    number = float(line.strip())
                except ValueError:
                    number = 0
                data.append(number)
        return data


    def get_statics(self, data):
        """
            Calculate all statistical data
        """
        median = 0
        mod = 0
        sd = 0
        variance = 0
        count = len(data)
        mean = sum(data) / count

        # Calculate the median
        sorted_data = sorted(data)
        if count % 2 == 0:
            mid1 = sorted_data[count // 2 - 1]
            mid2 = sorted_data[count // 2]
            median = (mid1 + mid2) / 2
        else:
            median = sorted_data[count // 2]

        # Calculate the mode
        frequencies = {}
        for number in data:
            if number in frequencies:
                frequencies[number] += 1
            else:
                frequencies[number] = 1

        max_frequency = max(frequencies.values())
        mode = [number for number, frequency in frequencies.items() if frequency == max_frequency]
        mod=max(mode)

        # Calculate the variance
        variance = sum((x - mean) ** 2 for x in data) / (count -  1)

        # Calculate the deviate standard
        sd = variance ** 0.5

        statics = {
            "count":  count,
            "mean": round(mean, self.decimals),
            "median": median,
            "mod": mod,
            "sd": round(sd, self.decimals),
            "variance": round(variance, self.decimals)
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
