import qrcode
from PIL import Image, ImageChops, ImageEnhance
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import ImageColorMask
from qrcode.image.styles.moduledrawers import (
    CircleModuleDrawer,
    SquareModuleDrawer,
    RoundedModuleDrawer,
)


def generate_basic_qr_code(website, output_path):
    """
    Generate a basic QR code with the provided website link.

    :param website: The website URL for the QR code.
    :param output_path: Output path to save the QR code image.
    :return: The generated QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(website)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)
    return img


def generate_qr_code_with_background(website, logo_path, output_path):
    """
    Generate a QR code with a background image and the provided website.

    :param website: The website URL for the QR code.
    :param logo_path: Path to the logo image.
    :param output_path: Output path to save the QR code image.
    :return: The generated QR code image.
    """
    img_bg = Image.open(logo_path)
    qr = qrcode.QRCode(box_size=5)
    qr.add_data(website)
    qr.make()
    img_qr = qr.make_image()
    pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])
    img_bg.paste(img_qr, pos)
    img_bg.save(output_path)
    rgb_img = img_bg.convert("RGB")
    return rgb_img


def generate_qr_code_with_colormask(website, logo_path, output_path):
    """
    Generate a QR code with a color mask using the provided website and logo.

    :param website: The website URL for the QR code.
    :param logo_path: Path to the logo image.
    :param output_path: Output path to save the QR code image.
    :return: The generated QR code image.
    """
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(website)
    qr_img = qr.make_image(
        image_factory=StyledPilImage,
        color_mask=ImageColorMask(color_mask_path=logo_path),
    )
    qr_img.save(output_path)
    return qr_img


def generate_custom_styled_qr_code(website, logo_path, output_path):
    """
    Generate a custom styled QR code with transparency and a background gradient.

    :param website: The website URL for the QR code.
    :param logo_path: Path to the logo image.
    :param output_path: Output path to save the QR code image.
    :return: The generated QR code image.
    """
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(website)
    qr.make(fit=True)
    qr_code_img = qr.make_image(fill_color="white", back_color="black")

    gradient = Image.new("RGB", qr_code_img.size, (17, 13, 53))  # Gradient color
    blended_image = ImageChops.blend(gradient, qr_code_img, alpha=0.5)

    logo = Image.open(logo_path)
    logo_with_transparency = logo.copy()
    enhancer = ImageEnhance.Brightness(logo_with_transparency)
    logo_with_transparency = enhancer.enhance(0.7)  # Adjust transparency

    qr_width, qr_height = qr_code_img.size
    logo_width, logo_height = logo_with_transparency.size
    position = ((qr_width - logo_width) // 2, (qr_height - logo_height) // 2)

    blended_image.paste(logo_with_transparency, position, logo_with_transparency)

    blended_image.save(output_path)
    return blended_image


def generate_qr_code_with_custom_position(website, logo_path, output_path, position):
    """
    Generate a QR code with a custom position for the logo.

    :param website: The website URL for the QR code.
    :param logo_path: Path to the logo image.
    :param output_path: Output path to save the QR code image.
    :param position: Custom position tuple (x, y) for the logo.
    :return: The generated QR code image.
    """
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(website)
    qr.make(fit=True)
    qr_code_img = qr.make_image(fill_color="white", back_color="black")

    logo = Image.open(logo_path)
    logo_with_transparency = logo.copy()
    enhancer = ImageEnhance.Brightness(logo_with_transparency)
    logo_with_transparency = enhancer.enhance(0.7)  # Adjust transparency

    qr_width, qr_height = qr_code_img.size
    logo_width, logo_height = logo_with_transparency.size

    qr_code_img.paste(logo_with_transparency, position, logo_with_transparency)

    qr_code_img.save(output_path)
    return qr_code_img
