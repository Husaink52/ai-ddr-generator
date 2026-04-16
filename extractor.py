import fitz  # PyMuPDF
import os

def extract_pdf_content(file_path, output_folder="extracted_images"):
    doc = fitz.open(file_path)
    full_text = []
    images = []

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for page_num, page in enumerate(doc):
        text = page.get_text()
        full_text.append(text)

        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            image_filename = f"{output_folder}/page{page_num+1}_img{img_index}.png"
            with open(image_filename, "wb") as f:
                f.write(image_bytes)

            images.append({
                "page": page_num + 1,
                "path": image_filename
            })

    return "\n".join(full_text), images