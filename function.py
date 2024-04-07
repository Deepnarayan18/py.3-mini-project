from flask import Flask,render_template,request , make_response 
import random 


app = Flask(__name__) 

@app.route('/') 
def index():
  return render_template('start.html')
 
@app.route('/check_guess',methods=['POST']) 
def check_guess(): 
    secret_number_str = request.cookies.get('secret_number')
    if secret_number_str is None:
        return "Secret number is missing. Please start the game first."
    
    try:
        secret_number = int(secret_number_str)
    except ValueError:
        return "Invalid secret number. Please start the game again."
    
    attempts = int(request.cookies.get('attempts', 0)) 
    guess = int(request.form['guess']) 
    result = ""  
    
    print("____ now it is integer",secret_number)
    
    if guess == secret_number: 
        result = f"congratulation!you have guessed{secret_number}in{attempts}attempts!"
    elif guess < secret_number: 
        result = "too low." 
    else: 
        result = "too high." 
    
    return render_template('guess_result.html', result=result) 
@app.route('/start_game')     
def start_game(): 
   secret_number = random.randint(1, 100) 
   response = make_response(render_template('guess.html')) 
   response.set_cookie('secret_number', str(secret_number).encode('utf-8')) 
   response.set_cookie('attempts', b'0') 
   return response  

if __name__ ==  '__main__' :  
    app.run(debug=True)
      
          