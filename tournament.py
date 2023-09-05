import os
import importlib
import importlib.util




# dynamic import code from https://stackoverflow.com/questions/57878744/how-do-i-dynamically-import-all-py-files-from-a-given-directory-and-all-sub-di

def get_py_files(src):
    cwd = os.getcwd() # Current Working directory
    py_files = []
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith(".py"):
                py_files.append(os.path.join(cwd, root, file))
    return py_files


def dynamic_import(module_name, py_path):
    module_spec = importlib.util.spec_from_file_location(module_name, py_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module


def dynamic_import_from_src(src):
    my_py_files = get_py_files(src)
    modules = []
    for py_file in my_py_files:
        module_name = os.path.split(py_file)[-1].strip(".py")
        imported_module = dynamic_import(module_name, py_file)
        modules.append(imported_module)
    return modules

if __name__ == "__main__":
    modules = dynamic_import_from_src("players")
    print(modules)
    
    players = []
    for module in modules:
        players.append(module.Player())
        
    print(players)