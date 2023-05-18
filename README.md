# Genome Informatics for Evolutionary Immunology (GI4EI)

An ISM under Dr. Rintu Kutum

[https://docs.google.com/document/d/1eOEItP3G_WcbvD_11t1aMJ-VEWK0_KFQ_rTvyGLv4Cg/edit](https://docs.google.com/document/d/1eOEItP3G_WcbvD_11t1aMJ-VEWK0_KFQ_rTvyGLv4Cg/edit)

---

The repository contains the pdf of my Final Report for this ISM, alongwith a FastQC report of an extract of a `fastq` file called `ext.fastq` (due to size constraints).

The final report contains:

- An introduction to Next Generation Sequencing Technologies
- An overview of RNA-sequencing
- Appendix containing the following work done as part of the ISM:
    - Weekly reports
    - Presentations

## Codefile Descriptions

Everything is written in python

---

`qmatrix.py`

Input a `fastq` file to generate a score matrix from the ASCII characters in the file while implementing necessary checks. 
The x-axis in the matrix corresponds to the base position, y-axis to the read number.

`box_whisper.py`

Recreate the per base sequence quality report as seen in a FastQC report in python. Given a `fastq` file, generate the corresponding box_whisper plot as close as possible to that in the fastqc report. The plot contains a boxplot, a median line, and a striped background. The ends of boxes denote the first and third quartiles; the red line shows the median and the whiskers denote the range.

`plots.py`

a few plots as required by Dr. Rintu, plotting to the quality scores at a given position corresponding to the data in the score matrix