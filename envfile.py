# To mask sensitive information like email IDs, passwords, and MongoDB connection strings, you can use a .env file to store these values. Here's how you can modify the code to use a .env file:

# 1. Create a .env file in the same directory as your script. Add the following lines to the .env file:

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
FROM_EMAIL=your-email@gmail.com
PASSWORD=your-password
MONGO_CONNECTION_STRING=mongodb://localhost:27017/
RECIPIENTS=recipient1@example.com,recipient2@example.com

# 2. Install the python-dotenv library by running the following command:

pip install python-dotenv

# 3. Modify your script to load the values from the .env file. Add the following code at the beginning of your script:

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get values from .env file
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')
from_email = os.getenv('FROM_EMAIL')
password = os.getenv('PASSWORD')
mongo_connection_string = os.getenv('MONGO_CONNECTION_STRING')
recipients = os.getenv('RECIPIENTS').split(',')

# 4. Update the code to use the environment variables:

# Connect to MongoDB
client = MongoClient(mongo_connection_string)
db = client['mydatabase']
collection = db['mycollection']

# Email configuration
smtp_server = os.getenv('SMTP_SERVER')
smtp_port = os.getenv('SMTP_PORT')
from_email = os.getenv('FROM_EMAIL')
password = os.getenv('PASSWORD')
to_emails = recipients

# Create a message
msg['From'] = from_email
msg['To'] = ', '.join(to_emails)
msg['Subject'] = f'Today\'s data {today}'
msg['Date'] = formatdate(localtime=True)

# Send the email
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(from_email, password)
server.sendmail(from_email, to_emails, msg.as_string())
server.quit()

#print('Email sent successfully!')

# By using a .env file, you can easily update the values without modifying the code. 
# Make sure to add the .env file to your .gitignore file to prevent it from being committed to your repository.

# # 3. Import the dotenv library at the top of your script:

# from dotenv import load_dotenv

# # 4. Load the .env file by calling the load_dotenv() function:

# load_dotenv()

# # 5. Replace the hardcoded values in the code with the values from the .env file:

# smtp_server = os.getenv('SMTP_SERVER')
# smtp_port = int(os.getenv('SMTP_PORT'))
# from_email = os.getenv('FROM_EMAIL')
# password = os.getenv('PASSWORD')
# mongo_connection_string = os.getenv('MONGO_CONNECTION_STRING')
# recipients = os.getenv('RECIPIENTS').split(',')