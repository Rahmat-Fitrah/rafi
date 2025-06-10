listCalon = []

def tambah_calon():
    idCal = input("Masukan ID Calon: ")
    if any (c['id'] == idCal for c in listCalon):
        print("ID sudah terdaftar.")
        return
    namaCal = input("Masukan Nama Calon: ")
    vimical = input("Masukan Nama visi misi: ")

    listCalon.append({"id":idCal, "Nama":namaCal, "visi":vimical, "jumlah_suara": 0})
    print("Calon berhasil didaftar!")

    def get_data():
        return listCalon

    def cari_calon(id):
        for c in listCalon:
            if p ['id'] == id:
                return p
        return None