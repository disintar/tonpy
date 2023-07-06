import os

if __name__ == "__main__":
    dst = os.listdir('dist')
    for file in dst:
        for tag in ['linux_x86_64', 'universal2', 'linux_aarch64']:
            if tag in file:
                os.rename(f"dist/{file}", f'dist/{file.replace(tag, os.getenv("TAG_FIX"))}')
