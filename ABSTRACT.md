The authors unveiled the **NDD20: The Northumberland Dolphin Dataset 2020**, an intricate image dataset meticulously annotated for both coarse and fine-grained instance segmentation and categorization. This dataset was conceived to address the burgeoning integration of computer vision into conservation research and the development of field-deployable systems tailored for extreme environmental conditions — an area notably lacking in open-source datasets. NDD20 comprises an extensive array of ***above*** and ***below*** water images capturing two distinct *dolphin* species, meticulously annotated for both coarse and fine-grained segmentation. All data within NDD20 was painstakingly collected manually in the North Sea along the Northumberland coastline, UK.

## Motivation

Conservation presents a promising avenue for the application of computer vision. Cetacean conservation, in particular, stands to gain significant benefits from the integration of computer vision tools. In the realm of studying cetacean population dynamics and health, researchers often rely on manual methods like photo ID, which involves identifying individuals based on unique characteristics. However, this manual identification process is time-consuming, often spanning several months. Introducing computer vision systems capable of fine-grained cetacean classification could provide researchers with more field time and reduce the time spent processing collected data.

Despite the potential, the availability of open-source datasets tailored for conservation or ecological purposes is notably scarce. Existing datasets mostly focus on simple animal detection in scenes, often limited to specific subsets like pets or birds. While some large-scale datasets showcase animals in natural settings, they typically provide species-level labels, insufficient for precise population estimation requiring individual identification.

Though challenging, cetacean researchers have manually identified individuals for over four decades by noting prominent markings on fins as they breach the waterline. This longstanding practice suggests the feasibility of an automated photo-ID process using computer vision, with ongoing efforts in this direction already underway.

## Data collection

Data collection for NDD20 involved two distinct fieldwork endeavors. ***below*** water data gathering comprised 36 opportunistic surveys of the Farne Deeps, a glacial trench known for its rich biodiversity, located approximately 14-20 nautical miles offshore from Seahouses, UK. These surveys spanned from 2011 to 2018. On the other hand, ***above*** water data collection involved 27 surveys along a designated stretch of the Northumberland coast known as the Coquet to St. Mary's Marine Conservation Zone (MCZ). ***above*** water photographs were captured using a DSLR camera from a small rigid inflatable boat during days characterized by fair weather and favorable sea conditions (typically less than four on the Beaufort scale). ***below*** water images in the dataset were extracted from high-definition video footage filmed with GoPro Hero 3 and GoPro Hero 4 cameras, operated by a diver under optimal sea conditions. Initially, ***above*** water surveys adhered to predetermined transect lines but later transitioned to more opportunistic approaches, leveraging shore-based volunteer observations shared on dedicated social media platforms.

## Dataset description

NDD20 encompasses a diverse range of image data categorized into two primary sections: ***above*** and ***below*** water. ***above*** water images, captured from the deck of a research vessel, adhere to the conventional data format widely used in cetacean research. In this format, individuals are typically identified based on the structure of their dorsal fins. Conversely, ***below*** water images, although less common, offer additional identifying features such as overall coloration, distinctive body markings, scars, and patterns resulting from injury or skin conditions.

To safeguard ongoing cetacean research endeavors, a pseudo-anonymization process has been undertaken. However, this does not diminish the data's significance for computer vision researchers. Notably, images with sequential filenames were not captured sequentially, and individual IDs have been randomly assigned numerical values instead of the codes used by Northumberland cetacean researchers. Furthermore, all EXIF data contained within the images has been removed.


## Above water images

