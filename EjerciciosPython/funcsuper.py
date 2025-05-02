def totalfin(preciototal,cantidad,precio,productollevado):
    codigosdeproductos={1:"papasfritas",2:"vinagre",3:"fosforos",4:"salsa de tomate",
                 5:"tallarines",6:"toalla nova",7:"cargador"}
    print("Usted lleva",codigosdeproductos[productollevado])
    return preciototal+cantidad*precio