# Azure Speech - Language Learning Assistant

## Overview
The aim of this project is to help people learn languages by checking their pronunciation or learning how to pronounce words, and also to translate what they are saying into different languages. To achieve this, it was used [Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-studio/) for __speech recognition__, __text-to-speech__, and __speech translation__. The available languages can be found in the [Support Languages](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?utm_source=chatgpt.com&tabs=stt) documentation.

## Getting started
### Contents
There are three notebooks:
- **SoundCorrect**: This will help you with your pronunciation by detecting what you have said.
- **SoundItOut**: If you are unsure how to pronounce something, you can check it here by typing it.
- **SoundTranslate**: If you want to know what you have said in another language, this will help you find out by translating it into the desired languages.

### Prerequisites
- Python +3.8
- Azure Account 
- **Azure AI API Keys**: You will need your own API keys for Speech services. To generate these:  
  1. Log in to your [Azure AI Portal](https://azure.microsoft.com/en-us/solutions/ai/?msockid=3009fcab721967863423e8d173d86651).  
  2. Create a new resource in the Azure AI Services section.  
  3. Retrieve the API key and endpoint URL from the resource's settings.  

#### Install 
1. Clone the repository:
   ```bash
   git clone https://github.com/mariajosesalasmiranda/azure-speech-language-assistant.git
   ```
2. Navigate to the project directory:
   ```bash
   cd azure-speech-language-assistant
   ```

#### Usage
To run the notebooks:
1. Open Jupyter Notebook or any other compatible environment.
2. Navigate to the desired notebook (e.g., `SoundCorrect.ipynb`, `SoundItOut.ipynb`, or `SoundTranslate.ipynb`).
3. Follow the instructions in the notebook to use the functionality.

## License 
This project is licensed under the MIT License. It is intended for educational purposes and personal use. For any commercial use or redistribution, please refer to the terms mentioned in the license file.

> [!Note]
>  This repository is primarily for educational purposes

