import os

if __name__ == "__main__":
    dst = os.listdir('dist')
    for file in dst:
        if 'linux_x86_64' in file:
            os.rename(f"dist/{file}", f'dist/{file.replace("linux_x86_64", "manylinux2014_x86_64")}')
