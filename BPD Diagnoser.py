#START


bpd_symptoms = ["Fear of abandonement / Avoidance of abandonement", "Unstable and/or intense relationships", "Uncertainty of self-image or identity", "Impulsive and/or risky behavior",
 "Paranoia and loss of contact with reality", "Self-harm and thoughts/fantasies of suicide", "Emotional reactivity and inastibility(mood swings, irritability, etc)", "feelings of emptiness / no purpose",
"Intense bouts of anger"]

my_symptoms = []

is_ongoing = False

def print_start():
    print("""

 __    __     _                            _          _   _              ___    ___  ___      ___ _                                       
/ / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___    / __\  / _ \/   \    /   (_) __ _  __ _ _ __   ___  ___  ___ _ __ 
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \  /__\// / /_)/ /\ /   / /\ / |/ _` |/ _` | '_ \ / _ \/ __|/ _ \ '__|
 \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/ / \/  \/ ___/ /_//   / /_//| | (_| | (_| | | | | (_) \__ \  __/ |   
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___| \_____/\/  /___,'   /___,' |_|\__,_|\__, |_| |_|\___/|___/\___|_|   
                                                                                                          |___/                           

""")
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("DISCLAIMER:\n")
    print("This program is not meant to properly or medically diagnose any mental illness or personality disorder.")
    print("It is only meant to raise awareness of a serious personality disorder that affects millions of people all over the world.\n")
    print("Please, follow up with proper medical advice if you or a loved one think they might have any kind of medical health disorder!")
    print("-----------------------------------------------------------------------------------------------------------------------------------------")





def print_symptoms():
    for symptom in bpd_symptoms:
        print(f"{bpd_symptoms.index(symptom) + 1}. {symptom}\n")

def print_my_symptoms():
    print("Here is your current list of symptoms:\n")
    for symptom in my_symptoms:
        print(f"{my_symptoms.index(symptom) + 1}. {symptom}\n")
        



print_start()

start = input("Are you ready to start? Y / N\n")

if start == "Y":
    is_ongoing = True
    while (is_ongoing):
        print_symptoms()
        print("-----------------------------------------------------------------------------------------------------------------------------------------\n")
        print_my_symptoms()
        add_symptom = input("Please enter the number of the symptom you think you may have to add it to your symptoms list. Otherwise type 'done' to finish\n")
        try:
            symp = int(add_symptom)
            
        except:
            if add_symptom == 'done':
                break
            else:
                print(f"You have to enter a number between 1 and {len(bpd_symptoms)}")
                continue

        if symp > 0 and symp <= len(bpd_symptoms):
            my_symptoms.append(bpd_symptoms[symp - 1])
            bpd_symptoms.remove(bpd_symptoms[symp - 1])
            continue

        
