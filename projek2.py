import streamlit as st

st.sidebar.title("TAHAPAN FIVES")
st.markdown("""
    <style>
    #posisi{
        position:absolute;
        top:-130px;
        left:20px;
        color:yellow;
        font-size:60px;
        z-index:2;
        font-family:"brush script mt";
    }
    div.st-key-coba button {
        background-color:green;
        border:2px solid black;
    }
    div.st-key-coba button .e121c1cl0{
            font-family:"bauhaus 93";
            font-size:20px;
    }
    #judul{
        font-size:30px;
        font-weight:bold;
        font-family:Times New Roman;
        color:blue;
    }
    div.st-key-coba button:hover {
        background-color:yellow;
        box-shadow:2px 2px 2px blue;
    }
    div.st-key-coba1 button {
        background-color:purple;
        border:2px solid black;
    }
    div.st-key-coba2 button {
        background-color:grey;
        border:2px solid black;
    }
    div.st-key-coba3 button {
        background-color:brown;
        border:2px solid black;
    }
    div.st-key-coba4 button {
        background-color:darkblue;
        border:2px solid black;
    }
    div.st-key-coba1 button .e121c1cl0{
            font-family:"bauhaus 93";
            font-size:16px;
            color:white;
    }
    div.st-key-coba2 button .e121c1cl0{
            font-family:"bauhaus 93";
            font-size:16px;
            color:black;
    }
    div.st-key-coba3 button .e121c1cl0{
            font-family:"bauhaus 93";
            font-size:16px;
            color:white;
    }
    div.st-key-coba4 button .e121c1cl0{
            font-family:"bauhaus 93";
            font-size:16px;
            color:white;
    }
    .isi{
        font-family:"Times New Roman";
        font-size:16px;
        text-align:justify;
        border-radius:10px;
        border: 2px solid black;
        background-color:pink;
        padding:5px;
        text-indent:40px;
        margin:10px;
        color:black;
    }
    .isi:hover{
        background-color:white;
        color:blue;
    }
    .isian{
        font-family:"Times New Roman";
        border:2px solid black;
        border-radius:0px 10px 0px 10px;
        background-color:cyan;
        padding:5px;
        text-align:justify;
        font-size:20px;
        box-shadow:2px 2px 2px 2px yellow;
    }
    div[data-testid="stExpander"] p{
        font-family:"brush script mt";
        font-size:30px;
        background-color:orange;
        font-weight:bold;
        padding:5px;
        border-radius:6px;
    }
    button[data-testid="stTab"] .e121c1cl0{
        font-family:Georgia;
        font-weight:bold;
        font-size:10px;
    }
    button[data-testid="stTab"]{
        background-image: linear-gradient(to right, yellow , orange);
        border-radius:10px;
        padding:5px;
    }
    .isikan{
        font-family:century;
        font-size:20px;
        text-align:justify;
        background-color:pink;
        padding:5px;
        border-radius:10px;
    }
    .stHeading h1{
        font-family:century;
        text-align:center;
    }
    .stHeading {
        background-image:linear-gradient(to bottom right, red, yellow);
        margin-bottom:5px;
        border-radius:10px;
    }
    .stSidebar{
        background-image:url("https://cdn.pixabay.com/photo/2020/02/24/18/04/background-4876985_960_720.jpg")
    }
    .stApp{
        background-image:url("https://cdn.pixabay.com/photo/2022/05/23/21/05/circle-7217259_960_720.png");
        background-repeat: no-repeat;
        background-size: cover;
    }
    header[data-testid="stHeader"]{
        position:relative;
        background-image:url("https://i.gifer.com/VJi.gif");
        background-repeat: no-repeat;
        background-size: cover;
        z-index:1;
    }
    div.stExpander{
        background-image:url("https://www.shutterstock.com/image-vector/wavy-pink-background-unicorn-glitter-260nw-2392756149.jpg");
        background-repeat: no-repeat;
        background-size: cover;
        border-radius:10px;
    }
    .judul1{
        font-family:"comic sans ms";
        color:blue;
        text-shadow:2px 2px 2px orange;
        font-size:16px;
    }
    #posisi span{
        font-family:"snap itc";
        text-shadow: 1px 1px 2px white, 0 0 25px yellow, 0 0 5px cyan;
        background: linear-gradient(to top, red, yellow);
        background-clip: text;
        color: transparent;
    }
    #tabel tr,td{
        border:2px solid black;
    }
    #tabel td{
        border:2px solid black;
    }
    .judul2{
        position:absolute;
        font-family:"cooper black";
        top:-50px;
        left:0px;
        font-size:40px;
        animation: jalankan1;
        animation-duration:2s;
        animation-iteration-count:infinite;
        animation-direction:alternate;
    }
    @keyframes jalankan1{
        0%{color:white;text-shadow:0px 0px 5px black;}
        100%{color:black;text-shadow:1px 1px 2px white, 0 0 25px yellow, 0 0 5px cyan;}
    }
    #text_area_1, #text_area_2, #text_area_3, #text_area_4, #text_area_5, #text_area_6{
        border:2px solid black;
        font-family:"commic sans ms";
        font-size:20px;
    }
    button.e7nj0r415{
        background-color:black;
        width:25px;
        height:25px;
        border:2px solid yellow;
        border-radius:4px;
        display:block;
    }
    button.e7nj0r41:hover{
        background-color: blue;
    }
    button.e7nj0r41>span{
        color:white;
    }
    div[data-testid="stMarkdownContainer"]>p{
        color:black;
    }
    div.st-emotion-cache-1qrd9al>p{
        color:black;
    }
    div.st-emotion-cache-1vsah7k>p{
        color:white;
        background-color:black;
    }
    </style>
    """, unsafe_allow_html=True)
st.markdown("<div id='posisi'><span>F</span>ives</div>",unsafe_allow_html=True)
if st.sidebar.button("🚀Masukan identitas Anda"):
    pass
if "nama" not in st.session_state:
    st.session_state["nama"]=""
if "NIM" not in st.session_state:
    st.session_state["NIM"]=""        
