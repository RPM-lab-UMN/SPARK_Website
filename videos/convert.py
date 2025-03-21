import os
import argparse

'''This converts from .mp4 to .gif'''
def convert(input_path, output_path):
    os.system(f'ffmpeg -i {input_path} -vf "fps=10,scale=320:-1:flags=lanczos" {output_path}')


def process_file(input_folder, output_folder, file):
        input_path = os.path.join(input_folder, file)
        
        output = file.split('-')[-1].replace('.mp4', '.gif')
        subfolder = output.split('_')[0]
        name = output.split('_')[1]
        extension = '.gif'
        output_path = os.path.join(output_folder, subfolder, name + extension)

        # make subfolder if it doesn't exist
        if not os.path.exists(os.path.join(output_folder, subfolder)):
            os.makedirs(os.path.join(output_folder, subfolder))

        print(f'Converting {input_path} to {output_path}')
        convert(input_path, output_path)

def copy_file(input_folder, output_folder, file):
    input_path = os.path.join(input_folder, file)

    output = file.split('-')[-1]
    subfolder = output.split('_')[0]
    name = output.split('_')[1]
    extension = '.mp4'
    output_path = os.path.join(output_folder, subfolder, name + extension)

    # make subfolder if it doesn't exist
    if not os.path.exists(os.path.join(output_folder, subfolder)):
        os.makedirs(os.path.join(output_folder, subfolder))

    print(f'Copying {input_path} to {output_path}')
    os.system(f'cp {input_path} {output_path}')

def main():
    parser = argparse.ArgumentParser(description='Converts videos to gifs')
    parser.add_argument('input_folder', type=str, help='Input folder')
    parser.add_argument('output_folder', type=str, help='Output folder')
    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder

    files = []
    for file in os.listdir(input_folder):
        if file.endswith('.mp4'):
            files.append(file)
            # print(file)

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in files:
        # process_file(input_folder, output_folder, file)
        copy_file(input_folder, output_folder, file)


    



if __name__ == '__main__':
    main()