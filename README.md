# Detecting-Depression-through-YouTube-history
It is aimed at calculation of affective scores of videos using the audio visual feature and further analyzing the affective pattern generated from the YouTube watching history of an individual to predict his depression severity score. This repository maintains the code from our initial experiments where we used Long Short-Term Memory(LSTM) networks to understand the video content from the transcripts in order to identify if a video can trigger depression. Additionally, we propose a novel method of validating the results by analysing the CESD score of comments. You can find more details about this experiment in our [paper](https://aiforsocialgood.github.io/neurips2019/accepted/track1/pdfs/52_aisg_neurips2019.pdf) / [poster] (https://aiforsocialgood.github.io/neurips2019/accepted/track1/posters/52_aisg_neurips2019.pdf) that we presented at NeurIPS 2019 AI for Social Good Workshop. 

### Idea

It has been found that those in misery and depression, tend to find [comfort in having companions in woe](https://doi.org/10.1016/0022-1031(89)90020-6). Not just this, but studies also suggest that those in a sad mood tend to [prefer sadness in the music](https://psycnet.apa.org/doi/10.1037/a0023749) they listen to. While the surveys and self-descriptive tracking methods fail to diagnose symptoms of depression, peculiarities as those of rumination which come exclusively with depression can be analyzed to predict the state of mind of an individual.

On analyzing the comments as a function of videos present on YouTube, we found out that viewers tend to ruminate a lot on videos with Depressive triggers (e.g. Self-Injury, NSSI, Suicidal short films and multi fandoms). The nature of comments suggest that users tend to find a validation amongst others who are going through or have gone through the same situation. Not only do they feel comfortable, but at times it also gives them the courage to confess about their own situations. This acted as the base of our solution wherein we aim to analyze the watching patterns of an individual on YouTube by analyzing the affective content of the videos watched by her over a window size of 24 days with an overlap of 10 days.

### Solution Pipeline

We propose a solution to aid in early diagnosis of depression by giving a zoomed-in perspective of patient’s state of mind and experiences (usually undisclosed to physician) prior to process of seeking treatment in order to help target the at-risk population and improve diagnostic accuracy and efficiency. A pipeline of the solution is shown below:

For training our model, we'll require it to train on the CES-D scores of individuals corresponding to the patterns recorded in their YouTube watching history. To be precise, we would require the YouTube watching history of individuals over a period of time (preferably 3 months) and their score on the CES-D scale. We are in the process of building a platform that would anonymously record this data for our model to train upon.

Once we have this data, we'll calculate the affect of each video by predicting their arousal and valence values and calculating the affective score by cumulating them. The patterns observed in the affective scores of the videos watched over the duration will then be mapped to the CES-D score of the corresponding individual to help the model learn the watching patterns which correspond to a certain state of mind. The kind of patterns we expect to observe for individuals in or heading towards depression are:

* A gradual decline from happy/uplifting videos to sad/depressing videos over a period of time
* Videos of same affective content since they dent to do repetitive tasks for a long period of time (rumination)
* High frequency of depressive videos in the watching history. Note that depressive videos not only attract individuals with an unhealthy state of mind, but also tend to push them into one by activating the depressive mood for a long period of time.

What's important to note here is this whole line of research is not focused on predicting the affective score of the video itself, but the kind of mental experience it induces or attracts.

Once the model is ready, it can be used by an individual to track his/her change of watching patterns over a period of time. This behavioral pattern can be useful in determining the mental state of the viewer. This can be used to monitor recommendations and restrict the recommendations of triggering videos based on the watching activity. In case the patterns reveal the signs on unhealthy mental state, this tool can provide early diagnosis by warning the users about the change points in their mood and also direct them to the right portals for help. This would have a substantial impact for individuals both in the initial stage of depressive disorders and those who are already suffering from a depressed mental state. Our proposal aims at providing earlier intervention to improve recognition and management of depression in primary care by understanding patients’ inner experiences prior to and during the process of seeking treatment.

### Success Metrics

In an ideal scenario, our model should:

* Make an individual aware of his/her mental health and seek help if required.
* Help physicians diagnose Depression and the stage an individual is in (Mild, Clinical).
* Provide an extension for YouTube to monitor recommendations and restrict the recommendations of triggering videos based on a user’s watching activity.
