FROM ubuntu:22.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install software-properties-common -y
RUN apt-get install build-essential cmake wget -y
RUN apt-get update -y
RUN apt-get install python-is-python3
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip
RUN pip install --index-url https://test.pypi.org/simple/ --no-deps latex-test-pakholkov-package\
RUN yes | apt-get install texlive-latex-base
RUN pip install pdflatex
RUN mkdir working
RUN mkdir images

WORKDIR /working
RUN wget https://imgs.search.brave.com/6Gr3bxUYy9-IGboKL8o_hAQuK8X9FZpA97y65Gsgmkg/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/aXRwcm90b2RheS5j/b20vc2l0ZXMvaXRw/cm90b2RheS5jb20v/ZmlsZXMvc3R5bGVz/L2FydGljbGVfZmVh/dHVyZWRfc3RhbmRh/cmQvcHVibGljL2Rv/Y2tlci5qcGc_aXRv/az1vRmpJMEU5cQ
RUN mv docker.jpg /images
RUN python pdf_generate.py