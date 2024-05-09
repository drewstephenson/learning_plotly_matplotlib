import requests
import plotly.express as px

# Makes an API call and stores the response.
url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")

# Process results
response_dict = response.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repository information
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Create hover texts
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"Owner: {owner}<br />Description: {description}"
    hover_texts.append(hover_text)

# Plot the data
title = "Most-Starred Python Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size=24, xaxis_title_font_size=16, yaxis_title_font_size=16)

fig.update_traces(marker_color='skyblue', marker_line_color='black', marker_line_width=1)

fig.show()
