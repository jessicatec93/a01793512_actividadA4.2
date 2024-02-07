"""
Alumno: Jessica Lechuga Ramos
Matrícula: A01793512

Calculation of profits.
"""
import json
import sys
import time

from typing import TypedDict

class salesJSON(TypedDict):
    SALE_ID: int
    SALE_Date: str
    Product: str
    Quantity: int

class productJSON(TypedDict):
    title: str
    type: str
    description: str
    filename: str
    height: int
    width: int
    price: float
    rating: int

class ComputeSales:
    """
    Class to perform operations from two files that have sales.
    """

    def __init__(self):
        self.start_time = time.time()
        self.elapsed_time = None
        self.decimal = 2
        self.decimal_time = 4
        self.file_name_save = "SalesResults.txt"


    def get_file_data(self, file_name):
        """
        Extracts the data from the given file and returns it in a dictionary
        """
        objeto_json = None
        with open(file_name, 'r', encoding="utf-8") as file:
            data = json.load(file)

        # Check if the first item in the list is sales or products
        if 'SALE_ID' in data[0]:
            try:
                objeto_json = {"sales": [salesJSON(**item) for item in data]}
            except ValueError as e:
                print("Error al procesar datos de ventas:", e)
        elif 'title' in data[0]:
            try:
                objeto_json = {"products": [productJSON(**item) for item in data]}
            except ValueError as e:
                print("Error al procesar datos de productos:", e)
        else:
            print("No se puede determinar el tipo de datos")

        return objeto_json


    def get_total_sales(self, data):
        """
            Bring sales totals
        """
        results = []
        totals = 0
        total = 0
        order = 0
        product_data = data["products"]
        sales_data = data["sales"]
        for sale_data in sales_data:
            if order != sale_data["SALE_ID"]:
                if order != 0:
                    results.append(["Total", round(total, self.decimal)])
                    total = 0
                order = sale_data["SALE_ID"]
                results.append(["\n" + sale_data["SALE_Date"], "Order", order])
            product = [product for product in product_data if product["title"] == sale_data["Product"]][0]
            price = product["price"] * sale_data["Quantity"]
            sale = [sale_data["Quantity"], sale_data["Product"], round(price, self.decimal)]
            results.append(sale)
            total += price
            totals += price
        results.append(["Total", round(total, self.decimal)])
        results.append(["\n\nTotal of all orders", round(totals, self.decimal)])
        return results


    def set_print_total_sales(self, data):
        """
            Print result data to a file
        """
        print("\nRESULTS")
        for valor in data:
               print(" ".join(map(str, valor)) + "\n")
        end_time = time.time()
        self.elapsed_time = end_time - self.start_time
        print(f"\nTime elapsed: {round(self.elapsed_time, self.decimal_time)} seconds\n")


    def set_save_total_sales(self, data):
        """
            Save result data to a file
        """
        with open(self.file_name_save, 'w', encoding="utf-8") as file:
            for valor in data:
                file.write(" ".join(map(str, valor)) + "\n")
            file.write(f"\n\nTime elapsed: {round(self.elapsed_time, self.decimal_time)} seconds\n")


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
            data = self.get_file_data(products_file_name)
            data.update(self.get_file_data(sales_file_name))
            total_sales = self.get_total_sales(data)
            self.set_print_total_sales(total_sales)
            self.set_save_total_sales(total_sales)
        except FileNotFoundError:
            print(f"Error: File '{products_file_name}' or '{sales_file_name}' not found.")
        except ValueError as e:
            print(e)


if __name__ == '__main__':
    compute_sales = ComputeSales()
    compute_sales.operation()