st.session_state.nama = st.sidebar.text_input("Masukan Nama Anda",value = st.session_state.nama)
st.session_state.NIM = st.sidebar.text_input("Masukan Nim Anda", value = st.session_state.NIM)
if st.sidebar.button("FACT/FAKTA",icon='📖',use_container_width=True,key="coba"):
    st.markdown("<div class='judul2'>FACT</div>",unsafe_allow_html=True)
    tab = st.tabs(["1. Membaca Teks","2. Contoh Fakta-fakta","3. Tanya Jawab", "4. Menyampaikan","5. Membahas","6. Penguatan (Teks dan Video)", "7. Tuliskan"])
    with tab[0]:
        st.markdown("<div id='judul'>Manfaat Energi Listrik Dalam Kehidupan</div>",unsafe_allow_html=True)
        st.markdown("""<div class='isi'>
    Listrik adalah daya atau kekuatan yang ditimbulkan oleh adanya pergesekan 
    atau melalui proses kimia, dapat digunakan untuk menghasilkan panas atau 
    cahaya, atau untuk menjalankan mesin.Listrik merupakan salah satu 
    kebutuhan yang sangat diperlukan oleh masyarakat. Sekarang ini, hampir 
    seluruh tempat sudah menggunakan listrik sebagai penunjang kehidupan sehari-hari. 
    Dengan demikian, kita dapat melihat betapa pentingnya listrik dalam meningkatkan 
    kesejahteraan manusia. Listrik memudahkan banyak hal dalam kehidupan sehari-hari, 
    mulai dari memberikan penerangan, pemanas, pendingin udara, alat elektronik, 
    dan sebagainya. Energi listrik dapat dihasilkan dari berbagai sumber, 
    termasuk melalui reaksi kimia dalam baterai, melalui tenaga air dalam pembangkit 
    listrik hidroelektrik, atau melalui pembakaran bahan bakar fosil dalam pembangkit listrik. 
    </div>""",unsafe_allow_html=True)
        st.markdown("""<div class='isi'>
    Salah satu manfaat listrik yang paling besar ialah sebagai sumber tenaga untuk penerangan.
    Lampu listrik yang digunakan di rumah, kantor, dan jalan raya membantu meningkatkan 
    visibilitas dan membuat kita lebih mudah dalam melakukan berbagai aktivitas 
    pada malam hari. Selain itu, lampu LED yang efisien juga dapat menghemat energi dan 
    meminimalkan konsumsi listrik. Dengan penerangan yang stabil dan terjamin, kita dapat 
    melanjutkan aktivitas kita tanpa gangguan, seperti membaca buku, bekerja di malam hari, 
    atau melakukan pekerjaan rumah tangga. Listrik juga berfungsi sebagai penghasil panas 
    yang sangat berguna dalam kehidupan sehari-hari. Kompor listrik, rice cooker, dan setrika 
    listrik adalah contoh peralatan yang menggunakan listrik untuk menghasilkan panas. 
    Dengan menggunakan peralatan ini, kita dapat memasak makanan dengan lebih cepat dan mudah, 
    serta menjaga pakaian tetap rapi tanpa harus menggunakan bahan bakar tradisional yang 
    berpotensi membahayakan lingkungan. Selain itu, peralatan ini juga lebih mudah digunakan 
    dan membersihkan karena tidak ada asap atau sisa bahan bakar yang perlu dibersihkan. 
    </div>""",unsafe_allow_html=True)
        st.markdown("""<div class='isi'>
    Selain penerangan dan penghasil panas, listrik juga digunakan sebagai penghasil gerak. 
    Mesin pompa air, mesin cuci, dan peralatan elektronik lainnya menggunakan listrik untuk
     beroperasi. Dengan demikian, kita dapat menghemat waktu dan tenaga dalam melakukan 
    pekerjaan rumah tangga, seperti mencuci pakaian dan membersihkan rumah. Selain itu, 
    peralatan elektronik yang menggunakan listrik juga dapat meningkatkan efisiensi dalam 
    berbagai aspek kehidupan, seperti pengolahan makanan dan pengolahan data.
    </div>""",unsafe_allow_html=True)
    with tab[6]:
        st.markdown("""<div class='isian'>
    Silakan tuliskan hal-hal penting yang terdapat dalam teks bacaan, pada kolom berikut!
    (siapkan beberapa kolom untuk para siswa menuliskan hal-hal penting dari bacaan)
    </div>""",unsafe_allow_html=True)
        st.components.v1.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                #masukan1{{
                    width:300px;
                    height:100px;
                    border:1px solid black;
                    border-radius:10px;
                    margin:5px;
                }}
                #kirim{{
                    font-family:'brush script mt';
                    font-size:12px;
                    padding:3px;
                    margin:5px;
                    font-size:20px;
                    background-color:pink;     
                }}
                
            </style>
        </head>
        <body>
        <div id="komentar" style="color:red; font-family:'Times New Roman';font-size:18px">Masukan Jawaban</div>
        <div style="margin:5px">
            <label for="nama" style="font-family:'Times New Roman';font-weight:bold">Nama: </label>
            <input type="text" id="idnama" name="nama" value={st.session_state.nama}>
        </div>
        <div style="margin:5px">
            <label for="nim" style="font-family:'Times New Roman';font-weight:bold">NIM: </label>
            <input type="text" id="idnim" name="nim" value={st.session_state.NIM}>
        </div>
        <textarea name="masuk1" id="masuk1" rows="8" cols="50"></textarea><br>
        <button id="kirim">Kirim</button>
        <script type="module">
        // Firebase configuration
        const firebaseConfig = {{
            apiKey: "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
            authDomain: "percobaan-pertama-ae4ff.firebaseapp.com",
            databaseURL: "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
            projectId: "percobaan-pertama-ae4ff",
            storageBucket: "percobaan-pertama-ae4ff.firebasestorage.app",
            messagingSenderId: "298037230291",
            appId: "1:298037230291:web:73839320cd74cc9dba3226",
            measurementId: "G-BSVCLVBYX6"
        }};

            // Initialize Firebase
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
        import {{ getDatabase, ref, set  }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        document.getElementById("kirim").addEventListener("click",()=>{{
            const nama = document.getElementById("idnama").value
            const nim = document.getElementById("idnim").value
            set(ref(db, 'masukan1/'+nim ), {{
                indikator: "Fakta",
                soal:"1. Silakan tuliskan hal-hal penting yang terdapat dalam teks bacaan, pada kolom berikut! (siapkan beberapa kolom untuk para siswa menuliskan hal-hal penting dari bacaan) ",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk1").value
            }})
            .then(()=>{{
                alert("Sudah Masuk")}})
            .catch((error)=>{{
                alert(error)
            }})

        }})
    
        </script>

        </body>
        </html>
        """,height=1000)        
    with tab[4]:
        st.markdown("""<div class='isian'>
    Membahas fakta-fakta penting (Guru dan Siswa membahas fakta-fakta penting yang terdapat 
    dalam teks bacaan. Mulailah dari tingkatan domain Taksonomi kemampuan berpikir dalam 
    menuliskan fakta dari teks bacaan.
    </div>""",unsafe_allow_html=True)
        st.components.v1.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                #masukan1{{
                    width:300px;
                    height:100px;
                    border:1px solid black;
                    border-radius:10px;
                    margin:5px;
                }}
                #kirim{{
                    font-family:'Times New Roman';
                    font-size:12px;
                    padding:3px;
                    margin:5px;
                    font-size:20px;
                    background-color:pink;     
                }}
                
            </style>
        </head>
        <body>
        <div id="komentar" style="color:red; font-family:'snap itc';font-size:18px">Masukan Jawaban</div>
        <div style="margin:5px">
            <label for="nama" style="font-family:'comic sans ms';font-weight:bold">Nama: </label>
            <input type="text" id="idnama" name="nama" value={st.session_state.nama}>
        </div>
        <div style="margin:5px">
            <label for="nim" style="font-family:'comic sans ms';font-weight:bold">NIM: </label>
            <input type="text" id="idnim" name="nim" value={st.session_state.NIM}>
        </div>
        <textarea name="masuk1" id="masuk1" rows="8" cols="50"></textarea><br>
        <button id="kirim">Kirim</button>
        <script type="module">
        // Firebase configuration
        const firebaseConfig = {{
            apiKey: "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
            authDomain: "percobaan-pertama-ae4ff.firebaseapp.com",
            databaseURL: "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
            projectId: "percobaan-pertama-ae4ff",
            storageBucket: "percobaan-pertama-ae4ff.firebasestorage.app",
            messagingSenderId: "298037230291",
            appId: "1:298037230291:web:73839320cd74cc9dba3226",
            measurementId: "G-BSVCLVBYX6"
        }};

            // Initialize Firebase
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
        import {{ getDatabase, ref, set  }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        document.getElementById("kirim").addEventListener("click",()=>{{
            const nama = document.getElementById("idnama").value
            const nim = document.getElementById("idnim").value
            set(ref(db, 'masukan2/'+nim ), {{
                indikator: "Fakta",
                soal:"2. Membahas fakta-fakta penting (Guru dan Siswa membahas fakta-fakta penting yang terdapat dalam teks bacaan. Mulailah dari tingkatan domain Taksonomi kemampuan berpikir dalam menuliskan fakta dari teks bacaan.",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk1").value
            }})
            .then(()=>{{
                alert("Sudah Masuk")}})
            .catch((error)=>{{
                alert(error)
            }})

        }})
    
        </script>

        </body>
        </html>
        """,height=1000)  
        
    with tab[5]:
        st.markdown("""<div class='isian'>
    Lengkapi teks dengan video singkat atau slide-slide yang menunjang teks tersebut
    </div>""",unsafe_allow_html=True)
        st.components.v1.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                #masukan1{{
                    width:300px;
                    height:100px;
                    border:1px solid black;
                    border-radius:10px;
                    margin:5px;
                }}
                #kirim{{
                    font-family:'brush script mt';
                    font-size:12px;
                    padding:3px;
                    margin:5px;
                    font-size:20px;
                    background-color:pink;     
                }}
                
            </style>
        </head>
        <body>
        <div id="komentar" style="color:red; font-family:'snap itc';font-size:18px">Masukan Jawaban</div>
        <div style="margin:5px">
            <label for="nama" style="font-family:'comic sans ms';font-weight:bold">Nama: </label>
            <input type="text" id="idnama" name="nama" value={st.session_state.nama}>
        </div>
        <div style="margin:5px">
            <label for="nim" style="font-family:'comic sans ms';font-weight:bold">NIM: </label>
            <input type="text" id="idnim" name="nim" value={st.session_state.NIM}>
        </div>
        <textarea name="masuk1" id="masuk1" rows="8" cols="50"></textarea><br>
        <button id="kirim">Kirim</button>
        <script type="module">
        // Firebase configuration
        const firebaseConfig = {{
            apiKey: "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
            authDomain: "percobaan-pertama-ae4ff.firebaseapp.com",
            databaseURL: "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
            projectId: "percobaan-pertama-ae4ff",
            storageBucket: "percobaan-pertama-ae4ff.firebasestorage.app",
            messagingSenderId: "298037230291",
            appId: "1:298037230291:web:73839320cd74cc9dba3226",
            measurementId: "G-BSVCLVBYX6"
        }};

            // Initialize Firebase
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
        import {{ getDatabase, ref, set  }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        document.getElementById("kirim").addEventListener("click",()=>{{
            const nama = document.getElementById("idnama").value
            const nim = document.getElementById("idnim").value
            set(ref(db, 'masukan3/'+nim ), {{
                indikator: "Fakta",
                soal:"3. Lengkapi teks dengan video singkat atau slide-slide yang menunjang teks tersebut ",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk1").value
            }})
            .then(()=>{{
                alert("Sudah Masuk")}})
            .catch((error)=>{{
                alert(error)
            }})

        }})
    
        </script>

        </body>
        </html>
        """,height=1000)  
    with tab[2]:
        st.markdown("""<div class='isian'>
    Melakukan tanya jawab mengenai fakta-fakta dalam tayangan media tambahan. 
    </div>""",unsafe_allow_html=True)
        st.components.v1.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                #masukan1{{
                    width:300px;
                    height:100px;
                    border:1px solid black;
                    border-radius:10px;
                    margin:5px;
                }}
                #kirim{{
                    font-family:'brush script mt';
                    font-size:12px;
                    padding:3px;
                    margin:5px;
                    font-size:20px;
                    background-color:pink;     
                }}
                
            </style>
        </head>
        <body>
        <div id="komentar" style="color:red; font-family:'snap itc';font-size:18px">Masukan Jawaban</div>
        <div style="margin:5px">
            <label for="nama" style="font-family:'comic sans ms';font-weight:bold">Nama: </label>
            <input type="text" id="idnama" name="nama" value={st.session_state.nama}>
        </div>
        <div style="margin:5px">
            <label for="nim" style="font-family:'comic sans ms';font-weight:bold">NIM: </label>
            <input type="text" id="idnim" name="nim" value={st.session_state.NIM}>
        </div>
        <textarea name="masuk1" id="masuk1" rows="8" cols="50"></textarea><br>
        <button id="kirim">Kirim</button>
        <script type="module">
        // Firebase configuration
        const firebaseConfig = {{
            apiKey: "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
            authDomain: "percobaan-pertama-ae4ff.firebaseapp.com",
            databaseURL: "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
            projectId: "percobaan-pertama-ae4ff",
            storageBucket: "percobaan-pertama-ae4ff.firebasestorage.app",
            messagingSenderId: "298037230291",
            appId: "1:298037230291:web:73839320cd74cc9dba3226",
            measurementId: "G-BSVCLVBYX6"
        }};

            // Initialize Firebase
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
        import {{ getDatabase, ref, set  }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        document.getElementById("kirim").addEventListener("click",()=>{{
            const nama = document.getElementById("idnama").value
            const nim = document.getElementById("idnim").value
            set(ref(db, 'masukan4/'+nim ), {{
                indikator: "Fakta",
                soal:"4. Melakukan tanya jawab mengenai fakta-fakta dalam tayangan media tambahan.",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk1").value
            }})
            .then(()=>{{
                alert("Sudah Masuk")}})
            .catch((error)=>{{
                alert(error)
            }})

        }})
    
        </script>

        </body>
        </html>
        """,height=1000)  
    with tab[1]:
        st.markdown("""<div class='isian'>
    Memberikan contoh fakta-fakta faktual dari bacaan dikaitkan dengan 
    hal-hal yang diketahui siswa. 
    </div>""",unsafe_allow_html=True)
        st.components.v1.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                #masukan1{{
                    width:300px;
                    height:100px;
                    border:1px solid black;
                    border-radius:10px;
                    margin:5px;
                }}
                #kirim{{
                    font-family:'brush script mt';
                    font-size:12px;
                    padding:3px;
                    margin:5px;
                    font-size:20px;
                    background-color:pink;     
                }}
                
            </style>
        </head>
        <body>
        <div id="komentar" style="color:red; font-family:'snap itc';font-size:18px">Masukan Jawaban</div>
        <div style="margin:5px">
            <label for="nama" style="font-family:'comic sans ms';font-weight:bold">Nama: </label>
            <input type="text" id="idnama" name="nama" value={st.session_state.nama}>
        </div>
        <div style="margin:5px">
            <label for="nim" style="font-family:'comic sans ms';font-weight:bold">NIM: </label>
            <input type="text" id="idnim" name="nim" value={st.session_state.NIM}>
        </div>
        <textarea name="masuk1" id="masuk1" rows="8" cols="50"></textarea><br>
        <button id="kirim">Kirim</button>
        <script type="module">
        // Firebase configuration
        const firebaseConfig = {{
            apiKey: "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
            authDomain: "percobaan-pertama-ae4ff.firebaseapp.com",
            databaseURL: "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
            projectId: "percobaan-pertama-ae4ff",
            storageBucket: "percobaan-pertama-ae4ff.firebasestorage.app",
            messagingSenderId: "298037230291",
            appId: "1:298037230291:web:73839320cd74cc9dba3226",
            measurementId: "G-BSVCLVBYX6"
        }};

            // Initialize Firebase
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
        import {{ getDatabase, ref, set  }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        document.getElementById("kirim").addEventListener("click",()=>{{
            const nama = document.getElementById("idnama").value
            const nim = document.getElementById("idnim").value
            set(ref(db, 'masukan5/'+nim ), {{
                indikator: "Fakta",
                soal:"5. Memberikan contoh fakta-fakta faktual dari bacaan dikaitkan dengan hal-hal yang diketahui siswa.",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk1").value
            }})
            .then(()=>{{
                alert("Sudah Masuk")}})
            .catch((error)=>{{
                alert(error)
            }})

        }})
    
        </script>

        </body>
        </html>
        """,height=1000)  
    with tab[3]:
        st.markdown("""<div class='isian'>
    Mintalah siswa menyampaikan fakta-fakta yang ditemukannya 
    </div>""",unsafe_allow_html=True)
        st.components.v1.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                #masukan1{{
                    width:300px;
                    height:100px;
                    border:1px solid black;
                    border-radius:10px;
                    margin:5px;
                }}
                #kirim{{
                    font-family:'brush script mt';
                    font-size:12px;
                    padding:3px;
                    margin:5px;
                    font-size:20px;
                    background-color:pink;     
                }}
                
            </style>
        </head>
        <body>
        <div id="komentar" style="color:red; font-family:'snap itc';font-size:18px">Masukan Jawaban</div>
        <div style="margin:5px">
            <label for="nama" style="font-family:'comic sans ms';font-weight:bold">Nama: </label>
            <input type="text" id="idnama" name="nama" value={st.session_state.nama}>
        </div>
        <div style="margin:5px">
            <label for="nim" style="font-family:'comic sans ms';font-weight:bold">NIM: </label>
            <input type="text" id="idnim" name="nim" value={st.session_state.NIM}>
        </div>
        <textarea name="masuk1" id="masuk1" rows="8" cols="50"></textarea><br>
        <button id="kirim">Kirim</button>
        <script type="module">
        // Firebase configuration
        const firebaseConfig = {{
            apiKey: "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
            authDomain: "percobaan-pertama-ae4ff.firebaseapp.com",
            databaseURL: "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
            projectId: "percobaan-pertama-ae4ff",
            storageBucket: "percobaan-pertama-ae4ff.firebasestorage.app",
            messagingSenderId: "298037230291",
            appId: "1:298037230291:web:73839320cd74cc9dba3226",
            measurementId: "G-BSVCLVBYX6"
        }};

            // Initialize Firebase
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
        import {{ getDatabase, ref, set  }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        document.getElementById("kirim").addEventListener("click",()=>{{
            const nama = document.getElementById("idnama").value
            const nim = document.getElementById("idnim").value
            set(ref(db, 'masukan6/'+nim ), {{
                indikator: "Fakta",
                soal:"6. Mintalah siswa menyampaikan fakta-fakta yang ditemukannya",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk1").value
            }})
            .then(()=>{{
                alert("Sudah Masuk")}})
            .catch((error)=>{{
                alert(error)
            }})

        }})
    
        </script>

        </body>
        </html>
        """,height=1000)  
