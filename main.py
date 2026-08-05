import scanner as scan
import keyboard as kb

qr = scan.Scanner()
face = scan.Scanner()
def main():
    # scanner.scan_qr_code()
    face.scan_face()
    # if scanner.scan_qr_code():
    #     # scanner.kill()
    #     scanner.scan_face()

   #  if kill():
   #      scanner.kill()

def kill() -> bool:  
    return True

if kill:
    face.kill()
    

main()
kb.add_hotkey('q', kill)
kb.wait('esc') # exit or terminate program