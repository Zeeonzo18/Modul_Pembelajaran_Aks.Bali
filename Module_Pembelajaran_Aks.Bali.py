import tkinter as tk
from PIL import Image, ImageTk

# Jendela utama
root = tk.Tk()
root.geometry("1200x600")
root.iconbitmap("Buku.ico")
root.title("MELALI (Modul Pembelajaran Aksara Bali)")
# root.configure(bg="lightyellow")
# style = Style(theme="superhero")
# root = style.master

def menu_tombol():

    def collapse_menu_tombol():
        tombol_menu_frame.destroy()
        tombol_alih.config(text='☰')
        tombol_alih.config(command=menu_tombol)

    # Menus
    tombol_menu_frame = tk.Frame(root, bg='darkblue')

    tombol_beranda = tk.Button(tombol_menu_frame, text='Beranda', 
                               font=('Comic Neue', 14, 'bold'), bd=0, bg='darkblue', fg='white', 
                               activebackground='darkblue', activeforeground='white', command=beranda)
    tombol_beranda.place(x=10, y=10)

    tombol_materi = tk.Button(tombol_menu_frame, text='Materi', 
                              font=('Comic Neue', 14, 'bold'), bd=0, bg='darkblue', fg='white',
                              activebackground='darkblue', activeforeground='white', command=materi)
    tombol_materi.place(x=10, y=50)

    tombol_cthsoal = tk.Button(tombol_menu_frame, text='Contoh Soal',
                               font=('Comic Neue', 14, 'bold'), bd=0, bg='darkblue', fg='white', 
                               activebackground='darkblue', activeforeground='white', command=contohSoal)
    tombol_cthsoal.place(x=10, y=90)

    window_height = root.winfo_height()
    tombol_menu_frame.place(x=0, y=36, height=window_height, width=150)

    tombol_alih.config(text='x')
    tombol_alih.config(command=collapse_menu_tombol)

def beranda():
    judul_label.config(text="Om Swastiastu, teman-teman semuanya!\nSelamat Datang di Fitur MELALI (Melajah Aksara Bali),\nYuk Belajar Aksara Bali dengan Santi dan Nirwa!", font=("Comic Neue", 20, "bold"))


def materi():
    judul_label.config(text="Sejarah Perkembangan Bahasa Bali")

    isi_text = '''    Bahasa Bali adalah salah satu bahasa daerah di Indonesia yang hingga kini masih digunakan baik dalam komunikasi lisan maupun tulis oleh masyarakat Bali. Bahasa ini memiliki perkembangan yang dapat dibagi menjadi tiga fase utama, yaitu Bahasa Bali Kuno, Bahasa Bali Tengahan (Kawi-Bali), dan Bahasa Bali Kepara (Modern).\n
                   Bahasa Bali Kuno (Bali Mula) Bahasa Bali Kuno merupakan bentuk pertama dari bahasa Bali yang banyak ditemukan dalam prasasti-prasasti kuno Bali, terutama pada masa Bali Kuna. Dr. Rudolf Gorris menemukan bahwa prasasti-prasasti yang menggunakan bahasa Bali Kuno berjumlah sekitar 33 buah, yang menunjukkan bahwa pada masa ini bahasa Bali sudah digunakan dalam bentuk tulisan.
               '''
    
    # Buat frame untuk konten materi
    for widget in main_area.winfo_children():
        widget.destroy()  # Bersihkan konten sebelumnya di area utama
    
    # Tambahkan gambar
    img = Image.open("Sejarah_Aks.Bali.jpg")  # Ganti dengan nama file gambar Anda
    img = img.resize((300, 150))  # Resize gambar jika diperlukan
    img_tk = ImageTk.PhotoImage(img)
        
    img_label = tk.Label(main_area, image=img_tk)
    img_label.image = img_tk  # Menyimpan referensi gambar
    img_label.pack(pady=10)

    # Tambahkan teks
    materi_text = tk.Label(main_area, text=isi_text, wraplength=800, justify="left", font=("Comic Neue", 14))
    materi_text.pack(pady=10)


def contohSoal():
    judul_label.config(text="Contoh Aksara Bali")

# Frame root atributes
head_frame = tk.Frame(root, bg='darkblue',
                      highlightbackground='white', highlightthickness=1)

tombol_alih = tk.Button(head_frame, text='☰', bg='darkblue', fg='white', font=('bold', 20),
                        bd=0, activebackground='darkblue', activeforeground='white', command=menu_tombol)
tombol_alih.pack(side=tk.LEFT)

head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=40)

# Label Title
title_label = tk.Label(head_frame, text="Melajah Aksara Bali", bg='darkblue', 
                       fg='white', pady=10, font=('Comic Neue', 20, 'bold'))
title_label.pack(side=tk.TOP)


# Menampilkan judul
judul_label = tk.Label(root, text="Om Swastiastu, teman-teman semuanya!\nSelamat Datang di Fitur MELALI (Melajah Aksara Bali),\nYuk Belajar Aksara Bali dengan Santi dan Nirwa!", font=("Comic Neue", 20, "bold"))
judul_label.pack(pady=20)

# Main Area
main_area = tk.Frame(root)
main_area.pack(fill=tk.BOTH, expand=True)

root.mainloop()