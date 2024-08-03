"""
DISCLAIMER: Isi materi yang ada di sini tidak dijamin keakuratannya karena dibuat hanya berdasarkan catatan pribadi penulis selama course.
Materi ini dibuat semata untuk memenuhi tugas bootcamp Dibimbing AIML4 Day 5 - Git.
"""

def check_branchs():
    return [
        {
            "cmd": "git branch",
            "desc": "Menampilkan branch yang ada dan yang sedang aktif",
            "src": []
        }
    ]

def create_new_branch():
    return [
        {
            "cmd": 'git checkout -b "nama-branch"',
            "desc": "Membuat branch baru dengan nama 'nama-branch' sekaligus berpindah ke branch tersebut",
            "src": []
        }
    ]



def change_active_branch():
    return [
        {
            "cmd": 'git checkout "nama-branch"',
            "desc": "Berpindah ke branch 'nama-branch'",
            "src": []
        }
    ]