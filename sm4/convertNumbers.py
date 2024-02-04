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


    def decimal_to_binary(self, number, bits = 32):
        """
            Convert integer numbers to binary
        """
        if number == 0:
            return '0'

        result = ['0'] * bits
        is_negative = number < 0

        if is_negative:
            number = 2 ** bits + number

        for i in range(bits - 1, -1, -1):
            if number >= 2 ** i:
                result[bits - i - 1] = '1'
                number -= 2 ** i

        result_str  = ''.join(result)

        if not is_negative:
            result_str = result_str.lstrip('0') or '0'

        return result_str


    def decimal_to_hexadecimal(self, number, bits = 32):
        """
            Convert integer numbers to hexadecimal
        """
        if number == 0:
            return '0'

        result = ['0'] * bits
        is_negative = number < 0

        if is_negative:
            number = 2 ** bits + number

        first_bit = True
        for i in range(bits - 1, -1, -1):
            if number >= 2 ** i:
                result[bits - i - 1] = '1'
                number -= 2 ** i
                first_bit = False

        result_str = ''.join(result[32 - len(result) + first_bit:])

        # Remove leading zeros in positive integers
        if not is_negative:
            result_str = result_str.lstrip('0') or '0'

        hex_result = hex(int(result_str, 2))[2:]

        return hex_result.upper()


    def get_binary_data(self, data):
        """
            Calculate all statistical data
        """
        results = []
        for num in data:
            data = None
            try:
                number = int(num)
                binary = self.decimal_to_binary(number)
                hexadecimal = self.decimal_to_hexadecimal(number)
                data = [number, binary, hexadecimal]
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
