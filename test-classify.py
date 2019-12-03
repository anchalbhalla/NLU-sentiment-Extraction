import pandas as pd
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, ConceptsOptions, EmotionOptions, SentimentOptions, CategoriesOptions
from ibm_watson import ApiException
import operator


authenticator = IAMAuthenticator('oazSLaKBnFBuCzXOUuXRyVgoEgndPf-7TT-x6EaZDNXG')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    authenticator=authenticator)

natural_language_understanding.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')

data = pd.read_csv('Negative_joy.csv') 

all_person = []
all_organization = []
all_company = []
all_location = []

all_keywords_1 = []
all_keywords_2 = [] 
all_keywords_3 = []

all_category_1 = []
all_category_2 = [] 
all_category_3 = []

concepts = []

# categories = []
# cat_explain = []


overall_sentiment = []
overall_emotion = []

deviceid = []
free_data = [] 

emotion_conf = []
sentiment_conf = []


# for i in range(len(data)):
#     text = data['free_text'][i]

# response = natural_language_understanding.analyze(
#     text='I would like to give special thanks to mr. Ahmed al sherif for his kind job and helpful I been live in Dubai for 9 years ago and this first time met someone how   excetremly helpful and responsibility about his quality service Thank you so much ðŸ˜Š Mr. Ahmed and all kind of best of best to youEhab ',
#     features=Features(
#         entities=EntitiesOptions(emotion=True, sentiment=True, limit=10),
#         keywords=KeywordsOptions(emotion=True, sentiment=True,limit=3),
#         concepts=ConceptsOptions(limit=1),
#         emotion=EmotionOptions(document=True),
#         categories=CategoriesOptions(limit=3),
#         sentiment=SentimentOptions(document=True))).get_result()

# #json_result = json.dumps(response, indent=2) 

# sentiment_p = json.dumps(response['sentiment']['document']['label'])

# keyword_1 = "" 
# keyword_2 = "" 
# keyword_3 = ""
# if 'keywords' in response: 
#   for i in range(3) :
#     temp = json.dumps(response['keywords'][i]['text'])

#     if i == 0: 
#      keyword_1 = temp 
#     elif i == 1:
#       keyword_2 = temp
#     elif i == 2:
#       keyword_3 = temp

# print(keyword_1)
# print(keyword_2)
# print(keyword_3)


# category_1 = "" 
# category_2 = "" 
# category_3 = ""
# if 'categories' in response: 
#   for i in range(3) :
#     temp = json.dumps(response['categories'][i]['label'])

#     if i == 0: 
#      category_1 = temp 
#     elif i == 1:
#       category_2 = temp
#     elif i == 2:
#       category_3 = temp

# print(category_1)
# print(category_2)
# print(category_3) 


# person = "" 
# company = "" 
# organization = "" 
# location = "" 

# print(len(response['entities']))
# if 'entities' in response: 
#   for i in range(len(response['entities'])) :
#     temp = json.dumps(response['entities'][i]['type'])
#     temp1 = temp.replace("\"", "")
#     print(temp)
#     if str(temp1) == str('Person'):
#       person = response['entities'][i]['text'] 
#     elif str(temp1) == str('Company'): 
#       company = response['entities'][i]['text']
#     elif str(temp1) == str('Organization'):
#       organization = response['entities'][i]['text']
#     elif str(temp1) == str('Location'): 
#       location = response['entities'][i]['text']


# print(person)
# print(company)
# print(organization)
# print(location)


# keywords_p = json.dumps(response['keywords'][0]['text'])
# keywords_p_1 = json.dumps(response['keywords'][0]['sentiment']['label'])

# keywords_p_2 = json.dumps(response['keywords'][0]['emotion'])
# i = json.loads(keywords_p_2)
# max_val =  max(i.items(), key=operator.itemgetter(1))[0] 
# print('max val : ') 
# print(max_val)
# emo = i.keys()

# entities_p = json.dumps(response['entities'][0]['text'])
# entities_p_1 = json.dumps(response['entities'][0]['sentiment']['label'])

# keywords_p_2 = json.dumps(response['entities'][0]['emotion'])
# i = json.loads(keywords_p_2)
# emo = i.keys()

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


# print(json.dumps(response, indent=2))


