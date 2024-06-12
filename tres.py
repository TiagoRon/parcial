from Jedi import jedis

def clave_jedi(jedi):
    return jedi['name'], jedi['species']

def ordenar_jedis():
    jedis_ordenados = sorted(jedis, key=clave_jedi)
    print("Jedis ordenados:")
    for jedi in jedis_ordenados:
        print(f"Nombre: {jedi['name']}, Especie: {jedi['species']}")

def obtener_info_jedi(nombre):
    for jedi in jedis:
        if jedi['name'] == nombre:
            print(f"Información de {nombre}: {jedi}")

def obtener_padawans(nombre_maestro):
    padawans = []
    for jedi in jedis:
        if jedi['master'] and nombre_maestro in jedi['master']:
            padawans.append(jedi['name'])
    print(f"Padawans de {nombre_maestro}: {padawans}")

def obtener_jedi_por_especie(especies):
    jedis_por_especie = []
    for jedi in jedis:
        if jedi['species'] == especies:
            jedis_por_especie.append(jedi['name'])
    print(f"Jedis de la especie {especies}: {jedis_por_especie}")

def obtener_jedi_comenzando_con(letra):
    jedis_comenzando_con = []
    for jedi in jedis:
        if jedi['name'].startswith(letra):
            jedis_comenzando_con.append(jedi['name'])
    print(f"Jedis cuyo nombre comienza con '{letra}': {jedis_comenzando_con}")

def obtener_jedi_con_multiples_colores_sable():
    jedis_con_multiples_colores = []
    for jedi in jedis:
        if jedi['lightsaber_color'] and '/' in jedi['lightsaber_color']:
            jedis_con_multiples_colores.append(jedi['name'])
    print(f"Jedis con múltiples colores de sable de luz: {jedis_con_multiples_colores}")

def obtener_jedi_con_color_sable(color):
    jedis_con_color = []
    for jedi in jedis:
        if jedi['lightsaber_color'] and color in jedi['lightsaber_color']:
            jedis_con_color.append(jedi['name'])
    print(f"Jedis con color de sable de luz {color}: {jedis_con_color}")

def obtener_jedi_por_rango(rango):
    jedis_por_rango = []
    for jedi in jedis:
        if jedi['rank'] == rango:
            jedis_por_rango.append(jedi['name'])
    print(f"Jedis con rango {rango}: {jedis_por_rango}")

ordenar_jedis()
obtener_info_jedi('Ahsoka Tano')
obtener_info_jedi('Kit Fisto')
obtener_padawans('Yoda')
obtener_padawans('Luke Skywalker')
obtener_jedi_por_especie('Human')
obtener_jedi_por_especie('Twi\'lek')
obtener_jedi_comenzando_con('A')
obtener_jedi_con_multiples_colores_sable()
obtener_jedi_con_color_sable('Yellow')
obtener_jedi_con_color_sable('Violet')
obtener_jedi_por_rango('Grand Master')
