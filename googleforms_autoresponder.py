import random
import time
import requests
from bs4 import BeautifulSoup

print("\nYour form URL MUST match this example: https://docs.google.com/forms/d/e/example123/formResponse")
FORM_POST_URL = input("Enter your form URL: ")
print(FORM_POST_URL)
if not isinstance(FORM_POST_URL, str):
    print("Please enter a valid URL.")
    exit(1)

TOTAL_RESPONSES = input("Enter the number of responses to send: ")
if not TOTAL_RESPONSES.isdigit():
    print("Please enter a valid number.")
    exit(1)
TOTAL_RESPONSES = int(TOTAL_RESPONSES)
if TOTAL_RESPONSES < 1:
    print("Please enter a number greater than 0.")
    exit(1)

def get_fbzx_value():
    r = requests.get(FORM_POST_URL)
    soup = BeautifulSoup(r.text, "html.parser")
    fbzx_input = soup.find("input", {"name": "fbzx"})
    if fbzx_input:
        fbzx_value = fbzx_input.get("value")
        return fbzx_value
    else:
        print("fbzx not found. Google probably moved the furniture again.")
        exit(1)

def generate_random_data():
    ranks = [str(r) for r in range(1, 6)]
    random.shuffle(ranks)

    age_groups = ["Under 18", "18-24", "18-24", "18-24", "25-34", "25-34", "Above 35"]
    storage_methods = ["Memorize them", "Write them down", "Use a password manager", "Use a password manager", "Use a password manager"]
    password_counts = ["1-3", "1-3", "1-3", "1-3", "4-6", "4-6", "7-10", "More than 10"]
    change_frequencies = ["Every month", "Every few months", "Once a year", "Once a year", "Never", "Never", "Never", "Never"]
    confidence_scales = ["1", "2", "3", "3", "4", "4", "5"]
    twofa_likelihood = ["1", "2", "3", "4", "5", "5"]
    tips = [
        "Use a mix of numbers and symbols.", "Don't use your birthday.",
        "Use a phrase instead of a word.", "Change them every few months.",
        "Don't share them with friends.", "Use a password manager.",
        "Make it long and complex.", "Avoid common words.",
        "Enable 2FA whenever possible."
    ]

    data = {
        # Required hidden fields for multi-section forms
        "fvv": "1",
        "fbzx": get_fbzx_value(),
        "pageHistory": "0,1",
#        "partialResponse": '[[[null,151614029,["Yes"],0]],null,"' + get_fbzx_value() + '"]',

        # Actual answers
        "entry.151614029": "Yes",
        "entry.1883360831": random.choice(["Yes", "No"]),
        "entry.716471041": random.choice(age_groups),
        "entry.975952784": random.choice(storage_methods),
        "entry.229464489": random.choice(password_counts),
        "entry.1228279095": random.choice(change_frequencies),

        "entry.946432161": ranks.pop(),
        "entry.1862493438": ranks.pop(),
        "entry.1543665017": ranks.pop(),
        "entry.1529904191": ranks.pop(),
        "entry.502443374": ranks.pop(),

        "entry.408681360": random.choice(confidence_scales),
        "entry.1409429975": str(random.randint(1, 5)),
        "entry.1170962348": random.choice(twofa_likelihood),
        "entry.1915345340": random.choice(tips),
    }

    return data


def send_response(data):
    response = requests.post(FORM_POST_URL, data=data)
    return response.status_code == 200


def main():
    successful = 0
    for i in range(1, TOTAL_RESPONSES + 1):
        payload = generate_random_data()
        ok = send_response(payload)

        if ok:
            print(f"[{i}/{TOTAL_RESPONSES}] Submitted.")
            successful += 1
        else:
            print(f"[{i}/{TOTAL_RESPONSES}] FAILED.")

        time.sleep(random.uniform(0.8, 2.0))

    print(f"\nDone. {successful}/{TOTAL_RESPONSES} submissions succeeded.")


if __name__ == "__main__":
    main()
