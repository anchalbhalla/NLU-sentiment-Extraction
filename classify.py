import pandas as pd
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, ConceptsOptions, EmotionOptions, SentimentOptions
from ibm_watson import ApiException
import operator


authenticator = IAMAuthenticator('oazSLaKBnFBuCzXOUuXRyVgoEgndPf-7TT-x6EaZDNXG')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator)

natural_language_understanding.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')

data = pd.read_csv('withoutNULLandnum.csv') 

entities = []
ent_sentiment = []
ent_emotion = []

keywords = []
key_sentiment = [] 
key_emotion = []

concepts = []

# categories = []
# cat_explain = []


overall_sentiment = []
overall_emotion = []

deviceid = []
free_data = []


# for i in range(len(data)):
#     text = data['free_text'][i]

response = natural_language_understanding.analyze(
    text='Great workers and nice department',
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True, limit=1),
        keywords=KeywordsOptions(emotion=True, sentiment=True,limit=1),
        concepts=ConceptsOptions(limit=1),
        emotion=EmotionOptions(document=True),
        sentiment=SentimentOptions(document=True))).get_result()

json_result = json.dumps(response, indent=2) 

# sentiment_p = json.dumps(response['sentiment']['document']['label'])
# keywords_p = json.dumps(response['keywords'][0]['text'])
# keywords_p_1 = json.dumps(response['keywords'][0]['sentiment']['label'])

# keywords_p_2 = json.dumps(response['keywords'][0]['emotion'])
# i = json.loads(keywords_p_2)
# max_val =  max(i.items(), key=operator.itemgetter(1))[0] 
# print('max val : ') 
# print(max_val)
# #emo = i.keys()

# # entities_p = json.dumps(response['entities'][0]['text'])
# # entities_p_1 = json.dumps(response['entities'][0]['sentiment']['label'])

# # keywords_p_2 = json.dumps(response['entities'][0]['emotion'])
# # i = json.loads(keywords_p_2)
# # emo = i.keys()

# emotion_p = json.dumps(response['emotion']['document']['emotion'])
# i1 = json.loads(emotion_p)
# emo1 = i1.keys() 

# print(next(iter(emo1))) 

# concepts_p = json.dumps(response['concepts'][0]['text'])

# print("concept : " + concepts_p)
# print("sentiment : " + sentiment_p)
# print("keyword : " + keywords_p)
# # print("keyword : " + keywords_p_2)
# # # print(next(iter(emo)))
# # print("entities : " + entities_p_1)
# print(next(iter(emo)))

emotion_p = json.dumps(response['emotion']['document']['emotion'])
i2 = json.loads(emotion_p)
emo2 = max(i2.items(), key=operator.itemgetter(1))[0] 

emotion_score = json.dumps(response['emotion']['document']['emotion'] [emo2]) 
print(emotion_score)  


sentiment_score = json.dumps(response['sentiment']['document']['score']) 
print(sentiment_score)
print(json.dumps(response, indent=2))


# for i in range(len(data)):
#      text_data = data['free_text'][i] 
#      dev_id = data['device_survey_id'][i]

#      try: 
#        response = natural_language_understanding.analyze(
#        text=text_data,features=Features(entities=EntitiesOptions(emotion=True, sentiment=True, limit=1),keywords=KeywordsOptions(emotion=True, sentiment=True,limit=1),concepts=ConceptsOptions(limit=1),emotion=EmotionOptions(document=True),sentiment=SentimentOptions(document=True))).get_result() 
#        sentiment_p = json.dumps(response['sentiment']['document']['label'])
#        keywords_p = json.dumps(response['keywords'][0]['text'])
#        keywords_p_1 = json.dumps(response['keywords'][0]['sentiment']['label'])
#        keywords_p_2 = json.dumps(response['keywords'][0]['emotion'])
#        i = json.loads(keywords_p_2)
#        emo =  max(i.items(), key=operator.itemgetter(1))[0] 

#        # entities_p = json.dumps(response['entities'][0]['text'])
#        # entities_p_1 = json.dumps(response['entities'][0]['sentiment']['label'])
#        # entities_p_2 = json.dumps(response['entities'][0]['emotion'])
#        # i1 = json.loads(entities_p_2)
#        # emo1 = max(i1.items(), key=operator.itemgetter(1))[0] 

#        emotion_p = json.dumps(response['emotion']['document']['emotion'])
#        i2 = json.loads(emotion_p)
#        emo2 = max(i2.items(), key=operator.itemgetter(1))[0] 

#        # concepts_p = json.dumps(response['concepts'][0]['text'])

#        # entities.append(entities_p)
#        # ent_sentiment.append(entities_p_1)
#        # ent_emotion.append(emo1)
#        keywords.append(keywords_p)
#        key_sentiment.append(keywords_p_1)
#        key_emotion.append(emo)
#        # concepts.append(concepts_p)
#        overall_emotion.append(emo2)
#        overall_sentiment.append(sentiment_p) 

#        free_data.append(text_data)
#        deviceid.append(dev_id) 

#        print('entities : ' + entities_p)



#      except Exception as ex:
#         #print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
#         error = ex
#         # entities.append('0')
#         # ent_sentiment.append('0')
#         # ent_emotion.append('0')
#         # keywords.append('0')
#         # key_sentiment.append('0')
#         # key_emotion.append('0')
#         # concepts.append(concepts_p)
#         # overall_emotion.append('0')
#         # overall_sentiment.append('0') 

#         # free_data.append(text_data)
#         # deviceid.append(data['device_survey_id'][i])

# print(len(deviceid))
# print(len(free_data))
# print(len(overall_sentiment))
# print(len(overall_emotion))
# print(len(keywords))
# print(len(key_sentiment))
# print(len(key_emotion))
# # print(len(concepts))


# df_temp = pd.DataFrame({"device_survey_id" : deviceid, "free_data" : free_data, "overall sentiment" : overall_sentiment, "overall_emotion" : overall_emotion, "keywords" : keywords, "keywords sentiment" : key_sentiment, "keywords emotion" : key_emotion })
# df_temp.to_csv('FinalResults-withoutconcepts.csv', index=False)