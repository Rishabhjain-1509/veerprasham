from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


Bl = list()

for i in range(1,25):
    Bl.append(str(i))


@app.route("/Vande Viram Magazine")
def magazine():
    return render_template("Vande Viram Magazine.html",Bl = Bl)


# making list of MS
MSL = ["P P sadhuhi bhagvant", "Surdasseth Ni Pole", "Sarkari Upashrya", "Shamlani Pole",
       "Sushil-Bhakti-Lalitprabhashriji", "Anandshriji M.S", "Gyanshriji M.S. ka Pariwar",
       "Pada Pole Upashrya", "Mitraprabhashriji M.s", "Ramnikshriji M.S", "Chandralatashriji M.S",
       "Samyakgunashriji M.S", "Kalpdarshitashriji M.S"]

List = ['PP' , 'SP' ,'SU', 'SM' , 'SB' , 'AM' , 'GM', 'PU' , 'MS', 'RM' , 'CM' , 'SKM' , 'KDM']
@app.route("/List")
def list():
    return render_template("List.html", MSL=MSL , List = List , len = len(List) )



#1 P P sadhuhi Bhagvant
mspp = ["P.P.A.V.Shri Bhanuchandrasurishwerji M", "Gacha.P.P.A.V.Shri Hemprabhsurishwerji M",
        "P.P.A.V.Shri Padamsurishwerji M",
        "P.P.A.Vijay Shri Arihantsidhsurishwerji M", "P.P.aachary bhagvant"]
mspp.sort()
@app.route("/MSPP")
def PP():
    return render_template("MSPP.html", len=len(mspp), mspp=mspp)




#2 Ni pole
SNP = ["Nirupamashriji M", "Divyaprabhashriji M.S",
        "Anilashriji M","Suyashashriji M","Rajratnashriji M","Amitpragnashriji M","Chandrakalashriji M",
        "Amitashriji M", "Saddgunashriji M"]
SNP.sort()
@app.route("/SNP")
def SP():
    return render_template("SNP.html", len=len(SNP), SNP=SNP)

#3 Ni pole
SUP = ["Nirupamashriji M", "Divyaprabhashriji M.S",
        "Anilashriji M","Suyashashriji M","Rajratnashriji M","Amitpragnashriji M","Chandrakalashriji M",
        "Amitashriji M", "Saddgunashriji M"]
SUP.sort()
@app.route("/SUP")
def SU():
    return render_template("SUP.html", len=len(SUP), SNP=SUP)


#4 Sham Pole
SMP = ["Bhasvaryashashriji M", "Divyayashashriji M",
        "Charuyashashriji M"]
SMP.sort()
@app.route("/SMP")
def SM():
    return render_template("SMP.html", len=len(SMP), SMP=SMP)



#5. Sushil-Bhakti-Lalitprabhashriji
SBL = ["Lalitprabhashriji M","Snehlatashriji M","Harshprabhashriji M",
       "Vishvapurnashriji M","Lakshagunashriji M","Harshitpragnashriji M","Kalpshilashriji M",
       "Kalpratnashriji M","Shasandarshnashriji M","Rashmirekhashriji M","Mokshapriyashriji M","Amitmalashriji M",
       "Mokshmalashriji M"]
SBL.sort()
@app.route("/SBL")
def SB():
    return render_template("SBL.html", len=len(SBL), SBL = SBL)



#6. Anandshriji M.S
AMS = ["Padmlatashriji M","Kusumprabhashriji M","Sheelvatishriji M",
       "Sanjaymalashriji M","Sarswatishriji M"]
AMS.sort()
@app.route("/AMS")
def AM():
    return render_template("AMS.html", len = len(AMS), AMS = AMS)




#7. Gyanshriji M.S. ka Pariwar
GMS = ["Anandshriji M","Chandrakalashriji M", "Kusumprabhashriji M"]
GMS.sort()
@app.route("/GMS")
def GM():
    return render_template("GMS.html", len=len(GMS), GMS = GMS)





#8.Pada Pole Upashrya
PPU = ["Kirtipurnashriji M"]
PPU.sort()
@app.route("/PPU")
def PU():
    return render_template("PPU.html", len=len(PPU), PPU = PPU)



#9 Mitraprabhashriji M.s
MMS = ["Mitraprabhashriji M"]
MMS.sort()
@app.route("/MMS")
def MS():
    return render_template("MMS.html", len=len(MMS), MMS = MMS)



#10. Ramnikshriji M.S
RMS = ["Manjulashriji M","Ramnikshriji M"]
RMS.sort()
@app.route("/RMS")
def RM():
    return render_template("RMS.html", len=len(RMS), RMS = RMS)



#11. Chandralatashriji M.S
CMS = ["Chandralatashriji M"]
CMS.sort()
@app.route("/CMS")
def CM():
    return render_template("CMS.html", len=len(CMS), CMS = CMS)



#12. Samyakgunashriji M.S
SKMS = ["Samyakgunashriji M"]
SKMS.sort()
@app.route("/SKMS")
def SKM():
    return render_template("SKMS.html", len=len(SKMS), SKMS = SKMS)



#13. Kalpdarshitashriji M.S
KDMS = ["Chintandarshitashriji M.S."]
KDMS.sort()
@app.route("/KDMS")
def KDM():
    return render_template("KDMS.html", len=len(KDMS), KDMS = KDMS)










@app.route("/Gallary")
def gallary():
    return render_template("Gallary.html")










def image():
    return ('static/images/book/1.png')










@app.route("/Contact")
def contact():
    return render_template("Contact.html")


if __name__ == "__main__":
    app.run()
