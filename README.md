# pdf_converter

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) 
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

This project utilizes the Python Unstructured library to extract and convert text content from PDF files into plain text format. It simplifies the process of transforming unstructured text data within PDFs into a more accessible and analyzable form, making it ideal for applications in data analysis, text processing, and natural language processing (NLP) tasks.

---

## Table of Contents

- [About the Project](#about-the-project)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [Contact](#contact)

---

## About the Project

This project utilizes the Python Unstructured library to efficiently extract and convert text content from PDF documents into plain text format. By leveraging this library, the project aims to simplify the processing and analysis of PDF data, enabling users to easily access and manipulate unstructured text data.  
In addition to text extraction, the project can handle various PDF layouts and structures, preserving the original text formatting as much as possible. This is particularly useful for tasks like data analysis, text mining, or further processing with natural language processing (NLP) tools..

### Prerequisites

Required python libraries: unstructured, pandas, re, numpy, os  
Python version: 3.11

### Installation

Step-by-step instructions to install the project:

```bash
# Clone the repository
git clone https://github.com/A004772214/pdf_converter.git

# Navigate to the project directory
cd pdf_converter

# Install dependencies
pip install -r requirements.txt
```

### Usage

Instructions on how to use the project:
```python

**Import necessary blocks**
from unstructured.partition.pdf import partition_pdf
import datetime
import os


**Example usage**
# Replace with your file folder path
start_time = datetime.datetime.now()
ca_pdf_path = "Your_file_folder_path"

# Replace with your file folder path
for root, path, files in os.walk(ca_pdf_path):
    for file in files:
        file_name = ("US_" + str(file)).replace(".pdf", "")
        file_path = root + "//" + file
        txt_path = "Your_file_folder_path" + "//" + file_name + ".txt"

        print(file_path)
```
### Features

List of key features of the project:

- Data Preprocessing: Preparing text data for analysis or machine learning.
- Text Analysis and NLP: Converting PDF documents into a suitable format for sentiment analysis, summarization, and other NLP tasks.
- Document Management: Streamlining the extraction of readable text from reports, research papers, invoices, and other PDF files.

### Contributing

Instructions for contributing to the project:

**Fork the repository to your GitHub account**

**Clone your forked repository**  
git clone https://github.com/A004772214/pdf_converter.git

**Create a new branch for your changes**  
git checkout -b feature/YourFeatureName

**Make changes and commit**  
git add .  
git commit -m "Add YourFeatureName"

**Push your changes to GitHub**  
git push origin feature/YourFeatureName

**Open a pull request to the main repository**  

### Contact

Project Link: https://github.com/A004772214/pdf_converter
