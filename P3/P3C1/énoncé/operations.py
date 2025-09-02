def controler_nombres(nombres):
    for nombre in nombres:
        if type(nombre) == str and not str.isnumeric(nombre):
            print(f"Le nombre '{nombre}' est incorrect.")
            return False
    return True

def addition(a, b):
    if controler_nombres([a, b]):
        return round(float(a) + float(b))
        
def multiplication(a, b):
    if controler_nombres([a, b]):
        return round(float(a) * float(b))
