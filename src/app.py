from importlib.resources import path
import sys  
import os.path
import os

import ebook
import tts


def help_text():
    print(""" Usage:
    > ebook_to_audio <ebook.pub> [output.mp3]
      - input parameter is mandatory and only supoprts epub for now
      - output parameter is options. In case of absence will be generated an mp3 file based on the input file name
--------------------
    """)


if __name__ == '__main__':

    if len(sys.argv) < 2:
        help_text()
        sys.exit(0)

    ebook_file = sys.argv[1]
    if ebook_file == '-help' or ebook_file == '--help' or ebook_file == '-h':
        help_text()
        sys.exit(0)

    if not os.path.exists(ebook_file):
        print('the file {} does not exists'.format(ebook_file))
        sys.exit(1)

    output_file = ''
    if len(sys.argv) > 2:
        output_file = sys.argv[2]        
    
    if output_file == '':
        output_file = ebook_file + '.mp3'
        name, ext = os.path.splitext(output_file)
        if ext != '.mp3':
            output_file = output_file + '.mp3'

    

    # load ebook
    book = ebook.load_ebook(ebook_file)
    text = ebook.extract_text(book.chapters)
    tts.text_to_audio(text, output_file)
    print('finished!')



