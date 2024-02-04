"""
The numbers must be converted to binary
"""
import sys
import time

class ComputeStatistics:
    """
    Class to convert a number to binary on a list of elements.
    """

    def __init__(self):
        self.file_name_save = "ConvertionResults.txt"
        self.title = ["NUMBER", "BIN", "HEX"]

    def get_file_data(self, file_name):
        """
            Extracts the data from the given file and returns it in an array
        """
        data = []
        with open(file_name, 'r', encoding="utf-8") as file:
            data = [line.strip() for line in file]
        return data

    def decimal_to_binary(self, decimal):
        if decimal < 0:
            return "Negative numbers are not supported"
        elif decimal == 0:
            return "0b0"

        binary_digits = []

        while decimal > 0:
            remainder = decimal % 2
            binary_digits.append(str(remainder))
            decimal //= 2

        binary_digits.reverse()
        binary_str = "0b" + "".join(binary_digits)

        return binary_str
    
    def decimal_to_hexadecimal(self, decimal):
        if decimal < 0:
            return "Los números negativos no son compatibles"
        elif decimal == 0:
            return "0x0"

        hexadecimal_digits = []
        hex_characters = "0123456789ABCDEF"

        while decimal > 0:
            remainder = decimal % 16
            hexadecimal_digits.append(hex_characters[remainder])
            decimal //= 16

        hexadecimal_digits.reverse()
        hexadecimal_str = "0x" + "".join(hexadecimal_digits)

        return hexadecimal_str

    def get_binary_data(self, data):
        """
            Calculate all statistical data
        """
        results = []
        for num in data:
            data = None
            try:
                number = int(num)
                bin = self.decimal_to_binary(number)
                hex = self.decimal_to_hexadecimal(number)
                data = [number, bin, hex]
            except ValueError:
                number = num
                err = "#VALUE!"
                data = [number, err, err]
            results.append(data)
        return results

    def set_print_binary_data(self, data):
        """
            Print result data to a file
        """
        print("\nRESULTS")
        print(" ".join(self.title) + "\n")
        for valor in data:
            print(" ".join(map(str, valor)))

    def set_save_binary_data(self, data):
        """
            Save result data to a file
        """
        with open(self.file_name_save, 'w', encoding="utf-8") as file:
            file.write(" ".join(self.title) + "\n")
            for valor in data:
                file.write(" ".join(map(str, valor)) + "\n")

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
            binary_data = self.get_binary_data(file_data)
            self.set_print_binary_data(binary_data)
            self.set_save_binary_data(binary_data)
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
