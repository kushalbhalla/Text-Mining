##### WELCOME IN Topic Modelling Projects ######
##### Here is main console for text classification that implementing by machine learning algorithms


#### Required python libraries

import pandas as pd
from csv import DictWriter
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import NMF
import plotly.graph_objects as go
import spacy
from tkinter import messagebox, filedialog

class Classy:

    def Getdata(self,fileN , topicN , wordN):
        self.fileNAME = fileN
        self.topicNO = topicN
        self.wordNO = wordN

    def MachineLearningModel(self):

        #### Reading Text data File for Classification of Text data

        self.dataFrame = pd.read_csv(self.fileNAME)
        self.heading = self.dataFrame.columns[0]


        #### Use TF-IDF Vecorization to create a vectorized document term matrix

        self.tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
        self.docTM = self.tfidf_vectorizer.fit_transform(self.dataFrame[self.heading])


        ####  Using Scikit-Learn create an instance of NMF with 20 expected components. (Use random_state=42)

        self.nmf_model = NMF(n_components=self.topicNO, random_state=42)
        self.nmf_model.fit(self.docTM)

        self.topic_results = self.nmf_model.transform(self.docTM)
        self.topic_results.argmax(axis=1)
        self.dataFrame['Topic'] = self.topic_results.argmax(axis=1)
        self.all_word_list = []


    def save(self):
        with open('cat.text', 'a') as wf:
            wf.truncate(0)

            self.count = 1
            for index, topic in enumerate(self.nmf_model.components_):
                wf.write(f"THE TOP {self.wordNO} WORDS FOR TOPIC #{index} \n")
                self.count = 1
                self.all_word_list.append([self.tfidf_vectorizer.get_feature_names()[i] for i in topic.argsort()[-self.wordNO:]])
                for word in [self.tfidf_vectorizer.get_feature_names()[i] for i in topic.argsort()[-self.wordNO:]]:
                    wf.write(f"{self.count} {word} \n")
                    self.count += 1


    def classification(self,selectTopic):

        self.sampleDataFrame = pd.DataFrame()
        self.sampleDataFrame = self.dataFrame.loc[self.dataFrame['Topic'] == selectTopic, [self.heading]]


        with open('classification.csv', 'w', newline='') as wf:
            self.title = "Topic " + str(selectTopic)+" " +"Related"+" "+self.heading
            self.csv_writer = DictWriter(wf, fieldnames=[self.title])
            self.csv_writer.writeheader()
            for self.questionEx in self.sampleDataFrame[self.heading]:
                self.csv_writer.writerow({
                    self.title: self.questionEx
                })

    def SearchT(self,sentance):
        try:
            return self.dataFrame.loc[self.dataFrame[self.heading] == sentance, 'Topic'].iloc[0]

        except IndexError:
            messagebox.showinfo('Error', 'Please enter sentance or paragraph without single or double quotes')

        # return self.dataFrame.loc[self.dataFrame[self.heading] == sentance, 'Topic'].iloc[0]

    def Show(self):
        self.Showdataframe = pd.DataFrame()
        for index, topic in enumerate(self.nmf_model.components_):
            self.Showdataframe[f'Topic {index}'] = [self.tfidf_vectorizer.get_feature_names()[i] for i in topic.argsort()[-self.wordNO:]]
        return  self.Showdataframe

    def See(self):
        self.mna = pd.DataFrame()
        self.mna['Sort'] = self.dataFrame['Topic'].value_counts().sort_index()
       
        fig = go.Figure(
            data=[go.Bar(y=self.mna['Sort'])],
            layout_title_text="Dominant Topic"
        )

        fig.update_layout(
            title="Plot Title",
            xaxis_title="Topics",
            yaxis_title="Nomber of Questions",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#7f7f7f"
            )

        )

        fig.show()

    def pyTopicPlot(self,search_word,amount):
        nlp = spacy.load('en_core_web_sm')

        self.topic_word_list = []
        for index, topic in enumerate(self.nmf_model.components_):
            self.topic_word_list.append([self.tfidf_vectorizer.get_feature_names()[i] for i in topic.argsort()[-self.wordNO:]])

        
        self.all_word = ''
        for word_list in self.topic_word_list:
            for word in word_list:
                self.all_word = self.all_word + ' ' + word


        self.all_word_vector = nlp(f'{self.all_word}')
        self.search_word_vector = nlp(f'{search_word}')
        self.search_word_dict = {}

        for tokens in self.all_word_vector:

            self.search_word_dict[tokens] = self.search_word_vector.similarity(tokens) * 100


        word_vector_value = []
        for i in self.search_word_dict.values():
            if (i in word_vector_value):
                continue
            else:
                word_vector_value.append(i)

        sort_vector_value = sorted(word_vector_value)
        sort_vector_value = sort_vector_value[-amount:]
        

        words = []
        for i in sort_vector_value:
            for key, values in self.search_word_dict.items():
                if values == i:
                        words.append(str(key))

        word_topicNo = []
        for word in words:
            
            for sub_list in self.topic_word_list:
                if word in sub_list:
                    word_topicNo.append(self.topic_word_list.index(sub_list))
                    break


        Check_Density = pd.DataFrame()
        Check_Density[f'Top {amount} word'] = words
        Check_Density['Topic No'] = word_topicNo
        Check_Density['Vector_similarity'] = sort_vector_value

        # Check_Density.iplot(kind='scatter', x='Top Ten word', y='Topic No', color='Blue', text='Vector_similarity',mode='markers')

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=Check_Density[f'Top {amount} word'],
            y=Check_Density['Topic No'],
            mode="markers",
            text=Check_Density['Vector_similarity'],
            textposition="bottom center",
        ))

        fig.update_layout(
            title="Similar word vector value char",
            xaxis_title=f"Top {amount} word ",
            yaxis_title="Related Topic ",
            font=dict(
                family="Courier New, monospace",
                size=18,
                color="#7f7f7f"
            )

        )

        fig.show()

