import pickle
from flask import Flask,render_template,request
# create object for the class Flask
app = Flask(__name__)

# Unpickle / Undumping the model
model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict' , methods = ['GET','POST'])
def predict():
    # Get the input data from the form as a string
    promotion_budget_str = request.form.get('Promotion_Budget')

    try:
        # Convert the input data to a numeric value (e.g., float)
        promotion_budget = float(promotion_budget_str)

        # Make the prediction using the numeric input
        prediction = model.predict([[promotion_budget]])

        # Round the prediction to 2 decimal places
        output = int(prediction)

        # Print the output (for debugging purposes)
        print(output)

        # Return the result to the template
        return render_template('index.html',my_text = f'You can expect {output} Passengers!!...Thanks')
    except ValueError:
        # Handle the case where the input cannot be converted to a numeric value
        error_message = "Invalid input. Please enter a numeric value for Promotion Budget."
        return render_template('error.html', error_message=error_message)


# To run the code
if __name__ == '__main__':
    app.run(debug=True)



