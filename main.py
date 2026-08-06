import scanner as sc
import keyboard as kb

qr = sc.Scanner()
face = sc.Scanner()


def main():
    qr.scan_qr_code()

    if qr.scan_qr_code():
        qr.kill()
        face.scan_face()
        return

    if face.scan_face():
        pass
        # Record attendance
        return


def kill():
    qr.kill()
    face.kill()


main()
kb.add_hotkey("q", kill())
