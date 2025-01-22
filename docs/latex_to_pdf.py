from pdflatex import PDFLaTeX

pdfl = PDFLaTeX.from_texfile("C:/Users/19831301/Desktop/pm_documentation/sberpm/docs/doc/latex/sberpm.tex")
pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)