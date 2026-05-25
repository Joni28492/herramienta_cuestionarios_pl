from playwright.sync_api import sync_playwright # importante requiere tener playwright instalado = playwright install


# todo hacer para todos los tests
class HtmlToPdfConverter():
    
    def __init__(self):
        self.root_path = 'E:\\ESCRITORIO 2023\\OPOSICIONES\\desarrollo applicaciones\\asturpol-game\\src\\pages\\api\\tests\\db'


if __name__ == "__main__": 
    pass


# def html_to_pdf(html_file, output_pdf):

#     with sync_playwright() as p:

#         browser = p.chromium.launch()

#         page = browser.new_page()

#         page.goto(
#             f"file:///{html_file}",
#             wait_until="networkidle"
#         )

#         page.pdf(
#             path=output_pdf,
#             format="A4",
#             print_background=True
#         )

#         browser.close()


# html_to_pdf(
#     "template.html",
#     "tests/prueba.pdf"
# )