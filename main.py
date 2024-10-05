from flask import Flask,render_template,request
import requests

url = "https://linkedin-data-api.p.rapidapi.com/search-jobs"

querystring = {"keywords":"golang","locationId":"102713980","datePosted":"anyTime","sort":"mostRelevant"}

headers = {
	"x-rapidapi-key": "4b8d3718c7msh125343dc4c513fcp125648jsn0c26d1a0e370",
	"x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
}


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/search')
def search():
    return render_template('searcher.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/profile',methods=['POST'])
def profile():
    info  = {}
    if request.method == 'POST':
        info['name'] = request.form.get('name')
        info['college'] = request.form.get('college')
        info['education'] = request.form.get('education')
        info['skills'] = request.form.get('skills')
        info['desc'] = request.form.get('additionalInfo')
        info['exp'] = request.form.get('experience')
        info['jobint'] = request.form.get('jobInterest')
        info['country'] = request.form.get('country')
    return render_template('profile.html',info=info)

@app.route('/jobs',methods=['POST'])
def jobs():
    if request.method == 'POST':
        querystring['keywords'] = request.form.get('query')
    response = requests.get(url, headers=headers, params=querystring)
    dataset = response.json()['data']
    return render_template('index.html',dataset=dataset)

@app.route('/courses')
def courses():
    return render_template('couse.html')

if __name__ == '__main__':
    app.run(debug=True)
