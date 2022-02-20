# JSON

```python
JSON = Javascript Object Notation
```

- [JSON](#json)
  - [Que es JSON](#que-es-json)
  - [JSON en Python](#json-en-python)
    - [De JSON a Pyhton (json -> dict)](#de-json-a-pyhton-json---dict)

<hr>

## Que es JSON
- Es un formato para reprensentar datos 
- Es usado ampliamente por APIs y para representar configuraciones.
- Es facil de leer, pesa poco y es facil de escribir.

Con JSON se pueden representar diferentes tipos de datos: 

- Strings 
- Numeros 
- Booleanos
- Null
- Arreglos 
- Objetos

La estructura de un archivo JSON es:

```json
{
    "key" : "value",
    "Nombre" : "Santiago",
    "Años" : "84"
}
```

## JSON en Python 

Los tipos de datos que se representan en Python deben ser convertidos a JSON
por medio de metodos incluidos en la libreria json

### De JSON a Pyhton (json -> dict)

```python
import json
  
# JSON strinAg
employee = '{"id":"09", "name": "Nitin", "department":"Finance"}'
  
# Convert string to Python dict
employee_dict = json.loads(employee)
print(employee_dict)
print(type(employee_dict))
print("\n")
  
# Convert Python dict to JSON
json_object = json.dumps(employee_dict, indent=4)
print(json_object)
print(type(json_object))
```








