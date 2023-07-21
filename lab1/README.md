# Test Large Language Model using AWS Foundation Models


## Access Foundation Model

Go to "Amazon Sagemaker" ---> "JumpStart" --> Foundation Models --> Search --> Jumbo --> AI21 Jurassic-2 Ultra

![image](https://github.com/jayyanar/gen-ai-labs-demos/assets/12956021/1bca29ab-b688-4fb0-ace5-f061f667e6e7)


## Select PlayGround


-  Go to Playground
  <img width="1017" alt="image" src="https://github.com/jayyanar/gen-ai-labs-demos/assets/12956021/100897e4-c181-4cf3-9ae6-f5b57aebc841">


  ![image](https://github.com/jayyanar/gen-ai-labs-demos/assets/12956021/5262a780-7a11-4d8e-8976-da31fdf62aca)


## Example Basic Prompting

- Prompting Example -->  "What is Sagemaker"

- Completion -->  "SageMaker is a fully managed service that provides everything needed to build, train, and deploy machine learning models. It includes a Jupyter notebook instance, a managed distributed training environment, and model hosting. SageMaker makes it easy to get started with machine learning, and scales to support advanced use cases."

<img width="898" alt="image" src="https://github.com/jayyanar/gen-ai-labs-demos/assets/12956021/aeda441b-aae3-483e-83a7-1e9a51acc08e">



## Example ZeroShot Prompting - Translation

- Prompting Example --> Translate English to French : "I love AWS User Group Bangalore. All the technical topic provided by them are insightful and make positive impacts"

- Completion -->  "J'aime AWS User Group Bangalore. Tous les sujets techniques fournis par eux sont précieux et auront un impact positif."

<img width="864" alt="image" src="https://github.com/jayyanar/gen-ai-labs-demos/assets/12956021/d9b28d00-f055-409c-a810-e5a9c0cf4c44">


## Example ZeroShot Prompting - Summarize the Text

- Prompting Example --> summarize the text below: "Amazon Comprehend uses natural language processing (NLP) to extract insights about the content of documents. It develops insights by recognizing the entities, key phrases, language, sentiments, and other common elements in a document. Use Amazon Comprehend to create new products based on understanding the structure of documents. For example, using Amazon Comprehend you can search social networking feeds for mentions of products or scan an entire document repository for key phrases."

- Completion --> "Amazon Comprehend is a natural language processing (NLP) service that extracts insights from text. It recognizes entities, key phrases, language, sentiments, and other common elements in a document. Use Amazon Comprehend to create new products or search social networking feeds for mentions of products."

<img width="873" alt="image" src="https://github.com/jayyanar/gen-ai-labs-demos/assets/12956021/6f283a64-a617-464c-b6ac-7d09fa8b748e">


## Example FewShot Prompting - QA Bot

- Prompting Example --> Below is SageMaker Low-code ML FAQ:

##
Q: Will my data (from inference or training) be used or shared to update the base model that is offered to customers using Amazon SageMaker JumpStart?
No. Your inference and training data will not be used nor shared to update or train the base model that SageMaker JumpStart surfaces to customers.

Q: Can I see the model weights and scripts of proprietary models in preview with Amazon SageMaker JumpStart?
No. Proprietary models do not allow customers to view model weights and scripts.

Q: Which open-source models are supported with Amazon SageMaker JumpStart?
Amazon SageMaker JumpStart includes 150+ pre-trained open-source models from PyTorch Hub and TensorFlow Hub. For vision tasks such as image classification and object detection, you can use models such as ResNet, MobileNet, and Single-Shot Detector (SSD). For text tasks such as sentence classification, text classification, and question answering, you can use models such as BERT, RoBERTa, and DistilBERT.

Q: What solutions come pre-built with Amazon SageMaker JumpStart?
SageMaker JumpStart includes solutions that are preconfigured with all necessary AWS services to launch a solution into production. Solutions are fully customizable so you can easily modify them to fit your specific use case and dataset. You can use solutions for over 15 use cases including demand forecasting, fraud detection, and predictive maintenance, and readily deploy solutions with just a few clicks. For more information about all solutions available, visit the SageMaker getting started page. 

Q: What built-in algorithms are supported in Amazon SageMaker Autopilot?
Amazon SageMaker Autopilot supports 2 built-in algorithms: XGBoost and Linear Learner.

Q: Can I stop an Amazon SageMaker Autopilot job manually?
Yes. You can stop a job at any time. When an Amazon SageMaker Autopilot job is stopped, all ongoing trials will be stopped and no new trial will be started.
##

Create a multiple choice quiz on the topic of SageMaker Low-code ML FAQ consisting of 4 questions. Each question should have 4 options. Also include the correct answer for each question using the starting string 'Correct Answer:`

- Completion --> "You can check it"

<img width="866" alt="image" src="https://github.com/jayyanar/gen-ai-labs-demos/assets/12956021/93f945cc-20ab-4123-89df-eb948a730819">


## Example ZeroShot Prompting - Reasoning Engine 1

## Example ZeroShot Prompting - Reasoning Engine 2


## Example Chain of Thoughts Prompting


