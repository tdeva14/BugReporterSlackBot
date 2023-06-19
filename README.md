# Bug Reporter Slack Bot

The Bug Reporter Slack Bot is a Python script that retrieves bug tickets from JIRA and posts them in a Slack channel. It provides an easy way to keep track of bug tickets for review.

## Setup

1. Install Python: Make sure you have Python installed on your machine. You can download it from the official Python website: [python.org](https://www.python.org).

2. Clone the Repository: Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/tdeva14/bugReporterSlackBot.git
   ```

3. Install Dependencies: Navigate to the cloned repository directory and install the required Python packages by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the Bot:

   - Replace the placeholder values in `bugreporter.py` with the actual values for the Slack BOT token, channel name, JIRA domain URL, JIRA username, JIRA password, search query, JIRA usernames, JIRA mail IDs, and Slack member IDs. Ensure you remove the `##` characters and provide the appropriate values.

5. Run the Bot: Execute the Python script by running the following command:

   ```bash
   python bugreporter.py
   ```

   The bot will retrieve bug tickets from JIRA and post them in the specified Slack channel.

## Additional Information

- The `requirements.txt` file lists the required Python packages. You can install them using the command mentioned in the setup instructions.

- The `.gitignore` file specifies the files and directories that should be ignored by Git. It includes common Python-related files and directories.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and enhance the code as per your requirements!
