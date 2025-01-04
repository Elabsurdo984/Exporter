from PIL import Image
from reportlab.pdfgen import canvas

def image_to_pdf(input_file, output_file):
    """
    Convierte una imagen a formato PDF.
    
    :param input_file: Ruta del archivo de imagen (.jpg, .png, etc.)
    :param output_file: Ruta donde se guardará el archivo PDF
    """

    img = Image.open(input_file)
    pdf_path = output_file

    # Usamos el metodo de Pillow para convertir la imagen a pdf
    img.save(pdf_path, 'PDF', resolution=100.0)