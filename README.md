**Welcome to YouTube Shorts**

To deploy this Program Follow the following steps.

1. Clone this repository.
2. Install the required modules in the requirements.txt
	i.   openai
	ii.  gtts
	iii. openai_whisper
	iv. google-api-python-client
	v.  oauth2client
3. Get the OpenAI API Key.
	i. Goto *"platform.openai.com"*
	ii. Signup for an account.
	iii. After creating account, click on your profile icon(top-right corner) and goto *"View API Keys"*.
	iv. Create a new secret key.(Be sure to copy it, you cannot view it later).
4. Insert the OpenAI API Key into utils/script.py.
	i. Replace *"your-api-key"* in line 3 with your API Key.
5. Obtain the Oauth Key from YouTube Data API.
	i. Goto *"console.cloud.google.com"*
	ii. Click on *"Select a Project"* in the top bar.
	iii. Now create a new project.
	iv. After project is created, goto *"APIs & Services"* in the left pane.
	v. Goto to Library.
	vi. Search for *"Youtube Data API V3"*. Enable that API.
	vii. Goto *"OAuth CONSENT SCREEN"*.
	vii. Click on *"External"* and Create.
	viii. Write *"App Name"*, choose the *"User Support Email"*, type the same email in *"Developer Contact Information"* and click *"save and continue".*
	ix. Click on *"Add or Remove Scopes"*, Search for *"upload"*, click on the item in the popup, tick the checkbox and click on *"update"*.
	x. Click on *"Save and Continue"*.
	xi. Click on *"Add Users"*, enter the email on which you created the channel and click *"Add"*. Click *"Save and Continue"*.
	xii. Click on *"Back to Dashboard"*.
	xiii. Click on *"Credentials"*. Click on "Create Credentials" and choose *"OAuth Client ID"*.
	xiv. Choose the *"Application Type"* to *"Desktop"*, Name the key, click on Create *"Create"*. Download the JSON File.
7. Replace the *"client_secret.json"* with your own file.
8. Now run the *"main.py"*
	i. When you run it for first time it gives you link for authentication from the browser. Copy that link and paste in the browser and give access to it.
