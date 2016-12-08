#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv 
 
class ProductosAnimales():
    # Empresa | Nombre Comercial del Producto | Numero de Regulacion | Forma Farmaceutica o Fisica
    data_list = []

    def __init__(self):
        pass
        
    def load_data(self):
        line = 1
        with open("data/listado_alimentos_vigentes.csv", "r") as file_open:
            data = csv.reader(file_open, delimiter=",")
            for row in data:
                if line > 1: 
                    self.data_list.append(row) 
                line += 1    

    def get_bussiness_list(self):
        bussiness_list = []
        for row in self.data_list:
            if row[0] not in bussiness_list: 
                bussiness_list.append(row[0])
        return bussiness_list

    def get_product_info_from(self, bussiness):
        product_info_list = []
        for row in self.data_list:  
            if bussiness == row[0]:  
                product_info_list.append(row)
        return product_info_list  