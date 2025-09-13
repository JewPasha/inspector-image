from PIL import Image, ExifTags
class ImageInspect:
    __imagePath = ""
    def __init__(__self__, imagePath):
        __self__.__imagePath = imagePath
    
    def decodeMessage(__self__):
        with open(__self__.__imagePath, "rb") as file:
            jpeg_content = str(file.read()).replace("\\n", "\n")
        # Find the start and end positions of the PGP public key block
        start_marker = "-----BEGIN PGP PUBLIC KEY BLOCK-----"
        end_marker = "-----END PGP PUBLIC KEY BLOCK-----"
        start_index = jpeg_content.find(start_marker)
        end_index = jpeg_content.find(end_marker)
        # Extract the PGP public key block if found
        if start_index != -1 and end_index != -1:
            pgp_public_key_block = jpeg_content[start_index:end_index + len(end_marker)]
            print(pgp_public_key_block)
        else:
            print("PGP public key block not found.")
    
    def getImageLocation(__self__):
        img = Image.open(__self__.__imagePath)
        exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
        # latitude and longitude calculation sum([element / 60 ** index])
        latitude = sum(list(map(lambda i, j:
            float(i) / 60 ** j, # callback function
            str(exif['GPSInfo'][2])[1:len(str(exif['GPSInfo'][2]))-2].split(","), # list of elements pre calculation [degrees, minutes, seconds]
            range(3) # list of indexes
        )))
        longitude = sum(list(map(lambda i, j:
            float(i) / 60 ** j,
            str(exif['GPSInfo'][4])[1:len(str(exif['GPSInfo'][4]))-2].split(","),
            range(3)
        )))
        
        print(f"Lat/Lon:\t({round(latitude, 5)}) / ({round(longitude, 5)})")