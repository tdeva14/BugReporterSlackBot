from slack_sdk import WebClient
import requests
import datetime

# Slack BOT token
SLACK_BOT_TOKEN = "##SLACKBOT_TOKEN##"
CHANNEL = "##CHANNEL_NAME##"
slack_client = WebClient(token=SLACK_BOT_TOKEN)

# JIRA API details
jira_domain = "##JIRA_DOMAIN_URL##"
browse_path = "/browse"
rest_path = "/rest/api/2"
search_api = "/search"
user_search_api = "/user/search"
api_url = jira_domain + rest_path + search_api

# JIRA credentials
username = "##JIRA_USERNAME##"
password = "##JIRA_PWD##"  # API token or password

# Headers with basic authentication
headers = {
    "Accept": "application/json"
}

# JIRA search query
jql_query = '##SEARCH_QUERY##'

# Map team members' username and email
eng_emailid_map = {
    '##JIRA_USERNAME##':'##JIRA_MAILID##'
}

# Map team members' email and slack member id
eng_memberid_map = {
    '##JIRA_MAILID##':'##SLACK_MEMBERID##',
}

# Update date
current_date = datetime.datetime.now()
result = "<!here> :alert: *Bug tickets for review - Week %s, %s/%s/%s*" % (current_date.isocalendar()[1], current_date.day, current_date.month, current_date.year)
slack_client.chat_postMessage(channel = CHANNEL, text = result)

for engineer in eng_emailid_map:
    query = jql_query + engineer

    # Parameters for the JQL query
    params = {
        "jql": query,
         "maxResults": 50  # Change this value as per your requirement
    }

    # Make the API request
    response = requests.get(api_url, auth=(username, password), headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        result = ":information_desk_person: " + "<@" + eng_memberid_map[eng_emailid_map[engineer]] + ">\n"
        result_dict = {}

        # Process the retrieved tickets
        if "issues" in data:
            issues = data["issues"]
            for issue in issues:
                # Fetch ticket summary, status, assginee
                summary = issue["fields"]["summary"]
                status = issue["fields"]["status"]["name"]
                curr_assignee = issue["fields"]["assignee"]["name"]
                assignee_name = issue["fields"]["assignee"]["displayName"]

                # Do not add ticket to current engineer's list if the assignee is a team member
                # Because the ticket needs to show up in the respective team member's list
                if curr_assignee == engineer or curr_assignee not in eng_emailid_map:
                    key = jira_domain + browse_path + '/' + issue["key"]
                    result += "<" + key + "|" + issue["key"] + ">"
                    result += ' : ' + summary + ' `Status: ' + status + '` ' + ' `Assignee: ' + assignee_name + '`\n'

                    # Group tickets based on status
                    if status not in result_dict:
                        result_dict.setdefault(status, [])
                    result_dict[status].append(result)
        else:
            result += "No issues found :smile:\n"

        # Post the report in slack
        slack_client.chat_postMessage(channel = CHANNEL, text = result)
    else:
        print("Failed to retrieve issues. Status code:", response.status_code)