if st.sidebar.button("2. INFERENCES/SIMPULAN",icon='📖',use_container_width=True,key="coba1"):
    st.markdown("<div class='judul2'>INFERENCES/SIMPULAN</div>",unsafe_allow_html=True)
    st.markdown("""<div class='judul1'>Sambungan dari Fact, teksnya yang dipakai di bagian F</div>""",unsafe_allow_html=True)
    with st.expander("Tanya Jawab"):
        st.markdown("""<div class="isikan">
        Tanya jawab mengenai isi bacaan, menggunakan petunjuk atau kata-kata 
        kunci dalam teks dan menggunakannya untuk memberikan jawaban atas pertanyaan-pertanyaan 
        pada tanya jawab.</div>
    """,unsafe_allow_html=True)
        st.components.v1.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                #masukan1{{
                    width:300px;
                    height:100px;
                    border:1px solid black;
                    border-radius:10px;
                    margin:5px;
                }}
                #kirim{{
                    font-family:'brush script mt';
                    font-size:12px;
                    padding:3px;
                    margin:5px;
                    font-size:20px;
                    background-color:pink;     
                }}
                
            </style>
        </head>
        <body>
        <div id="komentar" style="color:red; font-family:'snap itc';font-size:18px">Masukan Jawaban</div>
        <div style="margin:5px">
            <label for="nama" style="font-family:'comic sans ms';font-weight:bold">Nama: </label>
            <input type="text" id="idnama" name="nama" value={st.session_state.nama}>
        </div>
        <div style="margin:5px">
            <label for="nim" style="font-family:'comic sans ms';font-weight:bold">NIM: </label>
            <input type="text" id="idnim" name="nim" value={st.session_state.NIM}>
        </div>
        <textarea name="masuk1" id="masuk1" rows="8" cols="50"></textarea><br>
        <button id="kirim">Kirim</button>
        <script type="module">
        // Firebase configuration
        const firebaseConfig = {{
            apiKey: "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
            authDomain: "percobaan-pertama-ae4ff.firebaseapp.com",
            databaseURL: "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
            projectId: "percobaan-pertama-ae4ff",
            storageBucket: "percobaan-pertama-ae4ff.firebasestorage.app",
            messagingSenderId: "298037230291",
            appId: "1:298037230291:web:73839320cd74cc9dba3226",
            measurementId: "G-BSVCLVBYX6"
        }};

            // Initialize Firebase
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
        import {{ getDatabase, ref, set  }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        document.getElementById("kirim").addEventListener("click",()=>{{
            const nama = document.getElementById("idnama").value
            const nim = document.getElementById("idnim").value
            set(ref(db, 'masukan7/'+nim ), {{
                indikator: "Simpulan",
                soal:"1. Tanya jawab mengenai isi bacaan, menggunakan petunjuk atau kata-kata kunci dalam teks dan menggunakannya untuk memberikan jawaban atas pertanyaan-pertanyaan pada tanya jawab",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk1").value
            }})
            .then(()=>{{
                alert("Sudah Masuk")}})
            .catch((error)=>{{
                alert(error)
            }})

        }})
    
        </script>

        </body>
        </html>
        """,height=280)  
    with st.expander("Menghubungkan latar belakang pengetahuan "):
        st.markdown("""<div class="isikan">
        Menghubungkan latar belakang pengetahuan siswa dengan informasi 
        yang ada dalam teks bacaan</div>
    """,unsafe_allow_html=True)
        st.components.v1.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                #masukan1{{
                    width:300px;
                    height:100px;
                    border:1px solid black;
                    border-radius:10px;
                    margin:5px;
                }}
                #kirim{{
                    font-family:'brush script mt';
                    font-size:12px;
                    padding:3px;
                    margin:5px;
                    font-size:20px;
                    background-color:pink;     
                }}
                
            </style>
        </head>
        <body>
        <div id="komentar" style="color:red; font-family:'snap itc';font-size:18px">Masukan Jawaban</div>
        <div style="margin:5px">
            <label for="nama" style="font-family:'comic sans ms';font-weight:bold">Nama: </label>
            <input type="text" id="idnama" name="nama" value={st.session_state.nama}>
        </div>
        <div style="margin:5px">
            <label for="nim" style="font-family:'comic sans ms';font-weight:bold">NIM: </label>
            <input type="text" id="idnim" name="nim" value={st.session_state.NIM}>
        </div>
        <textarea name="masuk1" id="masuk1" rows="8" cols="50"></textarea><br>
        <button id="kirim">Kirim</button>
        <script type="module">
        // Firebase configuration
        const firebaseConfig = {{
            apiKey: "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
            authDomain: "percobaan-pertama-ae4ff.firebaseapp.com",
            databaseURL: "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
            projectId: "percobaan-pertama-ae4ff",
            storageBucket: "percobaan-pertama-ae4ff.firebasestorage.app",
            messagingSenderId: "298037230291",
            appId: "1:298037230291:web:73839320cd74cc9dba3226",
            measurementId: "G-BSVCLVBYX6"
        }};

            // Initialize Firebase
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
        import {{ getDatabase, ref, set  }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        document.getElementById("kirim").addEventListener("click",()=>{{
            const nama = document.getElementById("idnama").value
            const nim = document.getElementById("idnim").value
            set(ref(db, 'masukan8/'+nim ), {{
                indikator: "Simpulan",
                soal:"2. Menghubungkan latar belakang pengetahuan siswa dengan informasi yang ada dalam teks bacaan",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk1").value
            }})
            .then(()=>{{
                alert("Sudah Masuk")}})
            .catch((error)=>{{
                alert(error)
            }})

        }})
    
        </script>

        </body>
        </html>
        """,height=280)
    with st.expander("Berdasarkan fakta-fakta yang telah ditulis"):
        st.markdown("""<div class="isikan">
       Berdasarkan fakta-fakta yang telah ditulis, siswa diajak untuk mencoba menyimpulkan isi bacaan secara implisit/tersirat. 
        Kegiatan menyimpulkan berdasarkan: Inference = tc/ teks dalam buku + (pengalaman + pengetahuan siswa).
        </div>
    """,unsafe_allow_html=True)
        st.components.v1.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                #masukan1{{
                    width:300px;
                    height:100px;
                    border:1px solid black;
                    border-radius:10px;
                    margin:5px;
                }}
                #kirim{{
                    font-family:'brush script mt';
                    font-size:12px;
                    padding:3px;
                    margin:5px;
                    font-size:20px;
                    background-color:pink;     
                }}
                
            </style>
        </head>
        <body>
        <div id="komentar" style="color:red; font-family:'snap itc';font-size:18px">Masukan Jawaban</div>
        <div style="margin:5px">
            <label for="nama" style="font-family:'comic sans ms';font-weight:bold">Nama: </label>
            <input type="text" id="idnama" name="nama" value={st.session_state.nama}>
        </div>
        <div style="margin:5px">
            <label for="nim" style="font-family:'comic sans ms';font-weight:bold">NIM: </label>
            <input type="text" id="idnim" name="nim" value={st.session_state.NIM}>
        </div>
        <textarea name="masuk1" id="masuk1" rows="8" cols="50"></textarea><br>
        <button id="kirim">Kirim</button>
        <script type="module">
        // Firebase configuration
        const firebaseConfig = {{
            apiKey: "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
            authDomain: "percobaan-pertama-ae4ff.firebaseapp.com",
            databaseURL: "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
            projectId: "percobaan-pertama-ae4ff",
            storageBucket: "percobaan-pertama-ae4ff.firebasestorage.app",
            messagingSenderId: "298037230291",
            appId: "1:298037230291:web:73839320cd74cc9dba3226",
            measurementId: "G-BSVCLVBYX6"
        }};

            // Initialize Firebase
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
        import {{ getDatabase, ref, set  }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        document.getElementById("kirim").addEventListener("click",()=>{{
            const nama = document.getElementById("idnama").value
            const nim = document.getElementById("idnim").value
            set(ref(db, 'masukan9/'+nim ), {{
                indikator: "Simpulan",
                soal:"3. Berdasarkan fakta-fakta yang telah ditulis, siswa diajak untuk mencoba menyimpulkan isi bacaan secara implisit/tersirat. Kegiatan menyimpulkan berdasarkan: Inference = tc/ teks dalam buku + (pengalaman + pengetahuan siswa)",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk1").value
            }})
            .then(()=>{{
                alert("Sudah Masuk")}})
            .catch((error)=>{{
                alert(error)
            }})

        }})
    
        </script>

        </body>
        </html>
        """,height=280)
    with st.expander("Siswa menyimpulkan "):
        st.markdown("""<div class="isikan">
       Siswa menyimpulkan isi teks bacaan dengan cara mengaitkan isi teks dengan pengalaman 
        dan pengetahun siswa yang telah dimiliki, dengan menggunakan bahasa siswa 
        sendiri.
        </div>
    """,unsafe_allow_html=True)
        st.components.v1.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                #masukan1{{
                    width:300px;
                    height:100px;
                    border:1px solid black;
                    border-radius:10px;
                    margin:5px;
                }}
                #kirim{{
                    font-family:'brush script mt';
                    font-size:12px;
                    padding:3px;
                    margin:5px;
                    font-size:20px;
                    background-color:pink;     
                }}
                
            </style>
        </head>
        <body>
        <div id="komentar" style="color:red; font-family:'snap itc';font-size:18px">Masukan Jawaban</div>
        <div style="margin:5px">
            <label for="nama" style="font-family:'comic sans ms';font-weight:bold">Nama: </label>
            <input type="text" id="idnama" name="nama" value={st.session_state.nama}>
        </div>
        <div style="margin:5px">
            <label for="nim" style="font-family:'comic sans ms';font-weight:bold">NIM: </label>
            <input type="text" id="idnim" name="nim" value={st.session_state.NIM}>
        </div>
        <textarea name="masuk1" id="masuk1" rows="8" cols="50"></textarea><br>
        <button id="kirim">Kirim</button>
        <script type="module">
        // Firebase configuration
        const firebaseConfig = {{
            apiKey: "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
            authDomain: "percobaan-pertama-ae4ff.firebaseapp.com",
            databaseURL: "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
            projectId: "percobaan-pertama-ae4ff",
            storageBucket: "percobaan-pertama-ae4ff.firebasestorage.app",
            messagingSenderId: "298037230291",
            appId: "1:298037230291:web:73839320cd74cc9dba3226",
            measurementId: "G-BSVCLVBYX6"
        }};

            // Initialize Firebase
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
        import {{ getDatabase, ref, set  }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        document.getElementById("kirim").addEventListener("click",()=>{{
            const nama = document.getElementById("idnama").value
            const nim = document.getElementById("idnim").value
            set(ref(db, 'masukan10/'+nim ), {{
                indikator: "Simpulan",
                soal:"4. Siswa menyimpulkan isi teks bacaan dengan cara mengaitkan isi teks dengan pengalaman dan pengetahun siswa yang telah dimiliki, dengan menggunakan bahasa siswa sendiri.",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk1").value
            }})
            .then(()=>{{
                alert("Sudah Masuk")}})
            .catch((error)=>{{
                alert(error)
            }})

        }})
    
        </script>

        </body>
        </html>
        """,height=280)
    with st.expander("Menyimpulkan isi bacaan "):
        st.markdown("""<div class="isikan">
       Menyimpulkan isi bacaan dapat dilakukan dengan cara 
        berkolaborasi dalam kelompok dengan dipandu oleh lembar kerja
        </div>
    """,unsafe_allow_html=True)
        st.components.v1.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                #masukan1{{
                    width:300px;
                    height:100px;
                    border:1px solid black;
                    border-radius:10px;
                    margin:5px;
                }}
                #kirim{{
                    font-family:'brush script mt';
                    font-size:12px;
                    padding:3px;
                    margin:5px;
                    font-size:20px;
                    background-color:pink;     
                }}
                
            </style>
        </head>
        <body>
        <div id="komentar" style="color:red; font-family:'snap itc';font-size:18px">Masukan Jawaban</div>
        <div style="margin:5px">
            <label for="nama" style="font-family:'comic sans ms';font-weight:bold">Nama: </label>
            <input type="text" id="idnama" name="nama" value={st.session_state.nama}>
        </div>
        <div style="margin:5px">
            <label for="nim" style="font-family:'comic sans ms';font-weight:bold">NIM: </label>
            <input type="text" id="idnim" name="nim" value={st.session_state.NIM}>
        </div>
        <textarea name="masuk1" id="masuk1" rows="8" cols="50"></textarea><br>
        <button id="kirim">Kirim</button>
        <script type="module">
        // Firebase configuration
        const firebaseConfig = {{
            apiKey: "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
            authDomain: "percobaan-pertama-ae4ff.firebaseapp.com",
            databaseURL: "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
            projectId: "percobaan-pertama-ae4ff",
            storageBucket: "percobaan-pertama-ae4ff.firebasestorage.app",
            messagingSenderId: "298037230291",
            appId: "1:298037230291:web:73839320cd74cc9dba3226",
            measurementId: "G-BSVCLVBYX6"
        }};

            // Initialize Firebase
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
        import {{ getDatabase, ref, set  }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        document.getElementById("kirim").addEventListener("click",()=>{{
            const nama = document.getElementById("idnama").value
            const nim = document.getElementById("idnim").value
            set(ref(db, 'masukan11/'+nim ), {{
                indikator: "Simpulan",
                soal:"5. Menyimpulkan isi bacaan dapat dilakukan dengan cara berkolaborasi dalam kelompok dengan dipandu oleh lembar kerja",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk1").value
            }})
            .then(()=>{{
                alert("Sudah Masuk")}})
            .catch((error)=>{{
                alert(error)
            }})

        }})
    
        </script>

        </body>
        </html>
        """,height=280)
    with st.expander("Siswa mempresentasikan "):
        st.markdown("""<div class="isikan">
       Siswa mempresentasikan hasil menyimpulkan teks bacaan, 
        baik secara individu maupun kelompok.
        </div>
    """,unsafe_allow_html=True)
        st.components.v1.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                #masukan1{{
                    width:300px;
                    height:100px;
                    border:1px solid black;
                    border-radius:10px;
                    margin:5px;
                }}
                #kirim{{
                    font-family:'brush script mt';
                    font-size:12px;
                    padding:3px;
                    margin:5px;
                    font-size:20px;
                    background-color:pink;     
                }}
                
            </style>
        </head>
        <body>
        <div id="komentar" style="color:red; font-family:'snap itc';font-size:18px">Masukan Jawaban</div>
        <div style="margin:5px">
            <label for="nama" style="font-family:'comic sans ms';font-weight:bold">Nama: </label>
            <input type="text" id="idnama" name="nama" value={st.session_state.nama}>
        </div>
        <div style="margin:5px">
            <label for="nim" style="font-family:'comic sans ms';font-weight:bold">NIM: </label>
            <input type="text" id="idnim" name="nim" value={st.session_state.NIM}>
        </div>
        <textarea name="masuk1" id="masuk1" rows="8" cols="50"></textarea><br>
        <button id="kirim">Kirim</button>
        <script type="module">
        // Firebase configuration
        const firebaseConfig = {{
            apiKey: "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
            authDomain: "percobaan-pertama-ae4ff.firebaseapp.com",
            databaseURL: "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
            projectId: "percobaan-pertama-ae4ff",
            storageBucket: "percobaan-pertama-ae4ff.firebasestorage.app",
            messagingSenderId: "298037230291",
            appId: "1:298037230291:web:73839320cd74cc9dba3226",
            measurementId: "G-BSVCLVBYX6"
        }};

            // Initialize Firebase
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
        import {{ getDatabase, ref, set  }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        document.getElementById("kirim").addEventListener("click",()=>{{
            const nama = document.getElementById("idnama").value
            const nim = document.getElementById("idnim").value
            set(ref(db, 'masukan12/'+nim ), {{
                indikator: "Simpulan",
                soal:"6. Siswa mempresentasikan hasil menyimpulkan teks bacaan, baik secara individu maupun kelompok",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk1").value
            }})
            .then(()=>{{
                alert("Sudah Masuk")}})
            .catch((error)=>{{
                alert(error)
            }})

        }})
    
        </script>

        </body>
        </html>
        """,height=280)
