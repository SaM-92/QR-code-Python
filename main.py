from subs.functions_QRC import *


# Example usage:

# Define the website URL and paths for logos and output images


# link to the website
website = "https://t.me/DataMasterMind"

# logo
logo_path = "./Logos/logo-1.png"

# outputs
output_path_1 = "./QR_Codes/Ex-1.png"
output_path_2 = "./QR_Codes/Ex-2.png"
output_path_3 = "./QR_Codes/Ex-3.png"
output_path_4 = "./QR_Codes/Ex-4.png"
output_path_5 = "./QR_Codes/Ex-5.png"

# Generate a basic QR code
img_1 = generate_basic_qr_code(website, output_path_1)

# Generate a QR code with a background image
img_2 = generate_qr_code_with_background(website, logo_path, output_path_2)

# Generate a QR code with a color mask
img_3 = generate_qr_code_with_colormask(website, logo_path, output_path_3)

# Generate a QR code with a custom logo overlay
img_4 = generate_qr_code_with_custom_position(website, logo_path, output_path_4)

# Generate a custom styled QR code with transparency and gradient background
img_5 = generate_custom_styled_qr_code(website, logo_path, output_path_5)
