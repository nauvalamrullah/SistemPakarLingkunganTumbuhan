from flask import Flask, render_template, request

app = Flask(__name__)

class SistemPakarTanaman:
    def __init__(self):
        self.kondisi = {}
        self.basis_pengetahuan = {
            'pasir': {
                'rendah': {
                    'tinggi': ['Kaktus', 'Tumbuhan Sukulen'],
                    'sedang': ['Aloe Vera', 'Agave'],
                    'rendah': ['Tumbuhan Sukulen', 'Zaitun']
                },
                'sedang': {
                    'tinggi': ['Agave', 'Bougainvillea'],
                    'sedang': ['Bougainvillea', 'Lavender'],
                    'rendah': ['Zaitun', 'Kurma']
                },
                'tinggi': {
                    'tinggi': ['Kurma', 'Lavender'],
                    'sedang': ['Lavender', 'Sage'],
                    'rendah': ['Sage', 'Anggur']
                }
            },
            'lempung': {
                'rendah': {
                    'tinggi': ['Jagung', 'Gandum'],
                    'sedang': ['Gandum', 'Barley'],
                    'rendah': ['Barley', 'Kacang Tanah']
                },
                'sedang': {
                    'tinggi': ['Padi', 'Tebu'],
                    'sedang': ['Tebu', 'Kacang Kedelai'],
                    'rendah': ['Kacang Kedelai', 'Tomat']
                },
                'tinggi': {
                    'tinggi': ['Bambu', 'Teh'],
                    'sedang': ['Teh', 'Kopi'],
                    'rendah': ['Kopi', 'Pisang']
                }
            },
            'gembur': {
                'rendah': {
                    'tinggi': ['Tomat', 'Kentang'],
                    'sedang': ['Kentang', 'Selada'],
                    'rendah': ['Selada', 'Bayam']
                },
                'sedang': {
                    'tinggi': ['Strawberry', 'Blueberry'],
                    'sedang': ['Blueberry', 'Raspberry'],
                    'rendah': ['Raspberry', 'Anggur']
                },
                'tinggi': {
                    'tinggi': ['Brokoli', 'Kol'],
                    'sedang': ['Kol', 'Bayam'],
                    'rendah': ['Bayam', 'Selada']
                }
            }
        }

    def tambah_kondisi(self, faktor, nilai):
        self.kondisi[faktor] = nilai

    def rekomendasi_tanaman(self):
        jenis_tanah = self.kondisi.get('jenis_tanah')
        curah_hujan = self.kondisi.get('curah_hujan')
        suhu = self.kondisi.get('suhu')

        if jenis_tanah in self.basis_pengetahuan:
            if curah_hujan in self.basis_pengetahuan[jenis_tanah]:
                if suhu in self.basis_pengetahuan[jenis_tanah][curah_hujan]:
                    return ', '.join(self.basis_pengetahuan[jenis_tanah][curah_hujan][suhu])

        return 'Tanaman tidak diketahui'

sistem_pakar = SistemPakarTanaman()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        jenis_tanah = request.form.get('jenis_tanah').lower()
        curah_hujan = request.form.get('curah_hujan').lower()
        suhu = request.form.get('suhu').lower()

        if jenis_tanah not in ['pasir', 'lempung', 'gembur']:
            hasil = "Jenis tanah tidak valid!"
        elif curah_hujan not in ['rendah', 'sedang', 'tinggi']:
            hasil = "Curah hujan tidak valid!"
        elif suhu not in ['rendah', 'sedang', 'tinggi']:
            hasil = "Suhu tidak valid!"
        else:
            sistem_pakar.tambah_kondisi('jenis_tanah', jenis_tanah)
            sistem_pakar.tambah_kondisi('curah_hujan', curah_hujan)
            sistem_pakar.tambah_kondisi('suhu', suhu)
            hasil = sistem_pakar.rekomendasi_tanaman()
        
        return render_template('index.html', hasil=hasil)

    return render_template('index.html', hasil=None)

if __name__ == "__main__":
    app.run(debug=True)
