# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()
    words = text.split()
    count = len(words)
    print("Общее количество слов в файле:", count)


    import csv
with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["имя", "возраст", "город"])
    writer.writerow(["Анна", 20, "Алматы"])
    writer.writerow(["Иван", 22, "Астана"])
    writer.writerow(["Мария", 19, "Шымкент"])
    print("Файл students.csv успешно создан!")
