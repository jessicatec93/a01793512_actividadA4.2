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


    def decimal_to_binary(self, numero, bits = 10):
        """
            Convert integer numbers to binary
        """
        if numero == 0:
            return '0'

        resultado = ['0'] * bits
        es_negativo = numero < 0

        if es_negativo:
            numero = 2 ** bits + numero

        for i in range(bits - 1, -1, -1):
            if numero >= 2 ** i:
                resultado[bits - i - 1] = '1'
                numero -= 2 ** i

        resultado_str  = ''.join(resultado)

        if not es_negativo:
            resultado_str = resultado_str.lstrip('0') or '0'

        return resultado_str


    def decimal_to_hexadecimal(self, numero, bits = 32):
        """
            Convert integer numbers to hexadecimal
        """
        if numero == 0:
            return '0'

        resultado = ['0'] * bits
        es_negativo = numero < 0

        if es_negativo:
            numero = 2 ** bits + numero

        primer_bit = True
        for i in range(bits - 1, -1, -1):
            if numero >= 2 ** i:
                resultado[bits - i - 1] = '1'
                numero -= 2 ** i
                primer_bit = False

        resultado_str = ''.join(resultado[32 - len(resultado) + primer_bit:])

        # Remove leading zeros in positive integers
        if not es_negativo:
            resultado_str = resultado_str.lstrip('0') or '0'

        hex_resultado = hex(int(resultado_str, 2))[2:]

        return hex_resultado.upper()


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
