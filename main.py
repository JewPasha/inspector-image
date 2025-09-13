from src.image_inspect import ImageInspect
import sys
def main(args):
    if len(args) != 3:
        print("The format to call the program is: <programName> -<option> <imageName>")
        return
    imageInspect = ImageInspect(args[2])
    callbackMap = {
        "-map": imageInspect.getImageLocation,
        "-steg": imageInspect.decodeMessage
    }
    val = callbackMap.get(args[1])
    if val:
        val()
if __name__ == "__main__":
    main(sys.argv)
