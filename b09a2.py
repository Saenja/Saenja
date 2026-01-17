#

from datetime import datetime

def check_file(file: str) -> int:
    # Notiz für Interessierte: eigentlich sollte man Dateien, die man öffnet, auch schließen (file.close()). Das machen
    # wir hier nicht um den Code einfach zu halten und weil der Code nicht produktiv eingesetzt wird.
    try:
        file = open(file, 'r')
        datetime.strptime(next(file), "%d.%m.%Y")
    except FileNotFoundError:
        return 1
    except StopIteration:
        return 2
    except ValueError:
        return 3
    except:
        return 4
    
    return 0

if __name__ == "__main__":
    print(check_file("valid.txt"))    # Soll 0 ausgeben
    print(check_file("missing.txt"))  # Soll 1 ausgeben
    print(check_file("empty.txt"))    # Soll 2 ausgeben
    print(check_file("invalid.txt"))  # Soll 3 ausgeben
