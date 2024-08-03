"""File .py ini dibuat semata untuk memenuhi tugas AIML Batch 5 Dibimbing.
Materi yang ada di sini dibuat oleh penulis berdasarkan materi git yang telah dipelajari di hari ke-5 bootcamp AIML Dibiming dan beberapa dilengkapi dengan sumber dari internet.
DISCLAIMER: Deskripsi dan pengelompokan dari masing-masing perintah masih perlu diperiksa lagi keakuratannya.
"""

def basic_workflow():
    return [
        "Atur git username dan email.",
        "Buat repository lokal.",
        "Tambahkan file ke staging area",
        "Simpan perubahan secara lokal (commit)",
        "Buat remote repository",
        "Hubungkan remote repository dengan local repository",
        "Aktifkan tracking ke remote",
        "Update commit ke remote"
    ]

def configure_global_git_username_and_email():
    return [
        {
            "cmd":"git -config --global user.name",
            "desc": "memeriksa username yang akan dipakai dalam proses commit. Jika menggunakan parameter --global, setting yang dimaksud adalah setting yang diaplikasikan dalam level os. Untuk Windows OS, setting ini disimpan dalam 'C:\\Users\\\\.gitconfig'. Jika hasil menjalankan perintah ini adalah kosong maka artinya belum ada setting username yang terdaftar secara global. Untuk mendaftarkan secara global tambahkan parameter nama seperti ini: 'git -config --global user.name nama_anda'",
            "src": [
                "https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config"
            ]
        },
        {
            "cmd":"git -config --global user.email",
            "desc": "memeriksa email yang akan dipakai dalam proses commit. Parameter --global menunjukkan bahwa setting yang dimaksud adalah setting yang diaplikasikan dalam level os. Untuk Windows OS, setting ini disimpan dalam 'C:\\Users\\\\.gitconfig'. Jika hasil menjalankan perintah ini adalah kosong maka artinya belum ada setting username yang terdaftar secara global. Untuk mendaftarkan secara global tambahkan parameter email seperti ini: 'git -config --global user.email email_anda@domain.nya'",
            "src": [
                "https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-config"
            ]
        }
    ]

def create_local_repository():
    return [
        {
            "cmd":"git init",
            "desc": "Dipakai jika terdapat project di dalam perangkat lokal dan project tersebut belum memiliki repository git. 'git init' akan menghasilkan hidden folder '.git' di dalam folder project",
            "src": []
        },
        {
            "cmd":"git clone ",
            "desc": "Untuk menduplikat project dari remote repository (Github, misalnya). Jika mempergunakan 'git clone', di dalam folder project sudah ada folder '.git' yang berarti local repository sudah secara otomatis dibuatkan oleh perintah ini",
            "src": []
        }
    ]

def add_files_to_staging_area():
    return [
        {
            "cmd": 'git add "namafile.ext"',
            "desc": "Menambahkan 'namafile.ext' ke dalam staging area",
            "src": []
        },
        {
            "cmd": "git add .",
            "desc": "Menambahkan semua file ke dalam staging area, kecuali file-file yang dinyatakan dalam file '.gitignore'",
            "src": []
        }
    ]

def save_changes_locally():
    return [
        {
            "cmd": 'git commit -m "komentar untuk commit. NOTE: setiap commit harus selalu disertai komentar"',
            "desc": "Mirip save point! menyimpan history perubahan secara lokal",
            "src": []
        }
    ]

def check_repository_status():
    return [
        {
            "cmd": "git status",
            "desc": "Menampilkan status working directory dan staging area: perubahan yang sudah dan belum dilakukan serta menampilkan file mana saja yang sudah di-track",
            "src": ["https://www.atlassian.com/git/tutorials/inspecting-a-repository"]
        }
    ]