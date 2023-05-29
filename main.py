import xml.etree.ElementTree as ET
import os

# Mendefinisikan folder yang berisi file-file XML
folder_path = ''

# Mencari file output.xml dan menghapusnya jika sudah ada
output_file = os.path.join(folder_path, 'expected_result.xml')
if os.path.exists(output_file):
    os.remove(output_file)

# Mendapatkan daftar file XML dalam folder
xml_files = [file for file in os.listdir(folder_path) if file.endswith('.xml')]

# Membaca file XML pertama
tree1 = ET.parse(os.path.join(folder_path, xml_files[0]))
root1 = tree1.getroot()

# Menggabungkan elemen <transaction> dari file-file XML lainnya
for xml_file in xml_files[1:]:
    tree = ET.parse(os.path.join(folder_path, xml_file))
    root = tree.getroot()
    last_transaction_index = None
    for index, child in enumerate(root1):
        if child.tag == 'transaction':
            last_transaction_index = index
    for transaction in root.findall('transaction'):
        root1.insert(last_transaction_index + 1, transaction)
        last_transaction_index += 1

# Menyimpan hasil penggabungan ke dalam file baru
tree1.write(output_file)
