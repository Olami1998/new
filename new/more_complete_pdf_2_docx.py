from pdf2docx import Converter
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def pdf_to_docx(pdf_path, docx_path):
    """
    Converts a PDF file to a DOCX file using pdf2docx.
    
    Args:
        pdf_path (str): Path to the input PDF file.
        docx_path (str): Path to save the output DOCX file.
    """
    try:
        # Create a Converter object
        cv = Converter(pdf_path)

        # Convert the PDF to DOCX
        cv.convert(docx_path, start=0, end=None)  # Convert all pages
        cv.close()
        print(f"Successfully converted {pdf_path} to {docx_path}!")
    except Exception as e:
        print(f"An error occurred during PDF to DOCX conversion: {e}")

def docx_to_pdf(docx_path, pdf_path):
    """
    Converts a DOCX file to a PDF file.
    
    Args:
        docx_path (str): Path to the input DOCX file.
        pdf_path (str): Path to save the output PDF file.
    """
    try:
        # Read the DOCX file
        document = Document(docx_path)
        c = canvas.Canvas(pdf_path, pagesize=letter)

        # Add text from DOCX to PDF
        y = 750  # Starting y-position for text
        for para in document.paragraphs:
            if para.text.strip():  # Skip empty paragraphs
                c.drawString(50, y, para.text)
                y -= 12  # Move to the next line
                if y < 50:  # Add a new page if the current page is full
                    c.showPage()
                    y = 750

        # Save the PDF file
        c.save()
        print(f"Successfully converted {docx_path} to {pdf_path}!")
    except Exception as e:
        print(f"An error occurred during DOCX to PDF conversion: {e}")

def get_output_path(input_path, target_extension):
    """
    Generates the output file path in the same folder as the input file,
    with the same name but a different extension.
    
    Args:
        input_path (str): Path to the input file.
        target_extension (str): The desired file extension (e.g., ".docx" or ".pdf").
    
    Returns:
        str: The output file path.
    """
    # Get the directory and base name of the input file
    directory = os.path.dirname(input_path)
    base_name = os.path.splitext(os.path.basename(input_path))[0]

    # Create the output file path
    output_path = os.path.join(directory, f"{base_name}{target_extension}")
    return output_path

def get_user_input():
    """
    Prompts the user to input the file path and conversion type.
    """
    # Ask for the file path
    file_path = input("Enter the path of the file you want to convert: ").strip()

    # Check if the file exists
    if not os.path.exists(file_path):
        print("Error: The file does not exist. Please check the path and try again.")
        return

    # Ask for the conversion type
    conversion_type = input("Choose the conversion type (1 for PDF to DOCX, 2 for DOCX to PDF): ").strip()

    # Perform the conversion based on user input
    if conversion_type == "1":
        if not file_path.lower().endswith(".pdf"):
            print("Error: The input file must be a PDF for this conversion.")
            return
        output_path = get_output_path(file_path, ".docx")
        pdf_to_docx(file_path, output_path)
    elif conversion_type == "2":
        if not file_path.lower().endswith(".docx"):
            print("Error: The input file must be a DOCX for this conversion.")
            return
        output_path = get_output_path(file_path, ".pdf")
        docx_to_pdf(file_path, output_path)
    else:
        print("Error: Invalid conversion type. Please choose 1 or 2.")

# Main program
if __name__ == "__main__":
    print("Welcome to the File Converter!")
    get_user_input()