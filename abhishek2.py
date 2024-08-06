import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

words=[]
classes=[]
documents=[]
ignore_words=['?']
data_file=open('intents.json').read()
intents=json.loads(data_file)


for intent in intents['intents']:
    for pattern in intent['patterns']: w=nltk.word_tokenize(pattern)
        words.extend(w8
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
words=[lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words=sorted(list(set(words)))
classes=sorted(list(set(classes)))
# documents = combination between patterns and intents
print (len(documents), "documents")
# classes = intents
print (len(classes), "classes", classes)
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))
training=[]
output_empty=[0]*len(classes)
    bag=[]
    pattern_words=doc[0] pattern_words=[lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0); output_row=list(output_empty)
    output_row[classes.index(doc[1])]=1
    
    training.append([bag, output_row]);
train_x=list(training[:,0])
train_y=list(training[:,1])
print("Training data created")


# Create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains number of neurons
# equal to number of intents to predict output intent with softmax
model=Sequential()
model.add(Dense(128,input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))
hist=model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbotmodel.h5', hist)
print("model created")

_Intents JSON File:_

    "intents": [
        {
            "tag": "greeting",
            "patterns": ["Hi", "Hey", "Hello"],
            "responses": ["Hi there!", "How can I assist you?"]
        },
        {
            "tag": "goodbye",
            "patterns": ["Bye", "See you later"],
            "responses": ["See you later!", "Have a great day!"]
        }
    ]
}
```
