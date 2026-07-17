import sys

SILENT_MODE = False

def set_silent_mode(silent: bool):
    global SILENT_MODE
    SILENT_MODE = silent

def logger(step , data=None):
    if SILENT_MODE:
        return
    try:
        print(f"Step: {step}")
        if data is not None:
            print(f"Data: {data}")
    except UnicodeEncodeError:
        try:
            enc = sys.stdout.encoding or 'utf-8'
            safe_step = str(step).encode(enc, errors='replace').decode(enc)
            print(f"Step: {safe_step}")
            if data is not None:
                safe_data = str(data).encode(enc, errors='replace').decode(enc)
                print(f"Data: {safe_data}")
        except Exception:
            pass

def file_logger(step , data=None):
    try:
        with open("results.txt", "a", encoding="utf-8") as f:
            if step == "Start":
                f.write("\n" + "="*80 + "\n\n")
            f.write(f"Step: {step}\n")
            if data is not None:
                f.write(f"Data: {data}\n")
    except Exception:
        pass