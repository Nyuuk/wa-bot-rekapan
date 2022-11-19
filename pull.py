from sqlalchemy import create_engine
import csv

USER_DB = "uss_ppnh"
PASSW_DB = "ppnh2007"
DOM_DB = "10.42.0.1"
NAME_DB = "ppnh"
tb_name = "santri_putra"
tb_name_sakit = "rekap_sakit_pulang_pa"

engine = create_engine("postgresql://{}:{}@{}:5432/{}".format(USER_DB, PASSW_DB, DOM_DB, NAME_DB))

def list_all_from_database():
    with engine.connect() as conn:
        fet = conn.execute("SELECT * from {}".format(tb_name))
        row = fet.fetchall()
    return row

def edit_data_from_id(form):
    STR = ""
    if form["nama"]:
        STR += f'\nnama = \'{form["nama"]}\''
    if form["kamar"]:
        STR += f'\nkamar = \'{form["kamar"]}\''
    if form["kelas_up"]:
        STR += f",\nkelas_up = {form['kelas_up']}"
    if len(form["kelas_diniyah"]):
        STR += f',\nkelas_diniyah = \'{form["kelas_diniyah"]}\''
    if len(form["jenjang_up"]):
        STR += f',\njenjang_up = \'{form["jenjang_up"]}\''
    if len(form["jenjang_diniyah"]):
        STR += f',\njenjang_diniyah = \'{form["jenjang_diniyah"]}\''
    if len(form["nama_wali_laki"]):
        STR += f',\nnama_wali_laki = \'{form["nama_wali_laki"]}\''
    if len(form["kontak_wali"]):
        STR += f',\nkontak_wali = \'{form["kontak_wali"]}\''
    if len(form["status_pondok"]):
        STR += f',\nstatus_pondok = \'{form["status_pondok"]}\''
    if len(form["nama_wali_perempuan"]):
        STR += f',\nnama_wali_perempuan = \'{form["nama_wali_perempuan"]}\''
    with engine.connect() as conn:
        has = conn.execute(f"SELECT * from {tb_name} WHERE id = '{form['id']}'").fetchall()
        conn.execute(
            """UPDATE {}
            SET {}
            WHERE
            id = '{}'
            """.format(
                tb_name,
                STR,
                form["id"]
                )
            )
        # mengubah format yg tidak ada ke None
        status = True
        if has[0][1] == form["nama"]:
            # print(has[0][1])
            print(0)
            status = False
        if int(has[0][2]) == int(form["kelas_up"]):
            print(1)
            status = False
        if has[0][3] == form["jenjang_up"]:
            print(2)
            status = False
        if has[0][4] == form["kelas_diniyah"]:
            print(3)
            status = False
        if has[0][5] == form["jenjang_diniyah"]:
            print(4)
            status = False
        if has[0][6] == form["nama_wali_laki"]:
            print(5)
            status = False
        if has[0][7] == form["nama_wali_perempuan"]:
            print(6)
            status = False
        if has[0][8] == form["kontak_wali"]:
            print(7)
            status = False
        if has[0][9] == form["status_pondok"]:
            print(8)
            status = False
        if has[0][9] == form["status_pondok"]:
            print(9)
            status = False
        if has[0][9] == form["status_pondok"]:
            print(10)
            status = False
        return status

def add_(form):
    # INSERT INTO ppnh(id, nama, kelas_up, jenjang_up, kelas_diniyah, jenjang_diniyah, nama_wali_laki, nama_wali_perempuan, kontak_wali, status_pondok) VALUES ()
    COL = ['id']
    VAL = [form["id"]]
    STR = f"'{form['id']}'"
    if form["nama"]:
        form['nama'] = form['nama'].replace("'", "''")
        COL.append("nama")
        VAL.append(f'{form["nama"]}')
        STR += f",'{form['nama']}'"
    if form["kamar"]:
        COL.append("kamar")
        VAL.append(f'{form["kamar"]}')
        STR += f",'{form['kamar']}'"
    if form["kelas_up"]:
        COL.append("kelas_up")
        VAL.append(form["kelas_up"])
        STR += f",'{form['kelas_up']}'"
    if len(form["kelas_diniyah"]):
        COL.append("kelas_diniyah")
        VAL.append(f'{form["kelas_diniyah"]}')
        STR += f",'{form['kelas_diniyah']}'"
    if len(form["jenjang_up"]):
        COL.append("jenjang_up")
        VAL.append(f'{form["jenjang_up"]}')
        STR += f",'{form['jenjang_up']}'"
    if len(form["jenjang_diniyah"]):
        COL.append("jenjang_diniyah")
        VAL.append(f'{form["jenjang_diniyah"]}')
        STR += f",'{form['jenjang_diniyah']}'"
    if len(form["nama_wali_laki"]):
        COL.append("nama_wali_laki")
        VAL.append(f'{form["nama_wali_laki"]}')
        STR += f",'{form['nama_wali_laki']}'"
    if len(form["kontak_wali"]):
        COL.append("kontak_wali")
        VAL.append(f'{form["kontak_wali"]}')
        STR += f",'{form['kontak_wali']}'"
    if len(form["status_pondok"]):
        COL.append("status_pondok")
        VAL.append(f'{form["status_pondok"]}')
        STR += f",'{form['status_pondok']}'"
    if len(form["nama_wali_perempuan"]):
        COL.append("nama_wali_perempuan")
        VAL.append(f'{form["nama_wali_perempuan"]}')
        STR += f",'{form['nama_wali_perempuan']}'"

    with engine.connect() as conn:
        try:
            conn.execute(
                f"""INSERT INTO {tb_name}(
                {",".join(COL)}
                ) VALUES (
                {STR}
                )
                """
            )
        except Exception as ex:
            print("error: {}".format(ex))
            return False
        else:
            return True

