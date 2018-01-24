#import userinfo
from flask import Flask, render_template, request

'''
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_folder)
else:
'''
app = Flask(__name__)


@app.route('/')
def show_index():
    return render_template('userinfo.html')


'''
@app.route('/submit', methods=['POST'])
def submit():

    user_info = userinfo.Userinfo(request.form['name'], request.form['gender'], request.form['age'],
                        request.form['weight'], request.form['height'], request.form['objective'],
                        request.form['preferred_time'], request.form['use_DNA_data'], request.form['use_wearable_data'],
                        request.form['term'])
    # upload userinfo to database
    print(request.form)

'''
if __name__ == '__main__':
    app.run()
