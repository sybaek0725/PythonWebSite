from flask import Flask, request, render_template
from search import perform_search

app = Flask(__name__)

# 루트 경로
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('search_term')
    print("search_term", search_term)

    perform_search(search_term)

    return render_template('results.html', search_term=search_term)
if __name__ == '__main__':
    # app.run(debug=True)
    # 서버 테스트용
    app.run('0.0.0.0', port=5000, debug=True)