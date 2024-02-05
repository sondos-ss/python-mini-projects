import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

def encoder(data,output_path):
    """
    Encode data into a QR code and save it as an image.
    """
    qr =qrcode.QRCode(
        version=1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)



def decoder(image_path):
    """
    Decode a QR code image and return the decoded data.
    """
    img= Image.open(image_path)
    
    decoded_data = decode(img)
    return decoded_data





if __name__ == "__main__":
    data="Hello, this is QR code example!"
    output_path ="output/qrcode1.png"

    encoder(data, output_path)
    print(f"QR Code encoded and saved at {output_path}")

    
    decoded_data = decoder(output_path)
    print(f"Decoded data: {decoded_data}")
