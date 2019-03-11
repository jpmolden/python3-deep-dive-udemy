
print(f"Running {__name__}.py")

# See if runing the import again will re-run module1
# if module1 is in sys modules already the code will not re-run!!
import module1

def hello():
    print("module2 says hello!\nand...")
    module1.hello()