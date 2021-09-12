import tkinter as tk #Βιβλιοθήκη για δημιουργία GUI
from tkinter import ttk #Πρόσθετα της βιβλιοθήκης GUI
from random import randint  #Βιβλιοθήκη για δημιουργία τυχαίου ακεραίου
import winsound #module αναπαραγωγής ήχων
import time #Βιβλιοθήκη για εργασίες με χρόνο (time.sleep)
import threading    #threading ώστε να μην παγώνει το πρόγραμμα όταν εργαζόμαστε με συναρτήσεις χρόνου
#Γραμμές 1-6, οι απαραίτητες βιβλιοθήκες

root = tk.Tk()  #Κεντρικό παράθυρο
root.geometry("705x600")  # Μεγέθος παραθύρου
root.resizable(False, False)  # Κλείδωμα παραθύρου
root.title("PyFlashcards")  #Τίτλος που εμφανίζεται πάνω αριστερά


pointsds = 0    #Πόντοι δομών δεδομένων
pointsmath = 0  #Πόντοι μαθηματικού λογισμού
pointscs = 0    #Πόντοι επιστήμης υπολογιστών
pointspr = 0    #πόντοι εισαγωγής στον προγραμματισμό
pointspr2 = 0   #πόντοι προγραμματισμού υπολογιστών
pointspy = 0    #πόντοι εφαρμοσμένου προγραμματισμού με Python
pointspb = 0    #πόντοι πιθανοτήτων
pointshum = 0   #πόντοι πληροφορικής στις ανθρωπιστικές επιστήμες
pointslin = 0   #πόντοι γραμμικής άλγεβρας
pointsdm = 0    #πόντοι διακριτών μαθηματικών
totalpoints = pointshum + pointspb + pointsdm + pointspy + pointspr2 + pointspr + pointscs + pointsds + pointslin + pointsmath  #συνολικοί πόντοι (σύστημα πόντων)
pointscreated = 0   #πόντοι παιχνιδιού με κάρτες διάφορες των προσφερομένων μαθημάτων


class quest:
    def __init__(self, q, ra, wa1, wa2):  # Κλάση ερωτήσεων, με ολα τα στοιχεία που αποτελούν την κάρτα (ερώτηση και σετ απαντήσεων)
        self.q = q  #ερώτηση
        self.ra = ra    #σωστή απάντηση
        self.wa1 = wa1  #πρώτη λανθασμένη απάντηση
        self.wa2 = wa2  #δεύτερη λανθασμένη


class user: #κλάση δημιουργίας καρτών απο τον χρήστη για μαθήματα διάφορα των προσφερομένων
    def __init__(self, subj, uq, ura, uwa1, uwa2):
        self.subj = subj    #μάθημα
        self.uq = uq    #ερώτηση
        self.ura = ura  #σωστή απάντηση
        self.uwa1 = uwa1    #πρώτη λάθος απάντηση
        self.uwa2 = uwa2    #δεύτερη λάθος απάντηση




userquestion = tk.StringVar()   #ερώτηση
userright = tk.StringVar()  #σωστή απάντηση
userwrong1 = tk.StringVar()  # Μεταβλητές των Entry Box δημιουργίας καρτών μαθήματος διάφορου απο τα προσφερόμενα (Γραμμές 48-52) #πρώτη λάθος απάντηση
userwrong2 = tk.StringVar() #δεύτερη λάθος απάντηση
usersubj = tk.StringVar()   #μάθημα

createquestion = tk.StringVar() #μεταβλητές των Entry Box πρόσθεσης καρτών σε προσφερόμενο μάθημα, ερώτηση
createright = tk.StringVar()    #σωστή απάντηση
createwrong1 = tk.StringVar()   #πρώτη λάθος απάντηση
createwrong2 = tk.StringVar()   #δεύτερη λάθος απάντηση

modifyquestion = tk.StringVar() #μεταβλητές των Entry Box τροποποίησης καρτών μαθήματος, ερώτηση
modifyright = tk.StringVar()    #σωστή απάντηση
modifyw1 = tk.StringVar()       #πρώτη λάθος απάντηση
modifyw2 = tk.StringVar()       #δεύτερη λάθος απάντηση

userqstn = []
playlist = []   #λίστα δημιουργημένων απο τον χρήστη κάρτες, διαφόρου μαθήματος απο τα προσφερόμενα
mathright = []  #λίστα που περιέχει μια σωστά απαντημένη κάρτα μαθηματικού λογισμού
mathwrong = []  #λίστα που περιέχει μια λάθος απαντημένη κάρτα μαθηματικού λογισμού
dsright = []    #λίστα που περιέχει μια σωστά απαντημένη κάρτα δομών δεδομένων
dswrong = []    #λίστα που περιέχει μια λάθος απαντημένη κάρτα δομών δεδομένων
csright = []    #λίστα που περιέχει μια σψστά απαντημένη κάρτα επιστήμης υπολογιστών
cswrong = []    #λίστα που περιέχει μια λάθος απαντημένη κάρτα επιστήμης υπολογιστών
dmright = []    #λίστα που περιέχει μια σωστά απαντημένη κάρτα διακριτών μαθηματικων
dmwrong = []    #λίστα που περιέχει μια λάθος απαντημένη κάρτα διακριτών μαθηματικών
humright = []   #λίστα που περιέχει μια σωστά απαντημένη κάρτα πληροφορικής στις ανθρωπιστικές επιστήμες
humwrong = []   #λίστα που περιέχει μια λάθος απαντημένη κάρτα πληροφορικής στις ανθρωπιστικές επιστήμες
linright = []   #λίστα που περιέχει μια σωστά απαντημένη κάρτα γραμμικής άλγεβρας
linwrong = []   #λίστα που περιέχει μια λάθος απαντημένη κάρτα γραμμικής άλγεβρας
prright = []    #λίστα που περιέχει μια σωστά απαντημένη κάρτα εισαγωγής στον προγραμματισμό
prwrong = []    #λίστα που περιέχει μια λάθος απαντημένη κάρτα εισαγωγής στον προγραμματισμό
pr2right = []   #λίστα που περιέχει μια σωστά απαντημένη κάρτα προγραμματισμού υπολογιστών
pr2wrong = []   #λίστα που περιέχει μια λάθος απαντημένη κάρτα προγραμματισμού υπολογιστών
pyright = []    #λίστα που περιέχει μια σωστά απαντημένη κάρτα εφαρμοσμένου προγραμματιμού με python
pywrong = []    #λίστα που περιέχει μια λάθος απαντημένη κάρτα εφαρσμοσμένου προγραμματισμού με python
pbright = []    #λίστα που περιέχει μια σωστά απαντημένη κάρτα πιθανοτήτων
pbwrong = []    #λίστα που περιέχει μια λάθος απαντημένη κάρτα πιθανοτήτων
playlistright = []  #λίστα που περιέχει μια σωστά απαντημένη κάρτα διαφόρου μαθήματος απο τα προσφερόμενα
playlistwrong = []  #λίστα που περιέχει μια λάθος απαντημένη κάρτα διαφόρου μαθήματος απο τα προσφερόμενα
#Γραμμές 65-87, όλες οι λίστες που χρησιμοποιούνται για την παραλλαγή του συστήματος του Leitner
dq = [] #λίστα καρτών δομών δεδομένων
dq.append(quest("Ένα δένδρο είναι ειδική περίπτωση γράφου?", "Ναι", "Οχι","Ισχύει το αντίστροφο"))    # Γραμμές 89-158: Γέμισμα λιστών με ερωτήσεις σε όλες τις κατηγορίες
dq.append(quest("Η στατική δομή δεδομένων έχει:", "Όλες τις επιλογές", "Σταθερό μέγεθος", "Συγκεκριμένα στοιχεία"))
dq.append(quest("Ποιά η μη γραμμική δομή δεδομένων?", "Γράφος", "Πίνακας", "Ουρά"))
dq.append(quest("Η συνάρτηση 2n είναι της κλάσης:", "O(n)", "O(2n)", "O(n^2)"))
dq.append(quest("Σε ποιά αναζήτηση ο πίνακας πρέπει να είναι ταξινομημένος?", "Δυαδική", "Σειριακή", "Καμία"))
#σε όλες τις κατηγορίες πρόκειται για λίστες αντικειμένων με την σειρά να είναι ερώτηση,σωστή απάντηση, πρώτη λάθος και δεύτερη λάθος απάντηση
#όμως δεν εμφανίζονται με την ίδια σειρά σε όλες τις κατηγορίες ώστε ο χρήστης να μην γνωρίζει το μοτίβο
mathq = []  #λίστα καρτών μαθηματικού λογισμού

mathq.append(quest("Ποιά είναι η πρώτη παράγωγος,ως πρός x, της συνάρτησης f(x,y)=4xy?", "4x", "4y","4xy"))
mathq.append(quest("Ποιά είναι η πρώτη παράγωγος,ως προς y, της συνάρτησης f(x,y)=4xy?", "4y", "4x","4yx"))
mathq.append(quest("Ποιά είναι η σύνταξη της μικτής παραγώγου ως προς x?", "df/dxdy", "dx/dfdy", "dy/dfdx"))
mathq.append(quest("Ποιά είναι η σύνταξη της μικτής παραγώγου ως προς y?", "df/dydx", "dx/dfdy", "dy/dfdx"))

linq = []   #λίστα καρτών γραμμικής άλγεβρας
linq.append(quest("Τι σημαίνει vector?", "Πίνακας", "Διάνυσμα", "Τίποτα"))
linq.append(quest("Τι σημαίνει η μηδενική γραμμή για διανύσματα?", "Εξαρτημένα", "Ανεξάρτητα", "Τίποτα"))
linq.append(quest("Πως συμβολίζεται η διάσταση?", "Dim", "Row", "Col"))
linq.append(quest("Πως συμβολίζεται το ίχνος πίνακα?", "Tr", "Col", "Kerf"))
csq = []        #λίστα καρτών επιστήμης υπολογιστών
csq.append(quest("Πόσο κάνει 0 OR 1?", "1", "0", "Τίποτα"))
csq.append(quest("Πόσο κάνει 1 OR 1?", "1", "0", "Τίποτα"))
csq.append(quest("Πόσο κάνει 0 AND 0 ?", "0", "1", "Τίποτα"))
csq.append(quest("Η πύλη ονομάζεται:", " Λογική", "Αληθείας", "Τίποτα"))
csq.append(quest("Τι λειτουργεία επιτελούν οι καταχωρητές?", "Όλα", "Data in", "Data out"))
csq.append(quest("Ποια εντολή εκτελείται πρώτη στον λεγόμενο κύκλο της μηχανής?", "Fetch", "Execute", "Decode"))
csq.append(quest("Σε ποια μορφή αποθηκεύονται τα δεδομένα στους καταχωρητές και στην μνήμη;", "Δυαδική", "Οκταδική", "Δεκαεξαδική"))
csq.append(quest("Σύμφωνα με την ανατομία ενός byte που βρίσκεται το λιγότερο σημαντικό bit?", "Δεξιά", "Αριστερά", "Στην μέση"))
pbq = []    #λίστα καρτών πιθανοτήτων
pbq.append(quest("Αν VAR X=1, VARY=2, VAR(2Y+3X)=?", "Τίποτα", "0", "7"))
pbq.append(quest("Αν ACB:", "A+B", "Μόνο Β", "Μόνο Α"))
pbq.append(quest("Για να συμβεί Α+Β", "Α,Β ανεξάρτητα", "Εξαρτημένα", "Τίποτα"))
pbq.append(quest("COV(X+Y)=0 Aν", "Χ,Υ ανεξάρτητα", "εξαρτημένα", "τίποτα"))
prq = []    #λίστα καρτών εισαγωγής στον προγραμματισμό
prq.append(quest("Τι είναι array?", "Πίνακας", "Πίνακας", "Τίποτα"))
prq.append(quest("Πώς ελέγχεται μια συνθήκη?", "if", "switch", "while"))
prq.append(quest("Πώς ορίζεται νέος τύπος δεδομένων?", "typedef", "array", "len"))
prq.append(quest("Πώς επιτυγχάνεται ανταλλαγή τιμών?", "με temp", "με = ", "με ->"))
pr2q = []   #λίστα καρτών προγραμματισμού υπολογιστών
pr2q.append(quest("Τι ανήκει στη C++?", "Κλάση", "Tuple", "Κανένα"))
pr2q.append(quest("Πως δεσμεύεται δυναμικά μνήμη?", "new", "delete", "malloc"))
pr2q.append(quest("Πως διαγράφεται δεσμευμένη μνήμη?", "delete", "sizeof", "Κανένα"))
pr2q.append(quest("Πως ανατίθεται τιμή σε μεταβλητή?", "=", "==", "&"))
pyq = []    #λίστα καρτών εφαρμοσμένου προγραμματισμού με Python
pyq.append(quest("Που δεν αλλάζουν τα στοιχεία?", "Tuple", "List", "Array"))
pyq.append(quest("Που εφαρμόζεται το namespace?", "Dictionary", "List", "Tuple"))
pyq.append(quest("Κάθε αντικείμενο έχει data type?", "Ναι", "Οχι", "Μερικά"))
pyq.append(quest("Χρειάζονται όλες οι κλάσεις __init__?", "Ναι", "Οχι", "Μερικές"))
pyq.append(quest("Μια συμβολοσειρά παραμένει αμετάβλητη?", "Ναι", "Οχι", "Εξαρτάται την χρήση"))
pyq.append(quest("Ποιος τελεστής έχει μεγαλύτερη ιεραρχία?", "**", "%", "&"))
pyq.append(quest("x = 36 / 4 * (3 + 2) * 4 + 2", "182.0", "117", "37"))
pyq.append(quest("listOne = [20, 40, 60, 80], listTwo = [20, 40, 60, 80],print(listOne == listTwo),print(listOne is listTwo)", "Αληθής Ψευδής", "Αληθής Αληθής", "Ψευδής Αληθής"))
pyq.append(quest("for i in range(10, 15, 1):, print( i, end=' , ')", "10, 11, 12, 13, 14,", "10, 11, 12, 13,", "τιποτα από τα παραπάνω"))

humq = []   #λίστα καρτών πληροφορικής στις ανθρωπιστικές επιστήμες
humq.append(quest("Με ποιό ελέγχεται η ευφυία ενός συστήματος?", "Test turing", "Με κριτή", "Με κανένα"))
humq.append(quest("Τι χρησιμοποιείται για 3D γραφικά?", "Unity 3D", "MS Paint", "GoogleSketch"))
humq.append(quest("Πώς δημιουργείται το προφίλ ενός επισκέπτη μουσείου?", "Χρόνος σε εκθέματα", "Κίνηση χώρου", "Κανένα"))
humq.append(quest("Πως συμβολίζεται το μέσο μήκος πρότασης", "ΜΜΠ", "MSL", "MMS"))
humq.append(quest("Tι από τα παρακάτω αποτελεί χαρακτηριστικό της web 2.0 φάσης της εξέλιξης του ιστού, και δεν υπήρχε στην φάση web 1.0?", "Όλα", "Υπερσύνδεσμοι στις σελίδες", "Live feed"))
humq.append(quest("Ποιά από τα παρακάτω χαρακτηριστικά ανήκουν στην μορφή της ασύγχρονης τηλεκπαίδευσης?", "Μονόδρομη επικοινωνία", "Live επικοινωνία", "Απαίτηση εξοπλισμού"))
humq.append(quest("Ποιό από τα παρακάτω πρωτόκολλα εγγυάται την αξιόπιστη λήψη των δεδομένων από τον παραλήπτη στο διαδίκτυο;", "TCP", "HTTP", "IP"))
humq.append(quest("Απο που παρέχονται, στην στατιστική προσέγγιση στην Γλωσσική Τεχνολογία, οι κανόνες που διέπουν τα φαινόμενα μιας γλώσσας?", "Απο παραδείγματα", "Απο γλωσσολόγους ", "Απο επιστήμονες πληροφορικής"))

dmq = []    #λίστα καρτών διακριτών μαθηματικών
dmq.append(quest("Τι είναι αντίστοιχο του ολοκληρώματος?", "Άθροισμα", "Ακολουθία", "Διαφορά"))
dmq.append(quest("Τι είναι αντίστοιχο της παραγώγου?", "Διαφορά", "Ακολουθία", "Ολοκλήρωμα"))
dmq.append(quest("Πώς μένουν τα στοιχεία μετά απο κυκλική διάταξη?", "Ίδια", "Διαφορετικά", "Ανακατεμένα"))
dmq.append(quest("Υπάρχει αόριστο άθροισμα?", "Ναι", "Οχι", "Δεν ορίζεται"))



#ΥΠΟΜΝΗΜΑ: ran=right answer(κουμπί), wan1=wrong answer 1(κουμπί), wan2=wrong answer 2(κουμπί), lab2=label2(η ερώτηση,ετικέτα)
def domes():  # Γραμμές 163-960: Συναρτήσεις εμφάνισης των μαθημάτων
    winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME) #ηχητικό εφέ κουμπιού, όταν για παράδειγμα αλλάζουμε κάρτα

    if (len(dq) != 0):
        x = randint(0, len(dq) - 1) #ορισμός του εύρους παραγωγής τυχαίου αριθμού, απο 0 εως το μέγεθος της λίστας -1 και χρησιμοποίηση σαν δείκτης (απόλυτη τυχαιότητα)

        def button1():  #συνάρτηση που καλείται όταν απαντηθεί σωστά μια κάρτα
            global pointsds
            global totalpoints
            pointsds += 1   #αύξηση πόντων της συγκεκριμένης κατηγορίας
            totalpoints += pointsds #αλλαγή στους συνολικούς πόντους

            if (len(dq) != 0):
                dsright.append(quest(dq[x].q, dq[x].ra, dq[x].wa1, dq[x].wa2))  #σε περίπτωση σωστής απάντησης, η κάρτα μεταφέρεται σε εφεδρική λίστα
                dq.pop(x)   #και φεύγει για ορισμένο χρονικό διάστημα απο την κύρια λίστα ώστε να μην εμφανίζεται

            winsound.PlaySound("correct.wav", winsound.SND_FILENAME)    #ηχητικό εφέ σωστής απάντησης

            def correct():  # Γραμμές 181-208: Σύστημα επανεμφάνισης καρτών με βάση το σύστημα του Leitner(Υπάρχει σε όλες τις συναρτήσεις μαθημάτων, επακριβώς ίδιο οπότε δεν αναφέρεται παρακάτω)
                time.sleep(60)  #αναμονή 60 δευτερολέπτων
                if (len(dsright) != 0):
                    dq.extend(dsright)      #και μετά απο 60 δευτερόλεπτα η κάρτα επιστρέφει στη βασική λίστα

                if (x in dsright and len(dsright) != 0):
                    dsright.pop(x)  #αφαίρεση της προηγουμένως σωστά απαντηθείσας κάρτας απο την εφεδρική λίστα

            pu = threading.Thread(target=correct)   #threading, ώστε να μην παγώσει όλο το πρόγραμμα η συνάρτηση time.sleep
            pu.start()
            domes()

        def button2():  #συνάρτηση που καλείται σε περίπτωση λανθασμένης απάντησης
            dswrong.append(quest(dq[x].q, dq[x].ra, dq[x].wa1, dq[x].wa2))  #μεταφορά της λανθασμένης κάρτας σε εφεδρική λίστα
            dq.pop(x)   #αφαίρεση της απο την βασική λίστα
            winsound.PlaySound("wrong.wav", winsound.SND_FILENAME)  #ηχητικό εφέ λανθασμένης απάντησης

            def incorrect():

                time.sleep(25)      #αντίστοιχα σε λάθος απάντηση, η κάρτα τοποθετείται σε εφεδρική λίστα και επιστρέφει στην κύρια μετά απο 25 δευτερόλεπτα
                if (len(dswrong) != 0):
                    dq.extend(dswrong)
                if (x in dswrong and len(dswrong) != 0):
                    dswrong.pop(x)

            pu2 = threading.Thread(target=incorrect)    #hreading ώστε να μην παγώσει όλο το πρόγραμμα
            pu2.start()
            domes()

        hide()  #κατατροφή όλων των άλλων παραθύρων ώστε να μην εμφανιστούν πάνω απο το τρέχον παράθυρο
        domesf.grid()
        if (len(dq) == 0):
            lb = tk.Label(domesf, text="Δομές Δεδομένων", font=("Consolas", 10), background="black",
                          foreground="blue").grid(row=0, column=2, pady=10) #ετικέτα μαθήματος
            lb2 = tk.Label(domesf, text="Περίμενε ώστε να επιστρέψουν οι κάρτες", font=("Consolas", 10),
                           background="black", foreground="blue").grid(row=2, column=2, pady=10)    #ετικέτα ειδοποίησης σε περίπτωση άδειας λίστας
            b = ttk.Button(domesf, text="Επόμενο μάθημα", command=math, image=img13).grid(row=5, column=3, pady=12) #κουμπί μεταφοράς στο επόμενο μάθημα
        else:
            labm = tk.Label(domesf, text='Δομές Δεδομένων', font=("Consolas", 10), background="black",foreground="blue").grid(row=0, column=2, pady=10)
            lab = tk.Label(domesf, image=img24, background="black", font=("Consolas", 10)).grid(row=1, column=2,pady=10, padx=160)  #ετικέτα μαθήματος
            lab2 = tk.Message(domesf, text=dq[x].q, background="black", foreground="white", font=("Consolas", 10)).grid( row=1, column=2, pady=10, padx=160)#ετικέτα ερώτησης
            wan1 = tk.Button(domesf, text=dq[x].wa1, command=button2, wraplength=90, height=2, width=9,
                            font=("Consolas", 10), background="black", foreground="white", relief="solid").grid(row=3,
                                                                                                                column=1,
                                                                                                                pady=50,
                                                                                                                padx=12)#κουμπί λάθος απάντησης
            ran = tk.Button(domesf, text=dq[x].ra, command=button1, wraplength=90, height=2, width=9,
                             font=("Consolas", 10), background="black", foreground="white", relief="solid").grid(row=3,
                                                                                                                 column=2,
                                                                                                                 pady=50,
                                                                                                                 padx=12)#κουμπί σωστής απάντησης
            wan2 = tk.Button(domesf, text=dq[x].wa2, command=button2, wraplength=90, height=2, width=9,
                             font=("Consolas", 10), background="black", foreground="white", relief="solid").grid(row=3,
                                                                                                                 column=3,
                                                                                                                 pady=50,
                                                                                                                 padx=12)#κουμπί λάθος απάντησης
            b2 = tk.Button(domesf, text="Επόμενη ερώτηση", command=domes, wraplength=90, height=2, width=9,font=("Consolas", 10), background="black", foreground="white", relief="solid").grid(row=4,column=2,pady=20,padx=10)
            b = ttk.Button(domesf, text="Επόμενο μάθημα", command=math, image=img13).grid(row=5, column=3, pady=12)#κουμπί μεταφοράς στο επόμενο μάθημα
