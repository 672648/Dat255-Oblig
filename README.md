main.ipynb inneholder informasjon om hvordan modeller er laget. Mens Main.py er for å kjøre en modell i gradio. 

For å replikere resultatene må en først laste ned UTKFace datasettet https://www.kaggle.com/datasets/jangedoo/utkface-new, Human Images Dataset - Men and Women https://www.kaggle.com/datasets/snmahsa/human-images-dataset-men-and-women/data og Men/Women Classification https://www.kaggle.com/datasets/playlist/men-women-classification. 
Når de er lastet ned å alle bli flyttet til de samme mappene men go women. I vårt tilfelle er Human Images Dataset brukt som mappestruktur så de vil være base. Det vil si at i første celle av main.ipynb så må men_folder og women_folder være stedet Human Images Dataset ble lastet ned og unzipped på din PC. Mens source_folder må bli erstattet med der UTKFace ble lasted ned.
source_folder = r'DIN_STI_TIL_UTKFACE'
men_folder = r'DIN_STI_TIL_HUMAN_IMAGES_DATASET_MEN'
women_folder = r'DIN_STI_TIL_HUMAN_IMAGES_DATASET_WOMEN'

Etter dette må det i celle 2 endres på liknende måte, der men_source_folder må være der Men/Women Classification men mappen er lastet ned og women_source_folder må være der Men/Women Classification women mappen er lastet ned. 
men_source_folder = r'DIN_STI_TIL_MEN/WOMEN_CLASSIFICATION_MEN_MAPPE'
women_source_folder = r'DIN_STI_TIL_MEN/WOMEN_CLASSIFICATION_WOMEN_MAPPE'

Mens target folder må være der Human Images Dataset er lastet ned
men_target_folder = r'DIN_STI_TIL_HUMAN_IMAGES_DATASET_MEN'
women_target_folder = r'DIN_STI_TIL_HUMAN_IMAGES_DATASET_WOMEN'

Når alle bildene er lagret på samme plass å delt i menn og kvinner så må en i celle 3, celle 5 og celle 6 erstatte stiene fra data_dir til mappen der alle bildene er lagret. Eks. data_dir = r'C:\Users\Jonas\OneDrive\Pictures\treningsdataDAT255\gender_dataset' erstatt med mappen der mappen men og women er lagret. r'DIN_STI_TIL_HUMAN_IMAGES_DATASET'

Den siste cellen i main.ipynb blir brukt som et testsett. Bildene er hentet fra https://www.kaggle.com/datasets/neeeeeear/humanface-of-various-age-groups. Her må en erstatte test_dir = r'C:\Users\Jonas\Documents\treningsdataDAT255\testset\Humanface\Female' med stedet bildene ble lagret å endre if prediction <= 0.5: til if prediction >= 0.5: Hvis det er en menn og beholde den hvis det er damer.

Det var ikke plass til å laste opp selve modellen som er brukt i github. 
Derfor for å teste modellen i gradio så må en laste ned modellen her: https://drive.google.com/file/d/1efX5-szbc2cK3GA4COkTl6YxNqh1tIXL/view?usp=sharing
Når modellen er lastet ned kan en i main.py erstatte model = load_model('RESNET_w_rotate_15epochs_true.h5') med lokasjonen modellen ble lastet ned f.eks 
load_model(C:\Users\Jonas\Downloads\RESNET_w_rotate_15epochs_true.h5)
Etter det må må en kjøre programmet som vil generere en link som kan trykkes på. 
Når linken er åpnet på localhost i browser så kan en laste opp bildet å få modellen til å predikere om det er mann eller kvinne. 