if st.sidebar.button("3. VOCABULARY/KOSA KATA",icon='📖',use_container_width=True,key="coba2"):
    st.markdown("<div class='judul2'>VOCABULARY/KOSA KATA</div>",unsafe_allow_html=True)
    st.markdown("""<div class='judul1'>Bagian ini boleh dibantu dengan gambar, video, bagan dll yang interaktif 
                sehingga siswa mampu mamahami beberapa 
                kosa kata</div>""",unsafe_allow_html=True)
    kolom = st.columns(2,vertical_alignment='center', border=True)
    with kolom[0]:
        st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1738676791/langkah1_dhtgdm.png")
    with kolom[1]:
        st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1738676870/langkah2_cvnzor.png")
    with st.expander("Vocabulary "):
        st.markdown("""
        <div class="isikan">
            <ol>
                <li>Sebelum kegiatan membaca, guru memilih kata-kata baru yang kemungkinan sulit menurut siswa</li>
                <li>Bersama-sama mengidentifikasi  kata-kata sulit dalam teks 
                    (berkolaborasi dalam kelompok)</li>
                <li>Mempelajari kata-kata sulit dalam teks bacaan menggunakan kamus</li>
                <li>Siswa dalam kelompoknya mendiskusikan kata-kata sulit dengan menyamakan persepsi 
                    pada kelompoknya</li>
                <li>Saling berbagi kata-kata sulit dan artinya antarkelompok</li>
                <li>Menjelaskan dan membahasa arti kata-kata sulit</li>
                <li>Memberikan contoh penerapan kata-kata sulit dalam kalimat. Kegiatan ini dengan 
                    cara menuliskan kata-kata sulit berdasarkan 5W + 1H, dan contoh/noncontoh kalimat berdasarkan beberapa kata sulit, sesuai bagan berikut.
                    (bantu tampilan dg kolom-kolom yang akan diisi oleh kata-kata sulit yan akan dibuat kalimat. Kolomnya berisi: 
                    pilihan kata, apa, siapa, bagaimana, mengapa. Ditambah kolom contoh dan kolom bukan contoh)
                </li>
            </ol>
        </div>
        """,unsafe_allow_html=True)
