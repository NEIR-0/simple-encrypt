import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
from PIL import Image
import os

# ===== Fungsi untuk TEKS =====

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    return key

def load_key():
    return open("secret.key", "rb").read()

def encrypt_text_gui():
    plain = entry_text.get()
    if not plain:
        messagebox.showwarning("Peringatan", "Masukkan teks terlebih dahulu.")
        return
    key = generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(plain.encode())
    result_text.set(encrypted.decode())
    messagebox.showinfo("Sukses", "Teks berhasil dienkripsi. Kunci disimpan sebagai 'secret.key'.")

def decrypt_text_gui():
    encrypted = entry_text.get()
    if not encrypted:
        messagebox.showwarning("Peringatan", "Masukkan teks terenkripsi.")
        return
    try:
        key = load_key()
        f = Fernet(key)
        decrypted = f.decrypt(encrypted.encode()).decode()
        result_text.set(decrypted)
    except Exception as e:
        messagebox.showerror("Error", f"Dekripsi gagal: {e}")

# ===== Fungsi untuk GAMBAR =====

def xor_encrypt_decrypt_image(path, key_byte, output_path):
    with open(path, 'rb') as file:
        data = bytearray(file.read())
    for i in range(len(data)):
        data[i] ^= key_byte
    with open(output_path, 'wb') as file:
        file.write(data)

def choose_image_encrypt():
    file_path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.png *.bmp")])
    if file_path:
        key = entry_img_key.get()
        if not key.isdigit() or not (0 <= int(key) <= 255):
            messagebox.showwarning("Peringatan", "Kunci harus angka 0–255.")
            return
        key_byte = int(key)
        output_path = "encrypted_" + os.path.basename(file_path)
        xor_encrypt_decrypt_image(file_path, key_byte, output_path)
        messagebox.showinfo("Sukses", f"Gambar berhasil dienkripsi: {output_path}")

def choose_image_decrypt():
    file_path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.png *.bmp")])
    if file_path:
        key = entry_img_key.get()
        if not key.isdigit() or not (0 <= int(key) <= 255):
            messagebox.showwarning("Peringatan", "Kunci harus angka 0–255.")
            return
        key_byte = int(key)
        output_path = "decrypted_" + os.path.basename(file_path)
        xor_encrypt_decrypt_image(file_path, key_byte, output_path)
        messagebox.showinfo("Sukses", f"Gambar berhasil didekripsi: {output_path}")

# ===== GUI Setup =====

root = tk.Tk()
root.title("Encrypt & Decrypt - Teks dan Gambar")
root.geometry("600x400")
root.resizable(False, False)

# Frame Teks
frame_text = tk.LabelFrame(root, text="Enkripsi / Dekripsi Teks", padx=10, pady=10)
frame_text.pack(padx=10, pady=10, fill="x")

tk.Label(frame_text, text="Teks / Enkripsi:").pack(anchor="w")
entry_text = tk.Entry(frame_text, width=80)
entry_text.pack()

btn_frame = tk.Frame(frame_text)
btn_frame.pack(pady=5)
tk.Button(btn_frame, text="Enkripsi", command=encrypt_text_gui).pack(side="left", padx=5)
tk.Button(btn_frame, text="Dekripsi", command=decrypt_text_gui).pack(side="left", padx=5)

result_text = tk.StringVar()
tk.Label(frame_text, text="Hasil:").pack(anchor="w")
tk.Entry(frame_text, textvariable=result_text, width=80, state="readonly").pack()

# Frame Gambar
frame_image = tk.LabelFrame(root, text="Enkripsi / Dekripsi Gambar", padx=10, pady=10)
frame_image.pack(padx=10, pady=10, fill="x")

tk.Label(frame_image, text="Masukkan kunci angka (0–255):").pack(anchor="w")
entry_img_key = tk.Entry(frame_image, width=10)
entry_img_key.pack(anchor="w")

img_btn_frame = tk.Frame(frame_image)
img_btn_frame.pack(pady=5)
tk.Button(img_btn_frame, text="Pilih Gambar & Enkripsi", command=choose_image_encrypt).pack(side="left", padx=5)
tk.Button(img_btn_frame, text="Pilih Gambar & Dekripsi", command=choose_image_decrypt).pack(side="left", padx=5)

root.mainloop()
