![green_office](https://github.com/user-attachments/assets/3ee7fda1-87f8-49f7-8684-41d06ce01854)
# EDA_Health

¿Cómo se relaciona la exposición a zonas verdes con nuestra salud física y mental?
Las hipotesis a demostrar son:
H1: Más acceso universal a zonas verdes equivale a una mejor salud mental
H2: Mejor calidad del aire (menor PM2.5) equivale a una mejor salud física

En este proyecto se demuestra que la mayor disponibilidad de zonas verdes en tu ciudad contribuye a tu bienestar y salud mental.

Datos utilizados:
| Fuente                       | Variables clave                                                          | Cobertura                              |
| ---------------------------- | ------------------------------------------------------------------------ | -------------------------------------- |
| ESS (European Social Survey) | Salud física (w3hq58), mental (w3hq57), felicidad (w3xq1), regiones NUTS | 10.179 encuestas, 28 regiones europeas |
| ISGlobal HUDI 2022           | Acceso a zonas verdes, PM2.5 (Air quality), NO2          | 528 ciudades europeas                  |
| NDVI/Green2022               | NDVI medio, % población sin verde suficiente                             | 516 ciudades                           |

No podemos modificar toda nuestra ciudad, pero quizás sí los entornos en los que trabajamos. Una mejor salud mental nos hace disfrutar más de nuestro trabajo y ser más productivos.

En este estudio se correlaciona la disponibilidad de zonas verdes con la salud física y mental, con especial énfasis en la salud mental. Además de estudiar la salud auto percibida en comparación con la calidad del aire.

Hay una fuerte voluntad de ampliar este estudio, incluyendo más variables, y realizando un estudio más amplio, tanto a nivel localizado, como geograficamente hablando.

Este estudio sólo se ha realizado en una lista de 33 ciudades europeas, con datos estadísticos de la ESS (european social survey), y  los datos de ISglobalranking, que mide una serie de factores ambientales en las ciudades. Ambas organizaciones hacen un trabajo excepcional por registrar y detallar cómo nos sentimos y lo que nos rodea, en entornos tan complejos como son las grandes metropolis.

En este estudio se aprecia que a pesar de que la salud en general, y la salud mental en particular, es algo completamente multifactorial y tremendamente complejo. A pesar de las dificultades que nos plantea la sociedad para expresar nuestros posibles trastornos. 

A pesar de todas estas circunstancias, se puede demostrar una correlación clara entre la salud mental y la disponibilidad de zonas verdes.


<img width="1483" height="1184" alt="scatter2" src="https://github.com/user-attachments/assets/65b22920-aa71-4d56-bda3-ef2e041f25ce" />



## Requisitos

Ver requirements.txt

## Instalación

```bash
# Clonar el repositorio
git clone [https://github.com/<tu-usuario>/EDA_Health.git](https://github.com/PabloGlu/EDA_Health)
cd EDA_Health

# Crear y activar entorno virtual (PowerShell en Windows)
py -V:Astral/CPython3.13.12 -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
python -m pip install -r requirements.txt
```

## Uso

- Abrir el proyecto en VS Code.
- Seleccionar el intérprete `.venv`.
- Ejecutar la memoria.

## Estructura de carpetas

- `data/` – datos brutos. En este caso no se ha subido nada pues los datos son muy pesados.
- `src/` – código Python reutilizable, la memoria tiene todo el código
- `requirements.txt` – dependencias del proyecto.


Pablo da Cunha
The Bridge Data Science Bootcamp - Madrid, España