for j in range(len(data)):
     text_data = data['free_data'][j] 
     dev_id = data['device_survey_id'][j]

     try: 
       response = natural_language_understanding.analyze(
       text=text_data,features=Features(entities=EntitiesOptions(emotion=True, sentiment=True, limit=10),keywords=KeywordsOptions(emotion=True, sentiment=True,limit=3),concepts=ConceptsOptions(limit=1),emotion=EmotionOptions(document=True),categories=CategoriesOptions(limit=3), sentiment=SentimentOptions(document=True))).get_result() 
       
       sentiment_p = json.dumps(response['sentiment']['document']['label']) 

       sentiment_score = json.dumps(response['sentiment']['document']['score'])

       # print('sentiment done')

       keyword_1 = "" 
       keyword_2 = "" 
       keyword_3 = "" 
       # print(len(response['keywords']))
       if 'keywords' in response: 
         for i in range(len(response['keywords'])) :
          temp = json.dumps(response['keywords'][i]['text'])

          if i == 0: 
           keyword_1 = temp 
          elif i == 1:
            keyword_2 = temp
          elif i == 2:
            keyword_3 = temp

       all_keywords_1.append(keyword_1)
       all_keywords_2.append(keyword_2)
       all_keywords_3.append(keyword_3)
       # print('keywords done')

       category_1 = "" 
       category_2 = "" 
       category_3 = ""
       if 'categories' in response: 
         for i in range(len(response['categories'])) :
          temp = json.dumps(response['categories'][i]['label'])

          if i == 0: 
           category_1 = temp 
          elif i == 1:
            category_2 = temp
          elif i == 2:
            category_3 = temp

       all_category_1.append(category_1)
       all_category_2.append(category_2)
       all_category_3.append(category_3) 
       # print('category done')

       person = "" 
       company = "" 
       organization = "" 
       location = "" 

       # print(len(response['entities']))
       if 'entities' in response: 
         for i in range(len(response['entities'])) :
          temp = json.dumps(response['entities'][i]['type'])
          temp1 = temp.replace("\"", "")
          print(temp)
          if str(temp1) == str('Person'):
            person = response['entities'][i]['text'] 
          elif str(temp1) == str('Company'): 
            company = response['entities'][i]['text']
          elif str(temp1) == str('Organization'):
            organization = response['entities'][i]['text']
          elif str(temp1) == str('Location'): 
            location = response['entities'][i]['text']
       # print('entities done')

       all_person.append(person)
       all_company.append(company)
       all_organization.append(organization)
       all_location.append(location)



       # keywords_p = json.dumps(response['keywords'][0]['text'])
       # keywords_p_1 = json.dumps(response['keywords'][0]['sentiment']['label'])
       # keywords_p_2 = json.dumps(response['keywords'][0]['emotion'])
       # i = json.loads(keywords_p_2)
       # emo =  max(i.items(), key=operator.itemgetter(1))[0] 

       # entities_p = json.dumps(response['entities'][0]['text'])
       # entities_p_1 = json.dumps(response['entities'][0]['sentiment']['label'])
       # entities_p_2 = json.dumps(response['entities'][0]['emotion'])
       # i1 = json.loads(entities_p_2)
       # emo1 = max(i1.items(), key=operator.itemgetter(1))[0] 

       emotion_p = json.dumps(response['emotion']['document']['emotion'])
       i2 = json.loads(emotion_p)
       emo2 = max(i2.items(), key=operator.itemgetter(1))[0]  

       emotion_score = json.dumps(response['emotion']['document']['emotion'] [emo2])

       concepts_p = ""
       if 'concepts' in response:
        if(len(response['concepts']) == 1):
          concepts_p = json.dumps(response['concepts'][0]['text'])

       # entities.append(entities_p)
       # ent_sentiment.append(entities_p_1)
       # ent_emotion.append(emo1)
       # keywords.append(keywords_p)
       # key_sentiment.append(keywords_p_1)
       # key_emotion.append(emo)
       concepts.append(concepts_p)
       overall_emotion.append(emo2)
       overall_sentiment.append(sentiment_p) 

       free_data.append(text_data)
       deviceid.append(dev_id) 

       sentiment_conf.append(sentiment_score)
       emotion_conf.append(emotion_score)
       # print('entities : ' + entities_p)
       # print('done')


     except Exception as ex:
        #print ("Method failed with status code " + str(ex.code) + ": " + ex.message)
        error = ex
        print(ex)
        # entities.append('0')
        # ent_sentiment.append('0')
        # ent_emotion.append('0')
        # keywords.append('0')
        # key_sentiment.append('0')
        # key_emotion.append('0')
        # concepts.append(concepts_p)
        # overall_emotion.append('0')
        # overall_sentiment.append('0') 

        # free_data.append(text_data)
        # deviceid.append(data['device_survey_id'][i])

# print(len(deviceid))
# print(len(free_data))
# print(len(overall_sentiment))
# print(len(overall_emotion))
# print(len(keywords))
# print(len(key_sentiment))
# print(len(key_emotion))
# print(len(concepts))


df_temp = pd.DataFrame({"device_survey_id" : deviceid, "free_data" : free_data, "overall sentiment" : overall_sentiment, "sentiment score" : sentiment_conf, "overall_emotion" : overall_emotion, "emotion score" : emotion_conf, "keywords_1" : all_keywords_1, "keywords_2" : all_keywords_2, "keywords_3" : all_keywords_3, "category_1": all_category_1, "category_2": all_category_2, "category_3" : all_category_3, "Person": all_person, "Company": all_company, "Organization": all_organization, "Location" : all_location, "Concepts" : concepts })
df_temp.to_csv('FinalNegativeJoyResults.csv', index=False)