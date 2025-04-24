main.ipynb inneholder informasjon om hvordan modeller er laget, samt litt testing av dem. 

Det var ikke plass til å laste opp selve modellen som er brukt i github. 
Derfor for å teste modellen i gradio så må en laste ned modellen her: https://drive.google.com/file/d/1efX5-szbc2cK3GA4COkTl6YxNqh1tIXL/view?usp=sharing
Når modellen er lastet ned kan en i main.py erstatte model = load_model('RESNET_w_rotate_15epochs_true.h5') med lokasjonen modellen ble lastet ned f.eks 
load_model(C:\Users\Jonas\Downloads\RESNET_w_rotate_15epochs_true.h5)
Etter det må må en kjøre programmet som vil generere en link som kan trykkes på. 
Når linken er åpnet på localhost i browser så kan en laste opp bildet å få modellen til å predikere om det er mann eller kvinne. 
