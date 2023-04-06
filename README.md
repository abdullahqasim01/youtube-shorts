**Welcome to YouTube Shorts**

To deploy this Program Follow the following steps.

1. Clone this repository.
2. Install the required modules in the requirements.txt
	1.   openai
	2.  gtts
	3. openai_whisper
	4. google-api-python-client
	5.  oauth2client
3. Get the OpenAI API Key.
	1. Goto *"platform.openai.com"*
	2. Signup for an account.
	3. After creating account, click on your profile icon(top-right corner) and goto *"View API Keys"*.
	4. Create a new secret key.(Be sure to copy it, you cannot view it later).
4. Insert the OpenAI API Key into utils/script.py.
	1. Replace *"your-api-key"* in line 3 with your API Key.
5. Obtain the Oauth Key from YouTube Data API.
	1. Goto *"console.cloud.google.com"*
	2. Click on *"Select a Project"* in the top bar.
	3. Now create a new project.
	4. After project is created, goto *"APIs & Services"* in the left pane.
	5. Goto to Library.
	6. Search for *"Youtube Data API V3"*. Enable that API.
	7. Goto *"OAuth CONSENT SCREEN"*.
	8. Click on *"External"* and Create.
	9. Write *"App Name"*, choose the *"User Support Email"*, type the same email in *"Developer Contact Information"* and click *"save and continue".*
	10. Click on *"Add or Remove Scopes"*, Search for *"upload"*, click on the item in the popup, tick the checkbox and click on *"update"*.
	11. Click on *"Save and Continue"*.
	12. Click on *"Add Users"*, enter the email on which you created the channel and click *"Add"*. Click *"Save and Continue"*.
	13. Click on *"Back to Dashboard"*.
	14. Click on *"Credentials"*. Click on "Create Credentials" and choose *"OAuth Client ID"*.
	15. Choose the *"Application Type"* to *"Desktop"*, Name the key, click on Create *"Create"*. Download the JSON File.
6. Replace the *"client_secret.json"* with your own file.
7. Now run the *"main.py"*
	i. When you run it for first time it gives you link for authentication from the browser. Copy that link and paste in the browser and give access to it.
