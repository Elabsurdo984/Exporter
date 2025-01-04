import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def csv_to_pdf(input_file, output_file):
    """
    Convierte un archivo CSV a formato PDF.
    
    :param input_file: Ruta del archivo CSV
    :param output_file: Ruta donde se guardará el archivo PDF
    """
    df = pd.read_csv(input_file)
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    # Definir la posicion inicial de la tabla
    x = 40
    y = height - 40

    # Definir el ancho de las columnas
    column_widht = 100

    # Dibujar las cabeceras de la tabla
    for col in df.columns:
        c.drawString(x, y, str(col))
        x += column_widht
    
    y -= 20 # Mover hacia abajo para los datos

    # Dibujar las filas de la tabla
    for index, row in df.iterrows():
        x = 40
        for value in row:
            c.drawString(x, y, str(value))
            x += column_widht
        
        y -= 20
        if y < 40: # Si la pagina esta llena, añadir una nueva
            c.showPage()
            y = height - 40
    
    c.save()