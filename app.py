from flask import Flask, render_template, request , jsonify
import pickle
import base64
import io
from PIL import Image

# model = pickle.load("model/star_model.pkl" , "rb")

conselletions = [
    {
        "name": "Cancer",
        "link": "https://en.wikipedia.org/wiki/Cancer_(constellation)",
        "description": "Cancer is a faint constellation representing the crab in the zodiac. It is best known for containing the Beehive Cluster, a beautiful open star cluster."
    },
    {
        "name": "Cassiopeia",
        "link": "https://en.wikipedia.org/wiki/Cassiopeia_(constellation)",
        "description": "Cassiopeia is a distinctive 'W'-shaped constellation, representing the mythological queen. It is prominent in the northern sky and contains several notable deep-sky objects."
    },
    {
        "name": "Centaurus",
        "link": "https://en.wikipedia.org/wiki/Centaurus",
        "description": "Centaurus is a large constellation in the southern hemisphere. It is known for containing Alpha Centauri, the closest star system to Earth, and the bright star, Beta Centauri."
    },
    {
        "name": "Leo",
        "link": "https://en.wikipedia.org/wiki/Leo_(constellation)",
        "description": "Leo is a prominent constellation representing the lion. It is one of the zodiac signs and contains the bright star Regulus, along with several galaxies."
    },
    {
        "name": "Orion",
        "link": "https://en.wikipedia.org/wiki/Orion_(constellation)",
        "description": "Orion is one of the most recognizable constellations, representing the hunter. It features the bright stars Betelgeuse and Rigel, and the famous Orion Nebula."
    }
]

app = Flask(__name__ )
 
# @app.route('/process_image', methods=['POST'])
# def process_image():
#     data = request.json
#     image_data = data['image']
    
#     # Remove the data URL prefix
#     image_data = image_data.split(',')[1]
    
#     # Decode the base64 string
#     image_bytes = base64.b64decode(image_data)
    
#     # Open the image using PIL
#     image = Image.open(io.BytesIO(image_bytes))
    
#     # Perform your image preprocessing here
#     # For example:
#     # processed_image = your_preprocessing_function(image)
    
#     # For this example, we'll just return a success message
#     # In a real application, you might return processed image data or analysis results
#     return jsonify({'message': 'Image processed successfully'})

@app.route("/")
def indexs():
    return render_template("index.html")

@app.route("/predict")
def predicts():
    ## get image here 
    return render_template("predict.html")

if __name__ == '__main__':
    app.run(debug = True)