#απο εδώ και πέρα, σχόλια για τα επόμενα μαθήματα θα υπάρχουν μονάχα όπου υπάρχει διαφοροποίηση σε σχέση με το μάθημα στις γραμμές 163-238
#αυτό, διότι όλες οι τεχνικές παραμένουν ακριβώς οι ίδιες (ηχητικά εφέ, συναρτήσεις και κλήση τους, ετικέτες, κουμπιά) και αλλάζουν μόνο οι χρησιμοποιούμενες λίστες
def math(): #math: mathematic calculus
    winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
    if (len(mathq) != 0):   #λίστα μαθηματικού λογισμού
        x = randint(0, len(mathq) - 1)

        def button1():
            global pointsmath
            global totalpoints
            pointsmath += 1 #αλλαγή πόντων μαθήματος
            totalpoints += pointsmath
            if (len(mathq) != 0):
                mathright.append(quest(mathq[x].q, mathq[x].ra, mathq[x].wa1, mathq[x].wa2))   #mathright: λίστα σωστής απάντησης μαθ. λογισμού
                mathq.pop(x)
            winsound.PlaySound("correct.wav", winsound.SND_FILENAME)

            def correct():
                time.sleep(60)
                if (len(mathright) != 0):
                    mathq.extend(mathright)

                if (x in mathright and len(mathright) != 0):
                    mathright.pop(x)

            pu = threading.Thread(target=correct)
            pu.start()
            math()

        def button2():
            mathwrong.append(quest(mathq[x].q, mathq[x].ra, mathq[x].wa1, mathq[x].wa2))    #mathwrong: λίστα λάθος απαντημένης κάρτας μαθ. λογισμού
            mathq.pop(x)
            winsound.PlaySound("wrong.wav", winsound.SND_FILENAME)

            def incorrect():
                time.sleep(25)

                if (len(mathwrong) != 0):
                    mathq.extend(dswrong)

                if (x in mathwrong and len(mathwrong) != 0):
                    mathwrong.pop(x)

            pu2 = threading.Thread(target=incorrect)
            pu2.start()
            math()

        hide()
        mathf.grid()
        if (len(mathq) == 0):
            lb = tk.Label(mathf, text="Μαθηματικός λογισμός", font=("Consolas", 10), background="black",
                          foreground="blue").grid(row=0, column=2, pady=10)
            lb2 = tk.Label(mathf, text="Περίμενε ώστε να επιστρέψουν οι κάρτες", font=("Consolas", 10),
                           background="black", foreground="blue").grid(row=2, column=2, pady=10)
            b = ttk.Button(mathf, text="Επόμενο μάθημα", command=lin, image=img13).grid(row=5, column=3, pady=12)
        else:
            labm = tk.Label(mathf, text="Μαθηματικός Λογισμός", font=("Consolas", 10), background="#006400",
                            foreground="white").grid(row=0, column=2, pady=10)
            lab = tk.Label(mathf, image=img24, font=("Consolas", 10), background="#006400").grid(row=1, column=2,
                                                                                                 pady=10, padx=160)
            lab2 = tk.Message(mathf, text=mathq[x].q, font=("Consolas", 10), background="#006400",
                              foreground="white").grid(row=1, column=2, pady=10, padx=160)
            ran = tk.Button(mathf, text=mathq[x].ra, command=button1, wraplength=100, height=2, width=9,
                            font=("Consolas", 10), background="#006400", foreground="white", relief="solid").grid(row=3,
                                                                                                                  column=1,
                                                                                                                  pady=50,
                                                                                                                  padx=12)#κουμπί σωστής απάντησης
            wan1 = tk.Button(mathf, text=mathq[x].wa1, command=button2, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#006400", foreground="white", relief="solid").grid(
                row=3, column=2, pady=50, padx=12)  #κουμπί πρώτης λάθος απάντησης
            wan2 = tk.Button(mathf, text=mathq[x].wa2, command=button2, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#006400", foreground="white", relief="solid").grid(
                row=3, column=3, pady=50, padx=12) #κουμπί δεύτερης λάθος απάντησης
            b2 = tk.Button(mathf, text="Επόμενη ερώτηση", command=math, wraplength=100, height=2, width=9,
                           font=("Consolas", 10), background="#006400", foreground="white", relief="solid").grid(row=4,
                                                                                                                 column=2,
                                                                                                                 pady=20,
                                                                                                                 padx=12)
            b = ttk.Button(mathf, text="Επόμενο μάθημα", command=lin, image=img13).grid(row=5, column=3, pady=12)
            b = ttk.Button(mathf, text="Προηγούμενο μάθημα", command=domes, image=img25).grid(row=5, column=1, pady=12)
        #διαφορές σε σχέση με το μάθημα των δομών δεδομένων: η αλλαγμένη σειρά των κουμπιών απαντήσεων


def lin():  #lin: linear algebra
    winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
    if (len(linq) != 0):    #λίστα γραμμικής άλγεβρας
        x = randint(0, len(linq) - 1)

        def button1():
            global pointslin
            global totalpoints
            pointslin += 1
            totalpoints += pointslin

            linright.append(quest(linq[x].q, linq[x].ra, linq[x].wa1, linq[x].wa2))
            linq.pop(x)
            winsound.PlaySound("correct.wav", winsound.SND_FILENAME)

            def correct():
                time.sleep(60)

                if (len(linright) != 0):
                    linq.extend(linright)

                if (x in linright and len(linright) != 0):
                    linright.pop(x)

            pu = threading.Thread(target=correct)
            pu.start()
            lin()

        def button2():

            linwrong.append(quest(linq[x].q, linq[x].ra, linq[x].wa1, linq[x].wa2))
            linq.pop(x)
            winsound.PlaySound("wrong.wav", winsound.SND_FILENAME)

            def incorrect():
                time.sleep(25)
                if (len(linwrong) != 0):
                    linq.extend(linwrong)
                if (x in linwrong and len(linwrong) != 0):
                    linwrong.pop(x)

            pu2 = threading.Thread(target=incorrect)
            pu2.start()
            lin()

        hide()
        linf.grid()
        if (len(linq) == 0):
            lb = tk.Label(linf, text="Γραμμική άλγεβρα", font=("Consolas", 10), background="#d3d3d3",
                          foreground="black").grid(row=0, column=2, pady=10)
            lb2 = tk.Label(linf, text="Περίμενε ώστε να επιστρέψουν οι κάρτες", font=("Consolas", 10),
                           background="#d3d3d3", foreground="black").grid(row=2, column=2, pady=10)
        else:
            lab = tk.Label(linf, text="Γραμμική άλγεβρα", font=("Consolas", 10), background="#d3d3d3",
                           foreground="black").grid(row=0, column=2, pady=10)
            lab2 = tk.Label(linf, image=img24, font=("Consolas", 10), background="#d3d3d3", foreground="black").grid(
                row=1, column=2, pady=10, padx=160)
            lab3 = tk.Message(linf, text=linq[x].q, font=("Consolas", 10), background="#d3d3d3",
                              foreground="black").grid(row=1, column=2, pady=10, padx=160)

            ran = tk.Button(linf, text=linq[x].ra, command=button1, wraplength=100, height=2, width=9,
                            font=("Consolas", 10), background="#d3d3d3", foreground="black", relief="solid",
                            justify="center").grid(row=3, column=1, pady=50, padx=12)
            wan1 = tk.Button(linf, text=linq[x].wa1, command=button2, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#d3d3d3", foreground="black", relief="solid").grid(
                row=3, column=2, pady=50, padx=12)
            wan2 = tk.Button(linf, text=linq[x].wa2, command=button2, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#d3d3d3", foreground="black", relief="solid").grid(
                row=3, column=3, pady=50, padx=12)
            b2 = tk.Button(linf, text="Επόμενη ερώτηση", command=lin, wraplength=100, height=2, width=9,
                           font=("Consolas", 10), background="#d3d3d3", foreground="black", relief="solid").grid(row=4,
                                                                                                                 column=2,
                                                                                                                 pady=20,
                                                                                                                 padx=12)
            b = ttk.Button(linf, text="Επόμενο μάθημα", command=cs, image=img14)
            b.grid(row=5, column=3, pady=10)
            b = ttk.Button(linf, text="Προηγούμενο μάθημα", command=math, image=img25).grid(row=5, column=1, pady=10)
    #διαφορές: οι λίστες που χρησιμοποιούνται και η σειρά εμφάνισης των κουμπιών απαντήσεων


def cs():   #cs: computer science
    winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
    if (len(csq) != 0):
        x = randint(0, len(csq) - 1)

        def button1():
            global pointscs
            global totalpoints
            pointscs += 1
            totalpoints += pointscs

            csright.append(quest(csq[x].q, csq[x].ra, csq[x].wa1, csq[x].wa2))
            csq.pop(x)
            winsound.PlaySound("correct.wav", winsound.SND_FILENAME)

            def correct():
                time.sleep(60)
                if (len(csright) != 0):
                    csq.extend(csright)
                if (x in csright and len(csright) != 0):
                    csright.pop(x)

            pu = threading.Thread(target=correct)
            pu.start()
            cs()

        def button2():

            cswrong.append(quest(csq[x].q, csq[x].ra, csq[x].wa1, csq[x].wa2))
            csq.pop(x)
            winsound.PlaySound("wrong.wav", winsound.SND_FILENAME)

            def incorrect():
                time.sleep(25)
                if (len(cswrong) != 0):
                    csq.extend(cswrong)
                if (x in cswrong and len(cswrong) != 0):
                    cswrong.pop(x)

            pu2 = threading.Thread(target=incorrect)
            pu2.start()
            cs()

        hide()
        csf.grid()
        if (len(csq) == 0):
            lb = tk.Label(csf, text="Εισαγωγή στην επιστήμη των υπολογιστών", font=("Consolas", 10), background="black",
                          foreground="#add8e6").grid(row=0, column=2, pady=10)
            lb2 = tk.Label(csf, text="Περίμενε ώστε να επιστρέψουν οι κάρτες", font=("Consolas", 10),
                           background="black", foreground="#add8e6").grid(row=2, column=2, pady=10)
        else:
            lab = tk.Label(csf, text="Επιστήμη υπολογιστών", font=("Consolas", 10), background="black",
                           foreground="#add8e6").grid(row=0, column=2, pady=10)

            lab34 = tk.Label(csf, image=img24, font=("Consolas", 10), background="black", foreground="#add8e6").grid(
                row=1, column=2, pady=10, padx=160)
            lab2 = tk.Message(csf, text=csq[x].q, background="black", foreground="#add8e6").grid(row=1, column=2,
                                                                                                pady=10, padx=160)

            wan2 = tk.Button(csf, text=csq[x].wa2, command=button2, wraplength=100, height=2, width=9,
                            font=("Consolas", 10), background="black", foreground="#add8e6", relief="solid").grid(row=3,
                                                                                                                  column=1,
                                                                                                                  pady=50,
                                                                                                                  padx=12)
            wan1 = tk.Button(csf, text=csq[x].wa1, command=button2, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="black", foreground="#add8e6", relief="solid").grid(
                row=3, column=2, pady=50, padx=12)
            ran = tk.Button(csf, text=csq[x].ra, command=button1, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="black", foreground="#add8e6", relief="solid").grid(
                row=3, column=3, pady=50, padx=12)
            b2 = tk.Button(csf, text="Επόμενη ερώτηση", command=cs, wraplength=100, height=2, width=9,
                           font=("Consolas", 10), background="black", foreground="#add8e6", relief="solid").grid(row=4,
                                                                                                                 column=2,
                                                                                                                 pady=20,
                                                                                                                 padx=12)
            b = ttk.Button(csf, text="Επόμενο μάθημα", command=pr, image=img12)
            b.grid(row=5, column=3, pady=10)
            b = ttk.Button(csf, text="Προηγούμενο μάθημα", command=lin, image=img25).grid(row=5, column=1, pady=10)
    #Διαφορές: οι χρησιμοποιούμενες λίστες και η σειρά εμφάνισης κουμπιών απαντήσεων


def pr():   #pr: programming(εισαγωγή στον προγραμματισμό)
    winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
    if (len(prq) != 0):
        x = randint(0, len(prq) - 1)

        def button1():
            global pointspr
            global totalpoints
            pointspr += 1
            totalpoints += pointspr

            prright.append(quest(prq[x].q, prq[x].ra, prq[x].wa1, prq[x].wa2))
            prq.pop(x)
            winsound.PlaySound("correct.wav", winsound.SND_FILENAME)

            def correct():
                time.sleep(60)

                if (len(prright) != 0):
                    prq.extend(prright)
                if (x in prright and len(prright) != 0):
                    prright.pop(x)

            pu = threading.Thread(target=correct)
            pu.start()
            pr()

        def button2():

            prwrong.append(quest(prq[x].q, prq[x].ra, prq[x].wa1, prq[x].wa2))
            prq.pop(x)
            winsound.PlaySound("wrong.wav", winsound.SND_FILENAME)

            def incorrect():
                time.sleep(25)
                if (len(prwrong) != 0):
                    prq.extend(prwrong)
                if (x in prwrong and len(prwrong) != 0):
                    prwrong.pop(x)

            pu2 = threading.Thread(target=incorrect)
            pu2.start()
            pr()

        hide()
        prf.grid()
        if (len(prq) == 0):
            lb = tk.Label(prf, text="Εισαγωγή στον προγραμματισμό", font=("Consolas", 10), background="#0000FF",
                          foreground="#FFA500").grid(row=0, column=2, pady=10)
            lb2 = tk.Label(prf, text="Περίμενε ώστε να επιστρέψουν οι κάρτες", font=("Consolas", 10),
                           background="#0000FF",
                           foreground="#FFA500").grid(row=2, column=2, pady=10)
        else:
            lab = tk.Label(prf, text="Εισαγωγή στον προγραμματισμό", font=("Consolas", 10), background="#0000FF",
                           foreground="#FFA500").grid(row=0, column=2, pady=10)
            lab = tk.Label(prf, image=img24, font=("Consolas", 10), background="#0000FF").grid(row=1, column=2, pady=10,
                                                                                               padx=160)
            lab2 = tk.Message(prf, text=prq[x].q, font=("Consolas", 10), background="#0000FF",
                             foreground="#FFA500").grid(row=1, column=2, pady=10, padx=160)
            wan1 = tk.Button(prf, text=prq[x].wa1, command=button2, wraplength=100, height=2, width=9,
                            font=("Consolas", 10), background="#0000FF", foreground="#FFA500", relief="solid").grid(
                row=3, column=1, pady=50, padx=12)
            ran = tk.Button(prf, text=prq[x].ra, command=button1, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#0000FF", foreground="#FFA500", relief="solid").grid(
                row=3, column=2, pady=50, padx=12)
            wan2 = tk.Button(prf, text=prq[x].wa2, command=button2, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#0000FF", foreground="#FFA500", relief="solid").grid(
                row=3, column=3, pady=50, padx=12)
            b2 = tk.Button(prf, text="Επόμενη ερώτηση", command=pr, wraplength=100, height=2, width=9,
                           font=("Consolas", 10), background="#0000FF", foreground="#FFA500", relief="solid").grid(
                row=4, column=2, pady=20, padx=12)
            b = ttk.Button(prf, text="Επόμενο μάθημα", command=pr2, image=img16)
            b.grid(row=5, column=3, pady=10)
            b = ttk.Button(prf, text="Προηγούμενο μάθημα", command=cs, image=img25).grid(row=5, column=1, pady=10)
#Διαφορές: σειρά εμφάνισης κουμπιών και χρησιμοποιούμενων λιστών


def pr2():  #pr2:programming 2 (προγραμματισμός υπολογιστών)
    winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
    if (len(pr2q) != 0):
        x = randint(0, len(pr2q) - 1)

        def button1():
            global pointspr2
            global totalpoints
            pointspr2 += 1
            totalpoints += pointspr2

            pr2right.append(quest(pr2q[x].q, pr2q[x].ra, pr2q[x].wa1, pr2q[x].wa2))
            pr2q.pop(x)
            winsound.PlaySound("correct.wav", winsound.SND_FILENAME)

            def correct():
                time.sleep(60)
                if (len(pr2right) != 0):
                    pr2q.extend(pr2right)
                if (x in pr2right and len(pr2right) != 0):
                    pr2right.pop(x)

            pu = threading.Thread(target=correct)
            pu.start()
            pr2()

        def button2():

            pr2wrong.append(quest(pr2q[x].q, pr2q[x].ra, pr2q[x].wa1, pr2q[x].wa2))
            pr2q.pop(x)
            winsound.PlaySound("wrong.wav", winsound.SND_FILENAME)

            def incorrect():
                time.sleep(25)
                if (len(pr2wrong) != 0):
                    pr2q.extend(pr2wrong)
                if (x in pr2wrong and len(pr2wrong) != 0):
                    pr2wrong.pop(x)

            pu2 = threading.Thread(target=incorrect)
            pu2.start()
            pr2()

        hide()
        pr2f.grid()

        if (len(pr2q) == 0):
            lb = tk.Label(pr2f, text="Προγραμματισμός", font=("Consolas", 10), background="#32CD32",
                          foreground="black").grid(row=0, column=2, pady=10)
            lb2 = tk.Label(pr2f, text="Περίμενε ώστε να επιστρέψουν οι κάρτες", font=("Consolas", 10),
                           background="#32CD32",
                           foreground="black").grid(row=2, column=2, pady=10)
        else:

            lab = tk.Label(pr2f, text="Προγραμματισμός", font=("Consolas", 10), background="black",
                           foreground="#32CD32").grid(row=0, column=2, pady=10)
            lab = tk.Label(pr2f, image=img24, background="black").grid(row=1, column=2, pady=10, padx=160)
            lab2 = tk.Message(pr2f, text=pr2q[x].q, font=("Consolas", 10), background="black",
                             foreground="#32CD32").grid(row=1, column=2,
                                                        pady=10, padx=160)
            ran = tk.Button(pr2f, text=pr2q[x].ra, command=button1, wraplength=100, height=2, width=9,
                            font=("Consolas", 10), background="#32CD32", foreground="black", relief="solid").grid(row=3,
                                                                                                                  column=1,
                                                                                                                  pady=50,
                                                                                                                  padx=12)
            wan1 = tk.Button(pr2f, text=pr2q[x].wa1, command=button2, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#32CD32", foreground="black", relief="solid").grid(
                row=3, column=2, pady=50, padx=12)
            wan2 = tk.Button(pr2f, text=pr2q[x].wa2, command=button2, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#32CD32", foreground="black", relief="solid").grid(
                row=3, column=3, pady=50, padx=12)
            b2 = tk.Button(pr2f, text="Επόμενη ερώτηση", command=pr2, wraplength=100, height=2, width=9,
                           font=("Consolas", 10), background="#32CD32", foreground="black", relief="solid").grid(row=4,
                                                                                                                 column=2,
                                                                                                                 pady=20,
                                                                                                                 padx=12)
            b = ttk.Button(pr2f, text="Επόμενο μάθημα", command=py, image=img17)
            b.grid(row=5, column=3, pady=10)
            b = ttk.Button(pr2f, text="Προηγούμενο μάθημα", command=pr, image=img25).grid(row=5, column=1, pady=10)
