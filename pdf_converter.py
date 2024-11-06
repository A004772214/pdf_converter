from unstructured.partition.pdf import partition_pdf
import datetime
import os

start_time = datetime.datetime.now()

ca_pdf_path = "Your_file_folder_path"

count = 0

for root, path, files in os.walk(ca_pdf_path):
    for file in files:
        file_name = ("US_" + str(file)).replace(".pdf", "")
        file_path = root + "//" + file
        txt_path = "Your_file_folder_path" + "//" + file_name + ".txt"

        print(file_path)

        try:
            elements = partition_pdf(file_path)

            element_text_list = []

            for element in elements:
                element_text_list.append(element.text + "\n" + "\n")

            with open(txt_path, "w+", encoding="utf-8", errors='ignore') as txt:
                txt.writelines(element_text_list)

        except Exception as e:
            with open(txt_path, "w+", encoding="utf-8", errors='ignore') as txt:
                txt.write(str(e))

end_time = datetime.datetime.now()

total_time = end_time - start_time

print(total_time)

