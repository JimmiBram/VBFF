from flask import Flask, render_template, request, redirect, url_for, flash, session
import hashlib

def hash_password(password):
    # Encode the password to bytes
    password_bytes = password.encode('utf-8')
    # Use a hashing algorithm, e.g., SHA256
    hash_object = hashlib.sha256(password_bytes)
    # Get the hexadecimal representation of the hash
    return hash_object.hexdigest()

app = Flask(__name__, static_folder="static", static_url_path="/")
app.secret_key = "supersecretkey"

# Dummy credentials for demonstration purposes
USER_CREDENTIALS = {
    "student1": "4c713b660433b668d55b00b87f5c64ce2ad5aeb94207d3fbfc51634feefe9088",
    "student2": "1532e76dbe9d43d0dea98c331ca5ae8a65c5e8e8b99d3e2a42ae989356f6242a",
    "hacker1": "7a7801334db4cb75baa54b9a4d7c136212d3abe882abcb88de94e5615d71cb48",
    "hacker2": "921a95e8b614f668981d9eee4d24a3ffdb6821162246bb8036f73f4fd7d20564",
    "teacher1": "a3918628a8f2821ae8abe7bbe1d817241df2cb93dccd4cfae83b2d8c64107c43",
    "teacher2": "501d5acb4acc06d85d1fe1979a5d36b68f2becc069756164f763fc8bd275d0f0",
    "admin": "a8589dbb7121f100b2fe2abb201e5f927275d060168156a1421a3ffa36d0319c",
    "superadmin": "abdb9dec52c7936258206899e60d5d5ebc277469c847ac2a04c49d2f579b4601",
    "demo": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",
    "adam": "8019d97d49534181e4518e5eca077e9a39c354c00cd2e1342617dd0c9637721d",
    "beta": "02d38d5db021b57a551248d063d183429a4703e57312e7416f12002244a2a25f",
    "casper": "2cac39c223798f8ee1f1c49173d00d71fec741ce520806e25b358d3199041283",
    "dennis": "f3eb8cf6a3b3c89508f9416c87ca40cd99bf174cdff3bad9acb47968b3c48c51",
    "ethan": "780d06d3a2af1b22aa2f657aa1385e3813a9d2ecc16edffb23f6e30b05dc4b45",
    "findus": "1c9f8eec5eeca58237f9ebc37654bdc2d8530af53f1ebf6e057fe81e6968259f",
    "maxadmin": "90bb8effacd228d691819f82eed88c90bff78dfc4dd927b5f242927c0d26c2ef",
    "superduperadmin": "a6ff5758306b36f76c8af68afe6261e20ec3f8b411d0b2bbd452bf494a3c9693"
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        password_hash = str(hash_password(password))
        print("PASS:" + password_hash)

        # Check credentials
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password_hash:
            session['username'] = username
            flash('Du lykkedes med at logge ind!', 'success')
            return redirect(url_for('success'))
        else:
            flash('Forkert brugernavn eller adgangskode. Prøv igen!', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/success')
def success():
    if 'username' not in session:
        flash('Du skal være logget ind for at se denne side.', 'danger')
        return redirect(url_for('login'))
    flag = str(hash_password(session['username']))
    flag = flag[-4:]
    return render_template('success.html', username=session['username'], flag=flag)

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Du er blevet logget ud.', 'info')
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=80)



