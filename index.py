

from flask import Flask, render_template, request, send_file

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/cuadradosMedios')
def cuadradosMedios():
    return render_template('cuadradosMedios.html')

@app.route('/mediamm')
def mediamm():
    return render_template('mediamm.html')

@app.route('/imprimirCuadradosMedios')
def imprimirCuadradosMedios():
    return render_template('imprimirCuadradosMedios.html')

@app.route('/calcularCuadradosMedios', methods=['GET','POST'])
def calcularCuadradosMedios():
    n = request.form.get('numeroIteraciones', type=int)
    r = request.form.get('semilla', type=int)

    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from pandas import ExcelWriter
    from matplotlib import pyplot as plt
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure
    import io
    from io import BytesIO 
    import base64

    # n=100
    # r=23456 
    l=len(str(r))
    lista = []
    lista2 = []
    i=1
    while i <= n:
        x=str(r*r)
        if l % 2 == 0:
            x = x.zfill(l*2)
        else:
            x = x.zfill(l)
        y=(len(x)-l)/2
        y=int(y)
        r=int(x[y:y+l])
        lista.append(r)
        lista2.append(x)
        i=i+1  
    
    #Generador de Números Aleatorios Cuadrados Medios o CuadradosMedios
    df = pd.DataFrame({'X2':lista2,'Xi':lista})
    dfrac = df["Xi"]/10**l
    df['ri'] = dfrac

    buf = io.BytesIO()
    x1=df['ri']
    plt.plot(x1)
    plt.title('Generador de Números Aleatorios Cuadrados Medios')
    plt.xlabel('Serie')
    plt.ylabel('Aleatorios')
    fig = plt.gcf()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buf)
    fig.clear()
    plot_url = base64.b64encode(buf.getvalue()).decode('UTF-8')

    data= df.to_html(classes="table table-dark table-striped", justify="justify-all", border=0)

    

    return render_template('imprimirCuadradosMedios.html', data=data, image=plot_url)


@app.route('/congruencialLineal')
def congruencialLineal():
    return render_template('congruencialLineal.html')

@app.route('/imprimirCongruencialLineal')
def imprimirCongruencialLineal():
    return render_template('imprimirCongruencialLineal.html')

@app.route('/calcularCongruencialLineal', methods=['GET','POST'])

#calcularCongruencialLineal
def calcularCongruencialLineal():
    n = request.form.get("numeroIteraciones", type=int)
    x0 = request.form.get("semilla", type=int) 
    a = request.form.get("multiplicador", type=int)
    c = request.form.get("incremento", type=int)
    m = request.form.get("modulo", type=int)

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from pandas import ExcelWriter
    from matplotlib import pyplot as plt
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure
    import io
    from io import BytesIO 
    import base64

    #n, m, a, x0, c = 20,1000,101,4,457
    x = [1]*n
    r = [0.1]*n
    for i in range(0,n):
            x[i] = ((a*x0)+c) % m
            x0 = x[i]
            r[i] = x0/m
    df = pd.DataFrame({'Xn': x, 'ri':r})
    
    # Graficamos los numeros generados
    buf = io.BytesIO()
    plt.plot(r,marker='o')
    plt.title('Generador de Números Aleatorios Congruencial Lineal')
    plt.xlabel('Serie')
    plt.ylabel('Aleatorios')
    fig = plt.gcf()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buf)
    fig.clear()
    plot_url = base64.b64encode(buf.getvalue()).decode('UTF-8')

    data= df.to_html(classes="table table-dark table-striped", justify="justify-all", border=0)


    return render_template('imprimirCongruencialLineal.html', data=data, image=plot_url)


@app.route('/congruencialMultiplicativo')
def congruencialMultiplicativo():
    return render_template('congruencialMultiplicativo.html')

@app.route('/imprimirCongruencialMultiplicativo')
def imprimirCongruencialMultiplicativo():
    return render_template('imprimirCongruencialMultiplicativo.html')

@app.route('/calcularCongruencialMultiplicativo', methods=['GET','POST'])

#Generador de Números Aleatorios Congruencial Multiplicativo
def calcularCongruencialMultiplicativo():
    n = request.form.get("numeroIteraciones", type=int)
    x0 = request.form.get("semilla", type=int) 
    a = request.form.get("multiplicador", type=int)
    m = request.form.get("modulo", type=int)

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    from pandas import ExcelWriter
    from matplotlib import pyplot as plt
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure
    import io
    from io import BytesIO 
    import base64

    # n, m, a, x0 = 20, 1000, 747, 123
    x = [1] * n
    r = [0.1] * n
    for i in range(0, n):
     x[i] = (a*x0) % m
     x0 = x[i]
     r[i] = x0 / m
    d = {'Xn': x, 'ri': r }
    df = pd.DataFrame(data=d)

    buf = io.BytesIO()
    plt.plot(r,'g-', marker='o',)
    plt.title('Generador de Números Aleatorios Congruencial Multiplicativo')
    plt.xlabel('Serie')
    plt.ylabel('Aleatorios')
    fig = plt.gcf()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buf)
    fig.clear()
    plot_url = base64.b64encode(buf.getvalue()).decode('UTF-8')

    data= df.to_html(classes="table table-dark table-striped", justify="justify-all", border=0)


    return render_template('imprimirCongruencialMultiplicativo.html', data=data, image=plot_url)


@app.route('/calcularMediaModaMediana', methods=['GET','POST'])
def calcularMediaModaMediana():
    columna = request.form.get("nombreColumna")

    file = request.files['file'].read()

    # importamos la libreria Pandas, matplotlib y numpy que van a ser de mucha utilidad para poder hacer gráficos
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.backends.backend_agg import FigureCanvasAgg
    from matplotlib.figure import Figure
    import io
    from io import BytesIO 
    import base64
    from pandas import DataFrame

    # leemos los datos de la tabla del directorio Data de trabajo
    datos = pd.read_excel(file)
    #Presentamos los datos en un DataFrame de Pandas
    datos

    # Preparando para el grafico para la columna TOTAL PACIENTES
    buf = io.BytesIO()
    x=datos[columna]
    plt.figure(figsize=(10,5))
    plt.hist(x,bins=8,color='blue')
    plt.axvline(x.mean(),color='red',label='Media')
    plt.axvline(x.median(),color='yellow',label='Mediana')
    plt.axvline(x.mode()[0],color='green',label='Moda')
    plt.xlabel('Total de datos')
    plt.ylabel('Frecuencia')
    plt.legend()
    
    fig = plt.gcf()
    canvas = FigureCanvasAgg(fig)
    canvas.print_png(buf)
    fig.clear()
    plot_url = base64.b64encode(buf.getvalue()).decode('UTF-8')

    media = datos[columna].mean()
    moda = datos[columna].mode()
    mediana = datos[columna].median()
    
    df = pd.DataFrame(columns=('Media', 'Moda', 'Mediana'))
    df.loc[len(df)]=[media, moda, mediana] 
    df
    data = df.to_html(classes="table table-striped", justify="justify-all", border=0)

    # Tomamos los datos de las columnas
    df2 = datos[[columna]].describe()
    # describe(), nos presenta directamente la media, desviación standar, el valor mínimo, valor máximo, el 1er cuartil, 2do Cuartil, 3er Cuartil
    data2 = df2.to_html(classes="table table-dark table-striped", justify="justify-all", border=0)

    return render_template('imprimirMediaMedianaModa.html', data=data, data2=data2, image=plot_url)


if __name__ == '__main__':
    app.run(debug=True)