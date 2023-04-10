import tkinter as tk


# функция для обработки данных
def process_data():
    input_data = input_widget.get()
    search_data = search_widget.get()
    # здесь должна быть ваша логика обработки данных
    output_widget.configure(text=f"Результат: {input_data.upper()}Поиск: {search_data}")


# создаем главное окно
root = tk.Tk()
root.title("Мое приложение")
root.configure(background='#E8F6FA')

# устанавливаем иконку приложения
root.iconbitmap('C:/Users/User/Desktop/Tk/img/Calculator.ico')

# создаем фреймы
input_frame = tk.Frame(root, bg="#E8F6FA")
search_frame = tk.Frame(root, bg="#E8F6FA")
output_frame = tk.Frame(root, bg="#E8F6FA")
button_frame = tk.Frame(root, bg="#E8F6FA")

# создаем виджеты
tk.Label(input_frame, text="Введите данные: ", font=("Helvetica", 16), bg="#E8F6FA").pack(side="left", padx=10, pady=10)
input_widget = tk.Entry(input_frame, font=("Helvetica", 16), bg="#F1F1F1", fg="#2C2C2C")
input_widget.pack(side="left", padx=10, pady=10)

tk.Label(search_frame, text="Поиск: ", font=("Helvetica", 16), bg="#E8F6FA").pack(side="left", padx=10, pady=10)
search_widget = tk.Entry(search_frame, font=("Helvetica", 16), bg="#F1F1F1", fg="#2C2C2C")
search_widget.pack(side="left", padx=10, pady=10)

tk.Label(output_frame, text="Результат обработки данных: ", font=("Helvetica", 16), bg="#E8F6FA").pack(side="left", padx=10, pady=10)
output_widget = tk.Label(output_frame, font=("Helvetica", 16), bg="#E8F6FA", fg="#2C2C2C")
output_widget.pack(side="left", padx=10, pady=10)

button = tk.Button(button_frame, text="Обработать", command=process_data, font=("Helvetica", 16), background="#31A2C5", foreground="#FFFFFF", relief="raised")
button.pack(side="left", padx=10, pady=10)

# размещаем фреймы на главном окне
input_frame.pack(fill="x")
search_frame.pack(fill="x")
output_frame.pack(fill="x")
button_frame.pack(fill="x")

# задаем минимальный размер главного окна
root.minsize(500, 200)

# запускаем главный цикл приложения
root.mainloop()
