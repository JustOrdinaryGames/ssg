import os
import shutil
import markdown
from bs4 import BeautifulSoup

version = "1.0"

print("SSG v" + version)
print("---")

if os.path.exists('output'):
    shutil.rmtree('output')

# Create required directories (and files) if they don't exist
if not os.path.exists('layout'):
    os.mkdir('layout')

    top = open('layout/top.html', 'w')
    top.write("<html><head><title>SSG</title></head><body><header><h1>Your Website</h1></header><main>")
    top.close()

    bottom = open('layout/bottom.html', 'w')
    bottom.write("</main><footer><p>Created with SSG</p></footer></body>")
    bottom.close()
    print("Created layout folder, and empty files")

if not os.path.exists('static'):
    os.mkdir('static')
    print("Created static folder")

if not os.path.exists('components'):
    os.mkdir('components')
    example_component = open('components/example.html', 'w')
    example_component.write('<script>fetch("https://jsonplaceholder.typicode.com/posts").then(data => data.json()).then((data) => {document.getElementById(\'example\').innerHTML = "data[0]\'s title: " +data[0].title;})</script>')
    example_component.close()
    print("Created components folder")

if not os.path.exists('content'):
    os.mkdir('content')
    home_page = open('content/index.md', 'w')
    home_page.write('# Home\nYour website has been created! Edit the layout in ``layout/``, and edit the content in ``content/``.\n<component id="example"></component>')
    home_page.close()
    print("Created content folder")

# Copy all static files to the output folder
shutil.copytree('static', 'output')

# Get top & bottom file contents
top_file = open('layout/top.html', "r")
top_content = top_file.read()

bottom_file = open('layout/bottom.html', "r")
bottom_content = bottom_file.read()

# Loop through every file/folder inside of the content directory
for root, dirs, files in os.walk('content'):
    path = root.split(os.sep)
    for file in files:
        filename = os.fsdecode(file)

        full_file_path = os.path.join(root, filename)
        output_path = full_file_path.replace('.md', '.html').replace('.markdown', '.html').replace('content/', 'output/')

        # Create required directories for output file (ex: content/posts/test-post.md would need to create output/posts directory)
        if not os.path.exists(output_path):
            os.makedirs(output_path.replace('/' + file.replace('.md', '.html').replace('.markdown', '.html'), ''), exist_ok=True)
        
        # Get the current file, located in content/
        reading_file = open(full_file_path, "r")
        file_content = reading_file.read()
        reading_file.close()

        # Everything below here deals with writing the output file
        output_file = open(output_path, "w+")

        # Concatenate the top, content, and bottom sections (renders markdown as well)
        if filename.endswith(".md") or filename.endswith(".markdown"):
            formatted_content = markdown.markdown(file_content)
            output_file.write(top_content + formatted_content + bottom_content)
        else:
            output_file.write(top_content + file_content + bottom_content)
        
        output_file.close()

        print(full_file_path + " as " + output_path)

print("---")

# Loop through every file/folder inside of the output directory
for root, dirs, files in os.walk('output'):
    path = root.split(os.sep)
    for file in files:
        filename = os.fsdecode(file)
        full_file_path = os.path.join(root, filename)

        if filename.endswith(".html"):
            output_path = full_file_path.replace('.md', '.html').replace('.markdown', '.html').replace('content/', 'output/')

            # Get the current file
            reading_file = open(output_path, "r")
            reading_file_content = reading_file.read()
            reading_file.close()

            soup = BeautifulSoup(reading_file_content, features="html.parser")

            # Loop through every <component> tag, and append the content
            for tag in soup.find_all("component"):
                if tag.attrs['id'] != None:
                    tag_id = tag.attrs['id']

                    component_path = "components/" + tag_id + ".html"

                    if os.path.exists(component_path):
                        component_file = open(component_path, 'r')
                        component_content = component_file.read()
                        component_file.close()

                        new_tag = soup.new_tag(component_content)
                        tag.append(new_tag)
                        print("Found component: " + tag_id)
                    else:
                        tag.string ="A component named " + tag_id + " doesn't exist!"

                else:
                    tag.string ="You didn't set an id on this component!"
            
            output = soup.prettify()

            output_file = open(output_path, "w+")
            output_file.write(output)
            output_file.close()

print("---")
print("Everything should be finished now. Enjoy your website!")