NDD20 comprises a total of 2201 ***above*** water images, each accompanied by a JSON file. This JSON file provides detailed annotations for each image, including sets of (x,y) coordinates indicating regions of interest within the image. These coordinates are supplemented with attribute labels indicating various levels of difficulty in the recognition task. The first attribute level, labeled *dolphin*, delineates the area of the image containing any portion of a *dolphin* visible above the waterline at the time of capture. This attribute presents a standard, albeit challenging, instance segmentation task. Approximately 2900 masks are present in the above-water data, as some images feature multiple masks. The second attribute denotes the *dolphin*'s species, either BND (bottle nose dolphin) or WBD (white beaked dolphin), corresponding to ***tursiops truncatus*** and ***lagenorhynchus albirostris***, respectively. This aspect poses a fine-grained categorization challenge due to subtle inter-species differences. Although all above-water masks bear this label, there's an imbalance in class distribution, with 73% labeled as BND. The final attribute label signifies individual *dolphin* identifications, meticulously determined by cetacean researchers specializing in the Northumberland coastal area. Around 14% of masks contain an ***id*** attribute, with 44 distinct classes present. Once again, this distribution imbalance presents both a fine-grained and few-shot learning challenge.

<img src="https://github.com/dataset-ninja/northumberland-dolphin/assets/120389559/2b71b1ab-d4e1-4b99-92ce-2f5b7198379b" alt="image" width="600">

<span style="font-size: smaller; font-style: italic;">The number of above water images per ID class.</span>

Identification based on individual ***id*** class labels poses the most daunting fine-grained challenge within NDD20, primarily because individual recognition beyond human facial recognition remains largely unexplored in research. To discern individuals within the dataset, nuances such as scarring or pigmentation on the individual's surface, alongside the distinctive shape of the dorsal fin, must be meticulously considered. Moreover, the dataset contains only a limited number of examples for each individual, thereby presenting both a fine-grained and few-shot learning task. Several hurdles exist within the above-water data that necessitate overcoming. These challenges include images featuring small regions of interest, extensive blur or water splashes, partially obscured *dolphin* fins, photographs taken from oblique angles, and markings crucial for identification being present solely on one side of the fin.

<img src="https://github.com/dataset-ninja/northumberland-dolphin/assets/120389559/bf9d2e83-55ec-414d-90c0-f87dd84ffc17" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Example above water images. Both images contain one mask with the following attributes: Left - object dolphin, species WBD, id:11. Right - object:dolphin, species BND, id:8.</span>

## Below water images

The 2201 ***below*** water images presented constitute a subset of a much broader image collection dating back to 2011. The labeling methodology for these images mirrors that of the ***above*** water images. The authors supply a JSON file containing coordinates for manually drawn mask annotations and multiple attribute labels. Similarly to the ***above*** water images, the first attribute level pertains to *dolphin*, representing areas within the image where any part of the object is visible. However, in contrast to the above-water images, all ***below*** water images feature at least one mask with an ***id*** attribute, encompassing 82 classes. Variations in the frequency of appearance among ***id*** class labels arise due to the data collection process involving free-roaming individuals, thereby presenting a genuine few-shot learning challenge reflective of real-world scenarios. Unlike the ***above*** water images, no species label is provided for the ***below*** water images, as all images depict ***lagenorhynchus albirostris***. Additionally, ***below*** water images are tagged with an ***out of focus*** flag, indicating whether the individual is deemed to be ***out of focus***.

<img src="https://github.com/dataset-ninja/northumberland-dolphin/assets/120389559/7a7e131e-6b68-4f05-9537-502f327a332b" alt="image" width="600">

<span style="font-size: smaller; font-style: italic;">The number of below water images per ID class.</span>

The primary obstacles concerning the below-water images revolve around water clarity, influenced by factors like algae blooms and sunlight refraction. These elements can obscure areas of the individual crucial for identification or introduce artificial markings that impede the process. Many challenges akin to those encountered with above-water images are also pertinent here, particularly the probability that unique features are exclusive to one side of the body.

<img src="https://github.com/dataset-ninja/northumberland-dolphin/assets/120389559/7b24a68d-f72a-45af-b640-4ba22157e676" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Example below water images. Both images contain one mask with the following attributes: Left - object dolphin, id:9, out of focus false. Right - object dolphin, id:30, out of focus false.</span>



