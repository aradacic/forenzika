import magic
import glob
filenames = glob.glob("Dokaz_1/*")

for filename in filenames:
    print(filename, magic.from_file(filename))
    print(magic.from_buffer(open(filename, "rb").read(2048)))