#διαφορές: χρησιμοποιούμενες λίστες και σειρά εμφάνισης κουμπιών


def py():   #python (εφαρμοσμένος προγραμματισμός με python)
    winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
    if (len(pyq) != 0):
        x = randint(0, len(pyq) - 1)

        def button1():
            global pointspy
            global totalpoints
            pointspy += 1
            totalpoints += pointspy

            pyright.append(quest(pyq[x].q, pyq[x].ra, pyq[x].wa1, pyq[x].wa2))
            pyq.pop(x)
            winsound.PlaySound("correct.wav", winsound.SND_FILENAME)

            def correct():
                time.sleep(60)
                if (len(pyright) != 0):
                    pyq.extend(pyright)
                if (x in pyright and len(pyright) != 0):
                    pyright.pop(x)

            pu = threading.Thread(target=correct)
            pu.start()
            py()

        def button2():

            pywrong.append(quest(pyq[x].q, pyq[x].ra, pyq[x].wa1, pyq[x].wa2))
            pyq.pop(x)
            winsound.PlaySound("wrong.wav", winsound.SND_FILENAME)

            def incorrect():
                time.sleep(25)
                if (len(pywrong) != 0):
                    pyq.extend(pywrong)
                if (x in pywrong and len(pywrong) != 0):
                    pywrong.pop(x)

            pu2 = threading.Thread(target=incorrect)
            pu2.start()
            py()

        hide()
        pyf.grid()
        if (len(pyq) == 0):
            lb = tk.Label(pyf, text="Python", font=("Consolas", 10), background="#FFFF00",
                          foreground="black").grid(row=0, column=2, pady=10)
            lb2 = tk.Label(pyf, text="Περίμενε ώστε να επιστρέψουν οι κάρτες", font=("Consolas", 10),
                           background="#FFFF00",
                           foreground="black").grid(row=2, column=2, pady=10)
        else:
            lab = tk.Label(pyf, text="Python", font=("Consolas", 10), background="black", foreground="#FFFF00").grid(
                row=0, column=2, pady=10)

            lab = tk.Label(pyf, image=img24, font=("Consolas", 10), background="black").grid(row=1, column=2, pady=10,
                                                                                             padx=160)
            lab2 = tk.Message(pyf, text=pyq[x].q, font=("Consolas", 10), background="black", foreground="#FFFF00").grid(
                row=1, column=2, pady=10, padx=160)
            wan2 = tk.Button(pyf, text=pyq[x].wa2, command=button2, wraplength=100, height=2, width=9,
                            font=("Consolas", 10), background="#FFFF00", foreground="black", relief="solid").grid(row=3,
                                                                                                                  column=1,
                                                                                                                  pady=50,
                                                                                                                  padx=12)
            wan1 = tk.Button(pyf, text=pyq[x].wa1, command=button2, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#FFFF00", foreground="black", relief="solid").grid(
                row=3, column=2, pady=50, padx=12)
            ran = tk.Button(pyf, text=pyq[x].ra, command=button1, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#FFFF00", foreground="black", relief="solid").grid(
                row=3, column=3, pady=50, padx=12)
            b2 = tk.Button(pyf, text="Επόμενη ερώτηση", command=py, wraplength=100, height=2, width=9,
                           font=("Consolas", 10), background="#FFFF00", foreground="black", relief="solid").grid(row=4,
                                                                                                                 column=2,
                                                                                                                 pady=20,
                                                                                                                 padx=10)
            b = ttk.Button(pyf, text="Επόμενο μάθημα", command=dm, image=img18)
            b.grid(row=5, column=3, pady=10)
            b = ttk.Button(pyf, text="Προηγούμενο μάθημα", command=pr2, image=img25).grid(row=5, column=1, pady=10)



def dm():   #discrete mathematics
    winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
    if (len(dmq) != 0):
        x = randint(0, len(dmq) - 1)

        def button1():
            global pointsdm
            global totalpoints
            pointsdm += 1
            totalpoints += pointsdm

            dmright.append(quest(dmq[x].q, dmq[x].ra, dmq[x].wa1, dmq[x].wa2))
            dmq.pop(x)
            winsound.PlaySound("correct.wav", winsound.SND_FILENAME)

            def correct():
                time.sleep(60)
                if (len(dmright) != 0):
                    dmq.extend(dmright)
                if (x in dmright and len(dmright) != 0):
                    dmright.pop(x)

            pu = threading.Thread(target=correct)
            pu.start()
            dm()

        def button2():

            dmwrong.append(quest(dmq[x].q, dmq[x].ra, dmq[x].wa1, dmq[x].wa2))
            dmq.pop(x)
            winsound.PlaySound("wrong.wav", winsound.SND_FILENAME)

            def incorrect():
                time.sleep(25)
                if (len(dmwrong) != 0):
                    dmq.extend(dmwrong)
                if (x in dmwrong and len(dmwrong) != 0):
                    dmwrong.pop(x)

            pu2 = threading.Thread(target=incorrect)
            pu2.start()
            dm()

        hide()
        dmf.grid()
        if (len(dmq) == 0):
            lb = tk.Label(dmf, text="Διακριτά μαθηματικά", font=("Consolas", 10), background="#C0C0C0",
                          foreground="black").grid(row=0, column=2, pady=10)
            lb2 = tk.Label(dmf, text="Περίμενε ώστε να επιστρέψουν οι κάρτες", font=("Consolas", 10),
                           background="#C0C0C0",
                           foreground="black").grid(row=2, column=2, pady=10)
        else:
            lab = tk.Label(dmf, text="Διακριτά μαθηματικά", font=("Consolas", 10), background="#C0C0C0").grid(row=0,
                                                                                                              column=2,
                                                                                                              pady=10)
            lab = tk.Label(dmf, image=img24, font=("Consolas", 10), background="#C0C0C0").grid(row=1, column=2, pady=10,
                                                                                               padx=160)
            lab2 = tk.Message(dmf, text=dmq[x].q, background="#C0C0C0", foreground="black").grid(row=1, column=2,
                                                                                                pady=10, padx=160)
            wan1 = tk.Button(dmf, text=dmq[x].wa1, command=button2, wraplength=100, height=2, width=9,
                            font=("Consolas", 10), background="#C0C0C0", foreground="black", relief="solid").grid(row=3,
                                                                                                                  column=1,
                                                                                                                  pady=50,
                                                                                                                  padx=12)
            ran = tk.Button(dmf, text=dmq[x].ra, command=button1, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#C0C0C0", foreground="black", relief="solid").grid(
                row=3, column=2, pady=50, padx=12)
            wan2 = tk.Button(dmf, text=dmq[x].wa2, command=button2, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#C0C0C0", foreground="black", relief="solid").grid(
                row=3, column=3, pady=50, padx=12)
            b2 = tk.Button(dmf, text="Επόμενη ερώτηση", command=dm, wraplength=100, height=2, width=9,
                           font=("Consolas", 10), background="#C0C0C0", foreground="black", relief="solid").grid(row=4,
                                                                                                                 column=2,
                                                                                                                 pady=20,
                                                                                                                 padx=12)
            b = ttk.Button(dmf, text="Επόμενο μάθημα", command=pb, image=img19)
            b.grid(row=5, column=3, pady=10)
            b = ttk.Button(dmf, text="Προηγούμενο μάθημα", command=py, image=img25).grid(row=5, column=1, pady=10)



def pb():   #pb:probabilities
    winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
    if (len(pbq) != 0):
        x = randint(0, len(pbq) - 1)

        def button1():
            global pointspb
            global totalpoints
            pointspb += 1
            totalpoints += pointspb

            pbright.append(quest(pbq[x].q, pbq[x].ra, pbq[x].wa1, pbq[x].wa2))
            pbq.pop(x)
            winsound.PlaySound("correct.wav", winsound.SND_FILENAME)

            def correct():
                time.sleep(60)
                if (len(pbright) != 0):
                    pbq.extend(pbright)
                if (x in pbright and len(pbright) != 0):
                    pbright.pop(x)

            pu = threading.Thread(target=correct)
            pu.start()
            pb()

        def button2():

            pbwrong.append(quest(pbq[x].q, pbq[x].ra, pbq[x].wa1, pbq[x].wa2))
            pbq.pop(x)
            winsound.PlaySound("wrong.wav", winsound.SND_FILENAME)

            def incorrect():
                time.sleep(25)
                if (len(pbwrong) != 0):
                    pbq.extend(pbright)
                if (x in pbwrong and len(pbwrong) != 0):
                    pbwrong.pop(x)

            pu2 = threading.Thread(target=incorrect)
            pu2.start()
            pb()

        hide()
        pbf.grid()
        if (len(pbq) == 0):
            lb = tk.Label(pbf, text="Πιθανότητες", font=("Consolas", 10), background="#ffcccb",
                          foreground="white").grid(row=0, column=2, pady=10)
            lb2 = tk.Label(pbf, text="Περίμενε ώστε να επιστρέψουν οι κάρτες", font=("Consolas", 10),
                           background="#ffcccb",
                           foreground="white").grid(row=2, column=2, pady=10)
        else:
            lab = tk.Label(pbf, text="Πιθανότητες", font=("Consolas", 10), background="white", foreground="black").grid(
                row=0, column=2, pady=10)
            lab = tk.Label(pbf, image=img24, font=("Consolas", 10), background="white").grid(row=1, column=2, pady=10,
                                                                                             padx=160)
            lab2 = tk.Message(pbf, text=pbq[x].q, font=("Consolas", 10), background="white", foreground="black").grid(
                row=1, column=2, pady=10, padx=160)
            ran = tk.Button(pbf, text=pbq[x].ra, command=button1, wraplength=100, height=2, width=9,
                            font=("Consolas", 10), background="#ffcccb", foreground="white", relief="solid").grid(row=3,
                                                                                                                  column=1,
                                                                                                                  pady=50,
                                                                                                                  padx=12)
            wan1 = tk.Button(pbf, text=pbq[x].wa1, command=button2, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#00008b", foreground="white", relief="solid").grid(
                row=3, column=2, pady=50, padx=12)
            wan2 = tk.Button(pbf, text=pbq[x].wa2, command=button2, wraplength=100, height=2, width=9,
                             font=("Consolas", 10), background="#add8e6", foreground="white", relief="solid").grid(
                row=3, column=3, pady=50, padx=12)
            b2 = tk.Button(pbf, text="Επόμενη ερώτηση", command=pb, wraplength=100, height=2, width=9,
                           font=("Consolas", 10), background="#00008b", foreground="white", relief="solid").grid(row=4,
                                                                                                                 column=2,
                                                                                                                 pady=20,
                                                                                                                 padx=12)
            b = ttk.Button(pbf, text="Επόμενο μάθημα", command=hum, image=img20)
            b.grid(row=5, column=3, pady=10)
            b = ttk.Button(pbf, text="Προηγούμενο μάθημα", command=dm, image=img25).grid(row=5, column=1, pady=10)
    #διαφορές: χρησιμοποιούμενες λίστες και σειρά εμφάνισης κουμπιών


def hum():  #hum: humanities(πληροφορική στις ανθρωπιστικές επιστήμες)
    winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
    if (len(humq) != 0):
        x = randint(0, len(humq) - 1)

        def button1():
            global pointshum
            global totalpoints
            pointshum += 1
            totalpoints += pointshum

            humright.append(quest(humq[x].q, humq[x].ra, humq[x].wa1, humq[x].wa2))
            humq.pop(x)
            winsound.PlaySound("correct.wav", winsound.SND_FILENAME)

            def correct():
                time.sleep(60)
                if (len(humright) != 0):
                    humq.extend(humright)
                if (x in humright and len(humright) != 0):
                    humright.pop(x)

            pu = threading.Thread(target=correct)
            pu.start()
            hum()

        def button2():

            humwrong.append(quest(humq[x].q, humq[x].ra, humq[x].wa1, humq[x].wa2))
            humq.pop(x)
            winsound.PlaySound("wrong.wav", winsound.SND_FILENAME)

            def incorrect():
                time.sleep(25)
                if (len(humwrong) != 0):
                    humq.extend(humwrong)
                if (x in humwrong and len(humwrong) != 0):
                    humwrong.pop(x)

            pu2 = threading.Thread(target=incorrect)
            pu2.start()
            hum()

        hide()
        humf.grid()
        if (len(humq) == 0):
            lb = tk.Label(humf, text="Πληροφορική στις ανθρωπιστικές επιστήμες", font=("Consolas", 10),
                          background="black",
                          foreground="blue").grid(row=0, column=2, pady=10)
            lb2 = tk.Label(humf, text="Περίμενε ώστε να επιστρέψουν οι κάρτες", font=("Consolas", 10),
                           background="black",
                           foreground="blue").grid(row=2, column=2, pady=10)
        else:
            lab = tk.Label(humf, text="Πληροφορική στις ανθρωπιστικές επιστήμες", font=("Consolas", 10),
                           background="black", foreground="white").grid(row=0, column=2, pady=10)
            lab = tk.Label(humf, image=img24, font=("Consolas", 10), background="black").grid(row=1, column=2, pady=10,
                                                                                              padx=160)
            lab2 = tk.Message(humf, text=humq[x].q, font=("Consolas", 10), background="black", foreground="white").grid(
                row=1, column=2, pady=10, padx=160)
            wan2 = tk.Button(humf, text=humq[x].wa2, command=button2, wraplength=80, height=2, width=9,
                            font=("Consolas", 10), background="#add8e6", foreground="black", relief="solid").grid(row=3,
                                                                                                                  column=1,
                                                                                                                  pady=50,
                                                                                                                  padx=12)
            wan1 = tk.Button(humf, text=humq[x].wa1, command=button2, wraplength=80, height=2, width=9,
                             font=("Consolas", 10), background="#add8e6", foreground="black", relief="solid").grid(
                row=3, column=2, pady=50, padx=12)
            ran = tk.Button(humf, text=humq[x].ra, command=button1, wraplength=80, height=2, width=9,
                             font=("Consolas", 10), background="#add8e6", foreground="black", relief="solid").grid(
                row=3, column=3, pady=50, padx=12)
            b2 = tk.Button(humf, text="Επόμενη ερώτηση", command=hum, wraplength=80, height=2, width=9,
                           font=("Consolas", 10), background="#add8e6", foreground="black", relief="solid").grid(row=4,
                                                                                                                 column=2,
                                                                                                                 pady=20,
                                                                                                                 padx=12)
            b = ttk.Button(humf, text="Προηγούμενο μάθημα", command=pb, image=img25)
            b.grid(row=5, column=1, pady=10)
#διαφορές: χρησιμοποιούμενες λίστες και σειρά εμφάνισης κουμπιών


def arxikh():  # Συνάρτηση της αρχικής σελίδας, στις γραμμές υπάρχουν τα κουμπιά και οι ετικέτες, καθώς και οι συναρτήσεις που ενεργοποιούν τα κουμπιά (command=....)
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    hide()
    arxikhf.pack(fill="both", expand=1)
    lab = tk.Label(arxikhf, text="Py Flashcards", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).pack(pady=20)
    gsb1 = tk.Label(arxikhf, text="Ξεκίνα το παιχνίδι", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=20)
    gsb = tk.Button(arxikhf, command=domes, image=img27, background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10), relief="solid").pack(pady=20)    #Όταν ξεκινάει το παιχνίδι απο την αρχική, μεταφερόμαστε στις δομές δεδομένων
    gs2 = tk.Label(arxikhf, text="Φτιάξε τις δικές σου κάρτες", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).pack(pady=20)
    gs2s = tk.Button(arxikhf, command=create, image=img27, background="#2F323B", foreground="#39FF14",
                     font=("Consolas", 10), relief="solid").pack(pady=20)
    gs3 = tk.Label(arxikhf, text="Παίξε με τις δικές σου κάρτες", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).pack(pady=20)
    gs3s = tk.Button(arxikhf, command=play, image=img27, background="#2F323B", foreground="#39FF14",
                     font=("Consolas", 10), relief="solid").pack(pady=20)


