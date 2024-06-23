from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 简单的数据库，用于存储小知识
knowledge_db = []

@app.route('/')
def index():
    return render_template('index.html', knowledge_db=knowledge_db)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        knowledge_db.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('submit.html')

@app.route('/detail/<int:knowledge_id>')
def detail(knowledge_id):
    knowledge = knowledge_db[knowledge_id]
    return render_template('detail.html', knowledge=knowledge, knowledge_id=knowledge_id)

if __name__ == '__main__':
    app.run(debug=True)
