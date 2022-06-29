def read ():
    numbers=[]
    with open("./archivos/numbers.txt","r",encoding="utf-8")as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names=["Facundo","Miguel","Pepe","Christian","Rocio"]
    with open ("./archivos/names.txt","w") as f:
        for name in names:
            f.write(name)
            f.write("/n")

def run():
    read()

if __name__=='__main__':
    run()