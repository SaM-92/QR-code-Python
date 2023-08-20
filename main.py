from subs.functions_QRC import *


# Example usage:

# the website you want the QRC to generate the image for
website = "https://t.me/DataMasterMind"

# Your logo
logo_path = "./Logos/logo-1.png"


# output path and output names for each function
output_path_1 = "./QR_Codes/Ex-1-teste.png"
output_path_2 = "./QR_Codes/Ex-2-qrc-with-backgrounds.png"
# output_path_3 = "./QR_Codes/Ex-3-colormask-qrcode.png"

# basic QRC
img_1 = generate_basic_qr_code(website, output_path_1)

# Creating a Simple QR Code with a Link on the Background Image
img_2 = generate_qr_code_with_background(website, logo_path, output_path_2)


# img_3 = generate_qr_code_with_colormask(website, logo_path, output_path_3)
