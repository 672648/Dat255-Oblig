1. Last ned datasett
Følgende datasett må lastes ned manuelt:

UTKFace Dataset https://susanqq.github.io/UTKFace/

Human Images Dataset - Men and Women https://www.kaggle.com/datasets/snmahsa/human-images-dataset-men-and-women/data

Men/Women Classification https://www.kaggle.com/datasets/playlist/men-women-classification

2. Organiser datasett
Alle bilder fra datasettene skal til slutt samles i én struktur, der de er sortert i to undermapper: men/ og women/.
Human Images Dataset brukes som basemappe, og gis navnet gender_dataset.

Endringer som må gjøres i main.ipynb
Celle 1:
Sett sti til dine lokale datasett:
source_folder = r'DIN_STI_TIL_UTKFACE'
men_folder = r'DIN_STI_TIL_HUMAN_IMAGES_DATASET\MEN'
women_folder = r'DIN_STI_TIL_HUMAN_IMAGES_DATASET\WOMEN'

Celle 2:
Angi hvor bildene fra "Men/Women Classification"-datasettet ligger:

men_source_folder = r'DIN_STI_TIL_MEN_WOMEN_CLASSIFICATION\MEN'
women_source_folder = r'DIN_STI_TIL_MEN_WOMEN_CLASSIFICATION\WOMEN'
Målet er å kopiere disse inn i samme mappe som Human Images Dataset:

men_target_folder = r'DIN_STI_TIL_HUMAN_IMAGES_DATASET\MEN'
women_target_folder = r'DIN_STI_TIL_HUMAN_IMAGES_DATASET\WOMEN'
Celle 3, 5 og 6:
Endre data_dir slik at det peker på hovedmappen hvor men/ og women/-bildene er samlet:

data_dir = r'DIN_STI_TIL_HUMAN_IMAGES_DATASET'
Eksempel:
data_dir = r'C:\Users\Jonas\OneDrive\Pictures\treningsdataDAT255\gender_dataset'


Den siste cellen i main.ipynb er laget for å evaluere modellens ytelse på et nytt, eksternt testsett.

Nedlasting av testdata
Testbildene brukes fra datasettet:

Humanface of Various Age Groups https://www.kaggle.com/datasets/neeeeeear/humanface-of-various-age-groups

Last det ned og pakk det ut på en ønsket plassering på din maskin.

Oppsett av teststi
I den siste cellen i main.ipynb, finn og endre følgende linje:

test_dir = r'C:\Users\Jonas\Documents\treningsdataDAT255\testset\Humanface\Female'
Bytt ut med din lokale sti til mappen hvor du har lagret testbildene. For eksempel:

test_dir = r'DIN_EGEN_STI_TIL_TESTBILDER'
Justering av klassifiseringsbetingelse
Modellen returnerer en sannsynlighet mellom 0 og 1:

Hvis prediction <= 0.5, tolkes det som mann

Hvis prediction > 0.5, tolkes det som kvinne

Avhengig av hvilket kjønn testbildene representerer, må du endre betingelsen på if setningen i siste celle linje 28:

Hvis du tester på kvinner skriv dette:
if prediction >= 0.5:  # korrekt hvis modellen gjetter kvinne
Hvis du tester på menn skrive dette:
if prediction <= 0.5:  # korrekt hvis modellen gjetter mann


Det var ikke plass til å laste opp selve modellen som er brukt i github. 
Derfor for å teste modellen i gradio så må en laste ned modellen her: https://drive.google.com/file/d/1efX5-szbc2cK3GA4COkTl6YxNqh1tIXL/view?usp=sharing
Når modellen er lastet ned kan en i main.py erstatte model = load_model('RESNET_w_rotate_15epochs_true.h5') med lokasjonen modellen ble lastet ned eller der du har laget din egen modell f.eks 
load_model(C:\Users\Jonas\Downloads\RESNET_w_rotate_15epochs_true.h5)
Etter det må en kjøre programmet som vil generere en link som kan trykkes på. 
Når linken er åpnet på localhost i browser, kan du laste opp bilder på nettsiden, og modellen vil returnere et resultat. 