def check_(form):
    """
    form = {
    "id": INTEGER,
    "nama": VARCHAR,
    "kelas_up": INTEGER,
    "jenjang_up": VARCHAR,
    "kelas_diniyah": VARCHAR,
    "jenjang_diniyah": VARCHAR,
    "nama_wali_laki": VARCHAR,
    "nama_wali_perempuan": VARCHAR,
    "kontak_wali": INTEGER,
    "status_pondok": VARCHAR
    }
    jika ada salah satu selain id yg beda maka akan mengembalikan nilai FALSE, dan TRUE jika semua sama
    """
    rows_from_database = list_all_from_database()
    for row in rows_from_database:
        if row[0] != form["id"]:
            continue
        else:
            if row[1] != form["nama"] or row[2] != form["kamar"] or row[2+1] != form["kelas_up"] or row[3+1] != form["jenjang_up"] or row[4+1] != form["kelas_diniyah"] != row[5+1] != form["jenjang_diniyah"] or row[6+1] != form["nama_wali_laki"] or row[7+1] != form["nama_wali_perempuan"] or row[8+1] != form["kontak_wali"] or row[9+1] != form["status_pondok"]:
                return False
            else:
                return True

def get_id_():
    all_data = list_all_from_database()
    only_id = [k[0] for k in all_data]
    # print(all_data,only_id)
    abdS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numS = [k for k in range(1, 101)]
    for abd1 in abdS:
        jadi_id = ""
        jadi_id += abd1
        for abd2 in abdS:
            jadi_id += abd2
            for abd3 in abdS:
                jadi_id += abd3
                for num in numS:
                    jadi_id = jadi_id[0:3]
                    if len(str(num)) << 2:
                        jadi_id = jadi_id[0:3]
                        jadi_id += f"00{num}"
                    if len(str(num)) == 2:
                        jadi_id = jadi_id[0:3]
                        jadi_id += f"0{num}"
                    if int(num) == 100:
                        jadi_id = jadi_id[0:3]
                        jadi_id += f"{num}"
                    if jadi_id not in only_id:
                        return jadi_id
                    else:
                        continue
                jadi_id = jadi_id[0:3]
            jadi_id = jadi_id[0:2]
        jadi_id = jadi_id[0:1]

def rekapan_absen_malam_push(req):
    "req = [id, nama, sakit/pulang, tanggal_absen, tanggal_sakit_pulang]"
    STR = "nama"
    VAL = "'" + req['nama'].replace("'", "''") + "'"
    if req[0]:
        STR += "id"
        VAL+=f"'{req['id']}'"
    if req[2]:
        STR+="sakit_pulang"
        VAL+=f"'{req['sakit_pulang']}'"
    if req[3]:
        STR+="tanggal_absen"
        VAL+=f"'{req['tanggal_absen']}'"
    if req[4]:
        STR+="tanggal_sakit_pulang"
        VAL+=f"'{req['tanggal_sakit_pulang']}'"
    with engine.connect() as conn:
        conn.execute(
            "INSERT INTO {}({}) VALUES ({})".format(tb_name_sakit,STR,VAL)
            )

def list_with_specific(req):
    "req = [column_defination, value]"
    with engine.connect() as conn:
        fet = conn.execute(f"SELECT id,nama,kelas_up FROM {tb_name} WHERE {req[0]}='{req[1]}'").fetchall()
        return fet

if __name__ == "__main__":
    with open("DATA-SANTRI-PUTRA(fix).csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                line_count += 1
                # tahap pertama ubah csv array ke dictonary
                if row[0].isnumeric():
                    idd=int(row[0])
                    status_id = True
                    form = dict(
                        id=idd,
                        nama=row[1],
                        kamar=row[2],
                        kelas_up=row[3],
                        jenjang_up=row[4],
                        kelas_diniyah=row[5],
                        jenjang_diniyah=row[6],
                        nama_wali_laki=row[7],
                        nama_wali_perempuan=row[8],
                        kontak_wali=row[9],
                        status_pondok=row[10]
                        )
                else:
                    idd=get_id_()
                    status_id = False
                    form = dict(
                        id=idd,
                        nama=row[1-1],
                        kamar=row[2-1],
                        kelas_up=row[3-1],
                        jenjang_up=row[4-1],
                        kelas_diniyah=row[5-1],
                        jenjang_diniyah=row[6-1],
                        nama_wali_laki=row[7-1],
                        nama_wali_perempuan=row[8-1],
                        kontak_wali=row[9-1],
                        status_pondok=row[10-1]
                        )
                # tahap kedua check id
                if check_(form):
                    print("Tidak ada perubahan dari nama Santri: \"{}\"",format(form["nama"]))
                else:
                    # tahap ketiga pengecekan id di database
                    idd_all = [k[0] for k in list_all_from_database()]
                    # jika id ada di database
                    if form["id"] in idd_all:
                        # mencoba mengedit row database dengan id yg sama
                        if edit_data_from_id(form):
                            # jika berhasil
                            print("Nama: {}, berhasil di update".format(form["nama"]))
                            line_count += 1
                        else:
                            # jika tidak berhasil
                            print("Nama: {}, tidak berhasil di update".format(form["nama"]))
                    else:
                        if add_(form):
                            print("Nama: {}, berhasil di tambahkan".format(form["nama"]))
                            line_count += 1
                        else:
                            print("Nama: {}, tidak berhasil di tambahkan".format(form["nama"]))
        print("Total data yang di masukan ke database: {}".format(line_count-1))