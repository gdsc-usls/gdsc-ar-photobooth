## Getting Started

### Overview
This Python script automates file tracking and uploading to Google Drive using the `Watchdog` library for file system events, `PyDrive` for interacting with Google Drive, and OAuth 2.0 for authentication. The script monitors a specified directory for file changes (creation only) and automatically uploads new files to a Google Drive folder when the script is running.

### Prerequisites
- Python 3.x installed on your system
- A Google account with access to Google Drive
- OAuth 2.0 credentials (client ID and client secret) for Google Drive API
- Required Python packages and modules: `Watchdog`, `PyDrive`, `dotenv`
- A stable Internet/Mobile Data connection

### Disclaimer
Always see to it that the script is **constantly running** so that file uploads are consistent.
Pressing **CTRL + C** will terminate the script - a `TERMINATE_NOTIF` will be logged into the console.

#### How to run the script
1. Open Command Prompt. (Win + R -> type cmd -> Enter)
2. Navigate to the directory of the script. (type "cd path\to\script\here")
3. Once in the directory, run the following command:
```bash
python main.py
```
4. A `WATCHER_TRIGGER_NOTIF` will be logged into the console if it has successfully started the script.
5. **Troubleshooting**: If any error/s occur, check the following:
* Python is installed: Run `python --version` to verify.
* Environment variables are correctly set: Ensure the `.env` file is in place with valid credentials.
* Images Folder is in the directory: Check if there is a `Screenshots` Folder.
* Creds folder is in the directory: Verify that creds folder contain the ff files: 
    * client_secrets_XXXX.json (OAuth 2.0 Client Secret for Google API)
    * credentials.json (OAuth 2.0 Tokens - Generated after first authentication)
    * settings.yml (Application-specific settings - folder paths, Google Drive ID)
* Internet Connection: Verify that the device is connected to the internet. 

### Libraries and API Setups
1. `Watchdog` - monitors the specified directory for changes and triggers events (file created, modified, deleted). [Watchdog Documentation](https://pypi.org/project/watchdog/)
2. [Google Drive Authentication Setup](https://d35mpxyw7m7k7g.cloudfront.net/bigdata_1/Get+Authentication+for+Google+Service+API+.pdf)  
3. When a file is created or modified, the script uses `PyDrive` to authenticate via OAuth 2.0 and upload the file to Google Drive. [PyDrive Setup](https://www.projectpro.io/recipes/upload-files-to-google-drive-using-python)

### Flowchart
Below is a flowchart of the file tracking and uploading process:
![SCRIPT FLOWCHART](https://drive.google.com/uc?export=view&id=1HOV52x1Koib68olhBU0zZl9oAJXi45Kp)

### Contact
If you have encountered any bugs/error, kindly notify the following officers ASAP via any GDSC - Related Group Chats.
1. John Octavio - Web Development Lead
2. Jared Ramon Elizan - Tech Officer (Web Development)
3. Toby Javelona - Tech Officer (AI)