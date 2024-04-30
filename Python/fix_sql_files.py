import os

def insert_sql_declaration(folder_path):
    files = os.listdir(folder_path)
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                first_line = f.readline()
            if not first_line.startswith('--! SQL'):
                with open(file_path, 'r+') as f:
                    content = f.read()
                    f.seek(0, 0)
                    f.write('--! SQL\n' + content)

folder_path = r'C:\Users\USER\Desktop\Code\code_progress_tracker\SQL'
insert_sql_declaration(folder_path)