if st.sidebar.button("EXPERIENCE/PENGALAMAN",icon='📖',use_container_width=True,key="coba3"):
    st.markdown("<div class='judul2'>EXPERIENCE/PENGALAMAN</div>",unsafe_allow_html=True)
    st.markdown("""<div class='judul1'>Bagian ini menyambungkan materi dengan teks, gambar, video pada 
                tahapan sebelumnya, dikaitkan dengan pengetahuan dan 
                pengalaman siswa sebelumnya.</div>""",unsafe_allow_html=True)
    with st.expander("bagian1"):
        st.markdown("""
        <div class="isikan">
            <ol>
                <li>Membuat hubungan/koneksi bacaan dengan pengalaman. Guru mengarahkan siswa untuk mengaitkan isi bacaan dengan pengalamannya</li>
                <li>Menghubungkan teks dengan pengalaman pribadi siswa</li>
                <li>Menghubungkan teks dengan pengetahuan umum</li>
                <li>Menghubungkan dan membandingkan teks dengan teks lain misalnya pada : buku lain, film, video, program TV, dll.</li>
            </ol>
        </div>
        """,unsafe_allow_html=True)

    st.markdown("""<div class='judul1'>(Kegiatan ini bisa dibantu dengan disediakan kolom/tabel seperti berikut, untuk diisi siswa)</div>""",unsafe_allow_html=True)
    st.markdown("""
    <table id="tabel">
            <tr>
                <th colspan=2>Nama:</th>
            </tr>
            <tr>
                <th colspan=2>Judul Bacaan:</th>
            </tr>
            <tr>
                <td>Informasi dalam Teks</td>
                <td>Yang diingat oleh saya</td>
            </tr>
            <tr>
                <td>1. ...</td>
                <td>...</td>
            </tr>
            <tr>
                <td>2. ...</td>
                <td>...</td>
            </tr>
            <tr>
                <td>3. ...</td>
                <td>...</td>
            </tr>
            <tr>
                <td>4. ...</td>
                <td>...</td>
            </tr>
            <tr>
                <td>5. ...</td>
                <td>...</td>
            </tr>
            <tr>
                <td>dll</td>
                <td></td>
            </tr>
    </table>
    """, unsafe_allow_html=True)
    st.components.v1.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <style>
                #masukan1{{
                    width:300px;
                    height:100px;
                    border:1px solid black;
                    border-radius:10px;
                    margin-top:5px;
                    
                }}
                #masuk1, #masuk2{{
                   margin-right:2px;
                }}
                #kirim{{
                    font-family:'brush script mt';
                    font-size:12px;
                    padding:3px;
                    margin:5px;
                    font-size:20px;
                    background-color:pink;     
                }}
                
            </style>
        </head>
        <body>
        <div id="komentar" style="color:red; font-family:'snap itc';font-size:18px">Masukan Jawaban</div>
        <div style="margin:5px">
            <label for="nama" style="font-family:'comic sans ms';font-weight:bold">Nama: </label>
            <input type="text" id="idnama" name="nama" value={st.session_state.nama}>
        </div>
        <div style="margin:5px">
            <label for="nim" style="font-family:'comic sans ms';font-weight:bold">NIM: </label>
            <input type="text" id="idnim" name="nim" value={st.session_state.NIM}>
        </div>
        <div style="display:flex">
            <div>Isi informasi dalam teks <textarea name="masuk1" id="masuk1" rows="8" cols="50"></textarea></div>
            <div>yang diingat oleh saya <textarea name="masuk2" id="masuk2" rows="8" cols="50"></textarea></div>
        </div>
        <button id="kirim">Kirim</button>
        <script type="module">
        // Firebase configuration
        const firebaseConfig = {{
            apiKey: "AIzaSyC9vDQ3wyq1Z4rqre7tVdvZRmUt8TGomo4",
            authDomain: "percobaan-pertama-ae4ff.firebaseapp.com",
            databaseURL: "https://percobaan-pertama-ae4ff-default-rtdb.firebaseio.com",
            projectId: "percobaan-pertama-ae4ff",
            storageBucket: "percobaan-pertama-ae4ff.firebasestorage.app",
            messagingSenderId: "298037230291",
            appId: "1:298037230291:web:73839320cd74cc9dba3226",
            measurementId: "G-BSVCLVBYX6"
        }};

            // Initialize Firebase
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-app.js";
        import {{ getDatabase, ref, set  }} from "https://www.gstatic.com/firebasejs/11.4.0/firebase-database.js";

        const app = initializeApp(firebaseConfig);
        const db = getDatabase(app);

        document.getElementById("kirim").addEventListener("click",()=>{{
            const nama = document.getElementById("idnama").value
            const nim = document.getElementById("idnim").value
            set(ref(db, 'masukan13/'+nim ), {{
                indikator: "Pengalaman",
                soal: "1. Isi Informasi dalam Teks",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk1").value
            }})
            set(ref(db, 'masukan14/'+nim ), {{
                indikator: "Pengalaman",
                soal: "2. yang diingat oleh saya",
                nama: nama,
                nim: nim,
                tulisan: document.getElementById("masuk2").value
            }})
            .then(()=>{{
                alert("Sudah Masuk")}})
            .catch((error)=>{{
                alert(error)
            }})

        }})
    
        </script>

        </body>
        </html>
        """,height=280)
    with st.expander("bagian2"):
        st.markdown("""
        <div class="isikan">
            <ol start=5>
                <li>Presentasi hasil diskusi</li>
                <li>Membahas hasil diskusi</li>
            </ol>
        </div>
        """,unsafe_allow_html=True)
if st.sidebar.button("SUMMARY/RINGKASAN",icon='📖',use_container_width=True,key="coba4"):
    st.markdown("<div class='judul2'>SUMMARY/RINGKASAN</div>",unsafe_allow_html=True)
    st.markdown("""<div class='judul1'>Pada tahapan ini, siswa membuat ringkasan dari teks 
                bacaan yang telah dipahami</div>""",unsafe_allow_html=True)
    with st.expander("Summary"):
        st.markdown("""
        <div class="isikan">
            <ol>
                <li>Membuat hubungan/koneksi bacaan dengan pengalaman. Guru mengarahkan siswa untuk mengaitkan isi bacaan dengan pengalamannya</li>
                <li>Menghubungkan teks dengan pengalaman pribadi siswa</li>
                <li>Menghubungkan teks dengan pengetahuan umum</li>
                <li>Menghubungkan dan membandingkan teks dengan teks lain misalnya pada : buku lain, film, video, program TV, dll.</li>
            </ol>
        </div>
        """,unsafe_allow_html=True)








