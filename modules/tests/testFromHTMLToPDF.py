from playwright.sync_api import sync_playwright # importante requiere tener playwright instalado = playwright install




def html_to_pdf(html_file, output_pdf):

    with sync_playwright() as p:

        browser = p.chromium.launch()

        page = browser.new_page()

        page.goto(
            f"file:///{html_file}",
            wait_until="networkidle"
        )

        page.pdf(
            path=output_pdf,
            format="A4",
            landscape=False,          # horizontal = True
            print_background=True,
            margin={
                "top": "10mm",
                "right": "10mm",
                "bottom": "10mm",
                "left": "10mm",
            },
            scale=0.85               # reduce si se corta
        )

        browser.close()


file = "_gozon_aux-02_solved"

html_to_pdf(
    f"html/{file}.html",
    f"pdfs/{file}.pdf"
)