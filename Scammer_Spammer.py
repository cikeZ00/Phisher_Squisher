#Import Libraries
import names, requests, random, string, os, urllib3, json

# Config generation and loading
default_config = {
    "Scammer_Spammer": {
        "URL": "URL Goes here",
        "Email_Param": "login_email",
        "Password_Param": "login_password"
    }
}
if not os.path.exists("config.json"):
    with open('config.json', 'w') as configout:
        json.dump(default_config, configout, indent=4)
    print("config.json generated!")
    quit()
else:
    with open("config.json") as f:
        config = json.load(f)

#Add proxies here. Need both HTTP and HTTPS.
proxies = {
    'http': 'http://49.51.68.122:1080',
    'https': 'http://49.51.68.122:1080',
}

#Create the session and set the proxies.
s = requests.Session()
#Uncomment below if you need to use proxies.
#s.proxies = proxies

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

# Email provder list
e_provder = ['@yahoo.com', '@gmail.com', '@gmx.com', '@icloud.com', '@mail.com', '@gmx.us', '@outlook.com', '@aol.com', '@comcast.net']

# Load params from config file
url = config["Scammer_Spammer"]["URL"]
email_param = config["Scammer_Spammer"]["Email_Param"]
pass_param = config["Scammer_Spammer"]["Password_Param"]

# Function for clearing console output
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

print('Started')

while True:
    #Generate random first/last name
    first = names.get_first_name().lower()
    last = names.get_last_name().lower()

    #Generate 3 random numbers
    rando = ''.join(random.choice(string.digits))
    rando2 = ''.join(random.choice(string.digits))
    rando3 = ''.join(random.choice(string.digits))

    #Chooses email format
    emailformat = random.choice([1,2,3,4,5,6,7,8,9,10,11])
    if emailformat == 1:        
        name = first + last + rando + rando2 + rando3
    if emailformat == 2:
        name = first + '_' + last + rando + rando2 + rando3
    if emailformat == 3:
        name = first + '-' + last + rando + rando2
    if emailformat == 4:
        name = last + first + rando + rando2 + rando3
    if emailformat == 5:
        name = first + rando + rando2 + last
    if emailformat == 6:
        name = last + rando + rando2 + rando3 + first
    if emailformat == 7:
        name = last + '-' + first + '-' + rando + rando2 + rando3 
    if emailformat == 8:
        name = first + last
    if emailformat == 9:
        name = last + first
    if emailformat == 10:
        name = first + rando + rando2 + rando3
    if emailformat == 11:
        name = first + '_' + last


    #Chooses email provider
    username = name.lower() + random.choice(e_provder)

    #Chooses randomly generated password between 8-16 characters long
    password = ''.join(random.choice(chars) for i in range(random.choice([8,8,8,9,10,11,12,13,14,15,16,17,18,19,20])))


    #Disables HTTPS warning
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    #Make post request
    #Replace parameters as needed.
    response= s.post(url, allow_redirects=False, verify=False, data={
		email_param: username,
		pass_param: password,
	})

    #prints output
    clearConsole()
    print()
    print("Sending username: " + username + " and Password: " + password )
    print("To: " + url)
    print(f'Status: {response.status_code}')