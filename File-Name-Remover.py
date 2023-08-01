import os
import tkinter as tk
from tkinter import filedialog

def remove_string_from_filenames(folder_path, target_string):
    try:
        files = os.listdir(folder_path)

        for filename in files:
            if target_string in filename:
                new_filename = filename.replace(target_string, "")
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_filename)
                os.rename(old_path, new_path)
        
        return True

    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return False

def on_select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_folder.delete(0, tk.END)
        entry_folder.insert(0, folder_path)

def on_remove_string():
    folder_path = entry_folder.get()
    target_string = entry_target_string.get()
    if folder_path and target_string:
        success = remove_string_from_filenames(folder_path, target_string)
        if success:
            label_result.config(text="ファイル名の文字列を削除しました。")
        else:
            label_result.config(text="エラーが発生しました。")

root = tk.Tk()
root.title("ファイル名文字列削除ツール")
root.geometry("375x150")  # ウィンドウサイズを調整
root.resizable(width=False, height=False) 

tk.Label(root, text="フォルダを選択してください：").grid(row=0, column=0, padx=(10,0), sticky="e")
entry_folder = tk.Entry(root)
entry_folder.grid(row=0, column=1, padx=10)
tk.Button(root, text="フォルダ選択", command=on_select_folder).grid(row=0, column=2, padx=(0,10))

tk.Label(root, text="文字列を入力してください：").grid(row=1, column=0, padx=(10,0), sticky="e")
entry_target_string = tk.Entry(root)
entry_target_string.grid(row=1, column=1, padx=10)

tk.Button(root, text="文字列を削除", command=on_remove_string).grid(row=2, column=0, columnspan=3, pady=10)

label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
