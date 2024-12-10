### QR Code Generator

# Enter list to generate codes
# Choose color for the code
# Enter filename
# Save code as an image

import qrcode

def qr_code_generator():
    prompt_text = input("Enter a list of items separated by commas: ")
    prompt_text = prompt_text.split(",")
    total_items = len(prompt_text)
    
    prompt_filename = (input("Enter the base filename: "))
    prompt_color_1 = (input("Enter primary color: ")).lower()
    prompt_color_2 = (input("Enter secondary color: ")).lower()

    count_items = 0
    while (count_items < total_items):
        # Create a QR Code object
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code (1 is smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in pixels
            border=4,  # Thickness of the border (minimum is 4)
        )

        # Add data to the QR Code
        qr.add_data(prompt_text[count_items])
        qr.make(fit=True)

        # Create an image of the QR Code
        img = qr.make_image(fill_color=prompt_color_1, back_color=prompt_color_2)

        # Save the QR Code image
        img.save(f"{prompt_filename}_{count_items}.png")
        print(f"QR Code saved as '{prompt_filename}_{count_items}.png'")

        count_items += 1