import os
import shutil
import markdown

if os.path.exists('output'):
    shutil.rmtree('output')

shutil.copytree('static', 'output')

top_file = open('layout/top.html', "r")
top_content = top_file.read()

bottom_file = open('layout/bottom.html', "r")
bottom_content = bottom_file.read()

for root, dirs, files in os.walk('content'):
    path = root.split(os.sep)
    for file in files:
        filename = os.fsdecode(file)

        full_file_path = os.path.join(root, filename)
        output_path = full_file_path.replace('.md', '.html').replace('.markdown', '.html').replace('content/', 'output/')

        if filename.endswith(".md") or filename.endswith(".markdown"):
            reading_file = open(full_file_path, "r")
            file_content = reading_file.read()
            reading_file.close()
            formatted_content = markdown.markdown(file_content)

            print(full_file_path + " as " + output_path)

            if not os.path.exists(output_path):
                os.makedirs(output_path.replace('/' + file.replace('.md', '.html').replace('.markdown', '.html'), ''), exist_ok=True)

            output_file = open(output_path, "w+")

            output_file.write(top_content + formatted_content + bottom_content)
            output_file.close()
        else:
            reading_file = open(full_file_path, "r")
            file_content = reading_file.read()
            reading_file.close()

            if not os.path.exists(output_path):
                os.makedirs(output_path.replace('/' + file.replace('.md', '.html').replace('.markdown', '.html'), ''), exist_ok=True)

            output_file = open(output_path, "w+")

            output_file.write(top_content + file_content + bottom_content)
            output_file.close()

print("Everything should be finished now. Enjoy your website!")