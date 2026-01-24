# Prologo
dia_1 = ["0", "515", "muerto"]
dia_2 = ["12", "559", "295", "10", "17", "527", "389", "30", "452", "292", 
         "387", "muerto"]
dia_3 = ["12", "559", "muerto"]
dia_4 = ["12", "559", "295", "10", "216", "573", "619", "47", "318", "15", 
         "460", "dormir"]
# Campaña
dia_5 = ["1", "75", "100", "137", "100", "556", "100", "454", "100", 
         "622", "100", "24", "dormir"]
dia_6 = ["1", "75", "100", "454", "370", "16", "151", "370", "334", "370", 
         "488", "370", "306", "370", "29", "370", "16", "36", "370", "571", 
         "370", "359", "407", "370", "388", "370", "183", "370", "16", "543", 
         "370", "100", "233", "380", "98", "233", "510", "233", "100", "622", 
         "100", "263", "100", "328", "100", "553", "612", "233", "380", "462", 
         "100", "57", "536", "147", "100", "622", "100", "536", "115", "100", 
         "622", "100", "24", "dormir"]
dia_7 = ["1", "75", "300", "620", "598", "594", "340", "285", "620", "300", 
         "162", "127", "46", "300", "112", "443", "112", "300", "497", "275", 
         "130", "275", "300", "298", "300", "220", "300", "636", "300", "545", 
         "300", "497", "245", "300", "162", "154", "300", "298", "300", "220", 
         "300", "24", "dormir"]
dia_8 = ["1", "75", "150", "62", "120", "333", "402", "120", "396", "120", 
         "150", "62", "120", "333", "352","120", "150", "62", "120", "333", 
         "584", "120", "150", "442", "150", "307", "66", "105", "66", "364", 
         "66", "555", "223", "315", "66", "110", "232", "66", "150", "184", 
         "150", "24", "dormir"]
dia_9 = ["1", "75", "150", "307", "244", "413", "66", "555", "476", "66", 
         "110", "270", "637", "66", "110", "76", "66", "110", "582", "66", 
         "105", "66", "364", "66", "150", "62", "120", "333", "584", "120", 
         "150", "498", "150", "200", "538", "200", "399", "607", "534", "200", 
         "525", "374", "200", "550", "200", "133", "156", "200", "24", "dormir"]
dia_10 = ["1", "75", "200"]


NODE_INFO = {
    # Terminal nodes
    "dormir": {"label": "A Dormir", "clue": ""},
    "muerto": {"label": "Dead end", "clue": ""},

    # Starting / unique nodes
    "0":  {"label": "0 \n Inicio",  "clue": ""},
    "1":  {"label": "1 \n Inicio",  "clue": ""},
    "24": {"label": "24 \n salida", "clue": ""},
    
    # Checkpoints / duplicates
    "75": {"label": "75 \n plaza de cronos", "clue": ""},
    "100": {"label": "100 \n Centro de la ciudad", "clue": ""},
    "150": {"label": "150 \n Arrabales Occidente", "clue": ""},
    "200": {"label": "200 \n Distrito Norte", "clue": ""},
    "300": {"label": "300 \n Distrito Sur", "clue": ""},
    "250": {"label": "250 \n Barrio Oriental", "clue": ""},

    # Other numeric nodes
    "137": {"label": "Node 137", "clue": "Intuición"},
    "334": {"label": "334 \n Puesto de comida", "clue": ""},
    "488": {"label": "488 \n Mensajería", "clue": "gastar pista: TEH"},
    "306": {"label": "306 \n Tienda de música", "clue": ""},
    "29":  {"label": "29  \n Papelería",  "clue": "gastar pista: PYR"},
    "571": {"label": "571 \n Carnicería", "clue": "bitec 30 creditos"},
    "407": {"label": "407 \n Tienda de electrónica", "clue": "comprar pistola térmica 100 creditos"},
    "388": {"label": "388 \n Comida", "clue": "comida 20 creditos"},
    "183": {"label": "183 \n Museo", "clue": "obtener baratija +50 creditos \n intuición obtener sable +2 cuerpo a cuerpo"},
    "543": {"label": "Node 543", "clue": "Obtener pista: NJA"},
    "510": {"label": "510 \n Oficina Alcalde David Malony", "clue": "gastar pista: MAL"},
    "263": {"label": "263 \n Agresor: 2", "clue": "obtener pista: temporal YUO"},
    "462": {"label": "462 ", "clue": "obtener pista: CHV"},
    # Nodes in days 7-10
    "598": {"label": "598 ", "clue": "gastar pista: NJA"},
    "594": {"label": "594", "clue": "roba urna tukusawa \n (mente 7)"},
    "285": {"label": "285", "clue": "gastar pista: CSG"},
    "127": {"label": "127 \n Agresor misterioso", "clue": "obtener pista: AMM"},
    "112": {"label": "112 \n Hospital", "clue": ""},
    "443": {"label": "443 \n Cura Mágica", "clue": "+4 vida"},
    "298": {"label": "298 \n Agresor: Escopeta", "clue": ""},
    "220": {"label": "220 \n Agencia de Autos", "clue": "1 auto 400 creditos"},
    "245": {"label": "245 \n Bomberos", "clue": "gastar pista: RAS"},
    "66":  {"label": "66 \n Obra Construcción",  "clue": "a las 11 am salvar al dentista ladrillazo"},
    "105": {"label": "105 \n Zona Industrial \n carro desguazado", "clue": "obtener +50 creditos gratis"},
    "364": {"label": "364", "clue": "gastar llave de hierro"},
    "223": {"label": "223 \n Almacen de la Dr. Watts", "clue": "taques de gas: risa/placer/sueño"},
    "498": {"label": "498 \n Tienda de Abarrotes", "clue": "matarratas \n herbicida \n llave inglesa \n linterna"},
    "607": {"label": "607 \n Departamentos lujosos", "clue": "sobornar al conserje 150 creditos"},
    "534": {"label": "534 \n Agresor: Conserje", "clue": " cuerpo 6/ vida 3"},
    "374": {"label": "374 \n Catedral", "clue": "+1 vida gratis"},
    "133": {"label": "133 \n Comisaría", "clue": ""},
}
