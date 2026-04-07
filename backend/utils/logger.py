def logger(step , data=None):
    print(f"Step: {step}")
    if data is not None:
        print(f"Data: {data}")

def file_logger(step , data=None):
    with open("results.txt", "a") as f:
        if step == "Start":
            f.write("\n" + "="*80 + "\n\n")
        f.write(f"Step: {step}\n")
        if data is not None:
            f.write(f"Data: {data}\n")