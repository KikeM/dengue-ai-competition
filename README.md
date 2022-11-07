- [dengue-ai-competition](#dengue-ai-competition)
  - [Folder Structure](#folder-structure)
    - [Why Bamboo?](#why-bamboo)
- [Installation](#installation)

# dengue-ai-competition
Dengue prediction competition from DrivenData.

> **Can you predict local epidemics of dengue fever?**
> 
> Dengue fever is a mosquito-borne disease that occurs in tropical 
> and sub-tropical parts of the world. 
> In mild cases, symptoms are similar to the flu: 
> fever, rash, and muscle and joint pain. 
> In severe cases, dengue fever can cause severe bleeding, low blood pressure, and even death.
> 
> Because it is carried by mosquitoes, the transmission dynamics of dengue are related 
> to climate variables such as temperature and precipitation. 
> Although the relationship to climate is complex, 
> a growing number of scientists argue that climate change is likely 
> to produce distributional shifts that will have significant public health implications worldwide.
> 
> From https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/

## Folder Structure
```
data : original dataset.
notebooks : exploratory notebooks.
src/bamboo : clean code to reuse for training. 
```

### Why Bamboo?
It was the name of a village in the Langtang Trek where
I stopped by when I was in Nepal. 
At the time I felt sick and didn't know what was happening,
later on a blood test confirmed I had dengue.

# Installation

I am working on a MacOS M1 laptop, and so I have runned into problems installing `darts`,
due to the `lightgbm` installation 
(https://github.com/unit8co/darts/blob/master/INSTALL.md#macos-issues-with-lightgbm).

As a workaround, once the environment is created (I am using `conda` as env manager),
I install `lightgbm` with `conda` and then the remaining of the environment with `pip`.
```bash
conda install lightgbm -y
pip install -e . -r requirements.txt
```

