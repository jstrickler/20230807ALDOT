"""Create a .env file that points to EXAMPLES/tests so that the 
    pytest tools in VSCode will work correctly
"""
import os

root_folder = os.path.dirname(os.getcwd())

for folder in 'examples', 'EXAMPLES':
    examples_folder = os.path.join(root_folder, folder)
    if os.path.exists(examples_folder):
        break
else:
    print("examples folder not found")
    exit(1)

for folder, subfolders, filenames in os.walk(examples_folder):
    if folder.endswith('tests'):
        print(folder)
        break
else:
    print("test folder not found!")
    exit(1)


