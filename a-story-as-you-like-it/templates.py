from narrative_data import StoryNode


def base_template(content:str):
    return f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Conte à votre façon</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="/css/style.css" rel="stylesheet">
    </head>
    <body>
    <header>
        <h1>Conte à votre façon</h1>
        <p>(À Raymond Queneau)</p>
    </header>
        <hr />
        <main>
        {content}    
        <hr />
        <p style="text-align:center"><a href="https://github.com/delfanbaum/osp/tree/main/a-story-as-you-like-it">Source on GitHub</a></p>
        </main>
    </body>
    <script src="https://unpkg.com/htmx.org@1.9.10" integrity="sha384-D1Kt99CQMDuVetoL1lrYwg5t+9QdHe7NLX/SoJYkXDFfX37iInKRy5xLSi8nO7UC" crossorigin="anonymous"></script>
</html>
"""


def display_story_node(sn: StoryNode):
    forks =""
    if sn.forks:
        forks += "<ul>"
        for k, v in sn.forks.items():
            forks += f"""
<li hx-post="/api/story/{k}"
    hx-target="#story">{v}</li>
"""
        forks += "</ul>"

    return f"""<div id="story">
<p>{sn.id}. {sn.text}</p>
{forks}
</div>
"""
