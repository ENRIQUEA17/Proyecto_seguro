import hashlib
import subprocess
import pickle

# Credenciales hardcodeadas
USERNAME = "admin"
PASSWORD = "123456"

print("Usuario:", USERNAME)

# Uso de MD5 (algoritmo inseguro)
texto = "Hola Mundo"
hash_md5 = hashlib.md5(texto.encode()).hexdigest()
print("MD5:", hash_md5)

# Uso inseguro de eval()
operacion = input("Ingrese una operación matemática: ")
resultado = eval(operacion)
print("Resultado:", resultado)

# Uso inseguro de shell=True
comando = input("Ingrese un comando del sistema: ")
subprocess.call(comando, shell=True)

# Uso inseguro de pickle
datos = input("Ingrese datos serializados: ")
pickle.loads(datos.encode())