import streamlit as st
import random

# ===================
# Data Senyawa Kimia
# ===================
senyawa_kimia = {
    "Asam": {
        "Asam Sulfat (H₂SO₄)": {
            "Risiko": "Korosif, menyebabkan luka bakar parah pada kulit dan mata.",
            "Penanganan": "Gunakan sarung tangan tahan asam, pelindung mata, dan lab coat.",
            "APD": "Sarung tangan karet, pelindung wajah, jas lab."
        }
    },
    "Basa": {
        "Natrium Hidroksida (NaOH)": {
            "Risiko": "Sangat korosif, menyebabkan luka bakar kimia.",
            "Penanganan": "Hindari kontak dengan kulit. Bersihkan tumpahan dengan netralisasi.",
            "APD": "Sarung tangan, pelindung mata, jas lab."
        }
    },
    "Pelarut Organik": {
        "Ethanol (C₂H₅OH)": {
            "Risiko": "Cairan mudah terbakar, uapnya dapat menyebabkan pusing.",
            "Penanganan": "Simpan di tempat sejuk dan berventilasi. Hindari nyala api.",
            "APD": "Masker jika digunakan dalam jumlah besar, sarung tangan."
        }
    },
    "Gas Berbahaya": {
        "Amonia (NH₃)": {
            "Risiko": "Bersifat iritan, dapat merusak saluran pernapasan dan mata.",
            "Penanganan": "Gunakan di ruang berventilasi baik. Hindari kontak langsung.",
            "APD": "Masker respirator, pelindung mata, sarung tangan nitril."
        },
        "Klorin (Cl₂)": {
            "Risiko": "Gas beracun, menyebabkan iritasi saluran napas.",
            "Penanganan": "Gunakan di bawah lemari asam. Jangan hirup uapnya.",
            "APD": "Respirator, pelindung mata, sarung tangan kimia."
        }
    }
}

# ===================
# Sidebar Navigation
# ===================
st.sidebar.title("🔬 Navigasi")
page = st.sidebar.radio("Menu", ["Beranda", "Senyawa Kimia", "Quiz"])

# ===================
# 1. Halaman Beranda
# ===================
if page == "Beranda":
    st.title("💡 Pengenalan Risiko dan Penanganan Senyawa Kimia")
    st.markdown("""
    Selamat datang di aplikasi edukatif ini!

    Aplikasi ini bertujuan untuk membantu Anda memahami **risiko**, **cara penanganan**, dan **APD** (Alat Pelindung Diri) yang diperlukan dalam bekerja dengan senyawa kimia umum.

    Silakan pilih menu di sebelah kiri untuk mulai menjelajahi senyawa atau menguji pengetahuan Anda melalui quiz!
    """)

# ============================
# 2. Halaman Senyawa Kimia
# ============================
elif page == "Senyawa Kimia":
    st.title("🧪 Daftar Senyawa Berdasarkan Golongan")

    golongan = st.selectbox("Pilih Golongan Senyawa", list(senyawa_kimia.keys()))

    if golongan:
        st.subheader(f"📚 Senyawa dalam Golongan: {golongan}")
        for nama, info in senyawa_kimia[golongan].items():
            with st.expander(f"🔍 {nama}"):
                st.markdown(f"**Risiko:** {info['Risiko']}")
                st.markdown(f"**Penanganan:** {info['Penanganan']}")
                st.markdown(f"**APD:** {info['APD']}")

# ===================
# 3. Halaman Quiz
# ===================
elif page == "Quiz":
    st.title("🧠 Quiz Penanganan Senyawa Kimia")
    st.markdown("Jawablah pertanyaan berikut dengan memilih jawaban yang paling tepat.")

    all_questions = []
    for golongan in senyawa_kimia:
        for nama, data in senyawa_kimia[golongan].items():
            all_questions.append({
                "senyawa": nama,
                "question": f"Apa APD yang dibutuhkan saat menangani {nama}?",
                "answer": data["APD"],
                "options": [
                    data["APD"],
                    "Sarung tangan kain, masker kain",
                    "Tidak perlu APD",
                    "Topi dan jas hujan"
                ]
            })

    # Random satu pertanyaan
    question = random.choice(all_questions)

    st.subheader(question["question"])
    pilihan = st.radio("Pilih jawaban Anda:", question["options"])

    if st.button("Cek Jawaban"):
        if pilihan == question["answer"]:
            st.success("✅ Jawaban benar!")
        else:
            st.error(f"❌ Jawaban salah. Jawaban yang benar adalah: **{question['answer']}**")