def create():  # Συνάρτηση δημιοργίας καρτών απο τον χρήστη για μάθημα διάφορο των προσφερομένων
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():   #Όταν πατάμε το κουμπί 'δημιουργία΄ ενεργοποιείται αυτή η συνάρτηση
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        userq = userquestion.get()  #παίρνουμε την ερώτηση απο το αντίστοιχο entry box
        userr = userright.get()     #παίρνουμε την σωστή απάντηση απο το αντίστοιχο entry box
        userw1 = userwrong1.get()   #παίρνουμε την πρώτη λάθος απάντηση απο το αντίστοιχο entry box
        userw2 = userwrong2.get()   #παίρνουμε την δεύτερη λάθος απάντηση απο το αντίστοιχο entry box
        usersub = usersubj.get()    #παίρνουμε το μάθημα απο το αντίστοιχο entry box
        userqstn.append(user(usersub, userq, userr, userw1, userw2))  # Τοποθέτηση της δημιουργηθείσας κάρτας στις σχετικές λίστες
        playlist.append(user(usersub, userq, userr, userw1, userw2))
        file = open("playcards.txt", "a")       #γραμμές 995-997: αποθήκευση της δημιουργηθείσας κάρτας σε αρχείο
        file.write(usersub + '~' + userq + '~' + userr + '~' + userw1 + '~' + userw2 + '\n')    #αποθήκευση σε αρχείο
        file.close()
        lbl3 = tk.Label(createf, text="Η κάρτα δημιουργήθηκε!", background="#2F323B", foreground="#39FF14").pack()


    def loadforcustom():    #γραμμές 1001-1022: η συνάρτηση με την οποία μπορούμε να φορτώσουμε κάρτες απο αρχείο
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)


        try:    #try, except για περίπτωση σφάλματος του αρχείου
            file = open("playcards.txt", "r")
            information = file.readlines()  #διάβασμα περιεχομένου του αρχείου
            for i in information:
                cards = i.split('~')    #για κάθε γραμμή, τα αντικείμενα χωρίζονται με κόμμα
                subject = cards[0]
                question = cards[1]
                rightanswer = cards[2]
                wronganswer1 = cards[3]
                wronganswer2 = cards[4]
                playlist.append(user(subject,question, rightanswer, wronganswer1, wronganswer2))    #append των στοιχείων στη σχετική λίστα

            lbl3 = tk.Label(createf, text="Οι κάρτες φορτώθηκαν!", background="#2F323B",
                                foreground="#39FF14").pack()
            file.close()
        except:
            lbl3 = tk.Label(createf, text="Κάτι πήγε στραβά με το αρχείο!", background="#2F323B",
                            foreground="#39FF14").pack()    #σε περίπτωση οποιουδήποτε σφάλματος με το αρχείο, εμφανίζεται σχετικό μήνυμα


    hide()
    createf.pack(fill="both", expand=1)

    userq = userquestion.get()  #γραμμές 1028-1032: οι μεταβλητές μαθήματος, ερώτησης και της τριπλέτας απαντήσεων
    userr = userright.get()
    userw1 = userwrong1.get()
    userw2 = userwrong2.get()
    usersub = usersubj.get()
    lab = tk.Label(createf, text="Φτιάξε την δική σου κάρτα", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).pack(pady=10)
    lab = tk.Label(createf, text="Θέμα/Μάθημα", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).pack(
        pady=10)
    us = ttk.Entry(createf, textvariable=usersubj).pack(pady=10)
    labb = tk.Label(createf, text="H ερώτηση σου", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    uqs = ttk.Entry(createf, textvariable=userquestion).pack(pady=10)

    # uqs.delete(0,"end")
    labr = tk.Label(createf, text="H σωστή απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    ura = ttk.Entry(createf, textvariable=userright).pack(pady=10)
    labw1 = tk.Label(createf, text="Η πρώτη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                     font=("Consolas", 10)).pack(pady=10)
    uwa1 = ttk.Entry(createf, textvariable=userwrong1).pack(pady=10)
    labw2 = tk.Label(createf, text="Η δεύτερη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                     font=("Consolas", 10)).pack(pady=10)
    uwa2 = ttk.Entry(createf, textvariable=userwrong2).pack(pady=10)

    btn = tk.Button(createf, text="Δημιουργία", command=append, background="#BFEBDC", relief="solid",
                    font=("Consolas", 10)).pack(pady=10)
    btn2 = tk.Button(createf, text="Φτιάξε άλλη", command=create, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).pack(pady=10)
    btn4 = ttk.Button(createf, text="Φόρτωση καρτών",command=loadforcustom).pack(pady=10)


def play():
    hide()
    playf.grid()
    leng = len(playlist)
    winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
    if (leng == 0):
        lbl = tk.Label(playf, text="Δέν υπάρχουν διαθέσιμες κάρτες", bg="#2F323B", fg="#39FF14",font=("Consolas",10)).grid(row=0,column=2,pady=150,padx=250)
        btn = tk.Button(playf, text="Δημιούργησε κάρτες", command=create,bg="#BFEBDC",relief="solid",font=("Consolas",10)).grid(row=1,column=2,pady=150,padx=250)
    else:
        x = randint(0, leng - 1)
        def delete():
            winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
            if (len(playlist) != 0):
                playlist.pop(x)
            play()


        def button1():

            global pointscreated
            pointscreated += 1

            playlistright.append(user(playlist[x].subj, playlist[x].uq, playlist[x].ura, playlist[x].uwa1, playlist[x].uwa2))

            playlist.pop(x)
            winsound.PlaySound("correct.wav", winsound.SND_FILENAME)

            def correct():
                time.sleep(60)
                if (len(playlistright) != 0):
                    playlist.extend(playlistright)
                if (x in playlistright and len(playlistright) != 0):
                    playlistright.pop(x)

            pu = threading.Thread(target=correct)
            pu.start()
            play()

        def button2():
            playlistwrong.append(user(playlist[x].subj, playlist[x].uq, playlist[x].ura, playlist[x].uwa1, playlist[x].uwa2))

            playlist.pop(x)
            winsound.PlaySound("wrong.wav", winsound.SND_FILENAME)

            def incorrect():
                time.sleep(25)

                if (len(playlistwrong) != 0):
                    playlist.extend(playlistwrong)
                if (x in playlistwrong and len(playlistwrong) != 0):
                    playlistwrong.pop(x)

            pu2 = threading.Thread(target=incorrect)
            pu2.start()
            play()


        lbl1 = tk.Label(playf, text=playlist[x].subj, bg="#2F323B", fg="#39FF14",font=("Consolas",10)).grid(row=0, column=2, pady=10)
        lab2 = tk.Label(playf, image=img24, bg="#2F323B").grid(row=1, column=2, pady=10, padx=160)
        lbl2 = tk.Message(playf, text=playlist[x].uq,font=("Consolas",10),bg="#2F323B",fg="#39FF14",relief="solid").grid(row=1, column=2, pady=10, padx=160)
        btn = tk.Button(playf, text=playlist[x].ura, command=button1,wraplength=100,height=2,width=9,font=("Consolas",10),bg="#BFEBDC",fg="black",relief="solid").grid(row=3, column=1, pady=60, padx=12)
        btn2 = tk.Button(playf, text=playlist[x].uwa1, command=button2,wraplength=100,height=2,width=9,font=("Consolas",10),bg="#BFEBDC",fg="black",relief="solid").grid(row=3, column=2, pady=60, padx=12)
        btn3 = tk.Button(playf, text=playlist[x].uwa2, command=button2,wraplength=100,height=2,width=9,font=("Consolas",10),bg="#BFEBDC",fg="black",relief="solid").grid(row=3, column=3, pady=60, padx=12)
        btn4 = tk.Button(playf, text="Επόμενη ερώτηση", command=play,wraplength=100,height=2,width=9,font=("Consolas",10),bg="#BFEBDC",fg="black",relief="solid").grid(row=4, column=2, pady=60, padx=12)
        btn44 = tk.Button(playf, text="Διαγραφή κάρτας", command=delete, wraplength=100, height=2, width=9,font=("Consolas", 10), bg="#BFEBDC", fg="black", relief="solid").grid(row=4, column=3,pady=60,padx=12)
        lbl11 = tk.Label(playf, text=pointscreated, bg="#2F323B", fg="#39FF14", font=("Consolas", 10)).grid(row=4,column=1,pady=10)

#γραμμές 1060-1125:Ακολουθούνται ακριβώς οι ίδιες τεχνικές για το σύστημα του παιχνιδιού με τις κάρτες, όπως με τα προηγούμενα μαθήματα
#οι μόνες διαφορές είναι πως στη χρησιμοποιούμενη λίστα προστίθεται και το μάθημα που έχει φτιάξει ο χρήστης

def points():   #γραμμές 1147-1198: Η συνάρτηση εμφάνισης των πόντων των μαθημάτων αναλυτικά και συνολικά
    winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
    hide()
    pointsf.grid()
    lbl0 = tk.Label(pointsf, text="Μαθήματα", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=1, column=1, pady=15, padx=120)
    lblp = tk.Label(pointsf, text="Πόντοι", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=1, column=5, pady=15, padx=120)
    lbl = tk.Label(pointsf, text="Δομές δεδομένων:", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=2, column=1, pady=15, padx=120)
    lbp = tk.Label(pointsf, text=pointsds, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=2, column=5, pady=15, padx=120)
    lbl2 = tk.Label(pointsf, text="Μαθηματικός λογισμός:", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).grid(row=3, column=1, pady=15, padx=120)
    lbp2 = tk.Label(pointsf, text=pointsmath, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=3, column=5, pady=15, padx=120)
    lbl3 = tk.Label(pointsf, text="Γραμμική άλγεβρα:", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).grid(row=4, column=1, pady=15, padx=120)
    lbp3 = tk.Label(pointsf, text=pointslin, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=4, column=5, pady=15, padx=120)
    lb4 = tk.Label(pointsf, text="Εισαγωγή στην επιστήμη των υπολογιστών:", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=5, column=1, padx=120)
    lbp4 = tk.Label(pointsf, text=pointscs, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=5, column=5, pady=15, padx=120)
    lb5 = tk.Label(pointsf, text="Εισαγωγή στον προγραμματισμό:", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=6, column=1, padx=120)
    lbp5 = tk.Label(pointsf, text=pointspr, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=6, column=5, pady=15, padx=120)
    lb6 = tk.Label(pointsf, text="Προγραμματισμός υπολογιστών:", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=7, column=1, pady=15, padx=120)
    lbp6 = tk.Label(pointsf, text=pointspr2, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=7, column=5, pady=15, padx=120)
    lb7 = tk.Label(pointsf, text="Εφαρμοσμένος προγραμματισμός με Python:", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=8, column=1, pady=15, padx=120)
    lbp7 = tk.Label(pointsf, text=pointspy, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=8, column=5, pady=15, padx=120)
    lb8 = tk.Label(pointsf, text="Διακριτά μαθηματικά:", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=9, column=1, pady=15, padx=120)
    lbp8 = tk.Label(pointsf, text=pointsdm, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=9, column=5, pady=15, padx=120)
    lb9 = tk.Label(pointsf, text="Πιθανότητες:", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=10, column=1, pady=15, padx=120)
    lbp9 = tk.Label(pointsf, text=pointspb, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=10, column=5, pady=15, padx=120)
    lb10 = tk.Label(pointsf, text="Πληροφορική στις ανθρωπιστικές επιστήμες:", background="#2F323B",
                    foreground="#39FF14", font=("Consolas", 10)).grid(row=11, column=1, pady=15, padx=120)
    lbp10 = tk.Label(pointsf, text=pointshum, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=11, column=5, pady=15, padx=120)
    lb11 = tk.Label(pointsf, text="Συνολικοί πόντοι:", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).grid(row=12, column=1, pady=15, padx=120)
    lbp11 = tk.Label(pointsf, text=totalpoints, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=12, column=5, pady=15, padx=120)



def cds():  #create data structs, δημιουργία κάρτας για το μάθημα των δομών δεδομένων
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():   #γραμμές 1204-1214: fetching ερώτησης και τριπλέτας απαντήσεων και εγγραφή τους σε αρχείο και τοποθέτηση στη σχετική λίστα
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        userqds = createquestion.get()  #ερώτηση
        userrds = createright.get() #σωστή απάντηση
        userw1ds = createwrong1.get()   #πρώτη λάθος απάντηση
        userw2ds = createwrong2.get()   #δεύτερη λάθος απάντηση
        dq.append(quest(userqds, userrds, userw1ds, userw2ds))  #τοποθέτηση στη λίστα των καρτών δομών δεδομένων
        file=open("datacards.txt","a")
        file.write(userqds + '~' +  userrds + '~' +  userw1ds + '~' + userw2ds + "\n")  #εγγραφή κάρτας στο σχετικό αρχείο
        file.close()
        lbl3 = tk.Label(cdsf, text="Η κάρτα δημιουργήθηκε!", background="#2F323B", foreground="#39FF14").pack()


    def loadfordatastructs():   #συνάρτηση φόρτωσης καρτών απο αρχείο, γραμμές 1200-1211
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        try: #try, except για περίπτωση λάθους με το σχετικό αρχείο
            file=open("datacards.txt","r")
            information=file.readlines()    #διάβασμα περιεχομένου απο το αρχείο
            for i in information:
                cards=i.split('~')  #διαχωρισμός των αντικειμένων με ~
                question=cards[0]   #το στοιχείο 0 του αρχείου είναι η ερώτηση
                rightanswer=cards[1]    #το στοιχείο 1 η σωστή απάντηση
                wronganswer1=cards[2]   #το στοιχείο 2 η πρώτη λάθος απάντηση
                wronganswer2=cards[3]   #το στοιχείο 3 η δεύτερη λάθος απάντηση
                dq.append(quest(question,rightanswer,wronganswer1,wronganswer2))

            file.close()
            lbl3 = tk.Label(cdsf, text="Οι κάρτες φορτώθηκαν!", background="#2F323B",
                                foreground="#39FF14").pack()
        except:
            lbl3 = tk.Label(cdsf, text="Κάτι πήγε στραβά με το αρχείο!", background="#2F323B",
                            foreground="#39FF14").pack()




    hide()
    cdsf.pack(fill="both", expand=1)
    userqds = createquestion.get()  # γραμμές 1225-1228, συνδυασμός ερώτησης και απαντήσεων προς εμφάνιση στην οθόνη, με τη συνάρτηση get() τις παίρνουμε απο τα entry box
    userrds = createright.get()
    userw1ds = createwrong1.get()
    userw2ds = createwrong2.get()
    lbl = tk.Label(cdsf, text="Δομές δεδομένων", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).pack(pady=10)
    lbl2 = tk.Label(cdsf, text="Ερώτηση", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).pack(
        pady=10)
    usrq = ttk.Entry(cdsf, textvariable=createquestion).pack(pady=10) #Entry box ερώτησης, όταν πατηθεί το κουμπί δημιουργία,
    #μεταφέρει το περιεχόμενο του Entry box στην σχετική μεταβλητή
    lbl3 = tk.Label(cdsf, text="Σωστή απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usrr = ttk.Entry(cdsf, textvariable=createright).pack(pady=10)#entry box σωστής ερώτησης, όταν πατηθεί το κουμπί δημιουργία,
    #μεταφέρει το περιεχόμενο του σχτικού entry box στην αντίστοιχη μεταβλητή
    lbl4 = tk.Label(cdsf, text="Πρώτη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw1 = ttk.Entry(cdsf, textvariable=createwrong1).pack(pady=10)#entry box πρώτης λάθος απάντησης, όταν πατηθεί το κουμπί δημιουργία
    #μεταφέρει το περιεχόμενο του entry box στην αντίστοιχη μεταβλητή
    lbl5 = tk.Label(cdsf, text="Δεύτερη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw2 = ttk.Entry(cdsf, textvariable=createwrong2).pack(pady=10)#entry box δεύτερης λάθος απάντησης, όταν πατηθεί το κουμπί δημιουργία
    #μεταφερει το περιεχόμενο του σχετικού entry box στην αντίστοιχη μεταβλητή
    btn = tk.Button(cdsf, text="Δημιουργία", command=append, background="#BFEBDC", font=("Consolas", 10),
                    relief="solid").pack(pady=10)
    btn2 = tk.Button(cdsf, text="Φτιάξε άλλη", command=cds, background="#BFEBDC", font=("Consolas", 10),
                     relief="solid").pack(pady=10)  #όταν θέλουμε να φτιάξουμε κι'άλλη κάρτα ξανακαλούμε την συνάρτηση
    btn3 = tk.Button(cdsf, text="Φτιάξε κάρτα για άλλο μάθημα", command=createsubj, background="#BFEBDC",
                     font=("Consolas", 10), relief="solid").pack(pady=10)
    load = ttk.Button(cdsf, text="Φόρτωση καρτών", command=loadfordatastructs).pack(pady=10)
    #ΣΗΜΕΙΩΣΗ: Στις επόμενες συναρτήσεις δημιουργίας κάρτας για τα υπάρχοντα μαθήματα ακολουθούνται ακριβώς οι ίδιες
    #μέθοδοι και τεχνικές με την αμέσως προηγούμενη συνάρτηση. Ως εκ τούτου, σχόλια θα υπάρχουν
    #μονάχα όοπου παρατηρούνται διαφορές

def cmath(): #create mathematic calculus (συνάρτηση δημιουργίας κάρτας για τον μαθηματικό λογισμό)
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        userqds = createquestion.get()
        userrds = createright.get()
        userw1ds = createwrong1.get()
        userw2ds = createwrong2.get()
        mathq.append(quest(userqds, userrds, userw1ds, userw2ds))   #πρόσθεση κάρτας στη σχετική λίστα του μαθ. λογισμού
        file = open("mathcards.txt", "a")   #άνοιγμα διαφορετικού πλέον αρχείου, του αρχείου του μαθ. λογισμού
        file.write(userqds + '~' + userrds + '~' + userw1ds + '~' + userw2ds + '\n')
        file.close()
        lbl3 = tk.Label(cmathf, text="Η κάρτα δημιουργήθηκε!", background="#2F323B", foreground="#39FF14").pack()

    def loadformath():
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        try:
            file = open("mathcards.txt", "r")
            information = file.readlines()
            for i in information:
                cards = i.split('~')
                question = cards[0]
                rightanswer = cards[1]
                wronganswer1 = cards[2]
                wronganswer2 = cards[3]
                mathq.append(quest(question, rightanswer, wronganswer1, wronganswer2))

            file.close()
            lbl3 = tk.Label(cmathf, text="Οι κάρτες φορτώθηκαν!", background="#2F323B",
                                foreground="#39FF14").pack()
        except:
            lbl3 = tk.Label(cmathf, text="Κάτι πήγε στραβά με το αρχείο!", background="#2F323B",
                            foreground="#39FF14").pack()
    hide()
    cmathf.pack(fill="both", expand=1)
    userqds = createquestion.get()
    userrds = createright.get()
    userw1ds = createwrong1.get()
    userw2ds = createwrong2.get()
    lbl = tk.Label(cmathf, text="Μαθηματικός λογισμός", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).pack(pady=10)
    lbl2 = tk.Label(cmathf, text="Ερώτηση", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).pack(
        pady=10)
    usrq = ttk.Entry(cmathf, textvariable=createquestion).pack(pady=10)
    lbl3 = tk.Label(cmathf, text="Σωστή απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usrr = ttk.Entry(cmathf, textvariable=createright).pack(pady=10)
    lbl4 = tk.Label(cmathf, text="Πρώτη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw1 = ttk.Entry(cmathf, textvariable=createwrong1).pack(pady=10)
    lbl5 = tk.Label(cmathf, text="Δεύτερη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw2 = ttk.Entry(cmathf, textvariable=createwrong2).pack(pady=10)
    btn = tk.Button(cmathf, text="Δημιουργία", command=append, background="#BFEBDC", font=("Consolas", 10),
                    relief="solid").pack(pady=10)
    btn2 = tk.Button(cmathf, text="Φτιάξε άλλη", command=cmath, background="#BFEBDC", font=("Consolas", 10),
                     relief="solid").pack(pady=10)
    btn3 = tk.Button(cmathf, text="Φτιάξε κάρτα για άλλο μάθημα", command=createsubj, background="#BFEBDC",
                     font=("Consolas", 10), relief="solid").pack(pady=10)
    load = ttk.Button(cmathf, text="Φόρτωση καρτών", command=loadformath).pack(pady=10)


def cpy():  #create python , συνάρτηση δημιουργίας κάρτας για εφαρμοσμένο προγραμματισμό με python
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        userqds = createquestion.get()
        userrds = createright.get()
        userw1ds = createwrong1.get()
        userw2ds = createwrong2.get()
        pyq.append(quest(userqds, userrds, userw1ds, userw2ds)) #πρόσθεση κάρτας στην αντίστοιχη λίστα
        file = open("pythoncards.txt", "a") #χρήση του αντίστοιχου αρχείου μαθήματος
        file.write(userqds + '~' + userrds + '~' + userw1ds + '~' + userw2ds + '\n')
        file.close()
        lbl3 = tk.Label(cpyf, text="Η κάρτα δημιουργήθηκε!", background="#2F323B", foreground="#39FF14").pack()

    def loadforpython():
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        try:
            file = open("pythoncards.txt", "r")
            information = file.readlines()
            for i in information:
                cards = i.split('~')
                question = cards[0]
                rightanswer = cards[1]
                wronganswer1 = cards[2]
                wronganswer2 = cards[3]
                pyq.append(quest(question, rightanswer, wronganswer1, wronganswer2))

            file.close()
            lbl3 = tk.Label(cpyf, text="Οι κάρτες φορτώθηκαν!", background="#2F323B",
                        foreground="#39FF14").pack()
        except:
            lbl3 = tk.Label(cpyf, text="Κάτι πήγε στραβά με το αρχείο!", background="#2F323B",
                        foreground="#39FF14").pack()
    hide()
    cpyf.pack(fill="both", expand=1)
    userqds = createquestion.get()
    userrds = createright.get()
    userw1ds = createwrong1.get()
    userw2ds = createwrong2.get()
    lbl = tk.Label(cpyf, text="Εφαρμοσμένος προγραμματισμός με Python", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).pack(pady=10)
    lbl2 = tk.Label(cpyf, text="Ερώτηση", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).pack(
        pady=10)
    usrq = ttk.Entry(cpyf, textvariable=createquestion).pack(pady=10)
    lbl3 = tk.Label(cpyf, text="Σωστή απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usrr = ttk.Entry(cpyf, textvariable=createright).pack(pady=10)
    lbl4 = tk.Label(cpyf, text="Πρώτη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw1 = ttk.Entry(cpyf, textvariable=createwrong1).pack(pady=10)
    lbl5 = tk.Label(cpyf, text="Δεύτερη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw2 = ttk.Entry(cpyf, textvariable=createwrong2).pack(pady=10)
    btn = tk.Button(cpyf, text="Δημιουργία", command=append, background="#BFEBDC", font=("Consolas", 10),
                    relief="solid").pack(pady=10)
    btn2 = tk.Button(cpyf, text="Φτιάξε άλλη", command=cpy, background="#BFEBDC", font=("Consolas", 10),
                     relief="solid").pack(pady=10)
    btn3 = tk.Button(cpyf, text="Φτιάξε κάρτα για άλλο μάθημα", command=createsubj, background="#BFEBDC",
                     font=("Consolas", 10), relief="solid").pack(pady=10)
    load = ttk.Button(cpyf, text="Φόρτωση καρτών", command=loadforpython).pack(pady=10)


def ccs():  #create computer science, συνάρτηση δημιουργίας κάρτας για επιστήμη υπολογιστών
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        userqds = createquestion.get()
        userrds = createright.get()
        userw1ds = createwrong1.get()
        userw2ds = createwrong2.get()
        csq.append(quest(userqds, userrds, userw1ds, userw2ds)) #τοποθέτηση κάρτας στην αντίστοιχη λίστα μαθήματος
        file = open("cscards.txt", "a") #χρήση του αντίστοιχου αρχείου μαθήματος
        file.write(userqds + '~' + userrds + '~' + userw1ds + '~' + userw2ds + '\n')
        file.close()
        lbl3 = tk.Label(ccsf, text="Η κάρτα δημιουργήθηκε!", background="#2F323B", foreground="#39FF14").pack()

    def loadforcs():
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        try:
            file = open("cscards.txt", "r")
            information = file.readlines()
            for i in information:
                cards = i.split('~')
                question = cards[0]
                rightanswer = cards[1]
                wronganswer1 = cards[2]
                wronganswer2 = cards[3]
                csq.append(quest(question, rightanswer, wronganswer1, wronganswer2))

            file.close()
            lbl3 = tk.Label(ccsf, text="Οι κάρτες φορτώθηκαν!", background="#2F323B",
                        foreground="#39FF14").pack()
        except:
            lbl3 = tk.Label(ccsf, text="Κάτι πήγε στραβά με το αρχείο!", background="#2F323B",
                            foreground="#39FF14").pack()

    hide()
    ccsf.pack(fill="both", expand=1)
    userqds = createquestion.get()
    userrds = createright.get()
    userw1ds = createwrong1.get()
    userw2ds = createwrong2.get()
    lbl = tk.Label(ccsf, text="Εισαγωγή στην επιστήμη των υπολογιστών", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).pack(pady=10)
    lbl2 = tk.Label(ccsf, text="Ερώτηση", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).pack(
        pady=10)
    usrq = ttk.Entry(ccsf, textvariable=createquestion).pack(pady=10)
    lbl3 = tk.Label(ccsf, text="Σωστή απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usrr = ttk.Entry(ccsf, textvariable=createright).pack(pady=10)
    lbl4 = tk.Label(ccsf, text="Πρώτη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw1 = ttk.Entry(ccsf, textvariable=createwrong1).pack(pady=10)
    lbl5 = tk.Label(ccsf, text="Δεύτερη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw2 = ttk.Entry(ccsf, textvariable=createwrong2).pack(pady=10)
    btn = tk.Button(ccsf, text="Δημιουργία", command=append, background="#BFEBDC", font=("Consolas", 10),
                    relief="solid").pack(pady=10)
    btn2 = tk.Button(ccsf, text="Φτιάξε άλλη", command=ccs, background="#BFEBDC", font=("Consolas", 10),
                     relief="solid").pack(pady=10)
    btn3 = tk.Button(ccsf, text="Φτιάξε κάρτα για άλλο μάθημα", command=createsubj, background="#BFEBDC",
                     font=("Consolas", 10), relief="solid").pack(pady=10)
    load = ttk.Button(ccsf, text="Φόρτωση καρτών", command=loadforcs).pack(pady=10)


def chum(): #create humanities, δημιουργία κάρτας για πληροφορική στις ανθρωπιστικές επιστήμες
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        userqds = createquestion.get()
        userrds = createright.get()
        userw1ds = createwrong1.get()
        userw2ds = createwrong2.get()
        humq.append(quest(userqds, userrds, userw1ds, userw2ds))    #πρόσθεση κάρτας στην αντίστοιχη λίστα
        file = open("humanitiescards.txt", "a") #χρήση του αντίστοιχου αρχείου
        file.write(userqds + '~' + userrds + '~' + userw1ds + '~' + userw2ds + '\n')
        file.close()
        lbl3 = tk.Label(chumf, text="Η κάρτα δημιουργήθηκε!", background="#2F323B", foreground="#39FF14").pack()

    def loadforhum():
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        try:
            file = open("humanitiescards.txt", "r")
            information = file.readlines()
            for i in information:
                cards = i.split('~')
                question = cards[0]
                rightanswer = cards[1]
                wronganswer1 = cards[2]
                wronganswer2 = cards[3]
                humq.append(quest(question, rightanswer, wronganswer1, wronganswer2))

            file.close()
            lbl3 = tk.Label(chumf, text="Οι κάρτες φορτώθηκαν!", background="#2F323B",
                        foreground="#39FF14").pack()
        except:
            lbl3 = tk.Label(chumf, text="Κάτι πήγε στραβά με το αρχείο!", background="#2F323B",
                            foreground="#39FF14").pack()


    hide()
    chumf.pack(fill="both", expand=1)
    userqds = createquestion.get()
    userrds = createright.get()
    userw1ds = createwrong1.get()
    userw2ds = createwrong2.get()
    lbl = tk.Label(chumf, text="Πληροφορική στις ανθρωπιστικές επιστήμες", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).pack(pady=10)
    lbl2 = tk.Label(chumf, text="Ερώτηση", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).pack(
        pady=10)
    usrq = ttk.Entry(chumf, textvariable=createquestion).pack(pady=10)
    lbl3 = tk.Label(chumf, text="Σωστή απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usrr = ttk.Entry(chumf, textvariable=createright).pack(pady=10)
    lbl4 = tk.Label(chumf, text="Πρώτη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw1 = ttk.Entry(chumf, textvariable=createwrong1).pack(pady=10)
    lbl5 = tk.Label(chumf, text="Δεύτερη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw2 = ttk.Entry(chumf, textvariable=createwrong2).pack(pady=10)
    btn = tk.Button(chumf, text="Δημιουργία", command=append, background="#BFEBDC", font=("Consolas", 10),
                    relief="solid").pack(pady=10)
    btn2 = tk.Button(chumf, text="Φτιάξε άλλη", command=chum, background="#BFEBDC", font=("Consolas", 10),
                     relief="solid").pack(pady=10)
    btn3 = tk.Button(chumf, text="Φτιάξε κάρτα για άλλο μάθημα", command=createsubj, background="#BFEBDC",
                     font=("Consolas", 10), relief="solid").pack(pady=10)
    load = ttk.Button(chumf, text="Φόρτωση καρτών", command=loadforhum).pack(pady=10)


def cpr():  #create programming, δημιουργία κάρτας για εισαγωγή στον προγραμματισμό
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        userqds = createquestion.get()
        userrds = createright.get()
        userw1ds = createwrong1.get()
        userw2ds = createwrong2.get()
        prq.append(quest(userqds, userrds, userw1ds, userw2ds)) #τοποθέτηση της κάρτας στην αντίστοιχη λίστα
        file = open("prcards.txt", "a") #χρήση του αντίστοιχου αρχείου
        file.write(userqds + '~' + userrds + '~' + userw1ds + '~' + userw2ds + '\n')
        file.close()
        lbl3 = tk.Label(cprf, text="Η κάρτα δημιουργήθηκε!", background="#2F323B", foreground="#39FF14").pack()

    def loadforpr():
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        try:
            file = open("prcards.txt", "r")
            information = file.readlines()
            for i in information:
                cards = i.split('~')
                question = cards[0]
                rightanswer = cards[1]
                wronganswer1 = cards[2]
                wronganswer2 = cards[3]
                prq.append(quest(question, rightanswer, wronganswer1, wronganswer2))

            file.close()
            lbl3 = tk.Label(cprf, text="Οι κάρτες φορτώθηκαν!", background="#2F323B",
                        foreground="#39FF14").pack()
        except:
            lbl3 = tk.Label(cprf, text="Κάτι πήγε στραβά με το αρχείο!", background="#2F323B",
                            foreground="#39FF14").pack()

    hide()
    cprf.pack(fill="both", expand=1)
    userqds = createquestion.get()
    userrds = createright.get()
    userw1ds = createwrong1.get()
    userw2ds = createwrong2.get()
    lbl = tk.Label(cprf, text="Εισαγωγή στον προγραμματισμό", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).pack(pady=10)
    lbl2 = tk.Label(cprf, text="Ερώτηση", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).pack(
        pady=10)
    usrq = ttk.Entry(cprf, textvariable=createquestion).pack(pady=10)
    lbl3 = tk.Label(cprf, text="Σωστή απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usrr = ttk.Entry(cprf, textvariable=createright).pack(pady=10)
    lbl4 = tk.Label(cprf, text="Πρώτη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw1 = ttk.Entry(cprf, textvariable=createwrong1).pack(pady=10)
    lbl5 = tk.Label(cprf, text="Δεύτερη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw2 = ttk.Entry(cprf, textvariable=createwrong2).pack(pady=10)
    btn = tk.Button(cprf, text="Δημιουργία", command=append, background="#BFEBDC", font=("Consolas", 10),
                    relief="solid").pack(pady=10)
    btn2 = tk.Button(cprf, text="Φτιάξε άλλη", command=cpr, background="#BFEBDC", font=("Consolas", 10),
                     relief="solid").pack(pady=10)
    btn3 = tk.Button(cprf, text="Φτιάξε κάρτα για άλλο μάθημα", command=createsubj, background="#BFEBDC",
                     font=("Consolas", 10), relief="solid").pack(pady=10)
    load = ttk.Button(cprf, text="Φόρτωση καρτών", command=loadforpr).pack(pady=10)


def cpr2(): #create programming 2, δημιουργία κάρτας για προγραμματισμό υπολογιστών
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        userqds = createquestion.get()
        userrds = createright.get()
        userw1ds = createwrong1.get()
        userw2ds = createwrong2.get()
        pr2q.append(quest(userqds, userrds, userw1ds, userw2ds))    #πρόσθεση κάρτας στην αντίστοιχη λίστα
        file = open("pr2cards.txt", "a")    #χρήση του αντίστοιχου αρχείου
        file.write(userqds + '~' + userrds + '~' + userw1ds + '~' + userw2ds + '\n')
        file.close()
        lbl3 = tk.Label(cpr2f, text="Η κάρτα δημιουργήθηκε!", background="#2F323B", foreground="#39FF14").pack()

    def loadforpr2():
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        try:
            file = open("pr2cards.txt", "r")
            information = file.readlines()
            for i in information:
                cards = i.split('~')
                question = cards[0]
                rightanswer = cards[1]
                wronganswer1 = cards[2]
                wronganswer2 = cards[3]
                pr2q.append(quest(question, rightanswer, wronganswer1, wronganswer2))

            file.close()
            lbl3 = tk.Label(cpr2f, text="Οι κάρτες φορτώθηκαν!", background="#2F323B",
                        foreground="#39FF14").pack()
        except:
            lbl3 = tk.Label(cpr2f, text="Κάτι πήγε στραβά με το αρχείο!", background="#2F323B",
                            foreground="#39FF14").pack()


    hide()
    cpr2f.pack(fill="both", expand=1)
    userqds = createquestion.get()
    userrds = createright.get()
    userw1ds = createwrong1.get()
    userw2ds = createwrong2.get()
    lbl = tk.Label(cpr2f, text="Προγραμματισμός υπολογιστών", background="#2F323B", foreground="#39FF14",font=("Consolas", 10)).pack(pady=10)
    lbl2 = tk.Label(cpr2f, text="Ερώτηση", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).pack(pady=10)
    usrq = ttk.Entry(cpr2f, textvariable=createquestion).pack(pady=10)
    lbl3 = tk.Label(cpr2f, text="Σωστή απάντηση", background="#2F323B", foreground="#39FF14",font=("Consolas", 10)).pack(pady=10)
    usrr = ttk.Entry(cpr2f, textvariable=createright).pack(pady=10)
    lbl4 = tk.Label(cpr2f, text="Πρώτη λάθος απάντηση", background="#2F323B", foreground="#39FF14",font=("Consolas", 10)).pack(pady=10)
    usw1 = ttk.Entry(cpr2f, textvariable=createwrong1).pack(pady=10)
    lbl5 = tk.Label(cpr2f, text="Δεύτερη λάθος απάντηση", background="#2F323B", foreground="#39FF14",font=("Consolas", 10)).pack(pady=10)
    usw2 = ttk.Entry(cpr2f, textvariable=createwrong2).pack(pady=10)
    btn = tk.Button(cpr2f, text="Δημιουργία", command=append, background="#BFEBDC", font=("Consolas", 10),relief="solid").pack(pady=10)
    btn2 = tk.Button(cpr2f, text="Φτιάξε άλλη", command=cpr2, background="#BFEBDC", font=("Consolas", 10), relief="solid").pack(pady=10)
    btn3 = tk.Button(cpr2f, text="Φτιάξε κάρτα για άλλο μάθημα", command=createsubj, background="#BFEBDC",font=("Consolas", 10), relief="solid").pack(pady=10)
    load = ttk.Button(cpr2f, text="Φόρτωση καρτών", command=loadforpr2).pack(pady=10)


def cpb():  #create probabilities, δημιουργία κάρτας για πιθανότητες
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        userqds = createquestion.get()
        userrds = createright.get()
        userw1ds = createwrong1.get()
        userw2ds = createwrong2.get()
        pbq.append(quest(userqds, userrds, userw1ds, userw2ds)) #πρόσθεση κάρτας στη σχετική λίστα
        file = open("probcards.txt", "a")   #χρήση αντίστοιχου αρχείου
        file.write(userqds + '~' + userrds + '~' + userw1ds + '~' + userw2ds + '\n')
        file.close()
        lbl3 = tk.Label(cpbf, text="Η κάρτα δημιουργήθηκε!", background="#2F323B", foreground="#39FF14").pack()

    def loadforpb():
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        try:
            file = open("probcards.txt", "r")
            information = file.readlines()
            for i in information:
                cards = i.split('~')
                question = cards[0]
                rightanswer = cards[1]
                wronganswer1 = cards[2]
                wronganswer2 = cards[3]
                pbq.append(quest(question, rightanswer, wronganswer1, wronganswer2))

            file.close()
            lbl3 = tk.Label(cpbf, text="Οι κάρτες φορτώθηκαν!", background="#2F323B",
                        foreground="#39FF14").pack()
        except:
            lbl3 = tk.Label(cpbf, text="Κάτι πήγε στραβά με το αρχείο!", background="#2F323B",
                            foreground="#39FF14").pack()

    hide()
    cpbf.pack(fill="both", expand=1)
    userqds = createquestion.get()
    userrds = createright.get()
    userw1ds = createwrong1.get()
    userw2ds = createwrong2.get()
    lbl = tk.Label(cpbf, text="Πιθανότητες", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).pack(
        pady=10)
    lbl2 = tk.Label(cpbf, text="Ερώτηση", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).pack(
        pady=10)
    usrq = ttk.Entry(cpbf, textvariable=createquestion).pack(pady=10)
    lbl3 = tk.Label(cpbf, text="Σωστή απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usrr = ttk.Entry(cpbf, textvariable=createright).pack(pady=10)
    lbl4 = tk.Label(cpbf, text="Πρώτη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw1 = ttk.Entry(cpbf, textvariable=createwrong1).pack(pady=10)
    lbl5 = tk.Label(cpbf, text="Δεύτερη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw2 = ttk.Entry(cpbf, textvariable=createwrong2).pack(pady=10)
    btn = tk.Button(cpbf, text="Δημιουργία", command=append, background="#BFEBDC", font=("Consolas", 10),
                    relief="solid").pack(pady=10)
    btn2 = tk.Button(cpbf, text="Φτιάξε άλλη", command=cpb, background="#BFEBDC", font=("Consolas", 10),
                     relief="solid").pack(pady=10)
    btn3 = tk.Button(cpbf, text="Φτιάξε κάρτα για άλλο μάθημα", command=createsubj, background="#BFEBDC",
                     font=("Consolas", 10), relief="solid").pack(pady=10)
    load = ttk.Button(cpbf, text="Φόρτωση καρτών", command=loadforpb).pack(pady=10)


def cdm():  #create discrete mathematics, δημιουργία κάρτας για διακριτά μαθηματικά
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        userqds = createquestion.get()
        userrds = createright.get()
        userw1ds = createwrong1.get()
        userw2ds = createwrong2.get()
        dmq.append(quest(userqds, userrds, userw1ds, userw2ds)) #πρόσθεση κάρτας στη σχετική λίστα
        file = open("discretemathcards.txt", "a")   #χρήση σχετικού αρχείου
        file.write(userqds + '~' + userrds + '~' + userw1ds + '~' + userw2ds + '\n')
        file.close()
        lbl3 = tk.Label(cdmf, text="Η κάρτα δημιουργήθηκε!", background="#2F323B", foreground="#39FF14").pack()

    def loadfordm():
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        try:
            file = open("discretemathcards.txt", "r")
            information = file.readlines()
            for i in information:
                cards = i.split('~')
                question = cards[0]
                rightanswer = cards[1]
                wronganswer1 = cards[2]
                wronganswer2 = cards[3]
                dmq.append(quest(question, rightanswer, wronganswer1, wronganswer2))

            file.close()
            lbl3 = tk.Label(cdmf, text="Οι κάρτες φορτώθηκαν!", background="#2F323B",
                        foreground="#39FF14").pack()
        except:
            lbl3 = tk.Label(cdmf, text="Κάτι πήγε στραβά με το αρχείο!", background="#2F323B",
                            foreground="#39FF14").pack()

    hide()
    cdmf.pack(fill="both", expand=1)
    userqds = createquestion.get()
    userrds = createright.get()
    userw1ds = createwrong1.get()
    userw2ds = createwrong2.get()
    lbl = tk.Label(cdmf, text="Διακριτά μαθηματικά", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).pack(pady=10)
    lbl2 = tk.Label(cdmf, text="Ερώτηση", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).pack(
        pady=10)
    usrq = ttk.Entry(cdmf, textvariable=createquestion).pack(pady=10)
    lbl3 = tk.Label(cdmf, text="Σωστή απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usrr = ttk.Entry(cdmf, textvariable=createright).pack(pady=10)
    lbl4 = tk.Label(cdmf, text="Πρώτη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw1 = ttk.Entry(cdmf, textvariable=createwrong1).pack(pady=10)
    lbl5 = tk.Label(cdmf, text="Δεύτερη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw2 = ttk.Entry(cdmf, textvariable=createwrong2).pack(pady=10)
    btn = tk.Button(cdmf, text="Δημιουργία", command=append, background="#BFEBDC", font=("Consolas", 10),
                    relief="solid").pack(pady=10)
    btn2 = tk.Button(cdmf, text="Φτιάξε άλλη", command=cdm, background="#BFEBDC", font=("Consolas", 10),
                     relief="solid").pack(pady=10)
    btn3 = tk.Button(cdmf, text="Φτιάξε κάρτα για άλλο μάθημα", command=createsubj, background="#BFEBDC",
                     font=("Consolas", 10), relief="solid").pack(pady=10)
    load = ttk.Button(cdmf, text="Φόρτωση καρτών", command=loadfordm).pack(pady=10)


def clin(): #create linear algebra, δημιουργία κάρτας για γραμμική άλγεβρα
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        userqds = createquestion.get()
        userrds = createright.get()
        userw1ds = createwrong1.get()
        userw2ds = createwrong2.get()
        linq.append(quest(userqds, userrds, userw1ds, userw2ds))    #πρόσθεση κάρτας στη σχετική λίστα
        file = open("linearcards.txt", "a") #χρήση του αντίστοιχου αρχείου
        file.write(userqds + '~' + userrds + '~' + userw1ds + '~' + userw2ds + '\n')
        file.close()
        lbl3 = tk.Label(clinf, text="Η κάρτα δημιουργήθηκε!", background="#2F323B", foreground="#39FF14").pack()

    def loadforlin():
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        try:
            file = open("linearcards.txt", "r")
            information = file.readlines()
            for i in information:
                cards = i.split('~')
                question = cards[0]
                rightanswer = cards[1]
                wronganswer1 = cards[2]
                wronganswer2 = cards[3]
                linq.append(quest(question, rightanswer, wronganswer1, wronganswer2))

            file.close()
            lbl3 = tk.Label(clinf, text="Οι κάρτες φορτώθηκαν!", background="#2F323B",
                        foreground="#39FF14").pack()
        except:
            lbl3 = tk.Label(clinf, text="Κάτι πήγε στραβά με το αρχείο!", background="#2F323B",
                            foreground="#39FF14").pack()

    hide()
    clinf.pack(fill="both", expand=1)
    userqds = createquestion.get()
    userrds = createright.get()
    userw1ds = createwrong1.get()
    userw2ds = createwrong2.get()
    lbl = tk.Label(clinf, text="Γραμμική άλγεβρα", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).pack(pady=10)
    lbl2 = tk.Label(clinf, text="Ερώτηση", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).pack(
        pady=10)
    usrq = ttk.Entry(clinf, textvariable=createquestion).pack(pady=10)
    lbl3 = tk.Label(clinf, text="Σωστή απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usrr = ttk.Entry(clinf, textvariable=createright).pack(pady=10)
    lbl4 = tk.Label(clinf, text="Πρώτη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw1 = ttk.Entry(clinf, textvariable=createwrong1).pack(pady=10)
    lbl5 = tk.Label(clinf, text="Δεύτερη λάθος απάντηση", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).pack(pady=10)
    usw2 = ttk.Entry(clinf, textvariable=createwrong2).pack(pady=10)
    btn = tk.Button(clinf, text="Δημιουργία", command=append, background="#BFEBDC", font=("Consolas", 10),
                    relief="solid").pack(pady=10)
    btn2 = tk.Button(clinf, text="Φτιάξε άλλη", command=clin, background="#BFEBDC", font=("Consolas", 10),
                     relief="solid").pack(pady=10)
    btn3 = tk.Button(clinf, text="Φτιάξε κάρτα για άλλο μάθημα", command=createsubj, background="#BFEBDC",
                     font=("Consolas", 10), relief="solid").pack(pady=10)
    load = ttk.Button(clinf, text="Φόρτωση καρτών", command=loadforlin).pack(pady=10)


def createsubj():   #συνάρτηση δημιουργίας κάρτας για τα προσφερόμενα μαθήματα, διακρίνεται σε ποιά συνάρτηση μας μεταφέρει το κάθε κουμπί (command=....)
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    hide()
    createsubjf.pack(fill="both", expand=1)
    lbl = tk.Label(createsubjf, text="Διάλεξε για ποίο μάθημα θέλεις να φτιάξεις κάρτες", background="#2F323B",
                   foreground="#39FF14", font=("Consolas", 10)).pack(pady=10)
    btn1 = tk.Button(createsubjf, text="Δομές δεδομένων", command=cds, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).pack(pady=10)
    btn2 = tk.Button(createsubjf, text="Μαθηματικός λογισμός", command=cmath, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).pack(pady=10)
    btn3 = tk.Button(createsubjf, text="Πιθανότητες", command=cpb, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).pack(pady=10)
    btn4 = tk.Button(createsubjf, text="Διακριτά μαθηματικά", command=cdm, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).pack(pady=10)
    btn5 = tk.Button(createsubjf, text="Γραμμική άλγεβρα", command=clin, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).pack(pady=10)
    btn6 = tk.Button(createsubjf, text="Εισαγωγή στην επιστήμη των υπολογιστών", command=ccs, background="#BFEBDC",
                     relief="solid", font=("Consolas", 10)).pack(pady=10)
    btn7 = tk.Button(createsubjf, text="Εισαγωγή στον προγραμματισμό", command=cpr, background="#BFEBDC",
                     relief="solid", font=("Consolas", 10)).pack(pady=10)
    btn8 = tk.Button(createsubjf, text="Προγραμματισμός υπολογιστών", command=cpr2, background="#BFEBDC",
                     relief="solid", font=("Consolas", 10)).pack(pady=10)
    btn9 = tk.Button(createsubjf, text="Εφαρμοσμένος προγραμματισμός με Python", command=cpy, background="#BFEBDC",
                     relief="solid", font=("Consolas", 10)).pack(pady=10)
    btn10 = tk.Button(createsubjf, text="Πληροφορική στις ανθρωπιστικές επιστήμες", command=chum, background="#BFEBDC",
                      relief="solid", font=("Consolas", 10)).pack(pady=10)


def modifyds(): #συνάρτηση τροποποίησης υφισταμένων καρτών στο μάθημα των δομών δεδομένων
    c = randint(0, len(dq) - 1) #δημιουργία δείκτη, πλήρως τυχαίου
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        #με τη συνάρτηση αυτή, παίρνουμε απο τα entry box τους νέους συνδυασμούς ερώτησης-απαντήσεων και τους θέτουμε στις θέσεις που βρίσκοταν προηγουμένως οι παλαιοί συνδυασμοί
        modq = modifyquestion.get() #γραμμές 1851-1854, fetching συνδυασμών απο entry box
        modr = modifyright.get()
        modw1 = modifyw1.get()
        modw2 = modifyw2.get()
        dq[c].q = modq  #γραμμές 1855-1858: ανάθεση νέων συνδυασμών στη θέση των προηγουμένων
        dq[c].ra = modr
        dq[c].wa1 = modw1
        dq[c].wa2 = modw2

    hide()
    modifydsf.grid()
    modq = modifyquestion.get() #τροποποιημένη ερώτηση
    modr = modifyright.get()    #τροποποιημένη σωστή απάντηση
    modw1 = modifyw1.get()  #τροποποιημένη πρώτη λάθος απάντηση
    modw2 = modifyw2.get()  #τροποποιημένη δεύτερη λάθος απάντηση
    l = tk.Label(modifydsf, text="Τρέχουσα κάρτα", background="#2F323B", foreground="#39FF14",
                 font=("Consolas", 10)).grid(row=1, column=0, pady=30, padx=40)
    l2 = tk.Label(modifydsf, text="Τροποποιημένη κάρτα", background="#2F323B", foreground="#39FF14",
                  font=("Consolas", 10)).grid(row=1, column=2, pady=30, padx=40)
    lbl = tk.Message(modifydsf, text=dq[c].q, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=2, column=0, pady=30, padx=40)
    lbl2 = tk.Message(modifydsf, text=dq[c].ra, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=3, column=0, pady=30, padx=40)
    lbl3 = tk.Message(modifydsf, text=dq[c].wa1, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=4, column=0, pady=30, padx=40)
    lbl4 = tk.Message(modifydsf, text=dq[c].wa2, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=5, column=0, pady=30, padx=40)
    lbq = tk.Label(modifydsf, text="<--- Ερώτηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=2, column=1, pady=30, padx=50)
    lbr = tk.Label(modifydsf, text="<--- Σωστή απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=3, column=1, pady=30, padx=50)
    lbw = tk.Label(modifydsf, text="<--- Πρώτη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=4, column=1, pady=30, padx=50)
    lbw2 = tk.Label(modifydsf, text="<--- Δεύτερη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).grid(row=5, column=1, pady=30, padx=50)
    modifyqe = ttk.Entry(modifydsf, textvariable=modifyquestion).grid(row=2, column=2, pady=30, padx=50)    #γραμμές 1886-1889, ανάθεση σε μεταβλητές απο τα entry box
    modifyre = ttk.Entry(modifydsf, textvariable=modifyright).grid(row=3, column=2, pady=30, padx=50)
    modifyw1e = ttk.Entry(modifydsf, textvariable=modifyw1).grid(row=4, column=2, pady=30, padx=50)
    modifyw2e = ttk.Entry(modifydsf, textvariable=modifyw2).grid(row=5, column=2, pady=30, padx=50)
    btn = tk.Button(modifydsf, text="Αλλαγή", command=append, background="#BFEBDC", relief="solid",
                    font=("Consolas", 10)).grid(row=6, column=0, pady=30, padx=50)
    btn2 = tk.Button(modifydsf, text="Άλλαξε άλλη κάρτα", command=modifyds, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).grid(row=6, column=2, pady=30, padx=50)
    #ΣΗΜΕΙΩΣΗ: Και στις υπόλοιπες συναρτήσεις τροποποίησης κάρτας, για όλα τα μαθήματα ακολουθούνται ακριβώς οι ίδιες μεθόδοι και τεχνικές

def modifymath(): #τροποποίηση κάρτας για μαθηματικό λογισμό
    c = randint(0, len(mathq) - 1)
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        modq = modifyquestion.get()
        modr = modifyright.get()
        modw1 = modifyw1.get()
        modw2 = modifyw2.get()
        mathq[c].q = modq
        mathq[c].ra = modr
        mathq[c].wa1 = modw1
        mathq[c].wa2 = modw2

    hide()
    modifymathf.grid()
    modq = modifyquestion.get()
    modr = modifyright.get()
    modw1 = modifyw1.get()
    modw2 = modifyw2.get()
    l = tk.Label(modifymathf, text="Τρέχουσα κάρτα", background="#2F323B", foreground="#39FF14",
                 font=("Consolas", 10)).grid(row=1, column=0, pady=31, padx=40)
    l2 = tk.Label(modifymathf, text="Τροποποιημένη κάρτα", background="#2F323B", foreground="#39FF14",
                  font=("Consolas", 10)).grid(row=1, column=2, pady=31, padx=40, columnspan=5)
    lbl = tk.Message(modifymathf, text=mathq[c].q, background="#2F323B", foreground="#39FF14",
                     font=("Consolas", 10)).grid(row=2, column=0, pady=31, padx=40)
    lbl2 = tk.Message(modifymathf, text=mathq[c].ra, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=3, column=0, pady=31, padx=40)
    lbl3 = tk.Message(modifymathf, text=mathq[c].wa1, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=4, column=0, pady=31, padx=40)
    lbl4 = tk.Message(modifymathf, text=mathq[c].wa2, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=5, column=0, pady=31, padx=40)
    lbq = tk.Label(modifymathf, text="<--- Ερώτηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=2, column=1, pady=31, padx=40)
    lbr = tk.Label(modifymathf, text="<--- Σωστή απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=3, column=1, pady=31, padx=40)
    lbw = tk.Label(modifymathf, text="<--- Πρώτη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=4, column=1, pady=31, padx=40)
    lbw2 = tk.Label(modifymathf, text="<--- Δεύτερη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).grid(row=5, column=1, pady=31, padx=40)
    modifyqe = ttk.Entry(modifymathf, textvariable=modifyquestion).grid(row=2, column=2, pady=31, padx=40)  ##γραμμές 1936-1943, ανάθεση σε μεταβλητές απο τα entry box
    modifyre = ttk.Entry(modifymathf, textvariable=modifyright).grid(row=3, column=2, pady=31, padx=40)
    modifyw1e = ttk.Entry(modifymathf, textvariable=modifyw1).grid(row=4, column=2, pady=31, padx=40)
    modifyw2e = ttk.Entry(modifymathf, textvariable=modifyw2).grid(row=5, column=2, pady=31, padx=40)
    btn = tk.Button(modifymathf, text="Αλλαγή", command=append, background="#BFEBDC", relief="solid",
                    font=("Consolas", 10)).grid(row=6, column=0, pady=31, padx=40)
    btn2 = tk.Button(modifymathf, text="Άλλαξε άλλη κάρτα", command=modifymath, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).grid(row=6, column=2, pady=31, padx=40)


def modifyprob():   #τροποποίηση κάρτας για πιθανότητες
    c = randint(0, len(pbq) - 1)
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        modq = modifyquestion.get()
        modr = modifyright.get()
        modw1 = modifyw1.get()
        modw2 = modifyw2.get()
        pbq[c].q = modq
        pbq[c].ra = modr
        pbq[c].wa1 = modw1
        pbq[c].wa2 = modw2

    hide()
    modifyprbf.grid()
    modq = modifyquestion.get()
    modr = modifyright.get()
    modw1 = modifyw1.get()
    modw2 = modifyw2.get()
    l = tk.Label(modifyprbf, text="Τρέχουσα κάρτα", background="#2F323B", foreground="#39FF14",
                 font=("Consolas", 10)).grid(row=1, column=0, pady=35, padx=40)
    l2 = tk.Label(modifyprbf, text="Τροποποιημένη κάρτα", background="#2F323B", foreground="#39FF14",
                  font=("Consolas", 10)).grid(row=1, column=2, pady=35, padx=40)
    lbl = tk.Message(modifyprbf, text=pbq[c].q, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=2, column=0, pady=35, padx=65)
    lbl2 = tk.Message(modifyprbf, text=pbq[c].ra, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=3, column=0, pady=35, padx=65)
    lbl3 = tk.Message(modifyprbf, text=pbq[c].wa1, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=4, column=0, pady=35, padx=65)
    lbl4 = tk.Message(modifyprbf, text=pbq[c].wa2, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=5, column=0, pady=35, padx=65)
    lbq = tk.Label(modifyprbf, text="<--- Ερώτηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=2, column=1, pady=35, padx=40)
    lbr = tk.Label(modifyprbf, text="<--- Σωστή απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=3, column=1, pady=35, padx=40)
    lbw = tk.Label(modifyprbf, text="<--- Πρώτη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=4, column=1, pady=35, padx=40)
    lbw2 = tk.Label(modifyprbf, text="<--- Δεύτερη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).grid(row=5, column=1, pady=35, padx=40)
    modifyqe = ttk.Entry(modifyprbf, textvariable=modifyquestion).grid(row=2, column=2, pady=35, padx=40)   #γραμμές 1986-1993, ανάθεση σε μεταβλητές απο τα entry box
    modifyre = ttk.Entry(modifyprbf, textvariable=modifyright).grid(row=3, column=2, pady=35, padx=40)
    modifyw1e = ttk.Entry(modifyprbf, textvariable=modifyw1).grid(row=4, column=2, pady=35, padx=40)
    modifyw2e = ttk.Entry(modifyprbf, textvariable=modifyw2).grid(row=5, column=2, pady=30, padx=40)
    btn = tk.Button(modifyprbf, text="Αλλαγή", command=append, background="#BFEBDC", relief="solid",
                    font=("Consolas", 10)).grid(row=6, column=0, pady=30, padx=40)
    btn2 = tk.Button(modifyprbf, text="Άλλαξε άλλη κάρτα", command=modifyprob, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).grid(row=6, column=2, pady=30, padx=40)


def modifypr(): #τροποποίηση κάρτας για εισαγωγή στον προγραμματισμό
    c = randint(0, len(prq) - 1)
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        modq = modifyquestion.get()
        modr = modifyright.get()
        modw1 = modifyw1.get()
        modw2 = modifyw2.get()
        prq[c].q = modq
        prq[c].ra = modr
        prq[c].wa1 = modw1
        prq[c].wa2 = modw2

    hide()
    modifyprf.grid()
    modq = modifyquestion.get()
    modr = modifyright.get()
    modw1 = modifyw1.get()
    modw2 = modifyw2.get()
    l = tk.Label(modifyprf, text="Τρέχουσα κάρτα", background="#2F323B", foreground="#39FF14",
                 font=("Consolas", 10)).grid(row=1, column=0, pady=30, padx=40)
    l2 = tk.Label(modifyprf, text="Τροποποιημένη κάρτα", background="#2F323B", foreground="#39FF14",
                  font=("Consolas", 10)).grid(row=1, column=2, pady=30, padx=40)
    lbl = tk.Message(modifyprf, text=prq[c].q, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=2, column=0, pady=30, padx=65)
    lbl2 = tk.Message(modifyprf, text=prq[c].ra, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=3, column=0, pady=30, padx=65)
    lbl3 = tk.Message(modifyprf, text=prq[c].wa1, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=4, column=0, pady=30, padx=65)
    lbl4 = tk.Message(modifyprf, text=prq[c].wa2, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=5, column=0, pady=30, padx=65)
    lbq = tk.Label(modifyprf, text="<--- Ερώτηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=2, column=1, pady=30, padx=50)
    lbr = tk.Label(modifyprf, text="<--- Σωστή απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=3, column=1, pady=30, padx=50)
    lbw = tk.Label(modifyprf, text="<--- Πρώτη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=4, column=1, pady=30, padx=50)
    lbw2 = tk.Label(modifyprf, text="<--- Δεύτερη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).grid(row=5, column=1, pady=30, padx=50)
    modifyqe = ttk.Entry(modifyprf, textvariable=modifyquestion).grid(row=2, column=2, pady=30, padx=50)   #γραμμές 2036-2043, ανάθεση σε μεταβλητές απο τα entry box
    modifyre = ttk.Entry(modifyprf, textvariable=modifyright).grid(row=3, column=2, pady=30, padx=50)
    modifyw1e = ttk.Entry(modifyprf, textvariable=modifyw1).grid(row=4, column=2, pady=30, padx=50)
    modifyw2e = ttk.Entry(modifyprf, textvariable=modifyw2).grid(row=5, column=2, pady=30, padx=50)
    btn = tk.Button(modifyprf, text="Αλλαγή", command=append, background="#BFEBDC", relief="solid",
                    font=("Consolas", 10)).grid(row=6, column=0, pady=30, padx=50)
    btn2 = tk.Button(modifyprf, text="Άλλαξε άλλη κάρτα", command=modifypr, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).grid(row=6, column=2, pady=30, padx=50)


def modifypr2():    #τροποποίηση κάρτας για προγραμματισμό υπολογιστών
    c = randint(0, len(pr2q) - 1)
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        modq = modifyquestion.get()
        modr = modifyright.get()
        modw1 = modifyw1.get()
        modw2 = modifyw2.get()
        pr2q[c].q = modq
        pr2q[c].ra = modr
        pr2q[c].wa1 = modw1
        pr2q[c].wa2 = modw2

    hide()
    modifypr2f.grid()
    modq = modifyquestion.get()
    modr = modifyright.get()
    modw1 = modifyw1.get()
    modw2 = modifyw2.get()
    l = tk.Label(modifypr2f, text="Τρέχουσα κάρτα", background="#2F323B", foreground="#39FF14",
                 font=("Consolas", 10)).grid(row=1, column=0, pady=30, padx=40)
    l2 = tk.Label(modifypr2f, text="Τροποποιημένη κάρτα", background="#2F323B", foreground="#39FF14",
                  font=("Consolas", 10)).grid(row=1, column=2, pady=30, padx=40)
    lbl = tk.Message(modifypr2f, text=pr2q[c].q, background="#2F323B", foreground="#39FF14",
                     font=("Consolas", 10)).grid(row=2, column=0, pady=30, padx=65)
    lbl2 = tk.Message(modifypr2f, text=pr2q[c].ra, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=3, column=0, pady=30, padx=65)
    lbl3 = tk.Message(modifypr2f, text=pr2q[c].wa1, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=4, column=0, pady=30, padx=65)
    lbl4 = tk.Message(modifypr2f, text=pr2q[c].wa2, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=5, column=0, pady=30, padx=65)
    lbq = tk.Label(modifypr2f, text="<--- Ερώτηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=2, column=1, pady=30, padx=50)
    lbr = tk.Label(modifypr2f, text="<--- Σωστή απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=3, column=1, pady=30, padx=50)
    lbw = tk.Label(modifypr2f, text="<--- Πρώτη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=4, column=1, pady=30, padx=50)
    lbw2 = tk.Label(modifypr2f, text="<--- Δεύτερη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).grid(row=5, column=1, pady=30, padx=50)
    modifyqe = ttk.Entry(modifypr2f, textvariable=modifyquestion).grid(row=2, column=2, pady=30, padx=50)   ##γραμμές 2086-2093, ανάθεση σε μεταβλητές απο τα entry box
    modifyre = ttk.Entry(modifypr2f, textvariable=modifyright).grid(row=3, column=2, pady=30, padx=50)
    modifyw1e = ttk.Entry(modifypr2f, textvariable=modifyw1).grid(row=4, column=2, pady=30, padx=50)
    modifyw2e = ttk.Entry(modifypr2f, textvariable=modifyw2).grid(row=5, column=2, pady=30, padx=50)
    btn = tk.Button(modifypr2f, text="Αλλαγή", command=append, background="#BFEBDC", relief="solid",
                    font=("Consolas", 10)).grid(row=6, column=0, pady=30, padx=50)
    btn2 = tk.Button(modifypr2f, text="Άλλαξε άλλη κάρτα", command=modifypr2, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).grid(row=6, column=2, pady=30, padx=50)


def modifypy(): #τροποποίηση κάρτας για εφαρμοσμένο προγραμματισμό με Python
    c = randint(0, len(pyq) - 1)
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        modq = modifyquestion.get()
        modr = modifyright.get()
        modw1 = modifyw1.get()
        modw2 = modifyw2.get()
        pyq[c].q = modq
        pyq[c].ra = modr
        pyq[c].wa1 = modw1
        pyq[c].wa2 = modw2

    hide()
    modifypyf.grid()
    modq = modifyquestion.get()
    modr = modifyright.get()
    modw1 = modifyw1.get()
    modw2 = modifyw2.get()
    l = tk.Label(modifypyf, text="Τρέχουσα κάρτα", background="#2F323B", foreground="#39FF14",
                 font=("Consolas", 10)).grid(row=1, column=0, pady=30, padx=40)
    l2 = tk.Label(modifypyf, text="Τροποποιημένη κάρτα", background="#2F323B", foreground="#39FF14",
                  font=("Consolas", 10)).grid(row=1, column=2, pady=30, padx=40)
    lbl = tk.Message(modifypyf, text=pyq[c].q, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=2, column=0, pady=30, padx=65)
    lbl2 = tk.Message(modifypyf, text=pyq[c].ra, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=3, column=0, pady=30, padx=65)
    lbl3 = tk.Message(modifypyf, text=pyq[c].wa1, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=4, column=0, pady=30, padx=65)
    lbl4 = tk.Message(modifypyf, text=pyq[c].wa2, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=5, column=0, pady=30, padx=65)
    lbq = tk.Label(modifypyf, text="<--- Ερώτηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=2, column=1, pady=30, padx=50)
    lbr = tk.Label(modifypyf, text="<--- Σωστή απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=3, column=1, pady=30, padx=50)
    lbw = tk.Label(modifypyf, text="<--- Πρώτη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=4, column=1, pady=30, padx=50)
    lbw2 = tk.Label(modifypyf, text="<--- Δεύτερη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).grid(row=5, column=1, pady=30, padx=50)
    modifyqe = ttk.Entry(modifypyf, textvariable=modifyquestion).grid(row=2, column=2, pady=30, padx=50)    #γραμμές 2136-2143, ανάθεση σε μεταβλητές απο τα entry box
    modifyre = ttk.Entry(modifypyf, textvariable=modifyright).grid(row=3, column=2, pady=30, padx=50)
    modifyw1e = ttk.Entry(modifypyf, textvariable=modifyw1).grid(row=4, column=2, pady=30, padx=50)
    modifyw2e = ttk.Entry(modifypyf, textvariable=modifyw2).grid(row=5, column=2, pady=30, padx=50)
    btn = tk.Button(modifypyf, text="Αλλαγή", command=append, background="#BFEBDC", relief="solid",
                    font=("Consolas", 10)).grid(row=6, column=0, pady=30, padx=50)
    btn2 = tk.Button(modifypyf, text="Άλλαξε άλλη κάρτα", command=modifypy, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).grid(row=6, column=2, pady=30, padx=50)


def modifydm(): #τροποποίηση κάρτας για διακριτά μαθηματικά
    c = randint(0, len(dmq) - 1)
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        modq = modifyquestion.get()
        modr = modifyright.get()
        modw1 = modifyw1.get()
        modw2 = modifyw2.get()
        dmq[c].q = modq
        dmq[c].ra = modr
        dmq[c].wa1 = modw1
        dmq[c].wa2 = modw2


    hide()
    modifydmf.grid()
    modq = modifyquestion.get()
    modr = modifyright.get()
    modw1 = modifyw1.get()
    modw2 = modifyw2.get()
    l = tk.Label(modifydmf, text="Τρέχουσα κάρτα", background="#2F323B", foreground="#39FF14",
                 font=("Consolas", 10)).grid(row=1, column=0, pady=30, padx=40)
    l2 = tk.Label(modifydmf, text="Τροποποιημένη κάρτα", background="#2F323B", foreground="#39FF14",
                  font=("Consolas", 10)).grid(row=1, column=2, pady=30, padx=40)
    lbl = tk.Message(modifydmf, text=dmq[c].q, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=2, column=0, pady=30, padx=65)
    lbl2 = tk.Message(modifydmf, text=dmq[c].ra, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=3, column=0, pady=30, padx=65)
    lbl3 = tk.Message(modifydmf, text=dmq[c].wa1, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=4, column=0, pady=30, padx=65)
    lbl4 = tk.Message(modifydmf, text=dmq[c].wa2, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=5, column=0, pady=30, padx=65)
    lbq = tk.Label(modifydmf, text="<--- Ερώτηση --->", background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=2, column=1, pady=30, padx=50)
    lbr = tk.Label(modifydmf, text="<--- Σωστή απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=3, column=1, pady=30, padx=50)
    lbw = tk.Label(modifydmf, text="<--- Πρώτη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=4, column=1, pady=30, padx=50)
    lbw2 = tk.Label(modifydmf, text="<--- Δεύτερη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).grid(row=5, column=1, pady=30, padx=50)
    modifyqe = ttk.Entry(modifydmf, textvariable=modifyquestion).grid(row=2, column=2, pady=30, padx=50)#γραμμές 2187-2194, ανάθεση σε μεταβλητές απο τα entry box
    modifyre = ttk.Entry(modifydmf, textvariable=modifyright).grid(row=3, column=2, pady=30, padx=50)
    modifyw1e = ttk.Entry(modifydmf, textvariable=modifyw1).grid(row=4, column=2, pady=30, padx=50)
    modifyw2e = ttk.Entry(modifydmf, textvariable=modifyw2).grid(row=5, column=2, pady=30, padx=50)
    btn = tk.Button(modifydmf, text="Αλλαγή", command=append, background="#BFEBDC", relief="solid",
                    font=("Consolas", 10)).grid(row=6, column=0, pady=30, padx=50)
    btn2 = tk.Button(modifydmf, text="Άλλαξε άλλη κάρτα", command=modifydm, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).grid(row=6, column=2, pady=30, padx=50)


def modifycs(): #τροποποίηση κάρτας για επιστήμη υπολογιστών
    c = randint(0, len(csq) - 1)
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        modq = modifyquestion.get()
        modr = modifyright.get()
        modw1 = modifyw1.get()
        modw2 = modifyw2.get()
        csq[c].q = modq
        csq[c].ra = modr
        csq[c].wa1 = modw1
        csq[c].wa2 = modw2

    hide()
    modifycsf.grid()
    modq = modifyquestion.get()
    modr = modifyright.get()
    modw1 = modifyw1.get()
    modw2 = modifyw2.get()
    l = tk.Label(modifycsf, text="Τρέχουσα κάρτα", background="#2F323B", foreground="#39FF14",
                 font=("Consolas", 10)).grid(row=1, column=0, pady=30, padx=40)
    l2 = tk.Label(modifycsf, text="Τροποποιημένη κάρτα", background="#2F323B", foreground="#39FF14",
                  font=("Consolas", 10)).grid(row=1, column=2, pady=30, padx=40)
    lbl = tk.Message(modifycsf, text=csq[c].q, background="#2F323B", foreground="#39FF14", font=("Consolas", 10)).grid(
        row=2, column=0, pady=30, padx=65)
    lbl2 = tk.Message(modifycsf, text=csq[c].ra, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=3, column=0, pady=30, padx=65)
    lbl3 = tk.Message(modifycsf, text=csq[c].wa1, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=4, column=0, pady=30, padx=65)
    lbl4 = tk.Message(modifycsf, text=csq[c].wa2, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=5, column=0, pady=30, padx=65)
    lbq = tk.Label(modifycsf, text="<--- Ερώτηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=2, column=1, pady=30, padx=50)
    lbr = tk.Label(modifycsf, text="<--- Σωστή απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=3, column=1, pady=30, padx=50)
    lbw = tk.Label(modifycsf, text="<--- Πρώτη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=4, column=1, pady=30, padx=50)
    lbw2 = tk.Label(modifycsf, text="<--- Δεύτερη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).grid(row=5, column=1, pady=30, padx=50)
    modifyqe = ttk.Entry(modifycsf, textvariable=modifyquestion).grid(row=2, column=2, pady=30, padx=50)#γραμμές 2237-2244, ανάθεση σε μεταβλητές απο τα entry box
    modifyre = ttk.Entry(modifycsf, textvariable=modifyright).grid(row=3, column=2, pady=30, padx=50)
    modifyw1e = ttk.Entry(modifycsf, textvariable=modifyw1).grid(row=4, column=2, pady=30, padx=50)
    modifyw2e = ttk.Entry(modifycsf, textvariable=modifyw2).grid(row=5, column=2, pady=30, padx=50)
    btn = tk.Button(modifycsf, text="Αλλαγή", command=append, background="#BFEBDC", relief="solid",
                    font=("Consolas", 10)).grid(row=6, column=0, pady=30, padx=50)
    btn2 = tk.Button(modifycsf, text="Άλλαξε άλλη κάρτα", command=modifycs, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).grid(row=6, column=2, pady=30, padx=50)


def modifylin():    #τροποποίηση κάρτας για γραμμική άλγεβρα
    c = randint(0, len(linq) - 1)
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        modq = modifyquestion.get()
        modr = modifyright.get()
        modw1 = modifyw1.get()
        modw2 = modifyw2.get()
        linq[c].q = modq
        linq[c].ra = modr
        linq[c].wa1 = modw1
        linq[c].wa2 = modw2

    hide()
    modifylinf.grid()
    modq = modifyquestion.get()
    modr = modifyright.get()
    modw1 = modifyw1.get()
    modw2 = modifyw2.get()
    l = tk.Label(modifylinf, text="Τρέχουσα κάρτα", background="#2F323B", foreground="#39FF14",
                 font=("Consolas", 10)).grid(row=1, column=0, pady=30, padx=40)
    l2 = tk.Label(modifylinf, text="Τροποποιημένη κάρτα", background="#2F323B", foreground="#39FF14",
                  font=("Consolas", 10)).grid(row=1, column=2, pady=30, padx=40)
    lbl = tk.Message(modifylinf, text=linq[c].q, background="#2F323B", foreground="#39FF14",
                     font=("Consolas", 10)).grid(row=2, column=0, pady=30, padx=65)
    lbl2 = tk.Message(modifylinf, text=linq[c].ra, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=3, column=0, pady=30, padx=65)
    lbl3 = tk.Message(modifylinf, text=linq[c].wa1, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=4, column=0, pady=30, padx=65)
    lbl4 = tk.Message(modifylinf, text=linq[c].wa2, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=5, column=0, pady=30, padx=65)
    lbq = tk.Label(modifylinf, text="<--- Ερώτηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=2, column=1, pady=30, padx=50)
    lbr = tk.Label(modifylinf, text="<--- Σωστή απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=3, column=1, pady=30, padx=50)
    lbw = tk.Label(modifylinf, text="<--- Πρώτη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=4, column=1, pady=30, padx=50)
    lbw2 = tk.Label(modifylinf, text="<--- Δεύτερη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).grid(row=5, column=1, pady=30, padx=50)
    modifyqe = ttk.Entry(modifylinf, textvariable=modifyquestion).grid(row=2, column=2, pady=30, padx=50)   #γραμμές 2287-2294, ανάθεση σε μεταβλητές απο τα entry box
    modifyre = ttk.Entry(modifylinf, textvariable=modifyright).grid(row=3, column=2, pady=30, padx=50)
    modifyw1e = ttk.Entry(modifylinf, textvariable=modifyw1).grid(row=4, column=2, pady=30, padx=50)
    modifyw2e = ttk.Entry(modifylinf, textvariable=modifyw2).grid(row=5, column=2, pady=30, padx=50)
    btn = tk.Button(modifylinf, text="Αλλαγή", command=append, background="#BFEBDC", relief="solid",
                    font=("Consolas", 10)).grid(row=6, column=0, pady=30, padx=50)
    btn2 = tk.Button(modifylinf, text="Άλλαξε άλλη κάρτα", command=modifylin, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).grid(row=6, column=2, pady=30, padx=50)


def modifyhum():    #τροποποίηση κάρτας για πληροφορική στις ανθρωπιστικές επιστήμες
    c = randint(0, len(humq) - 1)
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    def append():
        winsound.PlaySound("gamebutton.wav", winsound.SND_FILENAME)
        modq = modifyquestion.get()
        modr = modifyright.get()
        modw1 = modifyw1.get()
        modw2 = modifyw2.get()
        humq[c].q = modq
        humq[c].ra = modr
        humq[c].wa1 = modw1
        humq[c].wa2 = modw2

    hide()
    modifyhumf.grid()
    modq = modifyquestion.get()
    modr = modifyright.get()
    modw1 = modifyw1.get()
    modw2 = modifyw2.get()
    l = tk.Label(modifyhumf, text="Τρέχουσα κάρτα", background="#2F323B", foreground="#39FF14",
                 font=("Consolas", 10)).grid(row=1, column=0, pady=30, padx=40)
    l2 = tk.Label(modifyhumf, text="Τροποποιημένη κάρτα", background="#2F323B", foreground="#39FF14",
                  font=("Consolas", 10)).grid(row=1, column=2, pady=30, padx=40)
    lbl = tk.Message(modifyhumf, text=humq[c].q, background="#2F323B", foreground="#39FF14",
                     font=("Consolas", 10)).grid(row=2, column=0, pady=30, padx=65)
    lbl2 = tk.Message(modifyhumf, text=humq[c].ra, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=3, column=0, pady=30, padx=65)
    lbl3 = tk.Message(modifyhumf, text=humq[c].wa1, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=4, column=0, pady=30, padx=65)
    lbl4 = tk.Message(modifyhumf, text=humq[c].wa2, background="#2F323B", foreground="#39FF14",
                      font=("Consolas", 10)).grid(row=5, column=0, pady=30, padx=65)
    lbq = tk.Label(modifyhumf, text="<--- Ερώτηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=2, column=1, pady=30, padx=50)
    lbr = tk.Label(modifyhumf, text="<--- Σωστή απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=3, column=1, pady=30, padx=50)
    lbw = tk.Label(modifyhumf, text="<--- Πρώτη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                   font=("Consolas", 10)).grid(row=4, column=1, pady=30, padx=50)
    lbw2 = tk.Label(modifyhumf, text="<--- Δεύτερη λάθος απάντηση --->", background="#2F323B", foreground="#39FF14",
                    font=("Consolas", 10)).grid(row=5, column=1, pady=30, padx=50)
    modifyqe = ttk.Entry(modifyhumf, textvariable=modifyquestion).grid(row=2, column=2, pady=30, padx=50)#γραμμές 2337-2344, ανάθεση σε μεταβλητές απο τα entry box
    modifyre = ttk.Entry(modifyhumf, textvariable=modifyright).grid(row=3, column=2, pady=30, padx=50)
    modifyw1e = ttk.Entry(modifyhumf, textvariable=modifyw1).grid(row=4, column=2, pady=30, padx=50)
    modifyw2e = ttk.Entry(modifyhumf, textvariable=modifyw2).grid(row=5, column=2, pady=30, padx=50)
    btn = tk.Button(modifyhumf, text="Αλλαγή", command=append, background="#BFEBDC", relief="solid",
                    font=("Consolas", 10)).grid(row=6, column=0, pady=30, padx=50)
    btn2 = tk.Button(modifyhumf, text="Άλλαξε άλλη κάρτα", command=modifyhum, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).grid(row=6, column=2, pady=30, padx=50)


def modify():   #συνάρτηση επιλογής μαθήματος του οποίου επιθυμούμε να τροποποιήσουμε κάρτες, με command=... μεταφερόμαστε στο αντίστοιχο μάθημα
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)
    hide()
    modifyf.pack(fill="both", expand=1)
    lbl = tk.Label(modifyf, text="Διάλεξε για ποίο μάθημα θέλεις να τροποποιήσεις κάρτες", background="#2F323B",
                   foreground="#39FF14", font=("Consolas", 10)).pack(pady=10)
    btn1 = tk.Button(modifyf, text="Δομές δεδομένων", command=modifyds, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).pack(pady=10)
    btn2 = tk.Button(modifyf, text="Μαθηματικός λογισμός", command=modifymath, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).pack(pady=10)
    btn3 = tk.Button(modifyf, text="Πιθανότητες", command=modifyprob, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).pack(pady=10)
    btn4 = tk.Button(modifyf, text="Διακριτά μαθηματικά", command=modifydm, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).pack(pady=10)
    btn5 = tk.Button(modifyf, text="Γραμμική άλγεβρα", command=modifylin, background="#BFEBDC", relief="solid",
                     font=("Consolas", 10)).pack(pady=10)
    btn6 = tk.Button(modifyf, text="Εισαγωγή στην επιστήμη των υπολογιστών", command=modifycs, background="#BFEBDC",
                     relief="solid", font=("Consolas", 10)).pack(pady=10)
    btn7 = tk.Button(modifyf, text="Εισαγωγή στον προγραμματισμό", command=modifypr, background="#BFEBDC",
                     relief="solid", font=("Consolas", 10)).pack(pady=10)
    btn8 = tk.Button(modifyf, text="Προγραμματισμός υπολογιστών", command=modifypr2, background="#BFEBDC",
                     relief="solid", font=("Consolas", 10)).pack(pady=10)
    btn9 = tk.Button(modifyf, text="Εφαρμοσμένος προγραμματισμός με Python", command=modifypy, background="#BFEBDC",
                     relief="solid", font=("Consolas", 10)).pack(pady=10)
    btn10 = tk.Button(modifyf, text="Πληροφορική στις ανθρωπιστικές επιστήμες", command=modifyhum, background="#BFEBDC",
                      relief="solid", font=("Consolas", 10)).pack(pady=10)


def hide(): #συνάρτηση καταστροφής παραθύρων, όταν μετακινούμαστε μεταξύ παραθύρων για αποφυγή εμφάνισης ενός παραθύρου πάνω στο άλλο
    for widget in domesf.winfo_children():
        widget.destroy()
    for widget in mathf.winfo_children():
        widget.destroy()
    for widget in linf.winfo_children():
        widget.destroy()
    for widget in csf.winfo_children():
        widget.destroy()
    for widget in prf.winfo_children():
        widget.destroy()
    for widget in pr2f.winfo_children():
        widget.destroy()
    for widget in pyf.winfo_children():
        widget.destroy()
    for widget in dmf.winfo_children():
        widget.destroy()
    for widget in pbf.winfo_children():
        widget.destroy()
    for widget in humf.winfo_children():
        widget.destroy()
    for widget in mainf.winfo_children():
        widget.destroy()
    for widget in sxf.winfo_children():
        widget.destroy()
    for widget in arxikhf.winfo_children():
        widget.destroy()
    for widget in createf.winfo_children():
        widget.destroy()
    for widget in showf.winfo_children():
        widget.destroy()
    for widget in create2f.winfo_children():
        widget.destroy()
    for widget in deletef.winfo_children():
        widget.destroy()
    for widget in finaldelf.winfo_children():
        widget.destroy()
    for widget in show2f.winfo_children():
        widget.destroy()
    for widget in playf.winfo_children():
        widget.destroy()
    for widget in exatomikeushf.winfo_children():
        widget.destroy()
    for widget in pointsf.winfo_children():
        widget.destroy()
    for widget in createsubjf.winfo_children():
        widget.destroy()
    for widget in ccsf.winfo_children():
        widget.destroy()
    for widget in cdsf.winfo_children():
        widget.destroy()
    for widget in cdmf.winfo_children():
        widget.destroy()
    for widget in cpyf.winfo_children():
        widget.destroy()
    for widget in cpr2f.winfo_children():
        widget.destroy()
    for widget in chumf.winfo_children():
        widget.destroy()
    for widget in clinf.winfo_children():
        widget.destroy()
    for widget in cmathf.winfo_children():
        widget.destroy()
    for widget in cprf.winfo_children():
        widget.destroy()
    for widget in cpbf.winfo_children():
        widget.destroy()
    for widget in modifydsf.winfo_children():
        widget.destroy()
    for widget in modifymathf.winfo_children():
        widget.destroy()
    for widget in modifydmf.winfo_children():
        widget.destroy()
    for widget in modifycsf.winfo_children():
        widget.destroy()
    for widget in modifylinf.winfo_children():
        widget.destroy()
    for widget in modifyhumf.winfo_children():
        widget.destroy()
    for widget in modifyprf.winfo_children():
        widget.destroy()
    for widget in modifypr2f.winfo_children():
        widget.destroy()
    for widget in modifypyf.winfo_children():
        widget.destroy()
    for widget in modifyprbf.winfo_children():
        widget.destroy()
    for widget in modifyf.winfo_children():
        widget.destroy()
    domesf.grid_forget()
    mathf.grid_forget()
    linf.grid_forget()
    csf.grid_forget()
    prf.grid_forget()
    pr2f.grid_forget()
    pyf.grid_forget()
    dmf.grid_forget()
    pbf.grid_forget()
    humf.grid_forget()
    mainf.grid_forget()
    sxf.grid_forget()
    arxikhf.pack_forget()
    createf.pack_forget()
    showf.grid_forget()
    create2f.pack_forget()
    deletef.grid_forget()
    finaldelf.grid_forget()
    show2f.pack_forget()
    playf.grid_forget()
    exatomikeushf.pack_forget()
    pointsf.grid_forget()
    createsubjf.pack_forget()
    ccsf.pack_forget()
    cmathf.pack_forget()
    cdmf.pack_forget()
    cpbf.pack_forget()
    cdsf.pack_forget()
    chumf.pack_forget()
    clinf.pack_forget()
    cprf.pack_forget()
    cpr2f.pack_forget()
    cpyf.pack_forget()
    modifydsf.grid_forget()
    modifymathf.grid_forget()
    modifycsf.grid_forget()
    modifydmf.grid_forget()
    modifypyf.grid_forget()
    modifyprbf.grid_forget()
    modifyprf.grid_forget()
    modifypr2f.grid_forget()
    modifylinf.grid_forget()
    modifyhumf.grid_forget()
    modifyf.pack_forget()


# όλες οι εικόνες οι οποίες χρησιμοποιήθηκαν, για απόδοση αισθητικής σε φόντα και κουμπιά, γραμμές 2512-2537

img = tk.PhotoImage(file="data (3).ppm")    #δομών δεδομένων
img2 = tk.PhotoImage(file="calc.ppm")   #μαθηματικού λογισμού
img3 = tk.PhotoImage(file="linear (1) (1).ppm") #γραμμικής άλγεβρας
img4 = tk.PhotoImage(file="cs.ppm") #επιστήμης υπολογιστών
img5 = tk.PhotoImage(file="dis.ppm")    #διακριτών μαθηματικών
img6 = tk.PhotoImage(file="intro.ppm")  #εισαγωγή στον προγραμματισμό
img7 = tk.PhotoImage(file="c.ppm")  #προγραμματισμού υπολογιστών
img8 = tk.PhotoImage(file="kmf (1).ppm")    #πληροφορικής στις ανθρωπιστικές επιστήμες
img9 = tk.PhotoImage(file="pyt.ppm")    #εφαρμοσμένου προγραμματισμού με python
img10 = tk.PhotoImage(file="pro.ppm")   #πιθανοτήτων
img12 = tk.PhotoImage(file="next2r.png")    #γραμμές 2539-2554, εικόνες για διάφορα κουμπιά
img13 = tk.PhotoImage(file="next2r.png")
img14 = tk.PhotoImage(file="next2r.png")
img15 = tk.PhotoImage(file="next2r.png")
img16 = tk.PhotoImage(file="next2r.png")
img17 = tk.PhotoImage(file="next2r.png")
img18 = tk.PhotoImage(file="next2r.png")
img19 = tk.PhotoImage(file="next2r.png")
img20 = tk.PhotoImage(file="next2r.png")
img21 = tk.PhotoImage(file="next2r.png")
img22 = tk.PhotoImage(file="next2r.png")
img23 = tk.PhotoImage(file="next2r.png")
img24 = tk.PhotoImage(file="card3.png")
img25 = tk.PhotoImage(file="left2.png")
img27 = tk.PhotoImage(file="btns5.png")
img29 = tk.PhotoImage(file="btc.png")

# Παράθυρα για κάθε λειτουργία και πτυχή(μαθήματα, τροποποιήσεις, δημιουργία-πρόσθεση καρτών,πόντοι κλπ), γραμμές 2540-2583
domesf = tk.Canvas(root, width=700, height=600)
mathf = tk.Canvas(root, width=700, height=600)
linf = tk.Canvas(root, width=700, height=600)
csf = tk.Canvas(root, width=700, height=600)
prf = tk.Canvas(root, width=700, height=600)
pr2f = tk.Canvas(root, width=700, height=600)
pyf = tk.Canvas(root, width=700, height=600)
dmf = tk.Canvas(root, width=700, height=600)
pbf = tk.Canvas(root, width=700, height=600)
humf = tk.Canvas(root, width=700, height=600)
mainf = tk.Canvas(root, width=700, height=600)
sxf = tk.Canvas(root, width=700, height=600)
arxikhf = tk.Canvas(root, width=700, height=600, background="#2F323B")
createf = tk.Canvas(root, width=700, height=600, background="#2F323B")
showf = tk.Canvas(root, width=700, height=600, background="#2F323B")
create2f = tk.Canvas(root, width=700, height=600)
show2f = tk.Canvas(root, width=700, height=600)
playf = tk.Canvas(root, width=700, height=600, background="#2F323B")
exatomikeushf = tk.Canvas(root, width=700, height=600, background="#2F323B")
pointsf = tk.Canvas(root, width=700, height=600, background="#2F323B")
createsubjf = tk.Canvas(root, width=700, height=600, background="#2F323B")
cdsf = tk.Canvas(root, width=700, height=600, background="#2F323B")
cmathf = tk.Canvas(root, width=700, height=600, background="#2F323B")
clinf = tk.Canvas(root, width=700, height=600, background="#2F323B")
cpbf = tk.Canvas(root, width=700, height=600, background="#2F323B")
cdmf = tk.Canvas(root, width=700, height=600, background="#2F323B")
cpyf = tk.Canvas(root, width=700, height=600, background="#2F323B")
cprf = tk.Canvas(root, width=700, height=600, background="#2F323B")
cpr2f = tk.Canvas(root, width=700, height=600, background="#2F323B")
chumf = tk.Canvas(root, width=700, height=600, background="#2F323B")
ccsf = tk.Canvas(root, width=700, height=600, background="#2F323B")
modifydsf = tk.Canvas(root, width=700, height=600, background="#2F323B")
modifymathf = tk.Canvas(root, width=700, height=600, background="#2F323B")
modifydmf = tk.Canvas(root, width=700, height=600, background="#2F323B")
modifyhumf = tk.Canvas(root, width=700, height=600, background="#2F323B")
modifycsf = tk.Canvas(root, width=700, height=600, background="#2F323B")
modifyprbf = tk.Canvas(root, width=700, height=600, background="#2F323B")
modifyprf = tk.Canvas(root, width=700, height=600, background="#2F323B")
modifypr2f = tk.Canvas(root, width=700, height=600, background="#2F323B")
modifypyf = tk.Canvas(root, width=700, height=600, background="#2F323B")
modifylinf = tk.Canvas(root, width=700, height=600, background="#2F323B")
modifyf = tk.Canvas(root, width=700, height=600, background="#2F323B")
deletef = tk.Canvas(root, width=700, height=600, background="#2F323B")
finaldelf = tk.Canvas(root, width=700, height=600, background="#2F323B")



def exatomikeush():     #εξατομίκευση: Βάση της συλλογής πόντων απο τον χρήστη, δύναται να αλλάξουν τα χρώματα της εφαρμογής

                        #σημείωση: Μπορεί να φαίνεται πως υπάρχει άσκοπος παναλαμβανόμενος κώδικας, όμως η διαδικασία αλλαγής σε κάθε σενάριο πρεπει να γίνει απο την αρχή
    winsound.PlaySound("bamboobutton.wav", winsound.SND_FILENAME)                    #και οσο πληθαίνουν οι επιλογές, πρέπει να συμπεριλαμβάνονται όλες οι προηγούμενες συν τις νέες
    hide()
    exatomikeushf.pack(fill="both", expand=1)

    def changewhite():
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        #αλλαγή φόντου σε άσπρο
        createf.config(background="white")
        showf.config(background="white")
        exatomikeushf.config(background="white")
        playf.config(background="white")
        pointsf.config(background="white")
        createsubjf.config(background="white")
        cdsf.config(background="white")
        cmathf.config(background="white")
        clinf.config(background="white")
        cpbf.config(background="white")
        cdmf.config(background="white")
        cpyf.config(background="white")
        cprf.config(background="white")
        cpr2f.config(background="white")
        chumf.config(background="white")
        ccsf.config(background="white")
        modifydsf.config(background="white")
        modifymathf.config(background="white")
        modifydmf.config(background="white")
        modifyhumf.config(background="white")
        modifycsf.config(background="white")
        modifyprbf.config(background="white")
        modifyprf.config(background="white")
        modifypr2f.config(background="white")
        modifypyf.config(background="white")
        modifylinf.config(background="white")
        modifyf.config(background="white")
        for widget in createf.winfo_children():     #γραμμές 2624-4155: Καθώς αλλάζει χρώμα ένα παράθυρο, πρέπει να αλλάξουν χρώμα και ολα τα widget (κουμπιά, πλαίσια μηνυμάτων)
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in arxikhf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in showf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in create2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in deletef.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in finaldelf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in show2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in playf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in exatomikeushf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in pointsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in createsubjf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in ccsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in cdsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in cdmf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in cpyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in cpr2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in chumf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in clinf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in cmathf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in cprf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in cpbf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in modifydsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in modifymathf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in modifydmf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in modifycsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in modifylinf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in modifyhumf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in modifyprf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in modifypr2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in modifypyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in modifyprbf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
        for widget in modifyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="white", foreground="black", font=("Consolas", 10))

    def changeblack():
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        #αλλαγή χρώματος σε μαύρο
        createf.config(background="black")
        showf.config(background="black")
        exatomikeushf.config(background="black")
        playf.config(background="black")
        pointsf.config(background="black")
        createsubjf.config(background="black")
        cdsf.config(background="black")
        cmathf.config(background="black")
        clinf.config(background="black")
        cpbf.config(background="black")
        cdmf.config(background="black")
        cpyf.config(background="black")
        cprf.config(background="black")
        cpr2f.config(background="black")
        chumf.config(background="black")
        ccsf.config(background="black")
        modifydsf.config(background="black")
        modifymathf.config(background="black")
        modifydmf.config(background="black")
        modifyhumf.config(background="black")
        modifycsf.config(background="black")
        modifyprbf.config(background="black")
        modifyprf.config(background="black")
        modifypr2f.config(background="black")
        modifypyf.config(background="black")
        modifylinf.config(background="black")
        modifyf.config(background="black")
        for widget in createf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in arxikhf.winfo_children():
            if isinstance(widget, tk.Label):
                        widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                        widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                        widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in showf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in create2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in deletef.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in finaldelf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in show2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in playf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in exatomikeushf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in pointsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in createsubjf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in ccsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in cdsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in cdmf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in cpyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in cpr2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in chumf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in clinf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in cmathf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in cprf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in cpbf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in modifydsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in modifymathf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in modifydmf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in modifycsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in modifylinf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in modifyhumf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in modifyprf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in modifypr2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in modifypyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in modifyprbf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in modifyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))

    def changeblue():       #αλλαγή χρώματος σε μπλέ
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        createf.config(background="blue")
        showf.config(background="blue")
        exatomikeushf.config(background="blue")
        playf.config(background="blue")
        pointsf.config(background="blue")
        createsubjf.config(background="blue")
        cdsf.config(background="blue")
        cmathf.config(background="blue")
        clinf.config(background="blue")
        cpbf.config(background="blue")
        cdmf.config(background="blue")
        cpyf.config(background="blue")
        cprf.config(background="blue")
        cpr2f.config(background="blue")
        chumf.config(background="blue")
        ccsf.config(background="blue")
        modifydsf.config(background="blue")
        modifymathf.config(background="blue")
        modifydmf.config(background="blue")
        modifyhumf.config(background="blue")
        modifycsf.config(background="blue")
        modifyprbf.config(background="blue")
        modifyprf.config(background="blue")
        modifypr2f.config(background="blue")
        modifypyf.config(background="blue")
        modifylinf.config(background="blue")
        modifyf.config(background="blue")
        for widget in createf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in arxikhf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in showf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="black", foreground="white", font=("Consolas", 10))
        for widget in create2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in deletef.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in finaldelf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in show2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in playf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in exatomikeushf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in pointsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in createsubjf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in ccsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in cdsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in cdmf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in cpyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in cpr2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in chumf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in clinf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in cmathf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in cprf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in cpbf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in modifydsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in modifymathf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in modifydmf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in modifycsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in modifylinf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in modifyhumf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in modifyprf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in modifypr2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in modifypyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in modifyprbf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
        for widget in modifyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="blue", foreground="white", font=("Consolas", 10))

    def changeorange():     #αλλαγή χρώματος σε πορτοκαλί
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        createf.config(background="orange")
        showf.config(background="orange")
        exatomikeushf.config(background="orange")
        playf.config(background="orange")
        pointsf.config(background="orange")
        createsubjf.config(background="orange")
        cdsf.config(background="orange")
        cmathf.config(background="orange")
        clinf.config(background="orange")
        cpbf.config(background="orange")
        cdmf.config(background="orange")
        cpyf.config(background="orange")
        cprf.config(background="orange")
        cpr2f.config(background="orange")
        chumf.config(background="orange")
        ccsf.config(background="orange")
        modifydsf.config(background="orange")
        modifymathf.config(background="orange")
        modifydmf.config(background="orange")
        modifyhumf.config(background="orange")
        modifycsf.config(background="orange")
        modifyprbf.config(background="orange")
        modifyprf.config(background="orange")
        modifypr2f.config(background="orange")
        modifypyf.config(background="orange")
        modifylinf.config(background="orange")
        modifyf.config(background="orange")
        for widget in createf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in arxikhf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in showf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in create2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in deletef.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in finaldelf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in show2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in playf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in exatomikeushf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in pointsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in createsubjf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in ccsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in cdsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in cdmf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in cpyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in cpr2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in chumf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in clinf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in cmathf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in cprf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in cpbf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in modifydsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in modifymathf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in modifydmf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in modifycsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in modifylinf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in modifyhumf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in modifyprf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in modifypr2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in modifypyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in modifyprbf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
        for widget in modifyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="blue", foreground="orange", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="orange", foreground="blue", font=("Consolas", 10))

    def changered():        #αλλαγή χρώματος σε κόκκινο
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        createf.config(background="red")
        showf.config(background="red")
        exatomikeushf.config(background="red")
        playf.config(background="red")
        pointsf.config(background="red")
        createsubjf.config(background="red")
        cdsf.config(background="red")
        cmathf.config(background="red")
        clinf.config(background="red")
        cpbf.config(background="red")
        cdmf.config(background="red")
        cpyf.config(background="red")
        cprf.config(background="red")
        cpr2f.config(background="red")
        chumf.config(background="red")
        ccsf.config(background="red")
        modifydsf.config(background="red")
        modifymathf.config(background="red")
        modifydmf.config(background="red")
        modifyhumf.config(background="red")
        modifycsf.config(background="red")
        modifyprbf.config(background="red")
        modifyprf.config(background="red")
        modifypr2f.config(background="red")
        modifypyf.config(background="red")
        modifylinf.config(background="red")
        modifyf.config(background="red")
        for widget in createf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in arxikhf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in showf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in create2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in deletef.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in finaldelf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in show2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in playf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in exatomikeushf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in pointsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in createsubjf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in ccsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in cdsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in cdmf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in cpyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in cpr2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in chumf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in clinf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in cmathf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in cprf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in cpbf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in modifydsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in modifymathf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in modifydmf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in modifycsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in modifylinf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in modifyhumf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in modifyprf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in modifypr2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in modifypyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in modifyprbf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
        for widget in modifyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="red", foreground="black", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="black", foreground="red", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="red", foreground="black", font=("Consolas", 10))

    def changepink():       #αλλαγή χρώματος σε ρόζ
        winsound.PlaySound("woodenbutton.wav", winsound.SND_FILENAME)
        createf.config(background="pink")
        showf.config(background="pink")
        exatomikeushf.config(background="pink")
        playf.config(background="pink")
        pointsf.config(background="pink")
        createsubjf.config(background="pink")
        cdsf.config(background="pink")
        cmathf.config(background="pink")
        clinf.config(background="pink")
        cpbf.config(background="pink")
        cdmf.config(background="pink")
        cpyf.config(background="pink")
        cprf.config(background="pink")
        cpr2f.config(background="pink")
        chumf.config(background="pink")
        ccsf.config(background="pink")
        modifydsf.config(background="pink")
        modifymathf.config(background="pink")
        modifydmf.config(background="pink")
        modifyhumf.config(background="pink")
        modifycsf.config(background="pink")
        modifyprbf.config(background="pink")
        modifyprf.config(background="pink")
        modifypr2f.config(background="pink")
        modifypyf.config(background="pink")
        modifylinf.config(background="pink")
        modifyf.config(background="pink")
        for widget in createf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in arxikhf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in showf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in create2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in deletef.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in finaldelf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in show2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in playf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in exatomikeushf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in pointsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in createsubjf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in ccsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in cdsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in cdmf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in cpyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in cpr2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in chumf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in clinf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in cmathf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in cprf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in cpbf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in modifydsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in modifymathf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in modifydmf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in modifycsf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in modifylinf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in modifyhumf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in modifyprf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in modifypr2f.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in modifypyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in modifyprbf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
        for widget in modifyf.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))
            if isinstance(widget, tk.Button):
                widget.config(background="white", foreground="pink", font=("Consolas", 10))
            if isinstance(widget, tk.Message):
                widget.config(background="pink", foreground="white", font=("Consolas", 10))

    global totalpoints      #γραμμές 4120-4155: αναλόγως τους πόντους που έχει μαζέψει ο χρήστης, μπορεί να έχει στη διάθεση του ορισμένες αλλαγές χρωμάτων
    if (totalpoints < 6):
        lbl = tk.Label(exatomikeushf, text="Οι πόντοι σου δεν επαρκούν για κάποια αλλαγή", font=("Consolas", 10),
                       background="#2F323B", foreground="#39FF14").pack(pady=10)
    elif (totalpoints >= 6 and totalpoints < 24):
        lbl1 = tk.Label(exatomikeushf, text="Μπορείς να κάνεις αυτές τις αλλαγές:", font=("Consolas", 10),
                        background="#2F323B", foreground="#39FF14").pack(pady=10)

        btn = tk.Button(exatomikeushf, text="Άσπρο φόντο", font=("Consolas", 10), background="white",
                        foreground="black", command=changewhite).pack(pady=10)      #μέχρι 6 πόντους, γίνεται αλλαγή σε άσπρο
    elif (totalpoints >= 24 and totalpoints <= 75):
        lbl1 = tk.Label(exatomikeushf, text="Μπορείς να κάνεις αυτές τις αλλαγές:", font=("Consolas", 10),
                        background="#2F323B", foreground="#39FF14").pack(pady=10)

        btn = tk.Button(exatomikeushf, text="Μαύρο φόντο", font=("Consolas", 10), background="black",
                        foreground="white", command=changeblack).pack(pady=10)
        btn2 = tk.Button(exatomikeushf, text="Άσπρο φόντο", font=("Consolas", 10), background="white",
                         foreground="black", command=changewhite).pack(pady=10)
        btn = tk.Button(exatomikeushf, text="Μπλέ φόντο", font=("Consolas", 10), background="blue", foreground="white",
                        command=changeblue).pack(pady=10)       #μέχρι 24 πόντους, προσφέρονται το μάυρο, άσπρο και μπλέ
    elif (totalpoints > 75):
        lbl1 = tk.Label(exatomikeushf, text="Μπορείς να κάνεις αυτές τις αλλαγές:", font=("Consolas", 10),
                        background="#2F323B", foreground="#39FF14").pack(pady=10)

        btn = tk.Button(exatomikeushf, text="Μαύρο φόντο", font=("Consolas", 10), background="black",
                        foreground="white", command=changeblack).pack(pady=10)
        btn2 = tk.Button(exatomikeushf, text="Άσπρο φόντο", font=("Consolas", 10), background="white",
                         foreground="black", command=changewhite).pack(pady=10)
        btn3 = tk.Button(exatomikeushf, text="Μπλέ φόντο", font=("Consolas", 10), background="blue", foreground="white",
                         command=changeblue).pack(pady=10)
        btn4 = tk.Button(exatomikeushf, text="Πορτοκαλί φόντο", font=("Consolas", 10), background="orange",
                         foreground="blue", command=changeorange).pack(pady=10)
        btn5 = tk.Button(exatomikeushf, text="Κόκκινο φόντο", font=("Consolas", 10), background="red",
                         foreground="black", command=changered).pack(pady=10)
        btn6 = tk.Button(exatomikeushf, text="Ρόζ φόντο", font=("Consolas", 10), background="pink", foreground="white",
                         command=changepink).pack(pady=10)      #πάνω απο 24 πόντους προσφέρονταιι πλέον όλες οι επιλογές (μαυρο, άσπρο, μπλέ, ροζ, πορτοκαλί, κόκκινο)


menu = tk.Menu(root)
root.config(menu=menu)

mainfr = tk.Menu(menu)      #γραμμές 4161-4196: όλες οι επιλογές των drop-down μενού
menu.add_cascade(label="Αρχική", menu=mainfr)
mainfr.add_command(label="Ξεκινώντας", command=arxikh)


subjects = tk.Menu(menu)        #γραμμές 4166-4177: μενού μαθημάτων
menu.add_cascade(label="Μαθήματα", menu=subjects)
subjects.add_command(label="Δομές Δεδομένων", command=domes)
subjects.add_command(label="Μαθηματικός Λογισμός", command=math)
subjects.add_command(label="Γραμμική Άλγεβρα", command=lin)
subjects.add_command(label="Εισαγωγή στην επιστήμη των υπολογιστών", command=cs)
subjects.add_command(label="Εισαγωγή στον προγραμματισμό", command=pr)
subjects.add_command(label="Προγραμματισμός υπολογιστών", command=pr2)
subjects.add_command(label="Εφαρμοσμένος προγραμματιμός με Python", command=py)
subjects.add_command(label="Διακριτά μαθηματικά", command=dm)
subjects.add_command(label="Πιθανότητες", command=pb)
subjects.add_command(label="Πληροφορική στις ανθρωπιστικές επιστήμες", command=hum)

#μενού του editor, γραμμές 4179-4184
editor = tk.Menu(menu)
menu.add_cascade(label="Editor", menu=editor)
editor.add_command(label="Φτιάξε την δική σου κάρτα", command=create)
editor.add_command(label="Τροποποίησε μια υπάρχουσα κάρτα", command=modify)
editor.add_command(label="Πρόσθεσε κάρτες σε κάποιο μάθημα", command=createsubj)

# μενού ρυθμίσεων και εξατομίκευσης, γραμμές 4187-4189
settings = tk.Menu(menu)
menu.add_cascade(label="Ρυθμίσεις", menu=settings)
settings.add_command(label="Εξατομίκευση", command=exatomikeush)


# μενού για εμφάνιση καρτών, γραμμές 4192-4196
cards = tk.Menu(menu)
menu.add_cascade(label="Κάρτες", menu=cards)
cards.add_command(label="Παίξε με τις δικές σου κάρτες", command=play)
cards.add_command(label="Δες τους πόντους σου", command=points)


domesf.create_image(0, 0, image=img, anchor="nw")   #γραμμές 4199-4208: Τα φόντα των μαθημάτων
mathf.create_image(1, 1, image=img2, anchor="center")
linf.create_image(0, 0, image=img3, anchor="nw")
csf.create_image(0, 0, image=img4, anchor="nw")
prf.create_image(0, 0, image=img6, anchor="nw")
pr2f.create_image(0, 0, image=img7, anchor="nw")
dmf.create_image(0, 0, image=img5, anchor="nw")
pyf.create_image(0, 0, image=img9, anchor="nw")
pbf.create_image(0, 0, image=img10, anchor="nw")
humf.create_image(0, 0, image=img8, anchor="nw")

root.mainloop() #mainloop: ουσιαστικά, κρατάει ανοιχτή την εφαρμογή μέσω απείρων επανεκτελέσεων της. Εαν δεν υπήρχε, θα άνοιγε και θα έκλεινε αμέσως

