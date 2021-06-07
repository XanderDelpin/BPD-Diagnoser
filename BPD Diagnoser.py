import time


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
    print("Please, follow up with proper medical advice if you or a loved one think they might have any kind of mental health disorder!")
    print("-----------------------------------------------------------------------------------------------------------------------------------------")





def print_symptoms():
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------------------------------\n")
    print("These are the traits you can choose from...\n")
    for symptom in bpd_symptoms:
        print(f"\n{bpd_symptoms.index(symptom) + 1}. {symptom}")
    print("\n")

def print_my_symptoms():
    print("Here is your current list of symptoms:\n")
    for symptom in my_symptoms:
        print(f"{my_symptoms.index(symptom) + 1}. {symptom}\n")
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------------------------------\n")
    print("\n")

def check_for_suicide():
    if "Self-harm and thoughts/fantasies of suicide" in my_symptoms:
        print("It also appears you have suicidal thoughts or a tendency towards self-harm...")
        print("Please remember, you are always worth saving and healing. Don't give up! You are strong enough to overcome all of your intense feelings!")
        print("If you or a loved one are having suicidal thoughts and/or ideation please contact your local help line, I promise it will help.")
        print("Please call 1-800-273-8255 (National Suicide Hotline)\n")
        print("-----------------------------------------------------------------------------------------------------------------------------------------\n")

def print_end_note():
    print("This is the end of the program.\n\nRemember, I am not a trained doctor of any kind; these assumptions are in no way final and you should consult your doctor before building any concrete ideas!\n")
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------------------------------\n")



print_start()

temp = input("Are you ready to start? Y / N\n\n")
start = temp.upper()

if start == "Y":
    is_ongoing = True
    while (is_ongoing):
        print_symptoms()
        print("-----------------------------------------------------------------------------------------------------------------------------------------\n")
        print_my_symptoms()
        add_symptom = input("\nPlease enter the number of the symptom you think you may have to add it to your symptoms list. Otherwise type 'done' to finish\n")
        try:
            symp = int(add_symptom) 
        except:
            if add_symptom == 'done':
                is_ongoing = False
                break
        if symp > 0 and symp <= len(bpd_symptoms):
            my_symptoms.append(bpd_symptoms[symp - 1])
            bpd_symptoms.remove(bpd_symptoms[symp - 1])
            continue
        else:
            if len(bpd_symptoms) == 0:
                print("\n\n")
                print(f"\nIt seems like you have selected all symptoms. Please type 'done'.\n")
                continue
            elif len(bpd_symptoms) == 1:
                print("\n\n")
                print(f"\nIt seems like there's only one symptom left! You can add it to your symptom list or type 'done' once you're finished!\n")
                continue
            else:
                print("\n\n")
                print(f"\nYou have to enter a number between 1 and {len(bpd_symptoms)} or type 'done' when you're finished!\n")
                continue
    print(f"It appears you have {len(my_symptoms)} symptoms\n")
    print("I will now calculate your results using complex algorithms and calculus (just counting hehe)\n\n")

    time.sleep(1)

    print("Calculating...\n\n")

    time.sleep(3)

    if (len(my_symptoms) < 5):
        print("According to your traits, it appears you may have little to no BPD.\n\n")
    elif (len(my_symptoms) >= 5 and len(my_symptoms) < 8):
        print("According to your traits, it appears you may have moderate to severe BPD.\n\n")
    else:
        print("According to your traits, you may have a severe case of BPD. \n\n")

    print("-----------------------------------------------------------------------------------------------------------------------------------------\n")

    time.sleep(1)

    check_for_suicide()

    time.sleep(2)

    print_end_note()

elif start == "N":
    print("\nThat's alright! If you'd like to start when you're ready, please reopen this program!\n\n")

else:
    print("Please type either 'Y' or 'N'. Reopen the program to start again!")



    



        
