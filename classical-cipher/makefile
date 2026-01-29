OPEN = start
PDF = del solutions.tex 2>nul & type nul > solutions.tex & \
    pdflatex --shell-escape -halt-on-error -interaction=nonstopmode -file-line-error $@.tex && \
    pythontex main.tex && \
    makeindex $@.idx && \
    pdflatex --shell-escape $@.tex && \
    $(OPEN) $@.pdf
LATEXRM = del main.aux main.ilg main.log main.idx main.ind main.out main.py.err main.py.out main.pytxcode 2>nul & \
           rmdir /s /q __pycache__ 2>nul & \
           del comment.cut comment.err comment.out latex.py 2>nul

main: 
	$(PDF)

c:
	$(LATEXRM)

v:
	$(OPEN) main.pdf
