from jira import JIRA
import openai

openai.api_key = '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'

jira_options = {'server': 'https://hackton-gepeto.atlassian.net', 'verify': False}
jira = JIRA(options=jira_options, basic_auth=('davi.ribeirosantos11@gmail.com', 'ATATT3xFfGF0Jeb6OxMkQe4SOhNwWu0ngyMzFHxRHEjfCUEI2hGnS0a2t4LUqwf0GxpMFaGLRbhZwWudd_4C2Vno8x2KMmCdd40YyONW2hT8ZTFqPqY8KfxhDqZoGzKP4baZSN4S7DH7aJMh-cgHly2HPfXoEEeIN2YQzxidLslIM-w-HiqCq6E=EFC68043'))

def generate_description(prompt):
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=150)
    return response.choices[0].text.strip()

def create_epic_with_gpt_description():
    prompt = input("Digite um prompt para a descrição do épico: ")
    description = generate_description(prompt)

    epic_name = input("Digite o nome do épico: ")

    new_epic = {
        'project': {'key': 'SCRUM'},
        'summary': epic_name,
        'description': description,
        'issuetype': {'name': 'Epic'}
    }

    created_epic = jira.create_issue(fields=new_epic)
    print(f"Épico criado com ID: {created_epic.id}")

if __name__ == "__main__":
    create_epic_with_gpt_description()