import os
import shutil


class FileManager:
    def __init__(self, base_dir):
        self.base_dir = os.path.abspath(base_dir)
        self.current_dir = self.base_dir

        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def is_safe_path(self, path):
        abs_path = os.path.abspath(path)
        return abs_path.startswith(self.base_dir)

    def get_path(self, name):
        path = os.path.join(self.current_dir, name)
        abs_path = os.path.abspath(path)

        if not self.is_safe_path(abs_path):
            raise ValueError("Нельзя выходить за пределы рабочей директории")

        return abs_path

    def show_current_dir(self):
        print(f"\nТекущая директория: {self.current_dir}")

    def list_dir(self):
        print("\nСодержимое директории:")

        items = os.listdir(self.current_dir)

        if not items:
            print("Папка пустая")
            return

        for item in items:
            path = os.path.join(self.current_dir, item)

            if os.path.isdir(path):
                print(f"[DIR]  {item}")
            else:
                print(f"[FILE] {item}")

    def change_dir(self, folder_name):
        if folder_name == "..":
            parent = os.path.abspath(os.path.join(self.current_dir, ".."))

            if self.is_safe_path(parent):
                self.current_dir = parent
            else:
                print("Нельзя выйти за пределы рабочей директории")
            return

        path = self.get_path(folder_name)

        if os.path.isdir(path):
            self.current_dir = path
            print("Переход выполнен")
        else:
            print("Такой папки нет")

    def create_dir(self, folder_name):
        path = self.get_path(folder_name)

        if os.path.exists(path):
            print("Такая папка уже существует")
        else:
            os.makedirs(path)
            print("Папка создана")

    def delete_dir(self, folder_name):
        path = self.get_path(folder_name)

        if os.path.isdir(path):
            shutil.rmtree(path)
            print("Папка удалена")
        else:
            print("Такой папки нет")

    def create_file(self, file_name):
        path = self.get_path(file_name)

        if os.path.exists(path):
            print("Такой файл уже существует")
        else:
            with open(path, "w", encoding="utf-8") as file:
                pass
            print("Файл создан")

    def read_file(self, file_name):
        path = self.get_path(file_name)

        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()

            print("\nСодержимое файла:")
            print(content)
        else:
            print("Такого файла нет")

    def write_file(self, file_name, text):
        path = self.get_path(file_name)

        if os.path.isfile(path):
            with open(path, "w", encoding="utf-8") as file:
                file.write(text)
            print("Текст записан в файл")
        else:
            print("Такого файла нет")

    def copy_file(self, source_name, destination_name):
        source_path = self.get_path(source_name)
        destination_path = self.get_path(destination_name)

        if os.path.isfile(source_path):
            shutil.copy2(source_path, destination_path)
            print("Файл скопирован")
        else:
            print("Исходный файл не найден")

    def move_file(self, source_name, destination_name):
        source_path = self.get_path(source_name)
        destination_path = self.get_path(destination_name)

        if os.path.exists(source_path):
            shutil.move(source_path, destination_path)
            print("Файл или папка перемещены")
        else:
            print("Исходный объект не найден")

    def rename_file(self, old_name, new_name):
        old_path = self.get_path(old_name)
        new_path = self.get_path(new_name)

        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print("Объект переименован")
        else:
            print("Объект не найден")