import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the emotion predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json = myobj, headers = header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the score of each emotion
    if response.status_code == 200:
        # Save the scores of mentioned emotions
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        # Find the name of the emotion with the highest score
        for key, val in formatted_response['emotionPredictions'][0]['emotion'].items():
            if val == max(formatted_response['emotionPredictions'][0]['emotion'].values()):
                dominant_emotion_name = key

    # If the response status code is 500, set label and score to None
    elif (response.status_code == 500) or (response.status_code == 400):
        # Save the scores of mentioned emotions as 'None'
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion_name = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion_name
        }