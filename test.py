from jira import JIRA
import openai
import sys

openai.api_key = 'your_open_ai_key'

jira_options = {'server': 'https://hackton-gepeto.atlassian.net', 'verify': False}
jira = JIRA(options=jira_options, basic_auth=('davi.ribeirosantos11@gmail.com', 'ATATT3xFfGF0Jeb6OxMkQe4SOhNwWu0ngyMzFHxRHEjfCUEI2hGnS0a2t4LUqwf0GxpMFaGLRbhZwWudd_4C2Vno8x2KMmCdd40YyONW2hT8ZTFqPqY8KfxhDqZoGzKP4baZSN4S7DH7aJMh-cgHly2HPfXoEEeIN2YQzxidLslIM-w-HiqCq6E=EFC68043'))

def generate_description(prompt):
    #response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=150)
    #return response.choices[0].text.strip()
    return "Description from flask"

def create_epic_with_gpt_description(prompt, epic_name):
    description = generate_description(prompt)

    new_epic = {
        'project': {'key': 'SCRUM'},
        'summary': epic_name,
        'description': description,
        'issuetype': {'name': 'Epic'}
    }

    try:
      # created_epic = jira.create_issue(fields=new_epic)
      print(f"Épico criado com ID: {created_epic.id}")
    except Exception as e:
      print(str(e))

    return description

if __name__ == "__main__":
    create_epic_with_gpt_description(sys.argv[1], sys.argv[2])