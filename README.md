In preparations for this tutorial you will need to
    1. make an account on google cloud (which you alread have)
    2. make an account on https://platform.openai.com
        - it should give you free credits to start with
    3. install all requirements in requirements.txt



Overall steps:
SPEECH-TO-TEXT:
1. Go to your project and enable the speech-to-text api and create a service account and generate credentials.
2. Go to IAM & Admin, Service Accounts, Keys and click ADD KEY (download json). 
3. Create a bucket for the data:
    1. Go to create a bucket and name choose 
4. Upload the audio file to the bucket (UI)
5. Run the fine_tuting_data_prep code


FINE-TUNING:
1. Make open_ai profile
2. Create API keys and copy them into a file
    - Ex:     
        {                  
            "bearer_key" :
		}
3. export OPENAI_API_KEY=“bearer_token”
4. openai api fine_tunes.create -t ./fine_tuning_data.json -m davinci
    - this will input finetuning job into queue
5. openai api fine_tunes.list  
    - This gives info for all of your finetuning jobs. 
    - Can find id of model under "id"
    - Can find name of the model under “fine_tuned_model”
5. openai api fine_tunes.follow -i <id of model>
    - this will return the current status of your model
6. openai api fine_tunes.list    
    - Go find the name of the model under “fine_tuned_model”
7. Run the testing_openai.py