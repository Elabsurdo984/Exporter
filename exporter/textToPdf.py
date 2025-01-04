from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def text_to_pdf(input_file, output_file):
    """
    Convierte un archivo de texto a formato PDF.
    
    :param input_file: Ruta del archivo de texto (.txt)
    :param output_file: Ruta donde se guardará el archivo PDF
    """

    # Crear canvas para un pdf
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    y_position = height - 40 # Empezar a escribir cerca de la parte superior de la pagina
    for line in lines:
        c.drawString(40, y_position, line.strip())
        y_position -= 12 # Espacio entre lineas
        if y_position < 40:
            c.showPage()
            y_position = height - 40
    
    c.save()